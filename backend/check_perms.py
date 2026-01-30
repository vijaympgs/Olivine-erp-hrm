from core.auth_access.backend.user_management.models import ERPMenuItem, RolePermission, UserRole
from django.contrib.auth.models import User

def check_permissions():
    menu_id = 'INVENTORY_UOM_SETUP'
    print(f"\nChecking permissions for: {menu_id}")
    
    # 1. Check Menu Item
    try:
        item = ERPMenuItem.objects.get(menu_id=menu_id)
        print(f"✅ Menu Item Found: {item.menu_name}")
        print(f"   Applicable Toolbar: {item.applicable_toolbar_config}")
    except ERPMenuItem.DoesNotExist:
        print(f"❌ Menu Item NOT FOUND")
        return

    # 2. Check Admin User Roles
    try:
        user = User.objects.get(username='admin')
        print(f"✅ User Found: {user.username}")
        # Use UserRole mapping
        user_roles = UserRole.objects.filter(user=user, is_active=True)
        roles = [ur.role for ur in user_roles]
        print(f"   Active Roles Mapping: {[role.role_name for role in roles]}")
        
        if not roles:
            print("   ⚠️ User has NO active roles!")
            return

        # 3. Check Role Permissions
        for role in roles:
            perms = RolePermission.objects.filter(role=role, menu_item=item)
            if perms.exists():
                for p in perms:
                    print(f"   ✅ Permission found for role [{role.role_name}]:")
                    print(f"      Toolbar String: {getattr(p, 'toolbar_string', 'NOT SET')}")
                    print(f"      Toolbar Masks: {getattr(p, 'toolbar_permissions', 'NOT SET')}")
            else:
                print(f"   ❌ No RolePermission record for role [{role.role_name}] on this item")
                
    except User.DoesNotExist:
        print(f"❌ User 'admin' not found")

if __name__ == "__main__":
    check_permissions()




