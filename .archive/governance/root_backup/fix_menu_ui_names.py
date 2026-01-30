
import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def fix_names():
    # Mapping of ID -> Correct UI Name
    updates = {
        'CUSTOMER_MASTER': 'Customer Master',
        'SUPPLIER_MASTER': 'Supplier Master',
        'STOCK_TAKE': 'Stock Take',
        'PRICE_LIST_MASTER': 'Price List Master',
        'STOCK_TAKE_LIST': 'Stock Take' # Case where rename didn't happen or check needed
    }
    
    # Also explicitly ensure view_type is correct
    type_map = {
        'STOCK_TAKE': 'TRANSACTION',
        'CUSTOMER_MASTER': 'MASTER',
        'SUPPLIER_MASTER': 'MASTER',
        'PRICE_LIST_MASTER': 'MASTER'
    }

    print("correcting UI Names...")
    
    for mid, name in updates.items():
        try:
            item = ERPMenuItem.objects.filter(menu_id=mid).first()
            if item:
                print(f"Update {mid}: {item.menu_name} -> {name}")
                item.menu_name = name
                
                if mid in type_map:
                    item.view_type = type_map[mid]
                    print(f"  Type -> {type_map[mid]}")
                    
                item.save()
            else:
                print(f"Skipping {mid} (not found)")
                
        except Exception as e:
            print(f"Error {mid}: {e}")

if __name__ == '__main__':
    fix_names()



