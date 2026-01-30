import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.base")
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

# Query UOM entries
uom_entries = ERPMenuItem.objects.filter(menu_id__icontains='uom')

for entry in uom_entries:
    print(f"ID: {entry.menu_id}")
    print(f"Name: {entry.menu_name}")
    print(f"Config: {entry.applicable_toolbar_config}")
    print(f"Route: {entry.route_path}")
    print("-" * 50)




