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

from core.auth_access.backend.user_management.models import ERPMenuItem

def fix_toolbars():
    targets = [
        {'menu_id': 'COMPANY', 'config': 'NESCKVDXRQFIO'},
        {'menu_id': 'LOCATIONS_SETUP', 'config': 'NESCKVDXRQFIO'}
    ]
    
    for target in targets:
        try:
            item = ERPMenuItem.objects.get(menu_id=target['menu_id'])
            print(f"Updating {target['menu_id']}: {item.applicable_toolbar_config} -> {target['config']}")
            item.applicable_toolbar_config = target['config']
            item.save()
            print("✅ Success")
        except ERPMenuItem.DoesNotExist:
            print(f"❌ Error: {target['menu_id']} not found")

if __name__ == "__main__":
    fix_toolbars()




