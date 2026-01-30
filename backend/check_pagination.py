import os
import django
from django.conf import settings

# Setup Django (if not already handled by manage.py shell context, but this file is meant for shell exec)
# Assuming 'exec(open...)' in shell, so django is setup.

try:
    from HRM.backend.hrm.views import EmployeeViewSet, StandardResultsSetPagination
    print(f"EmployeeViewSet Pagination Class: {EmployeeViewSet.pagination_class}")
    print(f"Standard Pagination Page Size: {StandardResultsSetPagination.page_size}")
except ImportError as e:
    print(f"Import Error: {e}")
except AttributeError as e:
    print(f"Attribute Error: {e}")
except Exception as e:
    print(f"Error: {e}")
