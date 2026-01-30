import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def list_hrm_menu_items():
    print("Checking HRM Menu Items...")
    items = ERPMenuItem.objects.filter(module_name='HRM').order_by('menu_id')
    
    if not items.exists():
        print("No HRM menu items found.")
        return

    print(f"{'Menu ID':<40} | {'Menu Name':<40} | {'Route Path'}")
    print("-" * 100)
    for item in items:
        print(f"{item.menu_id:<40} | {item.menu_name:<40} | {item.route_path}")

if __name__ == "__main__":
    list_hrm_menu_items()
