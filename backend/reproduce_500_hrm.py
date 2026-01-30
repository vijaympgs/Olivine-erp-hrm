import os
import django
import sys

# Set up Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from HRM.backend.hrm.views.employee import EmployeeRecordViewSet
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

def test_employee_list():
    factory = APIRequestFactory()
    request = factory.get('/api/hrm/api/v1/employees/')
    
    # Get or create a superuser for testing
    user, _ = User.objects.get_or_create(username='admin', is_superuser=True, is_staff=True)
    force_authenticate(request, user=user)
    
    view = EmployeeRecordViewSet.as_view({'get': 'list'})
    
    try:
        response = view(request)
        print(f"Status Code: {response.status_code}")
        if response.status_code != 200:
            print(f"Response Data: {response.data}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_employee_list()
