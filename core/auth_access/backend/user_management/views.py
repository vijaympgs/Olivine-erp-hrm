from django.db import models
from rest_framework import viewsets, filters, status, views, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().select_related('reporting_manager')
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee_code', 'department', 'designation', 'status', 'business_unit']
    search_fields = ['employee_code', 'first_name', 'last_name', 'email']
    ordering_fields = ['employee_code', 'first_name', 'last_name', 'department', 'role', 'status', 'date_of_joining']
    ordering = ['last_name', 'first_name']


# OperatingCompanySerializer import removed - concept deleted
from .models import UserCompanyMapping  # New model to replace UserOperatingCompanyMapping

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []  # Disable authentication for login endpoint

    def post(self, request):
        # Accept both 'username' (new) and 'email' (legacy) for backward compatibility
        username_or_email = request.data.get('username') or request.data.get('email')
        password = request.data.get('password')
        requested_company_id = request.data.get('companyId')

        if not username_or_email or not password:
            return Response({'error': 'Username/email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate - try multiple approaches
        User = get_user_model()
        user = None
        
        # 1. Try direct username authentication
        user = authenticate(username=username_or_email, password=password)
        
        # 2. If not found, try finding user by email and authenticate with username
        if not user:
            try:
                user_obj = User.objects.filter(email=username_or_email).first()
                if user_obj:
                    user = authenticate(username=user_obj.username, password=password)
            except Exception:
                pass

        if user:
            if not user.is_active:
                return Response({'error': 'User account is disabled'}, status=status.HTTP_403_FORBIDDEN)

            # Generate/Get Token
            token, _ = Token.objects.get_or_create(user=user)
            
            # Fetch Authorized Companies (DIRECT - no OperatingCompany)
            from core.licensing.backend.business_entities.models import Company
            
            # Get companies user has access to via UserCompanyMapping
            company_mappings = UserCompanyMapping.objects.filter(
                user=user,
                is_active=True,
                company__status='ACTIVE'
            ).select_related('company')
            
            authorized_companies = Company.objects.filter(
                id__in=company_mappings.values_list('company_id', flat=True),
                status='ACTIVE'
            )
            
            # If no mappings exist, allow access to all companies (fallback for debug/initial setup)
            if not company_mappings.exists():
                authorized_companies = Company.objects.filter(status='ACTIVE')
            
            # Validate Requested Company Context
            selected_company_id = None
            if requested_company_id:
                # Check if user has access to this Company
                # Use Q object to match by ID or Code
                from django.db.models import Q
                target_company = authorized_companies.filter(
                    Q(id=requested_company_id) if str(requested_company_id).isdigit() else Q(code=requested_company_id)
                ).first()
                
                if not target_company:
                    return Response({
                        'error': f'User is not authorized for the requested Company. Available: {[c.code for c in authorized_companies]}'
                    }, status=status.HTTP_403_FORBIDDEN)
                
                selected_company_id = str(target_company.id)
            
            # Return Response with Context Data
            available_companies_for_frontend = [{
                'id': str(company.id),
                'code': company.code,
                'name': company.name,
                'legal_entity_type': company.legal_entity_type,
            } for company in authorized_companies]
            
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'name': user.get_full_name() or user.username,
                    'email': user.email,
                    'is_superuser': user.is_superuser,
                },
                'available_companies': available_companies_for_frontend,
                'context': {
                    'company_id': selected_company_id
                }
            })
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



# ============================================================================
# USER & PERMISSION MANAGEMENT API VIEWS
# ============================================================================

from rest_framework.decorators import action
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import (
    Role, UserProfile, MenuItemType, RolePermission, 
    UserRole, PermissionAudit, RoleAssignmentAudit
)
from .serializers import (
    RoleSerializer, UserProfileSerializer, UserSerializer,
    MenuItemTypeSerializer, RolePermissionSerializer, UserRoleSerializer,
    BulkRolePermissionSerializer,
    PermissionAuditSerializer, RoleAssignmentAuditSerializer
)
from .services.toolbar_permission_service import TOOLBAR_CHAR_MAP


