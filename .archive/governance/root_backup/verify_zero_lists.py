
import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')
sys.path.append(BACKEND_DIR)
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.dev")
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def verify():
    count = ERPMenuItem.objects.filter(view_type='LIST').count()
    print(f"Items with view_type='LIST': {count}")
    if count == 0:
        print("✅ SUCCESS: No LIST items remain.")
    else:
        print("❌ FAILURE: LIST items still exist.")

if __name__ == "__main__":
    verify()



