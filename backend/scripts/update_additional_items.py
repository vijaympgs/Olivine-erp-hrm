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

from core.auth_access.backend.user_management.models import ERPMenuItem

# Additional menu items found
ADDITIONAL_CONFIGS = {
    # Customer related (found in search)
    'customer-groups': 'MASTERS_SIMPLE',
    'customer-list': 'LIST_VIEW',
    
    # Stock related
    'stock-valuation': 'REPORTS',
    
    # These might exist with different names - we'll search and update
}

print("=" * 80)
print("UPDATING ADDITIONAL MENU ITEMS")
print("=" * 80)

updated_count = 0

# Standard configs
CONFIGS = {
    'MASTERS_SIMPLE': 'NESCKVDXRQF',
    'MASTERS_ADVANCED': 'NESCKVDXRQFIO',
    'TRANSACTIONS': 'NESCKZTJAVPMRDX1234QF',
    'TRANSACTIONS_SIMPLE': 'NESCKVDXRQF',
    'REPORTS': 'VRXPYQFG',
    'LIST_VIEW': 'NRQFX',
    'CONFIGURATION': 'ESCKXR',
}

for menu_id, config_type in ADDITIONAL_CONFIGS.items():
    config_string = CONFIGS[config_type]
    
    try:
        menu_item = ERPMenuItem.objects.get(menu_id=menu_id)
        old_config = menu_item.applicable_toolbar_config
        
        if old_config != config_string:
            menu_item.applicable_toolbar_config = config_string
            menu_item.save()
            
            print(f"\n[UPDATED] {menu_id}")
            print(f"  Name: {menu_item.menu_name}")
            print(f"  Old: {old_config or 'NOT SET'}")
            print(f"  New: {config_string}")
            updated_count += 1
        else:
            print(f"\n[UNCHANGED] {menu_id} (already {config_string})")
            
    except ERPMenuItem.DoesNotExist:
        print(f"\n[NOT FOUND] {menu_id}")

# Now search for items by name pattern and update
print("\n" + "=" * 80)
print("SEARCHING AND UPDATING BY NAME PATTERN")
print("=" * 80)

# Search patterns and their configs
PATTERN_CONFIGS = [
    ('category', 'MASTERS_SIMPLE'),
    ('brand', 'MASTERS_SIMPLE'),
    ('reason code', 'MASTERS_SIMPLE'),
]

for pattern, config_type in PATTERN_CONFIGS:
    config_string = CONFIGS[config_type]
    
    items = ERPMenuItem.objects.filter(
        module_name='RETAIL',
        menu_name__icontains=pattern
    ).exclude(menu_id='pos-checkout')  # Exclude POS Billing
    
    print(f"\n--- Pattern: '{pattern}' ---")
    
    for item in items:
        old_config = item.applicable_toolbar_config
        
        if old_config != config_string:
            item.applicable_toolbar_config = config_string
            item.save()
            
            print(f"\n[UPDATED] {item.menu_id}")
            print(f"  Name: {item.menu_name}")
            print(f"  Old: {old_config or 'NOT SET'}")
            print(f"  New: {config_string}")
            updated_count += 1
        else:
            print(f"  {item.menu_id} - already correct")

print("\n" + "=" * 80)
print(f"TOTAL UPDATED: {updated_count}")
print("=" * 80)




