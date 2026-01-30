"""
Toolbar Configuration Update Script
Updates 4 menu items with correct toolbar strings as per toolbar-revisit-checklist.md
"""

import os
import django
import sys

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'domain.master.settings')
django.setup()

from core.auth_access.backend.menu_registry.models import ERPMenuItem

def update_toolbar_configs():
    """Update toolbar configurations for 4 specific menu items"""
    
    updates = [
        {
            'menu_id': 'MOVEMENT_TYPES',
            'old_config': None,  # Will check current value
            'new_config': 'NRQFX',  # List view: New, Refresh, Search, Filter, Exit
            'description': 'Movement Types (List view)'
        },
        {
            'menu_id': 'VALUATION_METHODS',
            'old_config': None,
            'new_config': 'VRX',  # View, Refresh, Exit only
            'description': 'Valuation Methods (View only)'
        },
        {
            'menu_id': 'INV_PARAMETERS',
            'old_config': None,
            'new_config': 'ESCKXR',  # Edit, Save, Cancel, Clear, Exit, Refresh
            'description': 'Inventory Parameters (Edit-focused)'
        },
        {
            'menu_id': 'APPROVAL_RULES',
            'old_config': None,
            'new_config': 'NRQFX',  # List view: New, Refresh, Search, Filter, Exit
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
            
            print(f"📋 {update['description']}")
            print(f"   Menu ID: {update['menu_id']}")
            print(f"   Current Config: {menu_item.applicable_toolbar_config or 'None'}")
            print(f"   New Config: {update['new_config']}")
            
            # Update the configuration
            menu_item.applicable_toolbar_config = update['new_config']
            menu_item.save()
            
            print(f"   ✅ Updated successfully")
            print()
            
        except ERPMenuItem.DoesNotExist:
            print(f"❌ Menu item not found: {update['menu_id']}")
            print(f"   Creating new entry...")
            
            # Try to create it (though it should exist)
            try:
                menu_item = ERPMenuItem.objects.create(
                    menu_id=update['menu_id'],
                    label=update['description'],
                    applicable_toolbar_config=update['new_config'],
                    module='RETAIL'
                )
                print(f"   ✅ Created successfully")
            except Exception as e:
                print(f"   ❌ Error creating: {e}")
            print()
        
        except Exception as e:
            print(f"❌ Error updating {update['menu_id']}: {e}")
            print()
    
    print("=" * 80)
    print("UPDATE COMPLETE")
    print("=" * 80)
    
    # Verify updates
    print()
    print("VERIFICATION:")
    print("-" * 80)
    for update in updates:
        try:
            menu_item = ERPMenuItem.objects.get(menu_id=update['menu_id'])
            status = "✅" if menu_item.applicable_toolbar_config == update['new_config'] else "❌"
            print(f"{status} {update['menu_id']}: {menu_item.applicable_toolbar_config}")
        except ERPMenuItem.DoesNotExist:
            print(f"❌ {update['menu_id']}: NOT FOUND")

if __name__ == '__main__':
    update_toolbar_configs()




