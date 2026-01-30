"""
Fix benchmark screens - UOM and Purchase Orders
Run with: python backend/manage.py shell < backend/scripts/fix_benchmarks.py
"""
from core.auth_access.backend.user_management.models import ERPMenuItem

print("\n" + "="*80)
print("FIXING BENCHMARK SCREENS")
print("="*80 + "\n")

# Fix 1: UOM Setup
print("\n1. Fixing UOM Setup...")
print("-" * 80)

try:
    uom = ERPMenuItem.objects.get(menu_id='inventory_uom_setup')
    print(f"   Found: {uom.menu_name}")
    print(f"   Current config: {uom.applicable_toolbar_config}")
    print(f"   Current view_type: {uom.view_type}")
    
    # Update to match frontend and correct type
    uom.menu_id = 'INVENTORY_UOM_SETUP'
    uom.view_type = 'MASTER'
    uom.applicable_toolbar_config = 'NESCKVDXRQF'
    uom.save()
    
    print("   ✅ Updated UOM Setup:")
    print("      menu_id: INVENTORY_UOM_SETUP")
    print("      view_type: MASTER")
    print("      config: NESCKVDXRQF")
except ERPMenuItem.DoesNotExist:
    print("   ❌ UOM entry not found!")

# Fix 2: Purchase Orders (verify it's correct)
print("\n2. Verifying Purchase Orders (Transaction)...")
print("-" * 80)

try:
    po = ERPMenuItem.objects.get(menu_id='PURCHASE_ORDERS')
    print(f"   Found: {po.menu_name}")
    print(f"   Config: {po.applicable_toolbar_config}")
    print(f"   View Type: {po.view_type}")
    
    if po.applicable_toolbar_config == 'NESCKZTJAVPMRDX1234QF' and po.view_type == 'TRANSACTION':
        print("   ✅ Purchase Orders config is correct!")
    else:
        print("   ⚠️ Purchase Orders config needs update")
        po.applicable_toolbar_config = 'NESCKZTJAVPMRDX1234QF'
        po.view_type = 'TRANSACTION'
        po.save()
        print("   ✅ Updated!")
except ERPMenuItem.DoesNotExist:
    print("   ❌ Purchase Orders entry not found!")

# Fix 3: Create Purchase Orders List View entry if it doesn't exist
print("\n3. Checking Purchase Orders List View...")
print("-" * 80)

list_view, created = ERPMenuItem.objects.get_or_create(
    menu_id='purchase-orders',
    defaults={
        'menu_name': 'Purchase Orders List',
        'view_type': 'LIST_VIEW',
        'applicable_toolbar_config': 'NRQFX',
        'route_path': '/procurement/purchase-orders',
        'module_name': 'RETAIL',
        'submodule_name': 'PROCUREMENT',
        'is_active': True
    }
)

if created:
    print("   ✅ Created Purchase Orders List View entry")
else:
    print(f"   Found existing entry: {list_view.menu_name}")
    # Update if needed
    if list_view.applicable_toolbar_config != 'NRQFX' or list_view.view_type != 'LIST_VIEW':
        list_view.applicable_toolbar_config = 'NRQFX'
        list_view.view_type = 'LIST_VIEW'
        list_view.save()
        print("   ✅ Updated List View config")
    else:
        print("   ✅ List View config is correct")

print("\n" + "="*80)
print("BENCHMARK FIXES COMPLETE!")
print("="*80 + "\n")

# Summary
print("\nSUMMARY:")
print("-" * 80)

uom_final = ERPMenuItem.objects.get(menu_id='INVENTORY_UOM_SETUP')
po_final = ERPMenuItem.objects.get(menu_id='PURCHASE_ORDERS')
po_list_final = ERPMenuItem.objects.get(menu_id='purchase-orders')

print(f"\n✅ UOM Setup:")
print(f"   menu_id: {uom_final.menu_id}")
print(f"   view_type: {uom_final.view_type}")
print(f"   config: {uom_final.applicable_toolbar_config}")

print(f"\n✅ Purchase Orders (Transaction):")
print(f"   menu_id: {po_final.menu_id}")
print(f"   view_type: {po_final.view_type}")
print(f"   config: {po_final.applicable_toolbar_config}")

print(f"\n✅ Purchase Orders (List View):")
print(f"   menu_id: {po_list_final.menu_id}")
print(f"   view_type: {po_list_final.view_type}")
print(f"   config: {po_list_final.applicable_toolbar_config}")

print("\n" + "="*80 + "\n")




