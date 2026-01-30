"""Seed Employee Data for HRM Module
Run: python manage.py shell < seed_employees.py
"""
import os
import django
import sys
from datetime import date, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')

# Add paths
sys.path.append(os.getcwd())
sys.path.insert(0, os.path.dirname(os.getcwd()))  # Add project root

django.setup()

from HRM.backend.hrm.models.employee import EmployeeRecord
from HRM.backend.hrm.models.department import Department

print("=" * 80)
print("SEEDING EMPLOYEE DATA FOR HRM MODULE")
print("=" * 80)

# Create departments
departments_data = [
    {'name': 'Engineering', 'description': 'Software Development Team'},
    {'name': 'Human Resources', 'description': 'HR Management Team'},
    {'name': 'Finance', 'description': 'Finance and Accounting'},
    {'name': 'Marketing', 'description': 'Marketing and Sales'},
    {'name': 'Operations', 'description': 'Operations Team'},
    {'name': 'IT Support', 'description': 'IT Infrastructure'},
    {'name': 'Administration', 'description': 'Administrative Staff'},
]

print("\nCreating departments...")
for dept_data in departments_data:
    dept, created = Department.objects.get_or_create(
        name=dept_data['name'],
        defaults={
            'description': dept_data['description'],
            'is_active': True,
            'created_at': django.utils.timezone.now(),
            'updated_at': django.utils.timezone.now(),
        }
    )
    if created:
        print(f"✅ Created department: {dept.name}")
    else:
        print(f"🔄 Found department: {dept.name}")

