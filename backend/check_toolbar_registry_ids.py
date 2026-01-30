#!/usr/bin/env python
"""
Toolbar Registry ID Checker
===========================

This script queries the ERPMenuItem table to find the correct toolbar registry IDs
for all HRM modules. Use this to verify the correct menu_id values before implementing
toolbar functionality.

Usage:
    python check_toolbar_registry_ids.py                    # List all HRM menu items
    python check_toolbar_registry_ids.py <pattern>         # Search for specific menu
    python check_toolbar_registry_ids.py <menu_id>         # Check specific menu_id

Examples:
    python check_toolbar_registry_ids.py
    python check_toolbar_registry_ids.py Employee
    python check_toolbar_registry_ids.py HRM_EMPLOYEE_SELF_SERVICE

Output:
    - Lists all HRM menu items with their toolbar registry strings
    - Shows the correct menu_id to use in frontend MasterToolbar components
    - Identifies any missing or inconsistent toolbar configurations
    - Provides implementation examples for frontend and backend
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
django.setup()

def check_toolbar_registry_ids():
    """Check toolbar registry IDs from ERPMenuItem table"""
    
    try:
        from core.models import ERPMenuItem
        
        print("🔍 Toolbar Registry ID Checker")
        print("=" * 50)
        print()
        
        # Query all HRM menu items
        hrm_menu_items = ERPMenuItem.objects.filter(
            module_name__in=['HRM', 'Human Resources']
        ).order_by('menu_name')
        
        if not hrm_menu_items.exists():
            print("❌ No HRM menu items found in ERPMenuItem table")
            print()
            print("💡 Suggestions:")
            print("   1. Check if the module_name is correct (try 'HRM', 'Human Resources', etc.)")
            print("   2. Verify the ERPMenuItem table has been populated")
            print("   3. Run the menu item creation scripts")
            return
        
        print(f"📋 Found {hrm_menu_items.count()} HRM menu items:")
        print()
        
        # Display all HRM menu items
        for item in hrm_menu_items:
            menu_id = item.menu_name.upper().replace(' ', '_')
            print(f"🏷️  Menu Name: {item.menu_name}")
            print(f"🆔 Menu ID: {menu_id}")
            print(f"📍 Route URL: {item.route_url}")
            print(f"🔧 Toolbar Registry: {item.toolbar_registry_string or 'NOT SET'}")
            print(f"📂 Module: {item.module_name}")
            print("-" * 40)
        
        print()
        print("🎯 Frontend Implementation Guide:")
        print("=" * 30)
        print()
        
        # Show frontend implementation examples
        for item in hrm_menu_items:
            if item.toolbar_registry_string:
                menu_id = item.menu_name.upper().replace(' ', '_')
                print(f"// {item.menu_name}")
                print(f'<MasterToolbar')
                print(f'  viewId="{menu_id}"')
                print(f'  mode={getMode()}')
                print(f'  onAction={handleToolbarAction}')
                print(f'/>')
                print()
        
        print("🔧 Backend Implementation Guide:")
        print("=" * 35)
        print()
        
        # Show backend implementation examples
        for item in hrm_menu_items:
            if item.toolbar_registry_string:
                menu_id = item.menu_name.upper().replace(' ', '_')
                print(f"# {item.menu_name}")
                print(f'if menu_id == \'{menu_id}\':')
                print(f'    # Configure permissions for {menu_id}')
                print(f'    permissions = {{')
                print(f'        "toolbar_string": "{item.toolbar_registry_string}",')
                print(f'        "new": True, "edit": True, "view": True, "delete": True,')
                print(f'        # ... other permissions')
                print(f'    }}')
                print()
        
        # Check for missing toolbar configurations
        missing_toolbar = hrm_menu_items.filter(toolbar_registry_string__isnull=True)
        if missing_toolbar.exists():
            print("⚠️  Missing Toolbar Configurations:")
            print("=" * 40)
            for item in missing_toolbar:
                print(f"❌ {item.menu_name} - No toolbar registry string set")
            print()
        
        # Check for potential duplicates
        menu_names = list(hrm_menu_items.values_list('menu_name', flat=True))
        duplicates = []
        seen = set()
        
        for name in menu_names:
            if name in seen:
                duplicates.append(name)
            seen.add(name)
        
        if duplicates:
            print("🔄 Duplicate Menu Names Found:")
            print("=" * 35)
            for dup in duplicates:
                print(f"⚠️  '{dup}' appears multiple times")
            print()
        
        print("✅ Toolbar Registry ID Check Complete!")
        print()
        print("💡 Next Steps:")
        print("   1. Use the correct menu_id in your frontend MasterToolbar component")
        print("   2. Update backend toolbar_views.py to handle the correct menu_id")
        print("   3. Test the toolbar permissions endpoint")
        print("   4. Verify toolbar buttons appear correctly")
        
    except Exception as e:
        print(f"❌ Error checking toolbar registry IDs: {str(e)}")
        print()
        print("🔧 Troubleshooting:")
        print("   1. Ensure Django is properly configured")
        print("   2. Check if the core.models.ERPMenuItem exists")
        print("   3. Verify database connection")
        print("   4. Run migrations: python manage.py migrate")
        return False
    
    return True

def check_specific_pattern(pattern):
    """Check menu items matching a specific pattern"""
    
    try:
        from core.models import ERPMenuItem
        
        print(f"🔍 Searching for menu items matching: {pattern}")
        print("=" * 50)
        print()
        
        # Search for menu items containing the pattern
        matching_items = ERPMenuItem.objects.filter(
            menu_name__icontains=pattern
        ).order_by('menu_name')
        
        if not matching_items.exists():
            print(f"❌ No menu items found matching '{pattern}'")
            print()
            print("💡 Try these patterns:")
            print("   - 'Employee'")
            print("   - 'Self Service'")
            print("   - 'Service'")
            print("   - 'Request'")
            return
        
        for item in matching_items:
            menu_id = item.menu_name.upper().replace(' ', '_')
            print(f"🏷️  Menu Name: {item.menu_name}")
            print(f"🆔 Menu ID: {menu_id}")
            print(f"📍 Route URL: {item.route_url}")
            print(f"🔧 Toolbar Registry: {item.toolbar_registry_string or 'NOT SET'}")
            print(f"📂 Module: {item.module_name}")
            print("-" * 40)
        
        # Show the correct implementation
        if matching_items.exists():
            item = matching_items.first()
            if item.toolbar_registry_string:
                menu_id = item.menu_name.upper().replace(' ', '_')
                print()
                print("🎯 Correct Implementation:")
                print("=" * 25)
                print()
                print("Frontend:")
                print(f'<MasterToolbar viewId="{menu_id}" mode={getMode()} />')
                print()
                print("Backend:")
                print(f'if menu_id == \'{menu_id}\':')
                print(f'    # Configure permissions')
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False
    
    return True

def check_specific_menu_id(menu_id):
    """Check a specific menu_id configuration"""
    
    try:
        from core.models import ERPMenuItem
        
        print(f"🔍 Checking menu_id: {menu_id}")
        print("=" * 50)
        print()
        
        # Try to find by menu_id field first
        try:
            item = ERPMenuItem.objects.get(menu_id=menu_id)
        except ERPMenuItem.DoesNotExist:
            # Try to find by menu_name converted to menu_id format
            item = ERPMenuItem.objects.get(
                menu_name=menu_id.replace('_', ' ').title()
            )
        
        print(f"✅ Found: {item.menu_name}")
        print(f"🆔 Menu ID: {menu_id}")
        print(f"📍 Route URL: {item.route_url}")
        print(f"🔧 Toolbar Registry: {item.toolbar_registry_string or 'NOT SET'}")
        print(f"📂 Module: {item.module_name}")
        print(f"🟢 Is Active: {getattr(item, 'is_active', 'N/A')}")
        
        if item.toolbar_registry_string:
            print()
            print("🎯 Implementation:")
            print("=" * 20)
            print()
            print("Frontend:")
            print(f'<MasterToolbar viewId="{menu_id}" mode={getMode()} />')
            print()
            print("Backend:")
            print(f'if menu_id == \'{menu_id}\':')
            print(f'    permissions = {{')
            print(f'        "toolbar_string": "{item.toolbar_registry_string}",')
            print(f'        "new": True, "edit": True, "view": True, "delete": True')
            print(f'    }}')
        
        return item
        
    except ERPMenuItem.DoesNotExist:
        print(f"❌ Menu ID '{menu_id}' not found in ERPMenuItem table")
        print()
        print("📋 Available HRM menu items:")
        try:
            hrm_items = ERPMenuItem.objects.filter(
                module_name__in=['HRM', 'Human Resources']
            )
            for item in hrm_items:
                menu_id = item.menu_name.upper().replace(' ', '_')
                print(f"  - {menu_id}: {item.menu_name}")
        except Exception as e:
            print(f"  Error listing items: {str(e)}")
        return None
        
    except Exception as e:
        print(f"❌ Error checking menu_id: {str(e)}")
        return None

def list_all_menu_ids():
    """List all available menu_ids in the system"""
    
    try:
        from core.models import ERPMenuItem
        
        print("📋 All Available Menu IDs:")
        print("=" * 30)
        print()
        
        all_items = ERPMenuItem.objects.all().order_by('module_name', 'menu_name')
        
        if not all_items.exists():
            print("❌ No menu items found in ERPMenuItem table")
            return
        
        current_module = None
        for item in all_items:
            if item.module_name != current_module:
                if current_module:
                    print()
                print(f"📂 {item.module_name}:")
                current_module = item.module_name
            
            menu_id = item.menu_name.upper().replace(' ', '_')
            status = "✅" if item.toolbar_registry_string else "❌"
            print(f"  {status} {menu_id}: {item.menu_name}")
        
    except Exception as e:
        print(f"❌ Error listing menu IDs: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if arg.upper() == "--ALL":
            # List all menu IDs
            list_all_menu_ids()
        elif "_" in arg and arg.replace("_", "").isalnum():
            # Looks like a menu_id format
            check_specific_menu_id(arg)
        else:
            # Treat as search pattern
            check_specific_pattern(arg)
    else:
        # Check all HRM menu items
        check_toolbar_registry_ids()
