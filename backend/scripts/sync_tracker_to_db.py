import os
import sys
import django
import re

# Setup Django Environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(PROJECT_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.base")
django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

TRACKER_PATH = os.path.join(PROJECT_ROOT, '.steering', '04_EXECUTION_PLANS_FIX_REFERENCES', 'RETAIL_IMPLEMENTATION_TRACKER.md')

def get_suggested_type(feature_name):
    name = feature_name.lower()
    if any(x in name for x in ['report', 'analysis', 'valuation', 'dead stock', 'aging']):
        return 'REPORT'
    if any(x in name for x in ['dashboard', 'overview', 'monitor', 'summary', 'trends']):
        return 'DASHBOARD'
    if any(x in name for x in ['setup', 'configuration', 'parameter', 'settings']):
        return 'CONFIGURATION'
    if any(x in name for x in ['master', 'catalog', 'hierarchy', 'uom', 'directory']):
        if 'list' in name or 'directory' in name:
            return 'MASTER' # or LIST? Masters often have lists.
        return 'MASTER'
    if any(x in name for x in ['entry', 'checkout', 'register']):
        return 'TRANSACTION'
    if any(x in name for x in ['history', 'list', 'management', 'bills', 'payments', 'compliance', 'returns', 'receipts', 'orders', 'invoices', 'quotes', 'requisitions', 'rfqs', 'asns']):
        return 'LIST'
    
    return 'LIST' # Default for sidebar items

def audit_tracker_and_db():
    print("=" * 100)
    print("AUDITING TRACKER vs DATABASE")
    print("=" * 100)

    # 1. Load Tracker Data
    tracker_features = []
    with open(TRACKER_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        # Find table rows with | Feature | Path |
        # Handles various columns: | Feature | Path | UI | Tool ... or | Feature | Path | Status ...
        matches = re.findall(r'\|([^|]+)\|([^|]+)\|[^|]+\|', content)
        for m in matches:
            feature = m[0].strip()
            path = m[1].strip()
            # Skip header rows and non-path rows
            if feature and feature not in ['Feature', 'Sub-Module', 'Total UIs', 'Overall Retail Module UI Progress'] and path.startswith('/'):
                tracker_features.append({
                    'feature': feature,
                    'path': path,
                    'suggested_type': get_suggested_type(feature)
                })

    print(f"Loaded {len(tracker_features)} features from tracker.")

    # 2. Match with Database and Update
    updated_count = 0
    
    # Standard configuration strings
    CONFIGS = {
        'MASTER': 'NESCKVDXRQFIO',
        'TRANSACTION': 'NESCKZTJAVPMRDX1234QF',
        'REPORT': 'VRXPYQFG',
        'DASHBOARD': 'VRXQFG',
        'LIST': 'NRQFX',
        'CONFIGURATION': 'ESCKXR',
    }

    for feature in tracker_features:
        name = feature['feature']
        path = feature['path']
        type_suggested = feature['suggested_type']
        
        # Try to find by name or path
        items = ERPMenuItem.objects.filter(module_name='RETAIL').filter(
            django.db.models.Q(menu_name__iexact=name) | 
            django.db.models.Q(route_path=path) |
            django.db.models.Q(menu_id__iexact=name.replace(' ', '_'))
        )
        
        if not items.exists():
            # Try fuzzy name match
            items = ERPMenuItem.objects.filter(module_name='RETAIL', menu_name__icontains=name)

        for item in items:
            if item.view_type != type_suggested:
                print(f"[TYPE MISMATCH] {item.menu_name}")
                print(f"  ID: {item.menu_id}")
                print(f"  Tracker Feature: {name}")
                print(f"  Current Type: {item.view_type}")
                print(f"  Suggested Type: {type_suggested}")
                
                item.view_type = type_suggested
                # Update config if it's the standard one for that type
                if type_suggested in CONFIGS:
                    item.applicable_toolbar_config = CONFIGS[type_suggested]
                
                item.save()
                updated_count += 1
                print(f"  UPDATED")

    print("\n" + "=" * 100)
    print(f"Audit Complete. Total Updates: {updated_count}")
    print("=" * 100)

if __name__ == "__main__":
    audit_tracker_and_db()




