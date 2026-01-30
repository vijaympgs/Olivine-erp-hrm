import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
# Add paths
sys.path.append(os.getcwd())
sys.path.insert(0, os.path.dirname(os.getcwd()))  # Add project root
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem
from HRM.backend.hrm.models.employee import EmployeeRecord

print("=" * 80)
print("CHECKING HRM_EMPLOYEE_RECORDS MENU ITEM")
print("=" * 80)

# Check menu item
menu_item = ERPMenuItem.objects.filter(menu_id='HRM_EMPLOYEE_RECORDS').first()
if menu_item:
    print(f"✅ Menu Item Found:")
    print(f"   Menu ID: {menu_item.menu_id}")
    print(f"   Menu Name: {menu_item.menu_name}")
    print(f"   View Type: {menu_item.view_type}")
    print(f"   Module: {menu_item.module_name}")
    print(f"   Submodule: {menu_item.submodule}")
    print(f"   Toolbar Config: {menu_item.toolbar_config}")
    print(f"   Applicable Toolbar Config: {menu_item.applicable_toolbar_config}")
    print(f"   Is Active: {menu_item.is_active}")
else:
    print("❌ Menu Item NOT FOUND for 'HRM_EMPLOYEE_RECORDS'")
    print("\nSearching for similar menu items...")
    similar = ERPMenuItem.objects.filter(menu_id__icontains='EMPLOYEE').values_list('menu_id', 'menu_name')
    for menu_id, menu_name in similar:
        print(f"   - {menu_id}: {menu_name}")

print("\n" + "=" * 80)
print("CHECKING EMPLOYEE RECORDS DATA")
print("=" * 80)

# Check employee data
employee_count = EmployeeRecord.objects.count()
print(f"Total Employee Records: {employee_count}")

if employee_count > 0:
    print("\nFirst 5 employees:")
    for emp in EmployeeRecord.objects.all()[:5]:
        print(f"   - {emp.employee_number}: {emp.full_name} ({emp.department_name})")
else:
    print("❌ No employee records found in database")
    print("\nTo seed employee data, run:")
    print("   python backend/manage.py shell < seed_employees.py")

print("\n" + "=" * 80)
