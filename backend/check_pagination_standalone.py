import os
import sys
import django

# Add project root to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')

if __name__ == '__main__':
    try:
        django.setup()
        from HRM.backend.hrm.views import EmployeeViewSet
        print(f"Pagination Class: {EmployeeViewSet.pagination_class}")
        if hasattr(EmployeeViewSet.pagination_class, 'page_size'):
             print(f"Page Size: {EmployeeViewSet.pagination_class.page_size}")
    except Exception as e:
        print(f"Error: {e}")
