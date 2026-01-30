from core.auth_access.backend.user_management.models import RolePermission, ERPMenuItem, UserRole
from django.contrib.auth import get_user_model

try:
    menu_item = ERPMenuItem.objects.get(menu_id='HRM_EMPLOYEE_RECORDS')
    print(f"Menu Item Config: {menu_item.applicable_toolbar_config}")
    
    # 1. Update existing permissions
    perms = RolePermission.objects.filter(menu_item=menu_item)
    for p in perms:
        old = p.toolbar_permissions
        # Grant full access (1111...)
        new_perm = '1' * len(menu_item.applicable_toolbar_config)
        p.toolbar_permissions = new_perm
        p.save()
        print(f"Updated role {p.role.role_name}: {old} -> {new_perm}")

    # 2. Check the mystery user
    User = get_user_model()
    # Find any user with 'd73f' in username/id/email?
    # This part is just for my info, but won't show in log unless I read stdout/run directly.
    
except Exception as e:
    print(f"Error: {e}")
