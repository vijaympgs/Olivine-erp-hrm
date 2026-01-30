from core.auth-access.backend.user_management.models import MenuItemType

# Check Inventory Overview depth
inv_overview = MenuItemType.objects.get(menu_id='inventory-overview')
current = inv_overview
depth = 0
path = []

while current:
    path.insert(0, current.menu_name)
    if current.parent_menu:
        depth += 1
    current = current.parent_menu

print(f"Path: {' > '.join(path)}")
print(f"Depth: {depth}")
print(f"\nExpected depth for L3 items: 2")
print(f"Actual depth: {depth}")
print(f"\nThis means the admin is checking for depth == {depth} but we're checking for depth == 3")




