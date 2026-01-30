
import os
import sys
import django
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def setup_django():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    backend_dir = os.path.join(project_root, 'backend')
    if backend_dir not in sys.path:
        sys.path.insert(0, backend_dir)
        
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
    django.setup()

def build_parent_structure():
    from core.auth_access.backend.user_management.models import ERPMenuItem

    # Helper function to get or create a "Folder" menu item
    def get_or_create_folder(menu_id, name, module, submodule=None):
        item, created = ERPMenuItem.objects.get_or_create(
            menu_id=menu_id,
            defaults={
                'menu_name': name,
                'module_name': module,
                'submodule': submodule,
                'view_type': 'LIST', # Or abstract folder type if existed
                'route_path': '/abstract/' + menu_id,
                'toolbar_config': '0,0,0,0,0,0,0,0,0,0,0,1,0,0,0', # Empty
                'is_active': True 
            }
        )
        if created:
            logger.info(f"Created Folder: {name} ({menu_id})")
        return item

    # 1. PROCUREMENT Structure
    # Retail > Procurement > Vendor Management > ...
    # Retail > Procurement > Purchasing > ...
    # Retail > Procurement > Receiving & Fulfillment > ...

    procurement = 'PROCUREMENT' # Submodule code

    # Folders
    vendor_mgmt = get_or_create_folder('vendor-mgmt', 'Vendor Management', 'RETAIL', procurement)
    purchasing = get_or_create_folder('purchasing-group', 'Purchasing', 'RETAIL', procurement)
    receiving = get_or_create_folder('receiving-fulfillment', 'Receiving & Fulfillment', 'RETAIL', procurement)

    # Link Items to Vendor Management
    # suppliers, compliance
    for item_id in ['suppliers', 'compliance']:
        try:
            item = ERPMenuItem.objects.get(menu_id=item_id)
            item.parent_menu = vendor_mgmt
            item.submodule = procurement
            item.save()
            logger.info(f"Linked {item_id} to Vendor Management")
        except ERPMenuItem.DoesNotExist:
            pass

    # Link Items to Purchasing
    # requisitions, rfqs, purchase-orders
    for item_id in ['requisitions', 'rfqs', 'purchase-orders', 'orders', 'sales-orders', 'purchase-returns']: # Note: orders/sales are SALES submodule. Careful.
        # Only link PROCUREMENT items here
        pass

    purchasing_items = ['requisitions', 'rfqs', 'purchase-orders']
    for item_id in purchasing_items:
        try:
            item = ERPMenuItem.objects.get(menu_id=item_id)
            item.parent_menu = purchasing
            item.submodule = procurement
            item.save()
            logger.info(f"Linked {item_id} to Purchasing")
        except ERPMenuItem.DoesNotExist:
            logger.warning(f"Item {item_id} not found")

    # Link Items to Receiving
    # asns, receipts, purchase-returns (maybe here?)
    rec_items = ['asns', 'receipts', 'purchase-returns', 'bills', 'payments']
    for item_id in rec_items:
        try:
            item = ERPMenuItem.objects.get(menu_id=item_id)
            item.parent_menu = receiving
            item.submodule = procurement # Ensure submodule matches
            item.save()
            logger.info(f"Linked {item_id} to Receiving & Fulfillment")
        except:
            pass
            
    # 2. INVENTORY Structure
    # Retail > Inventory > Stock Management
    # Retail > Inventory > Stock Movements
    inventory = 'INVENTORY'
    stock_mgmt = get_or_create_folder('stock-mgmt-group', 'Stock Management', 'RETAIL', inventory)
    stock_moves = get_or_create_folder('stock-moves-group', 'Stock Movements', 'RETAIL', inventory)
    
    # Link basic levels
    for item_id in ['stock-levels', 'stock-by-location', 'stock-batch', 'low-stock-alerts']:
         try:
            item = ERPMenuItem.objects.get(menu_id=item_id)
            item.parent_menu = stock_mgmt
            item.submodule = inventory
            item.save()
         except: pass

    for item_id in ['movement-history', 'internal-transfers', 'intercompany-transfers']:
         try:
            item = ERPMenuItem.objects.get(menu_id=item_id)
            item.parent_menu = stock_moves
            item.submodule = inventory
            item.save()
         except: pass

if __name__ == '__main__':
    setup_django()
    build_parent_structure()




