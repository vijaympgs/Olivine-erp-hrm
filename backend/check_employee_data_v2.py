
import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from HRM.backend.hrm.models.employee import EmployeeRecord
from django.contrib.auth import get_user_model

User = get_user_model()

print("--- CHECKS ---")
count_total = EmployeeRecord.objects.count()
print(f"Total Employees: {count_total}")

count_mindra = EmployeeRecord.objects.filter(company_code='MINDRA').count()
print(f"MINDRA Employees: {count_mindra}")

count_default = EmployeeRecord.objects.filter(company_code='DEFAULT').count()
print(f"DEFAULT Employees: {count_default}")

print("\n--- VIEW LOGIC SIMULATION ---")
# Simulating the default user behavior if company_code is missing
# In the view: company_code = getattr(user, 'company_code', 'MINDRA')
# We can't easily simulate 'request.user' without a request, but we can check if the logic holds.

print(f"Queryset using company_code='MINDRA': {EmployeeRecord.objects.filter(company_code='MINDRA').count()}")
