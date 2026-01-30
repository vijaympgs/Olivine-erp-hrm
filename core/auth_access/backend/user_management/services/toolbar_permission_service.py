"""
Toolbar Permission Resolution Service
Implements the 5-step resolution pipeline for toolbar permissions.

This is PLATFORM LAW - no hardcoding, no screen-specific logic.
"""
from typing import Dict, List, Optional
from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.models import (
    ERPMenuItem,
    RolePermission,
    Role,
    UserRole
)

User = get_user_model()

# Character to action mapping (canonical)
TOOLBAR_CHAR_MAP = {
    'N': 'new',
    'E': 'edit',
    'S': 'save',
    'C': 'cancel',
    'K': 'clear',
    'V': 'view',
    'D': 'delete',
    'X': 'exit',
    'R': 'refresh',
    'Q': 'search',
    'F': 'filter',
    'I': 'import',
    'O': 'export',
    'Z': 'authorize',
    'T': 'submit',
    'J': 'reject',
    'A': 'amend',
    'P': 'print',
    'M': 'email',
    '1': 'first',
    '2': 'previous',
    '3': 'next',
    '4': 'last',
    'H': 'hold',
    'W': 'void',
    'B': 'notes',
    'G': 'attach',
    '?': 'help',
    'Y': 'settings',
}

# Mode law: which actions are allowed in each mode (PLATFORM LAW)
# VIEW = List View (Standard)
# NEW/EDIT = Form View
MODE_LAW = {
    'VIEW': {
        'exclude': ['S', 'C', 'K'],  # Never show Save, Cancel, Clear in List/View mode
    },
    'NEW': {
        'exclude': ['N', 'E', 'V', 'D', 'R', 'Q', 'F', 'I', 'O', '1', '2', '3', '4'], # Exclude list-specific actions from form
    },
    'EDIT': {
        'exclude': ['N', 'E', 'V', 'D', 'R', 'Q', 'F', 'I', 'O', '1', '2', '3', '4'], # Exclude list-specific actions from form
    },
    'VIEW_FORM': {
        # This is for True Read-Only mode on a Record/Form
        'exclude': ['N', 'V', 'D', 'S', 'C', 'K', 'R', 'Q', 'F', 'I', 'O', '1', '2', '3', '4'],
    }
}

# Common actions always granted (S, C, K, X)
COMMON_ACTIONS = ['S', 'C', 'K', 'X']


