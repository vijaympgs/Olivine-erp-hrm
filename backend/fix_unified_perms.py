import os
import sys
import django

# Setup path to project root
current_dir = os.path.dirname(os.path.abspath(__file__)) # backend/
project_root = os.path.dirname(current_dir) # c:\00mindra\olivine-platform
sys.path.insert(0, project_root)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.erp_core.settings')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem, RolePermission, Role

def fix_permissions(menu_id):
    print(f"Configuring permissions for: {menu_id}")
    try:
        # Get or Create Menu Item (Ensure it exists)
        menu_item, created = ERPMenuItem.objects.get_or_create(
            menu_id=menu_id,
            defaults={
                'menu_name': 'Employee Master',
                'module_name': 'HRM', 
                'view_type': 'MASTER',
                'toolbar_config': 'NESCKVDXRQFIO',
                'is_active': True
            }
        )
        if created:
            print(f"Created missing menu item: {menu_id}")
        else:
            print(f"Found existing menu item: {menu_id}")

        # Reset Permissions
        deleted_count, _ = RolePermission.objects.filter(menu_item=menu_item).delete()
        print(f"Cleared {deleted_count} existing permission overrides.")

        # Grant Full Access to System Administrator
        admin_role = Role.objects.filter(name='System Administrator').first()
        if admin_role:
            RolePermission.objects.create(
                role=admin_role,
                menu_item=menu_item,
                permission_mask='NESCKVDXRQFIO', # Full Access
                is_active=True
            )
            print(f"Granted FULL permissions to System Administrator for {menu_id}")
        else:
            print("Warning: 'System Administrator' role not found.")

    except Exception as e:
        print(f"Error processing {menu_id}: {str(e)}")

if __name__ == '__main__':
    # Fix the standard ID
    fix_permissions('HRM_EMPLOYEE_MASTER')
    # Also ensure the legacy ID works as a fallback
    fix_permissions('HRM_EMPLOYEE_RECORDS')
