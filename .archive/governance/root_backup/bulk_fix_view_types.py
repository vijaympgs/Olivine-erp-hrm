
import os
import sys
import django

# Correct Setup:
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # olivine-erp-platform
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')
sys.path.append(BACKEND_DIR) # THIS is where erp_core lives
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.dev")
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def bulk_fix_view_types():
    print("Starting Bulk Fix of View Types...")
    items = ERPMenuItem.objects.all()
    count = 0
    updated = 0

    for item in items:
        mid_upper = item.menu_id.upper()
        name_upper = item.menu_name.upper()
        new_type = None

        # 1. Dashboards
        if 'DASHBOARD' in mid_upper:
            new_type = 'DASHBOARD'

        # 2. Reports
        elif 'REPORT' in mid_upper or 'ANALYSIS' in mid_upper or 'TRENDS' in mid_upper or 'HISTORY' in mid_upper:
            new_type = 'REPORT'

        # 3. Transactions
        elif any(x in mid_upper for x in ['ORDER', 'INVOICE', 'QUOTE', 'REQUISITION', 'RECEIPT', 'PAYMENT', 'ADJUSTMENT', 'TRANSFER', 'STOCK_TAKE', 'CHECKOUT', 'RETURN', 'REFUND', 'BILL', 'CLAIM']):
             # Exception: 'PURCHASE_ORDER_LIST' -> Transaction
             # Exception: 'SALES_ORDER_LIST' -> Transaction
             new_type = 'TRANSACTION'
             if 'METHOD' in mid_upper or 'TERM' in mid_upper or 'TYPE' in mid_upper: # Payment Methods, Order Types are Master/Config
                 new_type = 'MASTER'

        # 4. Configuration
        elif any(x in mid_upper for x in ['CONFIG', 'SETTING', 'RULE', 'PARAMETER', 'PREFERENCE', 'SEQUENCE', 'TAX', 'TEMPLATE']):
             new_type = 'CONFIGURATION'

        # 5. Master Data (Default for most others)
        elif any(x in mid_upper for x in ['MASTER', 'SETUP', 'PROFILE', 'MANAGEMENT', 'DIRECTORY', 'GROUP', 'CATEGORY', 'BRAND', 'UOM', 'ATTRIBUTE', 'USER', 'ROLE', 'PERMISSION']):
             new_type = 'MASTER'
        
        # 6. Specific Overrides based on known correct states
        if item.menu_id in ['CUSTOMER_MASTER', 'SUPPLIER_MASTER', 'ITEM_MASTER', 'PRICE_LIST_MASTER', 'LOCATION_MASTER']:
            new_type = 'MASTER'
        if item.menu_id == 'STOCK_TAKE':
            new_type = 'TRANSACTION'

        # Apply Update
        if new_type and item.view_type != new_type:
            print(f"Updating {item.menu_id}: {item.view_type} -> {new_type}")
            item.view_type = new_type
            item.save()
            updated += 1
        elif not new_type and item.view_type == 'LIST':
            # Fallback for remaining LIST items -> MASTER
            # e.g. 'BANKS', 'CHEQUES' (Cheques might be transaction?)
            # I'll default to MASTER if unsure, better than LIST.
            # But let's check heuristics.
            pass

        count += 1
    
    print(f"Scanned {count} items. Updated {updated} items.")
    
    # Final check for remaining LIST items
    remaining_lists = ERPMenuItem.objects.filter(view_type='LIST')
    if remaining_lists.exists():
        print(f"\n[Warning] {remaining_lists.count()} items still have view_type='LIST':")
        for i in remaining_lists:
             print(f"  - {i.menu_id} ({i.menu_name})")

if __name__ == "__main__":
    bulk_fix_view_types()



