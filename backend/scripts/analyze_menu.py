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
from django.db.models import Count

print("MODULE     | TYPE            | COUNT")
print("-" * 40)
stats = ERPMenuItem.objects.values('module_name', 'view_type').annotate(count=Count('id')).order_by('module_name', 'view_type')
for s in stats:
    m = s['module_name'] or 'None'
    t = s['view_type']
    c = s['count']
    print(f"{m:10} | {t:15} | {c}")

print("\nLIST VIEWS IN DATABASE:")
lists = ERPMenuItem.objects.filter(view_type='LIST')
if not lists.exists():
    print("None found. (Clean!)")
else:
    for l in lists:
        print(f"- {l.menu_id} ({l.menu_name})")