def resolve_toolbar_permissions(user_id: int, menu_id: str, mode: str) -> Dict:
    """
    5-Step Resolution Pipeline (PLATFORM LAW)
    
    Toolbar = ScreenCapability ∩ UserPermission ∩ ModeLaw
    
    Args:
        user_id: User ID
        menu_id: Menu ID (e.g., 'PURCHASE_ORDERS')
        mode: UI mode ('VIEW', 'NEW', 'EDIT')
    
    Returns:
        Dict with:
            - menu_id: str
            - mode: str
            - toolbar_string: str
            - permission_mask: str
            - allowed_characters: List[str]
            - allowed_actions: List[str]
    """
    # Validate and normalize mode
    if mode == 'CREATE':
        mode = 'NEW'

    if mode not in ['VIEW', 'NEW', 'EDIT', 'VIEW_FORM']:
        raise ValueError(f"Invalid mode: {mode}. Must be VIEW, NEW, EDIT, or VIEW_FORM.")
    
    # Step 1: Get screen toolbar string
    try:
        menu_item = ERPMenuItem.objects.get(menu_id=menu_id)
        toolbar_string = menu_item.applicable_toolbar_config or ''
    except ERPMenuItem.DoesNotExist:
        return {
            'menu_id': menu_id,
            'mode': mode,
            'toolbar_string': '',
            'permission_mask': '',
            'allowed_characters': [],
            'allowed_actions': [],
            'error': f'Menu item {menu_id} not found'
        }
    
    if not toolbar_string:
        # No toolbar configured for this screen
        return {
            'menu_id': menu_id,
            'mode': mode,
            'toolbar_string': '',
            'permission_mask': '',
            'allowed_characters': [],
            'allowed_actions': []
        }
    
    # Step 2: Get user permission mask
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return {
            'menu_id': menu_id,
            'mode': mode,
            'toolbar_string': toolbar_string,
            'permission_mask': '',
            'allowed_characters': [],
            'allowed_actions': [],
            'error': f'User {user_id} not found'
        }
    
    # Check if admin - always full permissions
    if user.is_superuser or user.username == 'admin':
        permission_mask = '1' * len(toolbar_string)
    else:
        # Get user's role
        # For now, assume user has a 'role' field or we get it from UserRole
        # This is a simplified implementation - you may need to adjust based on your user model
        try:
            user_role = UserRole.objects.filter(user=user, is_active=True).first()
            
            if not user_role:
                # No role assigned - deny all except common actions
                permission_mask = _get_default_mask(toolbar_string)
            else:
                # Get from RolePermission
                role_perm = RolePermission.objects.filter(
                    role=user_role.role,
                    menu_item=menu_item
                ).first()
                
                if role_perm and role_perm.toolbar_permissions:
                    permission_mask = role_perm.toolbar_permissions
                else:
                    # No permission configured - identify if this is a 'System Administrator' role
                    role_key_lower = user_role.role.role_key.lower()
                    role_name_lower = user_role.role.role_name.lower()
                    
                    if 'admin' in role_key_lower or 'admin' in role_name_lower or 'super' in role_key_lower:
                        permission_mask = '1' * len(toolbar_string)
                    else:
                        permission_mask = _get_default_mask(toolbar_string)
        except Exception as e:
            # Fallback: deny all except common actions
            permission_mask = _get_default_mask(toolbar_string)
    
    # Ensure permission_mask matches toolbar_string length
    if len(permission_mask) < len(toolbar_string):
        # Pad with 0s
        permission_mask += '0' * (len(toolbar_string) - len(permission_mask))
    elif len(permission_mask) > len(toolbar_string):
        # Truncate
        permission_mask = permission_mask[:len(toolbar_string)]
    
    # Step 3: Apply permission filter
    allowed_chars = []
    for i, char in enumerate(toolbar_string):
        if i < len(permission_mask) and permission_mask[i] == '1':
            allowed_chars.append(char)
    
    # Step 4: Apply mode law (Strict Exclusion-based resolution)
    if mode in MODE_LAW:
        exclude_list = MODE_LAW[mode].get('exclude', [])
        allowed_chars = [c for c in allowed_chars if c not in exclude_list]
    
    # Step 5: Return final result
    allowed_actions = [TOOLBAR_CHAR_MAP.get(c, c.lower()) for c in allowed_chars]
    
    print(f"DEBUG: Toolbar Resolution - User: {user.username} ({user.id}), Menu: {menu_id}, Mode: {mode}")
    print(f"DEBUG: Mask: {permission_mask}, Allowed Chars: {allowed_chars}")
    print(f"DEBUG: Final Actions: {allowed_actions}")
    
    return {
        'menu_id': menu_id,
        'mode': mode,
        'toolbar_string': toolbar_string,
        'permission_mask': permission_mask,
        'allowed_characters': allowed_chars,
        'allowed_actions': allowed_actions
    }


def _get_default_mask(toolbar_string: str) -> str:
    """
    Generate default permission mask.
    Grants permission only for common actions (S, C, K, X).
    
    Args:
        toolbar_string: Toolbar capability string
    
    Returns:
        Permission mask with 1s for common actions, 0s for others
    """
    mask = []
    for char in toolbar_string:
        if char in COMMON_ACTIONS:
            mask.append('1')
        else:
            mask.append('0')
    return ''.join(mask)


def get_role_template_permissions(role_key: str, toolbar_string: str) -> str:
    """
    Get permission mask based on role template.
    
    Args:
        role_key: Role key (e.g., 'admin', 'backofficemanager')
        toolbar_string: Toolbar capability string
    
    Returns:
        Permission mask string
    """
    # Role templates (based on screenshots)
    templates = {
        'admin': 'all',  # All 1s
        'backofficemanager': ['N', 'E', 'S', 'C', 'K', 'V', 'D', 'X', 'R', 'Q', 'F', 'I', 'O'],  # No Z, T, J, A
        'backofficeuser': ['N', 'E', 'S', 'C', 'K', 'V', 'X', 'R', 'Q', 'F'],  # Basic operations
        'posmanager': ['N', 'E', 'S', 'C', 'K', 'V', 'D', 'X', 'R', 'Q', 'F', 'I', 'O', 'Z', 'T'],
        'posuser': ['N', 'S', 'C', 'K', 'V', 'X'],  # Minimal
    }
    
    template = templates.get(role_key, [])
    
    if template == 'all':
        return '1' * len(toolbar_string)
    
    # Build mask based on template
    mask = []
    for char in toolbar_string:
        if char in template or char in COMMON_ACTIONS:
            mask.append('1')
        else:
            mask.append('0')
    
    return ''.join(mask)




