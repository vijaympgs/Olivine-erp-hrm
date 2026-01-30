import os
import sys
import django

# Setup Django Environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.base")
django.setup()

from core.auth_access.backend.user_management.models import ERPToolbarControl, ERPMenuItem

def verify_and_create_uom_menu():
    """Verify UOM menu entry exists with correct toolbar config"""
    
    print("=" * 80)
    print("UOM TOOLBAR VERIFICATION")
    print("=" * 80)
    
    # Check if RETAIL toolbar control exists
    try:
        retail_control = ERPToolbarControl.objects.get(module_name='RETAIL')
        print(f"\n✅ RETAIL Toolbar Control Found:")
        print(f"   Master String: {retail_control.master_toolbar_string}")
    except ERPToolbarControl.DoesNotExist:
        print("\n❌ RETAIL Toolbar Control NOT FOUND - Run seed_toolbar_controls.py first!")
        return
    
    # Check for UOM menu entries
    uom_entries = ERPMenuItem.objects.filter(menu_id__icontains='uom')
    
    print(f"\n📋 Found {uom_entries.count()} UOM-related menu entries:")
    for entry in uom_entries:
        print(f"\n   Menu ID: {entry.menu_id}")
        print(f"   Name: {entry.menu_name}")
        print(f"   Module: {entry.module_name}")
        print(f"   View Type: {entry.view_type}")
        print(f"   Config: {entry.applicable_toolbar_config or 'NOT SET'}")
        print(f"   Route: {entry.route_path or 'NOT SET'}")
    
    # Define the correct UOM menu entry
    uom_menu_id = "inventory_uom_setup"
    
    # Check if it exists
    try:
        uom_menu = ERPMenuItem.objects.get(menu_id=uom_menu_id)
        print(f"\n✅ UOM Menu Entry Found: {uom_menu.menu_id}")
        
        # Verify configuration
        expected_config = "NESCKVDXRQF"  # Masters (Advanced): New, Edit, Save, Cancel, Clear, View, Delete, Exit, Refresh, Search, Filter
        
        if uom_menu.applicable_toolbar_config != expected_config:
            print(f"\n⚠️  Config Mismatch!")
            print(f"   Current: {uom_menu.applicable_toolbar_config}")
            print(f"   Expected: {expected_config}")
            
            # Update it
            uom_menu.applicable_toolbar_config = expected_config
            uom_menu.original_toolbar_string = retail_control.master_toolbar_string
            uom_menu.save()
            print(f"   ✅ Updated to: {expected_config}")
        else:
            print(f"   ✅ Config is correct: {expected_config}")
            
    except ERPMenuItem.DoesNotExist:
        print(f"\n❌ UOM Menu Entry NOT FOUND: {uom_menu_id}")
        print(f"   Creating new entry...")
        
        # Create the entry
        uom_menu = ERPMenuItem.objects.create(
            menu_id=uom_menu_id,
            menu_name="UOM Setup",
            module_name="RETAIL",
            submodule="INVENTORY",
            view_type="MASTER",
            route_path="/inventory/uoms",
            component_name="UOMSetup",
            applicable_toolbar_config="NESCKVDXRQF",
            original_toolbar_string=retail_control.master_toolbar_string,
            is_active=True,
            is_system_menu=True,
            menu_order=10,
            description="Unit of Measure master data management"
        )
        print(f"   ✅ Created: {uom_menu.menu_id}")
        print(f"   Config: {uom_menu.applicable_toolbar_config}")
    
    # Character mapping explanation
    print("\n" + "=" * 80)
    print("CHARACTER MAPPING FOR UOM (Masters - Advanced)")
    print("=" * 80)
    print("N - New (F2)")
    print("E - Edit (F3)")
    print("S - Save (F8)")
    print("C - Cancel (Esc)")
    print("K - Clear (F5)")
    print("V - View (F7)")
    print("D - Delete (F4)")
    print("X - Exit (Esc)")
    print("R - Refresh (F9)")
    print("Q - Search (Ctrl+F)")
    print("F - Filter (Alt+F)")
    print("=" * 80)
    
    # Additional entries to check
    print("\n📝 Checking for other common UOM-related entries...")
    
    common_ids = [
        "uom",
        "uom_setup",
        "uom-setup",
        "inventory-uom",
        "inventory_uom"
    ]
    
    for menu_id in common_ids:
        if menu_id != uom_menu_id:
            exists = ERPMenuItem.objects.filter(menu_id=menu_id).exists()
            if exists:
                print(f"   ⚠️  Duplicate found: {menu_id} (consider removing)")
    
    print("\n✅ Verification Complete!")
    print(f"\n🎯 Frontend should use: viewId=\"{uom_menu_id}\"")
    print("=" * 80)

if __name__ == "__main__":
    verify_and_create_uom_menu()




