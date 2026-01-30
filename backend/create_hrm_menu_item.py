#!/usr/bin/env python
import os
import sys

# Add the backend directory to Python path
backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

# Change to backend directory
os.chdir(backend_dir)

# Import Django management utility
import django
from django.core.management import execute_from_command_line

def create_hrm_menu_item():
    """Create HRM_EMPLOYEE_RECORDS menu item using Django management commands"""
    
    # Setup Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
    django.setup()
    
    from core.auth_access.backend.user_management.models import ERPMenuItem
    
    print("CHECKING HRM_EMPLOYEE_RECORDS MENU ITEM")
    print("=" * 80)
    
    # Check if menu item exists
    item = ERPMenuItem.objects.filter(menu_id='HRM_EMPLOYEE_RECORDS').first()
    if item:
        print("FOUND HRM_EMPLOYEE_RECORDS:")
        print(f"  Menu ID: {item.menu_id}")
        print(f"  Menu Name: {item.menu_name}")
        print(f"  View Type: {item.view_type}")
        print(f"  Toolbar Config: {item.applicable_toolbar_config}")
        print(f"  Module: {item.module}")
        print(f"  Is Active: {item.is_active}")
        return
    
    print("HRM_EMPLOYEE_RECORDS NOT FOUND")
    print("\nAvailable HRM items:")
    hrm_items = ERPMenuItem.objects.filter(menu_id__startswith='HRM')
    for i in hrm_items:
        print(f"  {i.menu_id} - {i.menu_name}")
    
    print("\nCreating HRM_EMPLOYEE_RECORDS menu item...")
    
    # Create the menu item
    ERPMenuItem.objects.create(
        menu_id='HRM_EMPLOYEE_RECORDS',
        menu_name='Employee Records',
        view_type='MASTER',
        applicable_toolbar_config='NESCKVDXRQFIO',  # Advanced Master config
        module='HRM',
        is_active=True,
        route_path='/hr/employees/records'
    )
    print("Created HRM_EMPLOYEE_RECORDS menu item successfully!")

if __name__ == '__main__':
    create_hrm_menu_item()
