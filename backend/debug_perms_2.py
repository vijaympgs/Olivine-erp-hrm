from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.services.toolbar_permission_service import resolve_toolbar_permissions

User = get_user_model()
print("--- START DEBUG 2 ---")

target_users = ['admin', 'bouser']

for uname in target_users:
    try:
        u = User.objects.get(username=uname)
        print(f"Testing User: {u.username}")
        res = resolve_toolbar_permissions(u.id, 'HRM_EMPLOYEE_RECORDS', 'NEW')
        print(f"  Allowed: {res.get('allowed_actions')}")
    except User.DoesNotExist:
        print(f"  User {uname} not found")

print("--- END DEBUG 2 ---")
