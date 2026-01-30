import os
import sys
import django

# Setup Django Environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(PROJECT_ROOT) # Add root to path for 'core' module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.base")
django.setup()

from core.auth_access.backend.user_management.models import ERPToolbarControl, ERPMenuItem

# Standard Character Mapping Documentation
# N: New
# E: Edit
# S: Save
# C: Cancel
# L: Clear
# Z: Authorize
# M: Submit
# J: Reject
# A: Amend
# V: View
# P: Print
# G: Email (Gmail/Mail)
# R: Refresh
# D: Delete
# H: Hold
# O: Void (0/O)
# X: Exit
# U: Upload
# W: Download (Write/Down)
# K: Clone
# F: First
# B: Prev (Back)
# N: Next (Conflict with New? Use T: Next(Target)) -> NO, Use > < logic or mapped
# Let's clean mapping for the super string:

# REVISED MAPPING:
# N: New
# E: Edit
# S: Save
# C: Cancel
# K: Clear (Klear)
# Z: Authorize
# T: Submit (Transmit)
# J: Reject
# A: Amend
# V: View
# P: Print
# M: Email
# R: Refresh
# D: Delete
# H: Hold
# O: Void
# X: Exit
# I: Import/Upload
# Y: Export/Download
# L: Clone (Like)
# 1: First
# 2: Prev
# 3: Next
# 4: Last
# Q: Search
# F: Filter
# B: Notes (Book)
# G: Attach (Group/Paperclip)
# W: Settings (Wrench)
# ?: Help

MASTER_STRING = "NESCKZTJAVPMRDHOXIYL1234QFBGW?"

def seed_toolbar_controls():
    print("Seeding ERPToolbarControl...")
    
    controls = [
        {
            "module": "RETAIL",
            "string": MASTER_STRING,
            "desc": "Standard Retail Operations Toolbar"
        },
        {
            "module": "FMS",
            "string": MASTER_STRING,
            "desc": "Standard Financial Management Toolbar"
        },
        {
            "module": "HRM",
            "string": MASTER_STRING,
            "desc": "Standard HR Toolbar"
        },
        {
            "module": "CRM",
            "string": MASTER_STRING,
            "desc": "Standard CRM Toolbar"
        }
    ]

    for c in controls:
        obj, created = ERPToolbarControl.objects.update_or_create(
            module_name=c['module'],
            defaults={
                'master_toolbar_string': c['string'],
                'description': c['desc']
            }
        )
        status = "Created" if created else "Updated"
        print(f"[{status}] {obj}")

def update_menu_items():
    print("\nUpdating ERPMenuItem references...")
    
    # Update logic:
    # 1. Fetch relevant control for the module.
    # 2. Update 'original_toolbar_string' from control.
    # 3. If 'applicable_toolbar_config' is empty, default it based on view_type.
    
    items = ERPMenuItem.objects.all()
    count = 0
    
    for item in items:
        # Get Control
        try:
            ctrl = ERPToolbarControl.objects.get(module_name=item.module_name)
            item.original_toolbar_string = ctrl.master_toolbar_string
        except ERPToolbarControl.DoesNotExist:
            print(f"Warning: No control found for module {item.module_name}")
            continue

        # Set Default Applicable Config if missing
        if not item.applicable_toolbar_config:
            if item.view_type == 'LIST':
                # List View Standard: New, Refresh, Search, Filter, Exit
                # Mapping: N, R, Q, F, X
                item.applicable_toolbar_config = "NRQFX"
            elif item.view_type in ['MASTER', 'TRANSACTION']:
                # Edit View Standard: Save, Cancel, Clear, Exit... usually dynamic based on mode
                # But we define the PERMITTED actions here.
                # Standard: New, Edit, Save, Cancel, Clear, View, Delete, Exit, Refresh
                # Mapping: N E S C K V D X R
                item.applicable_toolbar_config = "NESCKVDXR"
            else:
                # Reports/Dashboards: View, Refresh, Exit, Print, Export
                # Mapping: V R X P Y
                item.applicable_toolbar_config = "VRXPY"
        
        item.save()
        count += 1
        
    print(f"Updated {count} menu items.")

if __name__ == "__main__":
    seed_toolbar_controls()
    update_menu_items()




