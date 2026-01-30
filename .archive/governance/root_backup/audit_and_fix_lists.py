
import os
import sys
import django

# Setup Django
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')
sys.path.append(BACKEND_DIR)
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.dev")
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def fix_remaining():
    items = ERPMenuItem.objects.filter(view_type='LIST')
    count = items.count()
    print(f"Found {count} items with view_type='LIST':")
    
    if count == 0:
        print("✅ No LIST items found. All clear!")
        return

    for item in items:
        print(f" - {item.menu_id} ({item.menu_name}) -> Changing to MASTER")
        # Default policy: Eliminate LIST. Upgrade to MASTER (unless obvious Transaction)
        # Most of these are likely Containers or simple lists.
        # If 'Stock Movements' container -> Master is fine (it's structural).
        
        # Override for specific known transactions if any:
        if 'BATCH' in item.menu_id or 'SERIAL' in item.menu_id:
             item.view_type = 'MASTER' # Batch/Serial Mgmt is Master data usually? Or Transaction?
             # Plan says "Batch & Serial Tracking" -> Container -> Master.
        else:
             item.view_type = 'MASTER'
        
        item.save()

    print(f"\n✅ Updated {count} items to MASTER.")

if __name__ == "__main__":
    fix_remaining()