class UserListView(views.APIView):
    """List all users with their profiles and roles"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        User = get_user_model()
        users = User.objects.select_related('profile').prefetch_related('userrole_set__role').all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class GetUserPermissionsView(views.APIView):
    """Get effective permissions for a specific user"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        User = get_user_model()
        user = get_object_or_404(User, id=user_id)
        
        # Get all roles assigned to user
        user_roles = UserRole.objects.filter(user=user, is_active=True).select_related('role')
        
        # Get all permissions from assigned roles
        permissions = {}
        for user_role in user_roles:
            role_permissions = RolePermission.objects.filter(role=user_role.role).select_related('menu_item')
            for perm in role_permissions:
                menu_id = perm.menu_item.menu_id
                if menu_id not in permissions:
                    permissions[menu_id] = {
                        'can_view': False,
                        'can_create': False,
                        'can_edit': False,
                        'can_delete': False
                    }
                
                # Merge permissions (OR logic - if any role grants permission, user has it)
                permissions[menu_id]['can_view'] = permissions[menu_id]['can_view'] or perm.can_view
                permissions[menu_id]['can_create'] = permissions[menu_id]['can_create'] or perm.can_create
                permissions[menu_id]['can_edit'] = permissions[menu_id]['can_edit'] or perm.can_edit
                permissions[menu_id]['can_delete'] = permissions[menu_id]['can_delete'] or perm.can_delete

        return Response({
            'user_id': user_id,
            'username': user.username,
            'permissions': permissions
        })


class RoleListView(views.APIView):
    """List all roles"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        roles = Role.objects.filter(is_active=True)
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetRolePermissionsView(views.APIView):
    """Get permissions for a specific role"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, role_key):
        role = get_object_or_404(Role, role_key=role_key)
        permissions = RolePermission.objects.filter(role=role).select_related('menu_item')
        serializer = RolePermissionSerializer(permissions, many=True)
        return Response(serializer.data)


class PermissionMatrixView(views.APIView):
    """Get the complete permission matrix for all roles and menu items"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get all active roles and retail menu items
        roles = Role.objects.filter(is_active=True)
        menu_items = MenuItemType.objects.filter(module_name='retail', is_active=True).order_by('menu_order', 'menu_name')
        
        # All possible toolbar characters to ensure frontend has keys
        all_possible_chars = 'NESCKZTJAVPMRDX1234QFBG?'
        
        # Build permission matrix
        matrix = {}
        for role in roles:
            matrix[role.role_key] = {}
            role_permissions = RolePermission.objects.filter(role=role).select_related('menu_item')
            
            # Create lookup for existing permissions
            perm_lookup = {perm.menu_item.menu_id: perm for perm in role_permissions}
            
            for menu_item in menu_items:
                res = {
                    'can_access': False,
                    'can_view': False,
                    'can_create': False,
                    'can_edit': False,
                    'can_delete': False
                }
                
                # Initialize all character flags as False
                for c in all_possible_chars:
                    res[f'toolbar_{c}'] = False
                
                if menu_item.menu_id in perm_lookup:
                    perm = perm_lookup[menu_item.menu_id]
                    res.update({
                        'can_access': perm.can_access,
                        'can_view': perm.can_view,
                        'can_create': perm.can_create,
                        'can_edit': perm.can_edit,
                        'can_delete': perm.can_delete
                    })
                    
                    # Resolve toolbar flags from mask
                    t_str = perm.toolbar_string or menu_item.applicable_toolbar_config or ""
                    t_mask = perm.toolbar_permissions or ""
                    
                    for i, char in enumerate(t_str):
                        if i < len(t_mask):
                            res[f'toolbar_{char}'] = (t_mask[i] == '1')
                
                matrix[role.role_key][menu_item.menu_id] = res

        return Response({
            'roles': RoleSerializer(roles, many=True).data,
            'menu_items': MenuItemTypeSerializer(menu_items, many=True).data,
            'matrix': matrix
        })


class MenuItemListView(views.APIView):
    """List menu items with optional filtering"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        module = request.query_params.get('module', 'retail')
        menu_items = MenuItemType.objects.filter(module_name=module, is_active=True).order_by('menu_order', 'menu_name')
        serializer = MenuItemTypeSerializer(menu_items, many=True)
        return Response(serializer.data)


