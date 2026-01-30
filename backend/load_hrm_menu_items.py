#!/usr/bin/env python
import os
import sys

# Add the backend directory to Python path
backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

# Change to backend directory
os.chdir(backend_dir)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
import django
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def load_hrm_menu_items():
    """Load HRM menu items"""
    
    print("LOADING HRM MENU ITEMS")
    print("=" * 50)
    
    # HRM menu items to create
    hrm_items = [
        {
            'menu_id': 'HRM_EMPLOYEE_RECORDS',
            'menu_name': 'Employee Records',
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQFIO',
            'module': 'HRM',
            'is_active': True,
            'route_path': '/hr/employees/records'
        },
        {
            'menu_id': 'HRM_EMPLOYEE_DIRECTORY',
            'menu_name': 'Employee Directory',
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF',
            'module': 'HRM',
            'is_active': True,
            'route_path': '/hr/employees/directory'
        },
        {
            'menu_id': 'HRM_ORGANIZATION_CHART',
            'menu_name': 'Organization Chart',
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'VRXPYQFG',
            'module': 'HRM',
            'is_active': True,
            'route_path': '/hr/organization/chart'
        },
        {
            'menu_id': 'HRM_DEPARTMENTS',
            'menu_name': 'Departments',
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF',
            'module': 'HRM',
            'is_active': True,
            'route_path': '/hr/departments'
        },
        {
            'menu_id': 'HRM_DESIGNATIONS',
            'menu_name': 'Designations',
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF',
            'module': 'HRM',
            'is_active': True,
            'route_path': '/hr/designations'
        }
    ]
    
    created_count = 0
    updated_count = 0
    
    for item_data in hrm_items:
        menu_id = item_data['menu_id']
        item, created = ERPMenuItem.objects.update_or_create(
            menu_id=menu_id,
            defaults=item_data
        )
        
        if created:
            print(f"✅ Created: {menu_id}")
            created_count += 1
        else:
            print(f"🔄 Updated: {menu_id}")
            updated_count += 1
    
    print(f"\nSummary: {created_count} created, {updated_count} updated")
    
    # Show all HRM items
    print(f"\nAll HRM Menu Items:")
    hrm_items = ERPMenuItem.objects.filter(module='HRM')
    for item in hrm_items:
        print(f"  {item.menu_id} - {item.menu_name} ({item.applicable_toolbar_config})")

if __name__ == '__main__':
    load_hrm_menu_items()
