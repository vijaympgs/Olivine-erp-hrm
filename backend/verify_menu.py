from Core.auth_access.backend.user_management.models import ERPMenuItem

print("-" * 30)
retail_items = ERPMenuItem.objects.filter(module_name='retail')
print(f"Total Retail Menu Items in DB: {retail_items.count()}")

# Check for specific items requested by user
target_ids = ['ORDERS', 'QUOTES', 'sales-orders-group', 'RETAIL', 'retail']
for mid in target_ids:
    item = ERPMenuItem.objects.filter(menu_id=mid).first()
    if item:
        parent = item.parent_menu.menu_id if item.parent_menu else "None"
        print(f"Item: {mid} | Parent: {parent} | Name: {item.menu_name} | Toolbar: {getattr(item, 'original_toolbar_string', 'N/A')}")
    else:
        print(f"Item: {mid} | Status: MISSING")

print("-" * 30)
# List some key hierarchy paths for Retail
print("Hierarchy Sample:")
for item in retail_items[:15]:
    path = [item.menu_name]
    curr = item
    while curr.parent_menu:
        curr = curr.parent_menu
        path.insert(0, curr.menu_name)
    print(" -> ".join(path))
print("-" * 30)
