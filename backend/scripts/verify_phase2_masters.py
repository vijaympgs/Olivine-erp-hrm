"""
Verify Item Master, Customer Master, and Supplier Master toolbar configurations
"""
from core.auth_access.backend.user_management.models import ERPMenuItem

print("\n" + "="*80)
print("PHASE 2: MASTERS VERIFICATION")
print("="*80 + "\n")

# Check Item Master
print("1. ITEM MASTER")
print("-" * 80)
item_entries = ERPMenuItem.objects.filter(menu_id__icontains='item')
for item in item_entries:
    print(f"   Menu ID: {item.menu_id}")
    print(f"   Name: {item.menu_name}")
    print(f"   View Type: {item.view_type}")
    print(f"   Config: {item.applicable_toolbar_config}")
    print(f"   Route: {item.route_path}")
    print()

# Check Customer Master
print("\n2. CUSTOMER MASTER")
print("-" * 80)
customer_entries = ERPMenuItem.objects.filter(menu_id__icontains='customer')
for item in customer_entries:
    print(f"   Menu ID: {item.menu_id}")
    print(f"   Name: {item.menu_name}")
    print(f"   View Type: {item.view_type}")
    print(f"   Config: {item.applicable_toolbar_config}")
    print(f"   Route: {item.route_path}")
    print()

# Check Supplier Master
print("\n3. SUPPLIER MASTER")
print("-" * 80)
supplier_entries = ERPMenuItem.objects.filter(menu_id__icontains='supplier')
for item in supplier_entries:
    print(f"   Menu ID: {item.menu_id}")
    print(f"   Name: {item.menu_name}")
    print(f"   View Type: {item.view_type}")
    print(f"   Config: {item.applicable_toolbar_config}")
    print(f"   Route: {item.route_path}")
    print()

print("\n" + "="*80)
print("EXPECTED CONFIGURATIONS")
print("="*80)
print("\nItem Master:")
print("   Menu ID: ITEM_MASTER")
print("   View Type: MASTER")
print("   Config: NESCKVDXRQFIO (Masters - Advanced)")

print("\nCustomer Master:")
print("   Menu ID: CUSTOMER_MASTER")
print("   View Type: MASTER")
print("   Config: NESCKVDXRQFIO (Masters - Advanced)")

print("\nSupplier Master:")
print("   Menu ID: SUPPLIER_MASTER")
print("   View Type: MASTER")
print("   Config: NESCKVDXRQFIO (Masters - Advanced)")

print("\n" + "="*80 + "\n")




