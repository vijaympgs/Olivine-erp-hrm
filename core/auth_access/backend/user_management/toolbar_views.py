"""
Toolbar Configuration API Views
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ERPMenuItem, RolePermission, UserPermission, UserRole


def parse_toolbar_string(config_string):
    """
    Parse new character-based toolbar config string (e.g. "NESC")
    into full permission dictionary.
    """
    # Initialize all to False
    all_keys = [
        'new', 'edit', 'save', 'cancel', 'clear', 'authorize', 'submit', 'reject',
        'amend', 'view', 'print', 'email', 'refresh', 'delete', 'hold', 'void',
        'exit', 'upload', 'download', 'clone', 'first', 'prev', 'next', 'last',
        'search', 'filter', 'notes', 'attach', 'settings', 'help'
    ]
    perms = {k: False for k in all_keys}
    
    if not config_string:
        return perms

    # Character Map (Must match Seed/Frontend)
    # N:New, E:Edit, S:Save, C:Cancel, K:Clear
    # Z:Authorize, T:Submit, J:Reject, A:Amend
    # V:View, P:Print, M:Email
    # R:Refresh, D:Delete, H:Hold, O:Void
    # X:Exit
    # I:Import/Upload, Y:Export/Download, L:Clone
    # 1:First, 2:Prev, 3:Next, 4:Last
    # Q:Search, F:Filter
    # B:Notes, G:Attach, W:Settings, ?:Help
    
    mapping = {
        'N': 'new', 'E': 'edit', 'S': 'save', 'C': 'cancel', 'K': 'clear',
        'Z': 'authorize', 'T': 'submit', 'J': 'reject', 'A': 'amend',
        'V': 'view', 'P': 'print', 'M': 'email',
        'R': 'refresh', 'D': 'delete', 'H': 'hold', 'O': 'void',
        'X': 'exit', 'I': 'upload', 'Y': 'download', 'L': 'clone',
        '1': 'first', '2': 'prev', '3': 'next', '4': 'last',
        'Q': 'search', 'F': 'filter',
        'B': 'notes', 'G': 'attach', 'W': 'settings', '?': 'help'
    }
    
    for char in config_string:
        key = mapping.get(char)
        if key:
            perms[key] = True
            
    return perms

def parse_toolbar_config(config_string):
    """Parse output from LEGACY comma-separated config"""
    buttons = config_string.split(',')
    BUTTON_MAP = [
        'new', 'edit', 'save', 'cancel', 'clear',
        'authorize', 'amend', 'view', 'print', 'refresh',
        'delete', 'exit', 'upload', 'download', 'clone'
    ]
    perms = {button: False for button in BUTTON_MAP}
    for i, button in enumerate(BUTTON_MAP):
        if i < len(buttons) and buttons[i] == '1':
            perms[button] = True
    return perms


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_ui_config(request, view_id):
    """
    Get toolbar configuration for a specific view
    Applies role-based overrides if applicable
    """
    user = request.user
    company_id = request.GET.get('company_id')
    
    if not company_id:
        # For compatibility, we might proceed without company_id or error out.
        # Strict for now:
        pass 
        # return Response({'error': ...})
    
    try:
        menu_item = ERPMenuItem.objects.get(menu_id=view_id, is_active=True)
    except ERPMenuItem.DoesNotExist:
        return Response({'error': f'View {view_id} not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # DETERMINE CONFIG SOURCE
    # Prefer new field 'applicable_toolbar_config'. If empty, fall back to legacy 'toolbar_config'.
    effective_config = menu_item.applicable_toolbar_config
    is_legacy = False
    
    if not effective_config:
        effective_config = menu_item.toolbar_config
        is_legacy = True
        
    has_override = False
    
    # Check user-specific override
    user_perm = UserPermission.objects.filter(user=user, menu_item=menu_item).first()
    if user_perm and user_perm.toolbar_override:
        effective_config = user_perm.toolbar_override
        has_override = True
        is_legacy = ',' in effective_config # Guess format based on comma
    else:
        # Check role-based override
        user_roles = UserRole.objects.values_list('role_id', flat=True).filter(user=user, is_active=True)
        role_perm = RolePermission.objects.filter(
            role_id__in=user_roles,
            menu_item=menu_item,
            override_enabled=True
        ).first() # Priority?
        
        if role_perm and role_perm.toolbar_override:
            effective_config = role_perm.toolbar_override
            has_override = True
            is_legacy = ',' in effective_config

    # BREADCRUMB GENERATION
    # Desired: Module > Submodule > Parent > Item
    
    # 1. Build Hierarchy from DB parents
    hierarchy = []
    current = menu_item
    while current:
        hierarchy.insert(0, current.menu_name)
        current = current.parent_menu
        
    # 2. Determine Module Label
    simple_modules = {
        'RETAIL': 'Retail',
        'FMS': 'Finance',
        'HRM': 'HR',
        'CRM': 'CRM'
    }
    module_label = simple_modules.get(menu_item.module_name, menu_item.module_name.title()) 
    
    # 3. Determine Submodule Label
    submodule_label = None
    if menu_item.submodule and menu_item.submodule != menu_item.module_name:
        # Heuristic: Uppercase codes like 'PROCUREMENT' -> 'Procurement'
        # Special cases like 'POS' -> 'POS'
        if menu_item.submodule in ['POS', 'CRM', 'HR']:
            submodule_label = menu_item.submodule
        else:
            submodule_label = menu_item.submodule.title()

    # 4. Construct Final List
    breadcrumbs = [module_label]
    
    if submodule_label and (not hierarchy or hierarchy[0] != submodule_label):
         breadcrumbs.append(submodule_label)
         
    breadcrumbs.extend(hierarchy)
    
    # Clean up duplicates if Module == Hierarchy[0] (rare but possible)
    if len(breadcrumbs) > 1 and breadcrumbs[0] == breadcrumbs[1]:
        breadcrumbs.pop(0)

    # Calculate permissions based on config
    permissions = parse_toolbar_string(effective_config) if not is_legacy else parse_toolbar_config(effective_config)

    return Response({
        'view_id': menu_item.menu_id,
        'view_name': menu_item.menu_name,
        'view_type': menu_item.view_type,
        'module': menu_item.module_name,
        'submodule': menu_item.submodule,
        'toolbar_config': effective_config, # The raw string
        'permissions': permissions,         # The boolean map
        'has_override': has_override,
        'route_path': menu_item.route_path,
        'component_name': menu_item.component_name,
        'breadcrumbs': breadcrumbs
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_menu_items(request):
    """
    List all menu items for current user's company
    
    URL: /api/menu-items/?company_id=<company_id>&module=<module>
    """
    company_id = request.GET.get('company_id')
    module = request.GET.get('module')
    
    queryset = ERPMenuItem.objects.filter(is_active=True)
    
    if module:
        queryset = queryset.filter(module_name=module)
    
    items = queryset.values(
        'menu_id',
        'menu_name',
        'module_name',
        'submodule',
        'view_type',
        'route_path',
        'menu_order'
    ).order_by('module_name', 'submodule', 'menu_order')
    
    return Response(list(items))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_toolbar_permissions(request):
    """
    Get resolved toolbar permissions for a specific menu item and mode.
    Implements the 5-step resolution pipeline (PLATFORM LAW).
    
    URL: /api/toolbar-permissions/?menu_id=<menu_id>&mode=<mode>
    
    Args:
        menu_id: Menu ID (e.g., 'PURCHASE_ORDERS')
        mode: UI mode ('VIEW', 'NEW', 'EDIT')
    
    Returns:
        {
            'menu_id': str,
            'mode': str,
            'toolbar_string': str,
            'permission_mask': str,
            'allowed_characters': List[str],
            'allowed_actions': List[str]
        }
    """
    from .services.toolbar_permission_service import resolve_toolbar_permissions
    
    menu_id = request.GET.get('menu_id')
    mode = request.GET.get('mode', 'VIEW')
    
    if not menu_id:
        return Response(
            {'error': 'menu_id parameter is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Service handles normalization (CREATE -> NEW) and validation
    # if mode not in ['VIEW', 'NEW', 'EDIT']:
    #    return Response(...)
    
    # Let service handle it, or pre-normalize here
    if mode == 'CREATE':
        mode = 'NEW'

    
    try:
        result = resolve_toolbar_permissions(request.user.id, menu_id, mode)
        
        if 'error' in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        
        return Response(result)
    
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )





