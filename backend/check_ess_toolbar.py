import os
import sys
import django

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

try:
    django.setup()
    
    from core.auth_access.backend.user_management.models import ERPMenuItem
    
    # Check ESS menu item
    ess_menu = ERPMenuItem.objects.filter(menu_id='HRM_EMPLOYEE_SELF_SERVICE').first()
    
    if ess_menu:
        print("=== ESS Toolbar Configuration ===")
        print(f"Menu ID: {ess_menu.menu_id}")
        print(f"Menu Name: {ess_menu.menu_name}")
        print(f"Route Path: {ess_menu.route_path}")
        print(f"Toolbar Config: {ess_menu.toolbar_config}")
        print(f"Applicable Toolbar Config: {ess_menu.applicable_toolbar_config}")
        print(f"Component Name: {ess_menu.component_name}")
        print(f"View Type: {ess_menu.view_type}")
        print(f"Is Active: {ess_menu.is_active}")
        print()
        
        # Check toolbar controls
        from core.auth_access.backend.user_management.models import ERPToolbarControl
        
        toolbar_controls = ERPToolbarControl.objects.filter(
            control_id__in=list(ess_menu.toolbar_config)
        ).order_by('control_id')
        
        print("=== Available Toolbar Controls ===")
        for control in toolbar_controls:
            print(f"{control.control_id}: {control.control_name} ({control.control_type})")
        
    else:
        print("ESS menu item not found!")
        
except Exception as e:
    print(f"Error: {e}")
