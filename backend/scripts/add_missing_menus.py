
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

def add_missing_menus():
    from core.auth_access.backend.user_management.models import ERPMenuItem
    
    # Define missing items
    # Format: (menu_id, menu_name, submodule, view_type, toolbar_chars)
    new_items = [
        ('valuation-reports', 'Valuation Reports', 'INVENTORY', 'REPORT', 'RFYXP'),
        ('cost-analysis', 'Cost Analysis', 'INVENTORY', 'REPORT', 'RFYXP'),
        ('period-valuation', 'Period-end Valuation', 'INVENTORY', 'REPORT', 'RFYXP'),
        ('expiry-mgmt', 'Expiry Management', 'INVENTORY', 'LIST', 'NRQFX'),
        ('batch-trace', 'Batch Traceability', 'INVENTORY', 'LIST', 'RFQ'), # Traceability is usually search/view
    ]
    
    # Retrieve Parent Menus (Optional, skipping parent linking for speed as it's just flattened list in DB mostly)
    # But checking if parent linking is required for hierarchy in filters.
    # MenuLevelFilter relies on parent_menu.
    # We should try to find parents: 'inventory-valuation' and 'batch-serial'.
    
    inv_val_parent = ERPMenuItem.objects.filter(menu_id='inventory-valuation').first() # "Inventory Valuation" group
    batch_ser_parent = ERPMenuItem.objects.filter(menu_id='batch-serial').first() # "Batch & Serial Tracking" group
    
    for mid, name, submod, vtype, chars in new_items:
        if ERPMenuItem.objects.filter(menu_id=mid).exists():
            logger.info(f"Skipping existing: {mid}")
            continue
            
        parent = None
        if mid in ['valuation-reports', 'cost-analysis', 'period-valuation']:
            parent = inv_val_parent
        elif mid in ['expiry-mgmt', 'batch-trace']:
            parent = batch_ser_parent
            
        logger.info(f"Creating {mid}...")
        ERPMenuItem.objects.create(
            menu_id=mid,
            menu_name=name,
            module_name='RETAIL',
            submodule=submod,
            view_type=vtype,
            applicable_toolbar_config=chars,
            parent_menu=parent,
            is_active=True
        )
        logger.info(f"✅ Created {mid}")

if __name__ == '__main__':
    setup_django()
    add_missing_menus()




