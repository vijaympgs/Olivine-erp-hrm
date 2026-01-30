import os
import sys
import django

# Add project root to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.erp_core.settings')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem, RolePermission, Role

def fix_form_permissions():
    menu_id = 'HRM_EMPLOYEE_MASTER'
    print(f"Fixing permissions for {menu_id}...")
    
    try:
        menu_item = ERPMenuItem.objects.get(menu_id=menu_id)
        print(f"Found menu item: {menu_item.menu_name}")
        
        # Reset RolePermissions
        count = RolePermission.objects.filter(menu_item=menu_item).delete()
        print(f"Deleted {count[0]} existing role permissions")
        
        # We rely on default mask if no RolePermission exists
        # Default mask for NEW mode grants S, C, K, X.
        
        # However, to be safe, let's create a permissive one for System Administrator
        admin_role = Role.objects.filter(name='System Administrator').first()
        if admin_role:
             # Full permission mask
            all_perms = 'NESCKVDXRQFIO' 
            rp = RolePermission.objects.create(
                role=admin_role,
                menu_item=menu_item,
                permission_mask=all_perms,
                is_active=True
            )
            print(f"Created Admin permission: {rp.permission_mask}")
            
    except ERPMenuItem.DoesNotExist:
        print(f"ERROR: {menu_id} does not exist in ERPMenuItem table!")
        print("Please verify the menu_id used in frontend matches backend.")

if __name__ == '__main__':
    fix_form_permissions()
