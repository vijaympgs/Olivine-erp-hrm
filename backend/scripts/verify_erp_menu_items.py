import os
import sys
import django

# Setup path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.base")
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

print("-" * 30)

# IDs from menuConfig: 'user-management', 'layout-settings', 'security', 'audit-logs', 'backup'
# 'company', 'locations-setup', 'fiscal', 'currencies', 'tax-setup'

checks = [
    'USER_MANAGEMENT', 'LAYOUT_SETTINGS', 'SECURITY', 'AUDIT_LOGS', 'BACKUP',
    'COMPANY', 'LOCATIONS_SETUP', 'FISCAL', 'CURRENCIES', 'TAX_SETUP'
]

for c in checks:
    try:
        item = ERPMenuItem.objects.get(menu_id=c)
        print(f"{c}: {item.module_name} | {item.view_type} (Active: {item.is_active})")
    except ERPMenuItem.DoesNotExist:
        print(f"{c}: NOT FOUND")

print("-" * 30)




