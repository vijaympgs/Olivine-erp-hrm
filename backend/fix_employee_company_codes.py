import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
sys.path.insert(0, '..')
django.setup()

from HRM.backend.hrm.models.employee import EmployeeRecord
from core.licensing.backend.business_entities.models import Company

# Get the active company
company = Company.objects.filter(status='ACTIVE').first()
if not company:
    print("❌ No active company found!")
    sys.exit(1)

print(f"Active Company: {company.code} (ID: {company.id})")
print(f"Company Name: {company.name}")

# Get all employees
employees = EmployeeRecord.objects.all()
total_count = employees.count()

print(f"\nTotal Employee Records: {total_count}")

# Check current company codes
unique_codes = EmployeeRecord.objects.values_list('company_code', flat=True).distinct()
print(f"Current company codes in Employee Records: {list(unique_codes)}")

# Update all employees to use the active company code
print(f"\nUpdating all employee records to company_code='{company.code}'...")
updated_count = EmployeeRecord.objects.update(company_code=company.code)

print(f"✅ Updated {updated_count} employee records")

# Verify
unique_codes_after = EmployeeRecord.objects.values_list('company_code', flat=True).distinct()
print(f"\nCompany codes after update: {list(unique_codes_after)}")

# Show sample employees
print(f"\nSample employees (first 5):")
for emp in EmployeeRecord.objects.all()[:5]:
    print(f"  - {emp.employee_number}: {emp.full_name} | Company: {emp.company_code}")

print("\n✅ All employee records updated successfully!")
