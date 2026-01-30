from core.auth-access.backend.user_management.models import MenuItemType

print("=" * 80)
print("COMPLETE L3 INVENTORY VERIFICATION")
print("=" * 80)

# Get Inventory L1
inv = MenuItemType.objects.get(menu_id='inventory')
print(f"\nL1: {inv.menu_name} (id={inv.id})")

# Get all L2 items
l2_items = MenuItemType.objects.filter(parent_menu=inv).order_by('menu_order')
print(f"\nL2 Subgroups: {l2_items.count()}")

total_l3 = 0

for l2 in l2_items:
    l3_items = MenuItemType.objects.filter(parent_menu=l2).order_by('menu_order')
    count = l3_items.count()
    total_l3 += count
    print(f"\n  {l2.menu_name} (id={l2.id}):")
    print(f"    L3 count: {count}")
    for l3 in l3_items:
        print(f"      - {l3.menu_name} (id={l3.id}, menu_id={l3.menu_id})")

print("\n" + "=" * 80)
print(f"TOTALS:")
print(f"  L1: 1")
print(f"  L2: {l2_items.count()}")
print(f"  L3: {total_l3}")
print(f"  GRAND TOTAL: {1 + l2_items.count() + total_l3}")
print("=" * 80)




