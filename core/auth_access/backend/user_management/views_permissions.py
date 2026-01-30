from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from .models import (
    MenuItemType, UserPermission, GroupPermission, 
    UserLocationMapping, UserProfile
)
from .serializers import (
    MenuItemTypeSerializer, UserPermissionSerializer, 
    GroupPermissionSerializer, BulkUserPermissionSerializer,
    BulkRolePermissionSerializer, UserLocationMappingSerializer,
    UserSerializer
)
from .role_permissions import get_role_permissions, apply_role_template_to_user

User = get_user_model()

class MenuItemTypeViewSet(ModelViewSet):
    queryset = MenuItemType.objects.all()
    serializer_class = MenuItemTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all().select_related('profile')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserPermissionViewSet(ModelViewSet):
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return self.queryset.filter(user_id=user_id)
        return self.queryset

class GetUserPermissionsView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        permissions_perms = UserPermission.objects.filter(user=user).select_related('menu_item')
        
        data = {}
        for p in permissions_perms:
            data[p.menu_item.menu_item_id] = {
                'can_view': p.can_view,
                'can_create': p.can_create,
                'can_edit': p.can_edit,
                'can_delete': p.can_delete,
                'override': p.override
            }
        return Response(data)

class BulkUserPermissionView(APIView):
    def post(self, request):
        serializer = BulkUserPermissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = serializer.validated_data['user_id']
        perms_dict = serializer.validated_data['permissions']
        user = get_object_or_404(User, id=user_id)
        
        for menu_id, flags in perms_dict.items():
            menu_item = get_object_or_404(MenuItemType, menu_item_id=menu_id)
            UserPermission.objects.update_or_create(
                user=user,
                menu_item=menu_item,
                defaults={
                    'can_access': flags.get('can_view', False), # use can_view as proxy for access
                    'can_view': flags.get('can_view', False),
                    'can_create': flags.get('can_create', False),
                    'can_edit': flags.get('can_edit', False),
                    'can_delete': flags.get('can_delete', False),
                    'override': flags.get('override', True)
                }
            )
        return Response({'status': 'success'})

class GetRolePermissionsView(APIView):
    def get(self, request, role_key):
        # First check DB
        perms = GroupPermission.objects.filter(role_key=role_key).select_related('menu_item')
        if perms.exists():
            data = {}
            for p in perms:
                data[p.menu_item.menu_item_id] = {
                    'can_view': p.can_view,
                    'can_create': p.can_create,
                    'can_edit': p.can_edit,
                    'can_delete': p.can_delete
                }
            return Response(data)
        
        # Fallback to template
        template = get_role_permissions(role_key)
        if template:
            return Response(template.get('menu_items', {}))
        
        return Response({})

class BulkRolePermissionView(APIView):
    def post(self, request):
        serializer = BulkRolePermissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        role_key = serializer.validated_data['role_key']
        perms_dict = serializer.validated_data['permissions']
        
        group, _ = Group.objects.get_or_create(name=role_key)
        
        for menu_id, flags in perms_dict.items():
            menu_item = get_object_or_404(MenuItemType, menu_item_id=menu_id)
            GroupPermission.objects.update_or_create(
                group=group,
                role_key=role_key,
                menu_item=menu_item,
                defaults={
                    'can_access': flags.get('can_view', False),
                    'can_view': flags.get('can_view', False),
                    'can_create': flags.get('can_create', False),
                    'can_edit': flags.get('can_edit', False),
                    'can_delete': flags.get('can_delete', False),
                }
            )
        return Response({'status': 'success'})

class UserLocationMappingViewSet(ModelViewSet):
    queryset = UserLocationMapping.objects.all()
    serializer_class = UserLocationMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return self.queryset.filter(user_id=user_id)
        return self.queryset




