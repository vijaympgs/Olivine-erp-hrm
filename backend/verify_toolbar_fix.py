import os
import sys
import django

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.erp_core.settings')
django.setup()

from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.services.toolbar_permission_service import resolve_toolbar_permissions

User = get_user_model()

def verify_toolbar():
    print("Verifying Toolbar Permissions...")
    user = User.objects.filter(is_superuser=True).first()
    if not user:
        print("No superuser found.")
        return

    menu_id = 'HRM_EMPLOYEE_RECORDS'
    
    # Test CREATE mode (mapped to NEW)
    print(f"\nTesting {menu_id} in CREATE mode:")
    result = resolve_toolbar_permissions(user.id, menu_id, 'CREATE')
    actions = result.get('allowed_actions', [])
    print(f"Allowed Actions: {actions}")
    
    expected = ['save', 'cancel', 'clear']
    missing = [act for act in expected if act not in actions]
    
    if not missing:
        print("✅ SUCCESS: All expected actions are present.")
    else:
        print(f"❌ FAILURE: Missing actions: {missing}")

    # Test VIEW mode
    print(f"\nTesting {menu_id} in VIEW mode:")
    result_view = resolve_toolbar_permissions(user.id, menu_id, 'VIEW')
    actions_view = result_view.get('allowed_actions', [])
    print(f"Allowed Actions: {actions_view}")
    
    if 'view' in actions_view and 'new' in actions_view:
         print("✅ SUCCESS: VIEW actions present.")
    else:
         print("❌ FAILURE: Missing standard VIEW actions.")

if __name__ == '__main__':
    verify_toolbar()
