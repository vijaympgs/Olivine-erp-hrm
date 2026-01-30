import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
sys.path.append(os.getcwd())
sys.path.insert(0, os.path.dirname(os.getcwd()))
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem
from HRM.backend.hrm.models.employee import EmployeeRecord

# Check menu item
menu_item = ERPMenuItem.objects.filter(menu_id='HRM_EMPLOYEE_RECORDS').first()
if menu_item:
    print(f"MENU ITEM FOUND")
    print(f"Menu ID: {menu_item.menu_id}")
    print(f"Menu Name: {menu_item.menu_name}")
    print(f"View Type: {menu_item.view_type}")
    print(f"Toolbar Config: {menu_item.toolbar_config}")
    print(f"Applicable Config: {menu_item.applicable_toolbar_config}")
else:
    print("MENU ITEM NOT FOUND")

# Check employee data
employee_count = EmployeeRecord.objects.count()
print(f"\nEmployee Records: {employee_count}")

if employee_count > 0:
    emp = EmployeeRecord.objects.first()
    print(f"First Employee: {emp.full_name}")
