
import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def standardize_menu_ids():
    updates = {
        'CUSTOMER_LIST': 'CUSTOMER_MASTER',
        'SUPPLIERS': 'SUPPLIER_MASTER',
        'STOCK_TAKE_LIST': 'STOCK_TAKE',
        'PRICE_LISTS': 'PRICE_LIST_MASTER',
        'PRICE_LISTS_MASTER': 'PRICE_LIST_MASTER', # just in case
        'LOCATION_LIST': 'LOCATION_MASTER', # if exists
        'COMPANY_LIST': 'COMPANY_MASTER', # if exists
    }
    
    print("Standardizing Menu IDs...")
    
    for old_id, new_id in updates.items():
        try:
            item = ERPMenuItem.objects.filter(menu_id=old_id).first()
            if item:
                print(f"🔄 Renaming {old_id} -> {new_id}")
                item.menu_id = new_id
                # Also ensure view_type is correct (MASTER for most)
                if 'MASTER' in new_id:
                    item.view_type = 'MASTER'
                elif 'STOCK_TAKE' in new_id:
                    item.view_type = 'TRANSACTION'
                    
                item.save()
            else:
                # Check if new_id already exists to avoid duplication
                if ERPMenuItem.objects.filter(menu_id=new_id).exists():
                    print(f"✅ {new_id} already exists (and {old_id} not found)")
                else:
                    print(f"ℹ️ {old_id} not found (skipping)")
                    
        except Exception as e:
            print(f"❌ Error updating {old_id}: {e}")

if __name__ == "__main__":
    standardize_menu_ids()



