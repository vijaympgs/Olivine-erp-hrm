from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.services.toolbar_permission_service import resolve_toolbar_permissions

User = get_user_model()
user = User.objects.filter(is_superuser=True).first()
if user:
    print("\n--- CREATE MODE ---")
    res = resolve_toolbar_permissions(user.id, 'HRM_EMPLOYEE_RECORDS', 'CREATE')
    print(res.get('allowed_actions'))
    
    print("\n--- VIEW MODE ---")
    res2 = resolve_toolbar_permissions(user.id, 'HRM_EMPLOYEE_RECORDS', 'VIEW')
    print(res2.get('allowed_actions'))
else:
    print("No user")
