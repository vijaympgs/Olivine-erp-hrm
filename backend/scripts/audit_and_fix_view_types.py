import os
import sys
import django

# Setup Django Environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.base")
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def audit_and_update_menu_item_types():
    print("=" * 80)
    print("AUDITING RETAIL MENU ITEM TYPES")
    print("=" * 80)

    # Standard configuration strings
    CONFIGS = {
        'MASTER': 'NESCKVDXRQFIO',
        'TRANSACTION': 'NESCKZTJAVPMRDX1234QF',
        'REPORT': 'VRXPYQFG',
        'DASHBOARD': 'VRXQFG',
        'LIST': 'NRQFX',
        'CONFIGURATION': 'ESCKXR',
    }

    # Classification Keywords
    KEYWORDS = {
        'REPORT': ['Report', 'Analysis', 'Velocity', 'Dead Stock', 'Aging', 'Trends'],
        'DASHBOARD': ['Dashboard', 'Overview', 'Summary', 'Monitor'],
        'CONFIGURATION': ['Setup', 'Configuration', 'Parameters', 'Settings', 'Preferences'],
        'TRANSACTION': ['Entry', 'Posting'], # Specific keywords for forms
    }

    retail_items = ERPMenuItem.objects.filter(module_name='RETAIL').order_by('menu_name')
    
    updates_made = 0
    
    for item in retail_items:
        original_type = item.view_type
        original_config = item.applicable_toolbar_config
        
        suggested_type = original_type
        
        name_lower = item.menu_name.lower()
        
        # 1. Detect Reports
        if any(k.lower() in name_lower for k in KEYWORDS['REPORT']):
            suggested_type = 'REPORT'
            
        # 2. Detect Dashboards
        elif any(k.lower() in name_lower for k in KEYWORDS['DASHBOARD']):
            suggested_type = 'DASHBOARD'
            
        # 3. Detect Configuration
        elif any(k.lower() in name_lower for k in KEYWORDS['CONFIGURATION']):
            suggested_type = 'CONFIGURATION'
            
        # 4. Refine Transaction vs List
        # Common pattern: Items with 'History' or 'List' or 'Management' are usually LIST
        elif 'history' in name_lower or 'list' in name_lower:
            suggested_type = 'LIST'
            
        # 5. Masters
        elif 'master' in name_lower or 'directory' in name_lower or 'catalog' in name_lower:
            suggested_type = 'MASTER'

        # Special cases from Tracker/User Feedback
        if 'Adjustment Reports' in item.menu_name:
            suggested_type = 'REPORT'
        
        # If it's currently LIST but looks like it shouldn't be
        if original_type == 'LIST':
            # Check for specific Transaction patterns that often get misclassified as LIST
            transaction_types = ['Order', 'Invoice', 'Quote', 'Requisition', 'Receipt', 'Return', 'Adjustment', 'Transfer']
            # If the name is exactly the transaction name or ends with "Entry"
            if any(t.lower() == name_lower for t in transaction_types) or name_lower.endswith('entry'):
                # Note: Many of these ARE list views (index pages), so we must be careful.
                # Usually, if the menu_id is uppercase, it's the TRANSACTION (form).
                # If it's lowercase with hyphens, it's the LIST.
                if item.menu_id.isupper():
                    suggested_type = 'TRANSACTION'

        # Update if changed
        if suggested_type != original_type:
            item.view_type = suggested_type
            
            # Also update config to the standard for that type if it's currently the default LIST config
            if suggested_type in CONFIGS:
                item.applicable_toolbar_config = CONFIGS[suggested_type]
            
            item.save()
            print(f"[RECLASSIFIED] {item.menu_name}")
            print(f"  ID: {item.menu_id}")
            print(f"  Type: {original_type} -> {suggested_type}")
            print(f"  Config: {original_config} -> {item.applicable_toolbar_config}")
            updates_made += 1
            
    print("\n" + "=" * 80)
    print(f"Audit Complete. Total Updates: {updates_made}")
    print("=" * 80)

if __name__ == "__main__":
    audit_and_update_menu_item_types()




