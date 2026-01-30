import os
import sys
import django

# Setup Django
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

# Define mappings based on UI Category / View Type
CONFIG_MAPPING = {
    'LIST': 'NRQFX',             # New, Refresh, Search, Filter, Exit
    'MASTER': 'NESCKVDXR',       # New, Edit, Save, Cancel, Clear, View, Delete, Exit, Refresh
    'TRANSACTION': 'NESCKPVDXRTJZ', # Full Transactional set
    'REPORT': 'RFYXP',           # Refresh, Filter, Export, Exit, Print
    'DASHBOARD': 'RFQ',          # Refresh, Filter, Search
    'FORM': 'NESCKVDXR',         # Similar to Master
    'PAGE': 'NESCX',             # New, Edit, Save, Cancel, Exit (Used for Config)
}

def update_toolbars():
    print("Updating ERPMenuItem toolbar configurations...")
    count = 0
    
    # Batch update by view_type
    for view_type, config in CONFIG_MAPPING.items():
        updated = ERPMenuItem.objects.filter(view_type=view_type).update(applicable_toolbar_config=config)
        print(f"Updated {updated} items of type {view_type} to '{config}'")
        count += updated

    # Special Cases
    # Valuation Methods - often just View/Edit
    ERPMenuItem.objects.filter(menu_id='VALUATION_METHODS').update(applicable_toolbar_config='VRX')
    # Inventory Parameters - Edit focus
    ERPMenuItem.objects.filter(menu_id='INV_PARAMETERS').update(applicable_toolbar_config='ESCKXR')
    
    print(f"Total updated: {count}")

if __name__ == "__main__":
    update_toolbars()




