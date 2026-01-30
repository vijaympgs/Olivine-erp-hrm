#!/usr/bin/env python
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
django.setup()

def add_missing_hrm_menu_items():
    """Add missing HRM menu items to ERPMenuItem table"""
    
    from core.auth_access.backend.user_management.models import ERPMenuItem
    
    print("ADDING MISSING HRM MENU ITEMS")
    print("=" * 80)
    
    # Define the missing menu items
    missing_items = [
        {
            'menu_id': 'HRM_EMPLOYEE_SELF_SERVICE',
            'menu_name': 'Employee Self-Service',
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF',  # Standard Master config
            'module': 'HRM',
            'is_active': True,
            'route_path': '/hr/employees/self-service'
        },
        {
            'menu_id': 'HRM_DOCUMENT_MANAGEMENT',
            'menu_name': 'Document Management',
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF',  # Standard Master config
            'module': 'HRM',
            'is_active': True,
            'route_path': '/hr/employees/documents'
        },
        {
            'menu_id': 'HRM_EMPLOYEE_LIFECYCLE',
            'menu_name': 'Employee Lifecycle',
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF',  # Standard Master config
            'module': 'HRM',
            'is_active': True,
            'route_path': '/hr/employees/lifecycle'
        }
    ]
    
    # Check existing HRM items
    print("Checking existing HRM menu items...")
    existing_hrm_items = ERPMenuItem.objects.filter(menu_id__startswith='HRM')
    print(f"Found {existing_hrm_items.count()} existing HRM menu items:")
    for item in existing_hrm_items:
        print(f"  {item.menu_id} - {item.menu_name}")
    
    print("\nAdding missing menu items...")
    
    added_count = 0
    for item_data in missing_items:
        menu_id = item_data['menu_id']
        
        # Check if item already exists
        existing_item = ERPMenuItem.objects.filter(menu_id=menu_id).first()
        if existing_item:
            print(f"⚠️  {menu_id} already exists - skipping")
            continue
        
        # Create the menu item
        try:
            ERPMenuItem.objects.create(**item_data)
            print(f"✅ Created {menu_id} - {item_data['menu_name']}")
            added_count += 1
        except Exception as e:
            print(f"❌ Failed to create {menu_id}: {str(e)}")
    
    print(f"\nSummary: Added {added_count} new menu items")
    
    # Verify all HRM items
    print("\nAll HRM menu items after update:")
    all_hrm_items = ERPMenuItem.objects.filter(menu_id__startswith='HRM').order_by('menu_id')
    for item in all_hrm_items:
        status = "✅" if item.is_active else "❌"
        print(f"  {status} {item.menu_id} - {item.menu_name} ({item.view_type})")

if __name__ == '__main__':
    add_missing_hrm_menu_items()
