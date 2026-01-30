import os
import sys
import django
import json

if 'c:\\00mindra\\olivine-platform' not in sys.path:
    sys.path.append('c:\\00mindra\\olivine-platform')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.erp_core.settings')
django.setup()

from HRM.backend.hrm.models import EmployeeRecord
from django.db.models import Count, Q

def debug_hierarchy():
    try:
        print("Debugging Hierarchy View...")
        
        # Get CEO (employees with no manager and hierarchy_level = 0)
        ceo_employees = EmployeeRecord.objects.filter(
            manager__isnull=True,
            hierarchy_level=0,
            is_active=True
        ).order_by('hire_date')
        
        print(f"Found {ceo_employees.count()} CEOs.")
        
        def build_employee_hierarchy(employee):
            """Recursively build employee hierarchy tree"""
            # print(f"Processing: {employee.full_name}")
            employee_data = {
                'id': str(employee.id),
                'employee_number': employee.employee_number,
                'full_name': employee.full_name,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'position_title': employee.position_title,
                'department_name': employee.department_name,
                'work_email': employee.work_email,
                'is_active': employee.is_active,
                'hierarchy_level': employee.hierarchy_level,
                'manager_name': employee.manager_name,
                'children': []
            }
            
            # Get direct reports
            direct_reports = EmployeeRecord.objects.filter(
                manager=employee,
                is_active=True
            ).order_by('hierarchy_level', 'last_name', 'first_name')
            
            # Recursively add direct reports
            for report in direct_reports:
                employee_data['children'].append(build_employee_hierarchy(report))
            
            return employee_data
        
        # Build complete hierarchy starting from CEO(s)
        hierarchy_data = []
        for ceo in ceo_employees:
            print(f"Building tree for CEO: {ceo.full_name}")
            hierarchy_data.append(build_employee_hierarchy(ceo))
        
        print("Hierarchy build successful.")
        # print(json.dumps(hierarchy_data, indent=2))
        
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    debug_hierarchy()
