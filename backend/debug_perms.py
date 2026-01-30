from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.models import ERPMenuItem, UserRole, RolePermission

User = get_user_model()
print("--- START DEBUG ---")
users = User.objects.all()
for u in users:
    print(f"User: {u.username}")
    role_entry = UserRole.objects.filter(user=u).first()
    if role_entry:
        print(f"  Role: {role_entry.role.role_name} ({role_entry.role.role_key})")
        
        # Check Item
        item = ERPMenuItem.objects.filter(menu_id='HRM_EMPLOYEE_RECORDS').first()
        if item:
            perm = RolePermission.objects.filter(role=role_entry.role, menu_item=item).first()
            if perm:
                print(f"  RolePerm found. Mask: {perm.toolbar_permissions}")
            else:
                print("  No RolePermission found for this item.")
        else:
            print("  Item 'HRM_EMPLOYEE_RECORDS' not found.")
    else:
        print("  No UserRole found.")
print("--- END DEBUG ---")
