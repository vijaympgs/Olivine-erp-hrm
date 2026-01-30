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

# Search terms
search_terms = ['customer', 'category', 'brand', 'stock', 'reason', 'movement', 'transfer']

print("=" * 100)
print("SEARCHING FOR MISSING MENU ITEMS")
print("=" * 100)

for term in search_terms:
    print(f"\n{'='*100}")
    print(f"Search: '{term}'")
    print(f"{'='*100}")
    
    items = ERPMenuItem.objects.filter(module_name='RETAIL').filter(
        menu_name__icontains=term
    ) | ERPMenuItem.objects.filter(module_name='RETAIL').filter(
        route_path__icontains=term
    ) | ERPMenuItem.objects.filter(module_name='RETAIL').filter(
        menu_id__icontains=term
    )
    
    items = items.distinct().order_by('menu_id')
    
    if items.exists():
        for item in items:
            print(f"\nmenu_id: {item.menu_id}")
            print(f"  Name: {item.menu_name}")
            print(f"  View Type: {item.view_type}")
            print(f"  Config: {item.applicable_toolbar_config or 'NOT SET'}")
            print(f"  Route: {item.route_path or 'NOT SET'}")
    else:
        print(f"  No items found")

print("\n" + "=" * 100)
print("ALL RETAIL MENU ITEMS (for reference)")
print("=" * 100)

all_items = ERPMenuItem.objects.filter(module_name='RETAIL').order_by('menu_id')
for item in all_items:
    print(f"{item.menu_id:45} | {item.menu_name:45} | {item.route_path or 'N/A'}")




