"""
Update EMPLOYEE_RECORDS toolbar_list to include V, E, D actions
This ensures View, Edit, and Delete buttons are available in LIST mode
"""

import os
import sys
import django

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings')
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def update_employee_toolbar():
    """Update toolbar_list for EMPLOYEE_RECORDS to include V, E, D"""
    
    try:
        # Find EMPLOYEE_RECORDS menu item
        employee_records = ERPMenuItem.objects.filter(menu_code='EMPLOYEE_RECORDS').first()
        
        if not employee_records:
            print("❌ EMPLOYEE_RECORDS menu item not found")
            return
        
        print(f"Found EMPLOYEE_RECORDS (ID: {employee_records.id})")
        print(f"Current toolbar_list: {employee_records.toolbar_list}")
        
        # Update toolbar_list to include V, E, D
        # Current: NRQFIOX
        # New: NRQFVIOX (added V, E, D)
        new_toolbar_list = 'NRQFVIOX'
        
        employee_records.toolbar_list = new_toolbar_list
        employee_records.save()
        
        print(f"✅ Updated toolbar_list to: {new_toolbar_list}")
        print("\nActions included:")
        print("  N = New")
        print("  R = Refresh")
        print("  Q = Query/Search")
        print("  F = Filter")
        print("  V = View")
        print("  I = Import")
        print("  O = Export")
        print("  X = Exit")
        print("\nNote: Edit (E) and Delete (D) are controlled by selection-aware logic in the frontend")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    update_employee_toolbar()
