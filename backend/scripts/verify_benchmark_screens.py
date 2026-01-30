"""
Verify UOM and Purchase Order benchmark screens
"""
import os
import sys
import django

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def verify_benchmarks():
    print("\n" + "="*80)
    print("BENCHMARK SCREENS - BACKEND VERIFICATION")
    print("="*80 + "\n")
    
    # Check UOM
    print("1. UOM SETUP (Masters - Simple)")
    print("-" * 80)
    uom_entries = ERPMenuItem.objects.filter(menu_id__icontains='uom')
    for item in uom_entries:
        print(f"   Menu ID: {item.menu_id}")
        print(f"   Name: {item.menu_name}")
        print(f"   View Type: {item.view_type}")
        print(f"   Config: {item.applicable_toolbar_config}")
        print(f"   Route: {item.route_path}")
        print(f"   Module: {item.module_name}")
        print()
    
    # Check Purchase Orders
    print("\n2. PURCHASE ORDERS (Transactions)")
    print("-" * 80)
    po_entries = ERPMenuItem.objects.filter(menu_id__icontains='purchase').filter(menu_id__icontains='order')
    for item in po_entries:
        print(f"   Menu ID: {item.menu_id}")
        print(f"   Name: {item.menu_name}")
        print(f"   View Type: {item.view_type}")
        print(f"   Config: {item.applicable_toolbar_config}")
        print(f"   Route: {item.route_path}")
        print(f"   Module: {item.module_name}")
        print()
    
    print("\n" + "="*80)
    print("EXPECTED CONFIGURATIONS")
    print("="*80)
    print("\nUOM Setup:")
    print("   Menu ID: inventory_uom_setup or INVENTORY_UOM_SETUP")
    print("   View Type: MASTER or CONFIGURATION")
    print("   Config: NESCKVDXRQF (Masters - Simple)")
    print("\nPurchase Orders (List View):")
    print("   Menu ID: purchase-orders")
    print("   View Type: LIST_VIEW")
    print("   Config: NRQFX")
    print("\nPurchase Orders (Transaction):")
    print("   Menu ID: PURCHASE_ORDERS")
    print("   View Type: TRANSACTION")
    print("   Config: NESCKZTJAVPMRDX1234QF")
    print("\n" + "="*80 + "\n")

if __name__ == '__main__':
    verify_benchmarks()