class MenuItemHierarchyView(views.APIView):
    """Get menu items in hierarchical tree structure"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        module = request.query_params.get('module', 'retail')
        menu_items = MenuItemType.objects.filter(
            module_name=module, 
            is_active=True
        ).select_related('parent_menu').order_by('menu_order', 'menu_name')
        
        # Build tree structure
        items_by_id = {item.menu_id: {
            'id': item.menu_id,
            'name': item.menu_name,
            'module': item.module_name,
            'order': item.menu_order,
            'parent_id': item.parent_menu.menu_id if item.parent_menu else None,
            'children': []
        } for item in menu_items}
        
        hierarchy = []
        for item in menu_items:
            item_dict = items_by_id[item.menu_id]
            if item.parent_menu and item.parent_menu.menu_id in items_by_id:
                items_by_id[item.parent_menu.menu_id]['children'].append(item_dict)
            else:
                hierarchy.append(item_dict)
        
        return Response(hierarchy)


class BulkPermissionUpdateView(views.APIView):
    """Bulk update permissions for a role"""
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        role_key = request.data.get('role_key')
        permissions_data = request.data.get('permissions', {})
        
        if not role_key:
            return Response({'error': 'role_key is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        role = get_object_or_404(Role, role_key=role_key)
        
        updated_count = 0
        created_count = 0
        
        for menu_id, perms in permissions_data.items():
            menu_item = MenuItemType.objects.filter(menu_id=menu_id).first()
            if not menu_item:
                continue
            
            # Get old permissions for audit
            old_perm = RolePermission.objects.filter(role=role, menu_item=menu_item).first()
            old_values = None
            if old_perm:
                old_values = {
                    'can_access': old_perm.can_access,
                    'can_view': old_perm.can_view,
                    'can_create': old_perm.can_create,
                    'can_edit': old_perm.can_edit,
                    'can_delete': old_perm.can_delete
                }
            
            # Resolve toolbar_permissions mask if toolbar character flags are provided
            toolbar_string = menu_item.applicable_toolbar_config or ""
            toolbar_mask = ""
            
            if any(key.startswith('toolbar_') for key in perms):
                # Identify which characters are enabled
                mask_list = []
                for char in toolbar_string:
                    flag_key = f"toolbar_{char}"
                    is_enabled = perms.get(flag_key, perms.get(TOOLBAR_CHAR_MAP.get(char, char.lower()), False))
                    mask_list.append('1' if is_enabled else '0')
                toolbar_mask = "".join(mask_list)
            
            # Map legacy CRUD if not explicitly provided or to keep in sync
            can_view = perms.get('can_view', perms.get('toolbar_V', False))
            can_create = perms.get('can_create', perms.get('toolbar_N', False))
            can_edit = perms.get('can_edit', perms.get('toolbar_E', False))
            can_delete = perms.get('can_delete', perms.get('toolbar_D', False))
            can_access = perms.get('can_access', can_view)

            # Update or create permission
            defaults = {
                'can_access': can_access,
                'can_view': can_view,
                'can_create': can_create,
                'can_edit': can_edit,
                'can_delete': can_delete,
            }
            
            if toolbar_string:
                defaults['toolbar_string'] = toolbar_string
                if toolbar_mask:
                    defaults['toolbar_permissions'] = toolbar_mask

            obj, created = RolePermission.objects.update_or_create(
                role=role,
                menu_item=menu_item,
                defaults=defaults
            )
            
            if created:
                created_count += 1
            else:
                updated_count += 1
            
            # Create audit record
            PermissionAudit.objects.create(
                role=role,
                menu_item=menu_item,
                action='CREATE' if created else 'UPDATE',
                old_permissions=old_values,
                new_permissions=defaults,
                changed_by=request.user,
                ip_address=self._get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:500]
            )
        
        return Response({
            'status': 'success',
            'created': created_count,
            'updated': updated_count
        })
    
    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')


class UserRoleListView(views.APIView):
    """List and manage user-role mappings"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = request.query_params.get('user_id')
        queryset = UserRole.objects.select_related('user', 'role', 'assigned_by').filter(is_active=True)
        
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        
        serializer = UserRoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Assign role to user"""
        user_id = request.data.get('user_id')
        role_key = request.data.get('role_key')
        
        if not user_id or not role_key:
            return Response({'error': 'user_id and role_key are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        User = get_user_model()
        user = get_object_or_404(User, id=user_id)
        role = get_object_or_404(Role, role_key=role_key)
        
        user_role, created = UserRole.objects.get_or_create(
            user=user,
            role=role,
            defaults={
                'assigned_by': request.user,
                'is_active': True
            }
        )
        
        if not created and not user_role.is_active:
            user_role.is_active = True
            user_role.assigned_by = request.user
            user_role.save()
        
        # Create audit record
        RoleAssignmentAudit.objects.create(
            user=user,
            role=role,
            action='ASSIGN',
            assigned_by=request.user,
            ip_address=self._get_client_ip(request)
        )
        
        serializer = UserRoleSerializer(user_role)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    
    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')


class BulkUserRoleUpdateView(views.APIView):
    """Bulk update user-role mappings"""
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        """
        Expected payload:
        {
            "user_id": 1,
            "role_keys": ["admin", "posmanager"]
        }
        """
        user_id = request.data.get('user_id')
        role_keys = request.data.get('role_keys', [])
        
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        User = get_user_model()
        user = get_object_or_404(User, id=user_id)
        
        # Deactivate existing roles not in the new list
        existing_roles = UserRole.objects.filter(user=user, is_active=True)
        for ur in existing_roles:
            if ur.role.role_key not in role_keys:
                ur.is_active = False
                ur.save()
                
                RoleAssignmentAudit.objects.create(
                    user=user,
                    role=ur.role,
                    action='REMOVE',
                    assigned_by=request.user,
                    ip_address=self._get_client_ip(request)
                )
        
        # Add new roles
        for role_key in role_keys:
            role = Role.objects.filter(role_key=role_key).first()
            if not role:
                continue
            
            user_role, created = UserRole.objects.get_or_create(
                user=user,
                role=role,
                defaults={
                    'assigned_by': request.user,
                    'is_active': True
                }
            )
            
            if not created and not user_role.is_active:
                user_role.is_active = True
                user_role.assigned_by = request.user
                user_role.save()
                
                RoleAssignmentAudit.objects.create(
                    user=user,
                    role=role,
                    action='ASSIGN',
                    assigned_by=request.user,
                    ip_address=self._get_client_ip(request)
                )
        
        return Response({'status': 'success'})
    
    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')


# UserLocationListView and BulkUserLocationUpdateView removed - Location is Retail-only


class RoleTemplateView(views.APIView):
    """Get predefined role permission templates"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Return available role templates with their default permissions"""
        templates = {
            'admin': {
                'name': 'Administrator',
                'description': 'Full access to all modules',
                'default_permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': True
                }
            },
            'posmanager': {
                'name': 'POS Manager',
                'description': 'Manage POS operations and staff',
                'default_permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': False
                }
            },
            'posuser': {
                'name': 'POS User',
                'description': 'Basic POS operations only',
                'default_permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': False,
                    'can_delete': False
                }
            },
            'backofficemanager': {
                'name': 'Back Office Manager',
                'description': 'Manage back office operations',
                'default_permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': False
                }
            },
            'backofficeuser': {
                'name': 'Back Office User',
                'description': 'Basic back office access',
                'default_permissions': {
                    'can_view': True,
                    'can_create': False,
                    'can_edit': False,
                    'can_delete': False
                }
            }
        }
        return Response(templates)


class ApplyRoleTemplateView(views.APIView):
    """Apply a role template to a user"""
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        user_id = request.data.get('user_id')
        role_key = request.data.get('role_key')
        
        if not user_id or not role_key:
            return Response({'error': 'user_id and role_key are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        User = get_user_model()
        user = get_object_or_404(User, id=user_id)
        role = get_object_or_404(Role, role_key=role_key)
        
        # Assign role to user
        user_role, created = UserRole.objects.get_or_create(
            user=user,
            role=role,
            defaults={
                'assigned_by': request.user,
                'is_active': True
            }
        )
        
        if not created and not user_role.is_active:
            user_role.is_active = True
            user_role.assigned_by = request.user
            user_role.save()
        
        # Create audit record
        RoleAssignmentAudit.objects.create(
            user=user,
            role=role,
            action='ASSIGN',
            assigned_by=request.user,
            ip_address=request.META.get('REMOTE_ADDR')
        )
        
        return Response({
            'status': 'success',
            'message': f'Role {role.role_name} applied to user {user.username}'
        })


class CurrentUserView(views.APIView):
    """Get current authenticated user details"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UpdateUserProfileView(views.APIView):
    """Update current user profile"""
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
