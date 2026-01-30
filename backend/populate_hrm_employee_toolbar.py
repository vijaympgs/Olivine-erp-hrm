"""
Script to populate toolbar columns for HRM_EMPLOYEE_MASTER menu item
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def populate_hrm_employee_toolbar():
    """Populate toolbar columns for HRM_EMPLOYEE_MASTER"""
    try:
        menu_item = ERPMenuItem.objects.get(menu_id='HRM_EMPLOYEE_MASTER')
        
        # Set mode-specific toolbar configurations
        menu_item.toolbar_list = 'NRQFVIOX'  # New, Refresh, Query, Filter, View, Import, Export, Exit
        menu_item.toolbar_view = 'X'  # Exit only
        menu_item.toolbar_edit = 'SCX'  # Save, Cancel, Exit
        menu_item.toolbar_create = 'SCX'  # Save, Cancel, Exit
        
        menu_item.save()
        
        print("✅ Successfully populated toolbar columns for HRM_EMPLOYEE_MASTER:")
        print(f"   toolbar_list: {menu_item.toolbar_list}")
        print(f"   toolbar_view: {menu_item.toolbar_view}")
        print(f"   toolbar_edit: {menu_item.toolbar_edit}")
        print(f"   toolbar_create: {menu_item.toolbar_create}")
        
    except ERPMenuItem.DoesNotExist:
        print("❌ Error: HRM_EMPLOYEE_MASTER menu item not found")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    populate_hrm_employee_toolbar()
