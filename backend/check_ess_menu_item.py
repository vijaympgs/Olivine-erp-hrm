import os
import sys
import django

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')

try:
    django.setup()
    
    from core.auth_access.backend.user_management.models import ERPMenuItem
    
    # Check ESS menu item
    ess_menu = ERPMenuItem.objects.filter(menu_id='HRM_EMPLOYEE_SELF_SERVICE').first()
    
    if ess_menu:
        print("=== Current ESS Menu Item Configuration ===")
        print(f"Menu ID: {ess_menu.menu_id}")
        print(f"Menu Name: {ess_menu.menu_name}")
        print(f"Route Path: {ess_menu.route_path}")
        print(f"Toolbar Config: {ess_menu.toolbar_config}")
        print(f"Applicable Toolbar Config: {ess_menu.applicable_toolbar_config}")
        print(f"Component Name: {ess_menu.component_name}")
        print(f"View Type: {ess_menu.view_type}")
        print(f"Is Active: {ess_menu.is_active}")
        print()
        
        # Check if toolbar config is properly set
        if not ess_menu.toolbar_config:
            print("❌ Toolbar Config is EMPTY - needs to be updated")
        else:
            print(f"✅ Toolbar Config: {ess_menu.toolbar_config}")
            
    else:
        print("❌ ESS menu item not found! Creating new entry...")
        
        # Find HRM parent menu
        hrm_parent = ERPMenuItem.objects.filter(menu_id='HRM').first()
        if not hrm_parent:
            print("❌ HRM parent menu not found!")
            sys.exit(1)
            
        # Create ESS menu item
        ess_menu = ERPMenuItem.objects.create(
            menu_id='HRM_EMPLOYEE_SELF_SERVICE',
            menu_name='Employee Self Service',
            route_path='/hr/employees/self-service',
            toolbar_config='NESCKVDXRQF',  # New, Edit, Save, Close, Delete, Export, Refresh, Search, View, Delete, Print, Export, Filter
            applicable_toolbar_config='NESCKVDXRQF',
            component_name='EmployeeSelfService',
            view_type='ESS',
            parent=hrm_parent,
            sort_order=15,
            is_active=True,
            icon='User'
        )
        
        print("✅ ESS menu item created successfully!")
        print(f"Menu ID: {ess_menu.menu_id}")
        print(f"Menu Name: {ess_menu.menu_name}")
        print(f"Route Path: {ess_menu.route_path}")
        print(f"Toolbar Config: {ess_menu.toolbar_config}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
