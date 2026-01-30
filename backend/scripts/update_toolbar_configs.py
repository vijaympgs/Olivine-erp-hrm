import os
import sys
import django

# Setup Django Environment (same as seed_toolbar_controls.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.base")
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def update_toolbar_configs():
    """Update toolbar configurations for 4 specific menu items"""
    
    updates = [
        {
            'menu_id': 'MOVEMENT_TYPES',
            'new_config': 'NRQFX',
            'description': 'Movement Types (List view)'
        },
        {
            'menu_id': 'VALUATION_METHODS',
            'new_config': 'VRX',
            'description': 'Valuation Methods (View only)'
        },
        {
            'menu_id': 'INV_PARAMETERS',
            'new_config': 'ESCKXR',
            'description': 'Inventory Parameters (Edit-focused)'
        },
        {
            'menu_id': 'APPROVAL_RULES',
            'new_config': 'NRQFX',
            'description': 'Approval Rules (List view)'
        }
    ]
    
    print("=" * 80)
    print("TOOLBAR CONFIGURATION UPDATE")
    print("=" * 80)
    print()
    
    for update in updates:
        try:
            menu_item = ERPMenuItem.objects.get(menu_id=update['menu_id'])
            old_config = menu_item.applicable_toolbar_config or 'None'
            
            print(f"📋 {update['description']}")
            print(f"   Menu ID: {update['menu_id']}")
            print(f"   Current: {old_config}")
            print(f"   New: {update['new_config']}")
            
            menu_item.applicable_toolbar_config = update['new_config']
            menu_item.save()
            
            print(f"   ✅ Updated successfully")
            print()
            
        except ERPMenuItem.DoesNotExist:
            print(f"❌ Menu item not found: {update['menu_id']}")
            print()
        except Exception as e:
            print(f"❌ Error updating {update['menu_id']}: {e}")
            print()
    
    print("=" * 80)
    print("UPDATE COMPLETE")
    print("=" * 80)
    print()
    
    # Verify updates
    print("VERIFICATION:")
    print("-" * 80)
    for update in updates:
        try:
            menu_item = ERPMenuItem.objects.get(menu_id=update['menu_id'])
            if menu_item.applicable_toolbar_config == update['new_config']:
                print(f"✅ {update['menu_id']}: {menu_item.applicable_toolbar_config}")
            else:
                print(f"❌ {update['menu_id']}: {menu_item.applicable_toolbar_config} (expected {update['new_config']})")
        except ERPMenuItem.DoesNotExist:
            print(f"❌ {update['menu_id']}: NOT FOUND")

if __name__ == "__main__":
    update_toolbar_configs()




