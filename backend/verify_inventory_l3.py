"""
Verification script to identify missing L3 items
Compares database with INVENTORY_MENU_TREE.md structure
"""
from core.auth-access.backend.user_management.models import MenuItemType

# Expected L3 items per L2 subgroup (from INVENTORY_MENU_TREE.md)
expected_structure = {
    'inventory-dashboard': 5,
    'stock-management': 7,
    'stock-movements': 6,
    'stock-adjustments': 5,
    'physical-inventory': 5,
    'inventory-valuation': 4,
    'replenishment-planning': 5,
    'batch-serial': 4,
    'inventory-reports': 7,
    'inventory-config': 1,
}

print("=" * 80)
print("INVENTORY L3 VERIFICATION REPORT")
print("=" * 80)

inv = MenuItemType.objects.get(menu_id='inventory')
l2_items = MenuItemType.objects.filter(parent_menu=inv).order_by('menu_order')

total_expected = sum(expected_structure.values())
total_actual = 0
missing_items = []

for l2 in l2_items:
    l3_items = MenuItemType.objects.filter(parent_menu=l2).order_by('menu_order')
    actual_count = l3_items.count()
    expected_count = expected_structure.get(l2.menu_id, 0)
    total_actual += actual_count
    
    status = "✓" if actual_count == expected_count else "✗"
    print(f"\n{status} {l2.menu_name} ({l2.menu_id})")
    print(f"   Expected: {expected_count}, Actual: {actual_count}")
    
    if actual_count < expected_count:
        print(f"   Missing: {expected_count - actual_count} item(s)")
        missing_items.append(l2.menu_id)
    
    if actual_count > 0:
        for l3 in l3_items:
            print(f"     - {l3.menu_name} ({l3.menu_id})")

print("\n" + "=" * 80)
print(f"SUMMARY: Expected={total_expected}, Actual={total_actual}, Missing={total_expected - total_actual}")
print("=" * 80)

if missing_items:
    print(f"\nL2 groups with missing L3 items: {', '.join(missing_items)}")