# Sample employee data
employees_data = [
    {
        'employee_number': 'EMP001',
        'first_name': 'John',
        'last_name': 'Smith',
        'middle_name': 'Michael',
        'preferred_name': 'John',
        'name_prefix': 'Mr.',
        'name_suffix': 'Jr.',
        'gender': 'MALE',
        'date_of_birth': date(1985, 3, 15),
        'marital_status': 'MARRIED',
        'national_id': 'SSN123456789',
        'social_security_number': '123-45-67890',
        'passport_number': 'P123456789',
        'work_email': 'john.smith@mindra.com',
        'personal_email': 'john.smith.personal@gmail.com',
        'work_phone': '+1-555-123-4567',
        'mobile_phone': '+1-555-987-6543',
        'home_phone': '+1-555-234-5678',
        'hire_date': date(2020, 1, 15),
        'original_hire_date': date(2020, 1, 15),
        'employment_status': 'ACTIVE',
        'employment_type': 'FULL_TIME',
        'position_title': 'Senior Software Engineer',
        'department_name': 'Engineering',
        'job_category': 'Technical',
        'job_level': 'L5',
        'job_family': 'Engineering',
        'work_location_name': 'Main Office',
        'remote_work_eligible': True,
        'remote_work_percentage': 50,
        'manager_name_display': 'Jane Doe',
        'hierarchy_level': 3,
        'hr_business_partner_name': 'Sarah Wilson',
        'salary_grade': 'L5',
        'salary_step': '3',
        'annual_salary': 95000.00,
        'hourly_rate': 45.67,
        'currency': 'USD',
        'pay_frequency': 'BI_WEEKLY',
        'benefits_eligibility_date': date(2020, 1, 15),
        'benefits_package_name': 'Standard Package',
        'health_insurance_eligible': True,
        'dental_insurance_eligible': True,
        'vision_insurance_eligible': True,
        'retirement_plan_eligible': True,
        'life_insurance_eligible': True,
        'primary_emergency_contact_name': 'Mary Smith',
        'primary_emergency_contact_relationship': 'Spouse',
        'primary_emergency_contact_phone': '+1-555-111-2222',
        'secondary_emergency_contact_name': 'Robert Smith',
        'secondary_emergency_contact_relationship': 'Father',
        'secondary_emergency_contact_phone': '+1-555-333-4444',
        'is_active': True,
        'is_confidential': False,
        'is_key_employee': True,
        'is_high_potential': True,
        'username': 'john.smith',
        'role': 'SENIOR_ENGINEER',
    },
    {
        'employee_number': 'EMP002',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'middle_name': 'Elizabeth',
        'preferred_name': 'Jane',
        'name_prefix': 'Ms.',
        'name_suffix': '',
        'gender': 'FEMALE',
        'date_of_birth': date(1988, 7, 22),
        'marital_status': 'MARRIED',
        'national_id': 'SSN987654321',
        'social_security_number': '987-65-4321',
        'passport_number': 'P987654321',
        'work_email': 'jane.doe@mindra.com',
        'personal_email': 'jane.doe.personal@gmail.com',
        'work_phone': '+1-555-234-5678',
        'mobile_phone': '+1-555-876-5432',
        'home_phone': '+1-555-345-6789',
        'hire_date': date(2019, 6, 1),
        'original_hire_date': date(2019, 6, 1),
        'employment_status': 'ACTIVE',
        'employment_type': 'FULL_TIME',
        'position_title': 'HR Manager',
        'department_name': 'Human Resources',
        'job_category': 'Management',
        'job_level': 'L4',
        'job_family': 'Management',
        'work_location_name': 'Main Office',
        'remote_work_eligible': True,
        'remote_work_percentage': 30,
        'manager_name_display': 'CEO Office',
        'hierarchy_level': 2,
        'hr_business_partner_name': 'Sarah Wilson',
        'salary_grade': 'L4',
        'salary_step': '2',
        'annual_salary': 75000.00,
        'hourly_rate': 36.06,
        'currency': 'USD',
        'pay_frequency': 'BI_WEEKLY',
        'benefits_eligibility_date': date(2019, 6, 1),
        'benefits_package_name': 'Management Package',
        'health_insurance_eligible': True,
        'dental_insurance_eligible': True,
        'vision_insurance_eligible': True,
        'retirement_plan_eligible': True,
        'life_insurance_eligible': True,
        'primary_emergency_contact_name': 'John Doe',
        'primary_emergency_contact_relationship': 'Husband',
        'primary_emergency_contact_phone': '+1-555-111-2222',
        'secondary_emergency_contact_name': 'Elizabeth Doe',
        'secondary_emergency_contact_relationship': 'Mother',
        'secondary_emergency_contact_phone': '+1-555-333-4444',
        'is_active': True,
        'is_confidential': False,
        'is_key_employee': True,
        'is_high_potential': True,
        'username': 'jane.doe',
        'role': 'HR_MANAGER',
    },
    {
        'employee_number': 'EMP003',
        'first_name': 'Michael',
        'last_name': 'Johnson',
        'middle_name': 'David',
        'preferred_name': 'Mike',
        'name_prefix': 'Mr.',
        'name_suffix': '',
        'gender': 'MALE',
        'date_of_birth': date(1990, 11, 8),
        'marital_status': 'SINGLE',
        'national_id': 'SSN456789012',
        'social_security_number': '456-78-9012',
        'passport_number': 'P456789012',
        'work_email': 'michael.johnson@mindra.com',
        'personal_email': 'michael.johnson.personal@gmail.com',
        'work_phone': '+1-555-345-6789',
        'mobile_phone': '+1-555-987-6543',
        'home_phone': '+1-555-234-5678',
        'hire_date': date(2021, 3, 10),
        'original_hire_date': date(2021, 3, 10),
        'employment_status': 'ACTIVE',
        'employment_type': 'FULL_TIME',
        'position_title': 'Marketing Manager',
        'department_name': 'Marketing',
        'job_category': 'Management',
        'job_level': 'L4',
        'job_family': 'Marketing',
        'work_location_name': 'Main Office',
        'remote_work_eligible': True,
        'remote_work_percentage': 20,
        'manager_name_display': 'Jane Doe',
        'hierarchy_level': 3,
        'hr_business_partner_name': 'Sarah Wilson',
        'salary_grade': 'L4',
        'salary_step': '1',
        'annual_salary': 72000.00,
        'hourly_rate': 34.62,
        'currency': 'USD',
        'pay_frequency': 'BI_WEEKLY',
        'benefits_eligibility_date': date(2021, 3, 10),
        'benefits_package_name': 'Management Package',
        'health_insurance_eligible': True,
        'dental_insurance_eligible': True,
        'vision_insurance_eligible': True,
        'retirement_plan_eligible': True,
        'life_insurance_eligible': True,
        'primary_emergency_contact_name': 'Pat Johnson',
        'primary_emergency_contact_relationship': 'Father',
        'primary_emergency_contact_phone': '+1-555-555-1234',
        'secondary_emergency_contact_name': 'Linda Johnson',
        'secondary_emergency_contact_relationship': 'Mother',
        'secondary_emergency_contact_phone': '+1-555-555-5678',
        'is_active': True,
        'is_confidential': False,
        'is_key_employee': False,
        'is_high_potential': True,
        'username': 'michael.johnson',
        'role': 'MARKETING_MANAGER',
    },
    {
        'employee_number': 'EMP004',
        'first_name': 'Sarah',
        'last_name': 'Wilson',
        'middle_name': 'Ann',
        'preferred_name': 'Sarah',
        'name_prefix': 'Ms.',
        'name_suffix': '',
        'gender': 'FEMALE',
        'date_of_birth': date(1982, 5, 12),
        'marital_status': 'MARRIED',
        'national_id': 'SSN789012345',
        'social_security_number': '789-01-2345',
        'passport_number': 'P789012345',
        'work_email': 'sarah.wilson@mindra.com',
        'personal_email': 'sarah.wilson.personal@gmail.com',
        'work_phone': '+1-555-234-5678',
        'mobile_phone': '+1-555-876-5432',
        'home_phone': '+1-555-345-6789',
        'hire_date': date(2018, 9, 1),
        'original_hire_date': date(2018, 9, 1),
        'employment_status': 'ACTIVE',
        'employment_type': 'FULL_TIME',
        'position_title': 'Finance Manager',
        'department_name': 'Finance',
        'job_category': 'Management',
        'job_level': 'L4',
        'job_family': 'Finance',
        'work_location_name': 'Main Office',
        'remote_work_eligible': False,
        'remote_work_percentage': 0,
        'manager_name_display': 'CEO Office',
        'hierarchy_level': 2,
        'hr_business_partner_name': 'Sarah Wilson',
        'salary_grade': 'L4',
        'salary_step': '2',
        'annual_salary': 85000.00,
        'hourly_rate': 40.87,
        'currency': 'USD',
        'pay_frequency': 'BI_WEEKLY',
        'benefits_eligibility_date': date(2018, 9, 1),
        'benefits_package_name': 'Executive Package',
        'health_insurance_eligible': True,
        'dental_insurance_eligible': True,
        'vision_insurance_eligible': True,
        'retirement_plan_eligible': True,
        'life_insurance_eligible': True,
        'primary_emergency_contact_name': 'Tom Wilson',
        'primary_emergency_contact_relationship': 'Husband',
        'primary_emergency_contact_phone': '+1-555-111-2222',
        'secondary_emergency_contact_name': 'Nancy Wilson',
        'secondary_emergency_contact_relationship': 'Mother',
        'secondary_emergency_contact_phone': '+1-555-333-4444',
        'is_active': True,
        'is_confidential': False,
        'is_key_employee': True,
        'is_high_potential': False,
        'username': 'sarah.wilson',
        'role': 'FINANCE_MANAGER',
    },
    {
        'employee_number': 'EMP005',
        'first_name': 'Robert',
        'last_name': 'Brown',
        'middle_name': 'James',
        'preferred_name': 'Rob',
        'name_prefix': 'Mr.',
        'name_suffix': '',
        'gender': 'MALE',
        'date_of_birth': date(1979, 8, 25),
        'marital_status': 'DIVORCED',
        'national_id': 'SSN321654987',
        'social_security_number': '321-65-4987',
        'passport_number': 'P321654987',
        'work_email': 'robert.brown@mindra.com',
        'personal_email': 'robert.brown.personal@gmail.com',
        'work_phone': '+1-555-345-6789',
        'mobile_phone': '+1-555-987-6543',
        'home_phone': '+1-555-234-5678',
        'hire_date': date(2017, 5, 15),
        'original_hire_date': date(2017, 5, 15),
        'employment_status': 'ACTIVE',
        'employment_type': 'FULL_TIME',
        'position_title': 'Operations Manager',
        'department_name': 'Operations',
        'job_category': 'Management',
        'job_level': 'L3',
        'job_family': 'Operations',
        'work_location_name': 'Main Office',
        'remote_work_eligible': False,
        'remote_work_percentage': 0,
        'manager_name_display': 'Sarah Wilson',
        'hierarchy_level': 3,
        'hr_business_partner_name': 'Sarah Wilson',
        'salary_grade': 'L3',
        'salary_step': '1',
        'annual_salary': 65000.00,
        'hourly_rate': 31.25,
        'currency': 'USD',
        'pay_frequency': 'BI_WEEKLY',
        'benefits_eligibility_date': date(2017, 5, 15),
        'benefits_package_name': 'Standard Package',
        'health_insurance_eligible': True,
        'dental_insurance_eligible': True,
        'vision_insurance_eligible': True,
        'retirement_plan_eligible': True,
        'life_insurance_eligible': True,
        'primary_emergency_contact_name': 'Emily Brown',
        'primary_emergency_contact_relationship': 'Wife',
        'primary_emergency_contact_phone': '+1-555-111-2222',
        'secondary_emergency_contact_name': 'David Brown',
        'secondary_emergency_contact_relationship': 'Brother',
        'secondary_emergency_contact_phone': '+1-555-333-4444',
        'is_active': True,
        'is_confidential': False,
        'is_key_employee': False,
        'is_high_potential': False,
        'username': 'robert.brown',
        'role': 'OPERATIONS_MANAGER',
    }
]

