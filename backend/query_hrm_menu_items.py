import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

items = ERPMenuItem.objects.filter(module='HRM').values('menu_id', 'menu_name', 'route_path', 'sidebar_path')
print("HRM Menu Items:")
print("=" * 100)
for i in items:
    print(f"{i['menu_id']}: {i['menu_name']} | {i['route_path']} | {i['sidebar_path']}")
