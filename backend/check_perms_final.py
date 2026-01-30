import os
import sys
import django
import json

if 'c:\\00mindra\\olivine-platform' not in sys.path:
    sys.path.append('c:\\00mindra\\olivine-platform')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.erp_core.settings')
django.setup()

from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.services.toolbar_permission_service import resolve_toolbar_permissions

User = get_user_model()
user = User.objects.filter(is_superuser=True).first()

if not user:
    print("No Superuser found!")
else:
    print(f"Checking for user: {user.username}")
    
    # Check CREATE
    res = resolve_toolbar_permissions(user.id, 'HRM_EMPLOYEE_RECORDS', 'CREATE')
    print("--- CREATE MODE ---")
    print(json.dumps(res['allowed_actions'], indent=2))
    
    # Check VIEW
    res2 = resolve_toolbar_permissions(user.id, 'HRM_EMPLOYEE_RECORDS', 'VIEW')
    print("--- VIEW MODE ---")
    print(json.dumps(res2['allowed_actions'], indent=2))