print(f"\nCreating {len(employees_data)} employee records...")

created_count = 0
updated_count = 0

for emp_data in employees_data:
    # Create employee record
    employee, created = EmployeeRecord.objects.update_or_create(
        employee_number=emp_data['employee_number'],
        company_code='MINDRA',
        defaults={
            'first_name': emp_data['first_name'],
            'last_name': emp_data['last_name'],
            'middle_name': emp_data.get('middle_name', ''),
            'preferred_name': emp_data.get('preferred_name', ''),
            'name_prefix': emp_data.get('name_prefix', ''),
            'name_suffix': emp_data.get('name_suffix', ''),
            'gender': emp_data['gender'],
            'date_of_birth': emp_data['date_of_birth'],
            'marital_status': emp_data['marital_status'],
            'national_id': emp_data.get('national_id', ''),
            'social_security_number': emp_data.get('social_security_number', ''),
            'passport_number': emp_data.get('passport_number', ''),
            'work_email': emp_data['work_email'],
            'personal_email': emp_data.get('personal_email', ''),
            'work_phone': emp_data.get('work_phone', ''),
            'mobile_phone': emp_data.get('mobile_phone', ''),
            'home_phone': emp_data.get('home_phone', ''),
            'hire_date': emp_data['hire_date'],
            'original_hire_date': emp_data.get('original_hire_date', emp_data['hire_date']),
            'employment_status': emp_data['employment_status'],
            'employment_type': emp_data['employment_type'],
            'position_title': emp_data['position_title'],
            'department_name': emp_data['department_name'],
            'job_category': emp_data.get('job_category', ''),
            'job_level': emp_data['job_level'],
            'job_family': emp_data.get('job_family', ''),
            'work_location_name': emp_data['work_location_name'],
            'remote_work_eligible': emp_data['remote_work_eligible'],
            'remote_work_percentage': emp_data['remote_work_percentage'],
            'manager_name_display': emp_data['manager_name_display'],
            'hierarchy_level': emp_data['hierarchy_level'],
            'hr_business_partner_name': emp_data['hr_business_partner_name'],
            'salary_grade': emp_data['salary_grade'],
            'salary_step': emp_data['salary_step'],
            'annual_salary': emp_data['annual_salary'],
            'hourly_rate': emp_data['hourly_rate'],
            'currency': emp_data['currency'],
            'pay_frequency': emp_data['pay_frequency'],
            'benefits_eligibility_date': emp_data.get('benefits_eligibility_date', emp_data['hire_date']),
            'benefits_package_name': emp_data['benefits_package_name'],
            'health_insurance_eligible': emp_data['health_insurance_eligible'],
            'dental_insurance_eligible': emp_data['dental_insurance_eligible'],
            'vision_insurance_eligible': emp_data['vision_insurance_eligible'],
            'retirement_plan_eligible': emp_data['retirement_plan_eligible'],
            'life_insurance_eligible': emp_data['life_insurance_eligible'],
            'primary_emergency_contact_name': emp_data['primary_emergency_contact_name'],
            'primary_emergency_contact_relationship': emp_data['primary_emergency_contact_relationship'],
            'primary_emergency_contact_phone': emp_data['primary_emergency_contact_phone'],
            'secondary_emergency_contact_name': emp_data.get('secondary_emergency_contact_name', ''),
            'secondary_emergency_contact_relationship': emp_data.get('secondary_emergency_contact_relationship', ''),
            'secondary_emergency_contact_phone': emp_data.get('secondary_emergency_contact_phone', ''),
            'is_active': emp_data['is_active'],
            'is_confidential': emp_data['is_confidential'],
            'is_key_employee': emp_data['is_key_employee'],
            'is_high_potential': emp_data['is_high_potential'],
            'username': emp_data['username'],
            'role': emp_data['role'],
            'created_at': django.utils.timezone.now(),
            'updated_at': django.utils.timezone.now(),
        }
    )
    
    if created:
        created_count += 1
        print(f"✅ Created: {emp_data['first_name']} {emp_data['last_name']} ({emp_data['employee_number']})")
    else:
        updated_count += 1
        print(f"🔄 Updated: {emp_data['first_name']} {emp_data['last_name']} ({emp_data['employee_number']})")

print(f"\n✅ Seed complete: {created_count} created, {updated_count} updated")
print(f"Total employees: {EmployeeRecord.objects.count()}")

# Verify the seeded data
print("\n" + "=" * 80)
print("VERIFICATION")
print("=" * 80)

print(f"Total Employees: {EmployeeRecord.objects.count()}")

print("\nEmployee Count by Department:")
for dept in Department.objects.all():
    emp_count = EmployeeRecord.objects.filter(department_name=dept.name).count()
    print(f"  {dept.name}: {emp_count}")

print(f"\nActive Employees: {EmployeeRecord.objects.filter(is_active=True).count()}")
print(f"Inactive Employees: {EmployeeRecord.objects.filter(is_active=False).count()}")

print("\nFirst 5 employees:")
for emp in EmployeeRecord.objects.all()[:5]:
    print(f"  - {emp.employee_number}: {emp.first_name} {emp.last_name} ({emp.department_name})")

print("\n" + "=" * 80)
print("SEEDING COMPLETE")
print("=" * 80)
