import os
import sys
import django

sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem
from django.db.models import Q

items = ERPMenuItem.objects.all().order_by('module_name', 'menu_name')

print("-" * 80)
print(f"{'Menu Name':<30} | {'Module':<10} | {'Menu ID':<30}")
print("-" * 80)
for item in items:
    print(f"{item.menu_name:<30} | {item.module_name:<10} | {item.menu_id:<30}")
print("-" * 80)
