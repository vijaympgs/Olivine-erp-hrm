from HRM.models.employee import EmployeeRecord
from django.conf import settings

print(f"Checking Employee Count...")
try:
    count = EmployeeRecord.objects.count()
    print(f"Total Employees: {count}")
    
    if count > 0:
        first = EmployeeRecord.objects.first()
        print(f"First Employee: {first} (ID: {first.id})")
        print(f"Company Code: {getattr(first, 'company_code', 'N/A')}")
        print(f"Is Active: {first.is_active}")
except Exception as e:
    print(f"Error: {e}")
