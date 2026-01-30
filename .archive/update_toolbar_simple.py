"""
Simple script to update toolbar configurations
Run with: python backend/domain/master/manage.py shell
Then paste this code
"""

from core.auth_access.backend.menu_registry.models import ERPMenuItem

# Update configurations
updates = {
    'MOVEMENT_TYPES': 'NRQFX',
    'VALUATION_METHODS': 'VRX',
    'INV_PARAMETERS': 'ESCKXR',
    'APPROVAL_RULES': 'NRQFX'
}

print("Updating toolbar configurations...")
for menu_id, config in updates.items():
    try:
        item = ERPMenuItem.objects.get(menu_id=menu_id)
        old_config = item.applicable_toolbar_config
        item.applicable_toolbar_config = config
        item.save()
        print(f"✓ {menu_id}: {old_config} → {config}")
    except ERPMenuItem.DoesNotExist:
        print(f"✗ {menu_id}: NOT FOUND")

print("\nDone!")




