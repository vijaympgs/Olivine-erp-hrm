from core.auth_access.backend.user_management.models import ERPMenuItem

print("=" * 80)
print("UOM MENU ITEMS CHECK")
print("=" * 80)

uom_items = ERPMenuItem.objects.filter(menu_id__icontains='UOM')

if not uom_items.exists():
    print("❌ NO UOM menu items found!")
    print("\nSearching for similar items...")
    similar = ERPMenuItem.objects.filter(menu_name__icontains='UOM')[:5]
    for item in similar:
        print(f"  - {item.menu_id}: {item.menu_name}")
else:
    print(f"✅ Found {uom_items.count()} UOM menu items:\n")
    for item in uom_items:
        print(f"Menu ID: {item.menu_id}")
        print(f"Name: {item.menu_name}")
        print(f"Toolbar Config: {item.applicable_toolbar_config or 'NOT SET'}")
        print(f"View Type: {item.view_type}")
        print("-" * 80)

print("\n" + "=" * 80)
print("CHECKING EXACT MATCH: INVENTORY_UOM_SETUP")
print("=" * 80)

try:
    uom = ERPMenuItem.objects.get(menu_id='INVENTORY_UOM_SETUP')
    print(f"✅ FOUND!")
    print(f"  Menu ID: {uom.menu_id}")
    print(f"  Name: {uom.menu_name}")
    print(f"  Toolbar Config: {uom.applicable_toolbar_config or 'NOT SET ❌'}")
    print(f"  View Type: {uom.view_type}")
    print(f"  Module: {uom.module_name}")
except ERPMenuItem.DoesNotExist:
    print("❌ NOT FOUND: INVENTORY_UOM_SETUP")
    print("\nTrying alternative IDs...")
    alternatives = ['UOM_SETUP', 'UOMS', 'UOM', 'inventory_uom_setup']
    for alt_id in alternatives:
        try:
            item = ERPMenuItem.objects.get(menu_id=alt_id)
            print(f"✅ Found with ID: {alt_id}")
            print(f"   Config: {item.applicable_toolbar_config}")
            break
        except ERPMenuItem.DoesNotExist:
            print(f"❌ Not found: {alt_id}")

print("=" * 80)




