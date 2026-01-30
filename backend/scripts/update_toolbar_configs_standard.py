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

from core.auth_access.backend.user_management.models import ERPMenuItem, ERPToolbarControl

# Standard configuration strings
CONFIGS = {
    'MASTERS_SIMPLE': 'NESCKVDXRQF',
    'MASTERS_ADVANCED': 'NESCKVDXRQFIO',
    'TRANSACTIONS': 'NESCKZTJAVPMRDX1234QF',
    'TRANSACTIONS_SIMPLE': 'NESCKVDXRQF',
    'REPORTS': 'VRXPYQFG',
    'CONFIGURATION': 'ESCKXR'
}

# Mapping of menu_id to config type
MENU_CONFIGS = {
    # Inventory - Masters (Simple)
    'inventory_uom_setup': 'MASTERS_SIMPLE',
    'reason_codes': 'MASTERS_SIMPLE',
    'categories': 'MASTERS_SIMPLE',
    'brands': 'MASTERS_SIMPLE',
    'attributes': 'MASTERS_SIMPLE',
    
    # Inventory - Masters (Advanced)
    'ITEM_MASTER': 'MASTERS_ADVANCED',
    'item-master': 'MASTERS_ADVANCED',
    
    # Inventory - Transactions (Simple)
    'stock_movement': 'TRANSACTIONS_SIMPLE',
    'stock_adjustment': 'TRANSACTIONS_SIMPLE',
    'stock_transfer': 'TRANSACTIONS_SIMPLE',
    
    # Inventory - Reports
    'stock_valuation': 'REPORTS',
    'stock_report': 'REPORTS',
    'inventory_report': 'REPORTS',
    
    # Procurement - Masters (Advanced)
    'SUPPLIER_MASTER': 'MASTERS_ADVANCED',
    'suppliers': 'MASTERS_ADVANCED',
    
    # Procurement - Transactions
    'PURCHASE_REQUISITIONS': 'TRANSACTIONS',
    'PURCHASE_ORDERS': 'TRANSACTIONS',
    'GOODS_RECEIPTS': 'TRANSACTIONS',
    
    # Sales - Masters (Advanced)
    'CUSTOMER_MASTER': 'MASTERS_ADVANCED',
    'customers': 'MASTERS_ADVANCED',
    
    # Sales - Transactions
    'SALES_ORDERS': 'TRANSACTIONS',
    'SALES_INVOICES': 'TRANSACTIONS',
    'SALES_QUOTES': 'TRANSACTIONS',
    
    # Configuration
    'company_settings': 'CONFIGURATION',
    'system_parameters': 'CONFIGURATION',
    'user_preferences': 'CONFIGURATION',
}

def update_toolbar_configs():
    """Update ERPMenuItem entries with correct toolbar configurations"""
    
    print("=" * 80)
    print("UPDATING TOOLBAR CONFIGURATIONS")
    print("=" * 80)
    
    updated_count = 0
    not_found_count = 0
    
    for menu_id, config_type in MENU_CONFIGS.items():
        config_string = CONFIGS[config_type]
        
        try:
            menu_item = ERPMenuItem.objects.get(menu_id=menu_id)
            
            old_config = menu_item.applicable_toolbar_config
            menu_item.applicable_toolbar_config = config_string
            menu_item.save()
            
            status = "UPDATED" if old_config != config_string else "UNCHANGED"
            print(f"\n[{status}] {menu_id}")
            print(f"  Type: {config_type}")
            print(f"  Old Config: {old_config or 'NOT SET'}")
            print(f"  New Config: {config_string}")
            
            updated_count += 1
            
        except ERPMenuItem.DoesNotExist:
            print(f"\n[NOT FOUND] {menu_id}")
            print(f"  Expected Type: {config_type}")
            print(f"  Expected Config: {config_string}")
            not_found_count += 1
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total Processed: {len(MENU_CONFIGS)}")
    print(f"Updated/Verified: {updated_count}")
    print(f"Not Found: {not_found_count}")
    print("=" * 80)
    
    # Show all existing menu items for reference
    print("\n" + "=" * 80)
    print("ALL EXISTING MENU ITEMS (RETAIL MODULE)")
    print("=" * 80)
    
    all_retail_items = ERPMenuItem.objects.filter(module_name='RETAIL').order_by('submodule', 'menu_order')
    
    for item in all_retail_items:
        print(f"\n{item.menu_id}")
        print(f"  Name: {item.menu_name}")
        print(f"  Submodule: {item.submodule or 'N/A'}")
        print(f"  View Type: {item.view_type}")
        print(f"  Config: {item.applicable_toolbar_config or 'NOT SET'}")
        print(f"  Route: {item.route_path or 'NOT SET'}")

if __name__ == "__main__":
    update_toolbar_configs()




