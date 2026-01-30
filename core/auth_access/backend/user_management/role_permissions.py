"""
Role Permission Templates
Defines default permissions for each role.
Ported from 01practice-v2.
"""

ROLE_PERMISSION_TEMPLATES = {
    'admin': {
        'display_name': 'Administrator',
        'description': 'Full access to all modules',
        'menu_items': {
            'user_permissions': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'master_data': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'inventory': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'procurement': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'sales': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'pos': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'reports': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'system_settings': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
        }
    },
    'posmanager': {
        'display_name': 'POS Manager',
        'description': 'Full POS management',
        'menu_items': {
            'pos': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'master_data': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': False, 'can_delete': False},
        }
    },
    'posuser': {
        'display_name': 'POS User',
        'description': 'POS Billing and Settlement',
        'menu_items': {
            'pos': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': False},
        }
    },
    'backofficemanager': {
        'display_name': 'Back Office Manager',
        'description': 'Full access to Back Office operations',
        'menu_items': {
            'master_data': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'inventory': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'procurement': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
            'sales': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': True},
        }
    },
    'backofficeuser': {
        'display_name': 'Back Office User',
        'description': 'Back office operations with limited edit',
        'menu_items': {
            'master_data': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': False, 'can_delete': False},
            'inventory': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': False},
            'procurement': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': False},
            'sales': {'can_access': True, 'can_view': True, 'can_create': True, 'can_edit': True, 'can_delete': False},
        }
    },
}

def get_role_permissions(role):
    return ROLE_PERMISSION_TEMPLATES.get(role, {})

def apply_role_template_to_user(user, role_template=None):
    from .models import UserProfile
    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        return {}
        
    role_to_use = role_template or profile.role
    template = get_role_permissions(role_to_use)
    if not template:
        return {}
    
    permissions = {}
    for menu_item_id, perms in template.get('menu_items', {}).items():
        permissions[menu_item_id] = perms.copy()
    
    return permissions




