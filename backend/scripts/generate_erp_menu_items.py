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

# Configurations
CONFIGS = {
    'MASTER': 'NESCKVDXRQFIO',
    'SIMPLE_MASTER': 'NESCKVDXRQF',
    'TRANSACTION': 'NESCKZTJAVPMRDX1234QF',
    'REPORT': 'VRXPYQFG',
    'DASHBOARD': 'VRXQFG',
    'CONFIGURATION': 'ESCKXR',
    'LIST': 'NRQFX', # For Folder/List
}

# Module Rules (Top Level IDs)
MODULE_MAP = {
    'retail': 'RETAIL',
    'inventory': 'RETAIL',
    'procurement': 'RETAIL',
    'sales': 'RETAIL',
    'pos': 'RETAIL',
    'finance': 'FMS',
    'crm': 'CRM',
    'hr': 'HRM',
    'administration': 'ADMIN',
    'setup': 'RETAIL', # Mapped to Retail for visibility
    'security': 'ADMIN',
}

def get_view_type_and_config(label, path, has_children):
    """Determine View Type"""
    if has_children:
        # It's a Group/Folder
        return 'LIST', CONFIGS['LIST']

    # For Leaf Nodes
    l = label.lower()
    p = path.lower() if path else ''
    
    # Reports
    if any(x in l or x in p for x in ['report', 'analysis', 'valuation', 'history', 'log', 'trail', 'aging']):
        return 'REPORT', CONFIGS['REPORT']
    
    # Dashboards
    if 'dashboard' in l or 'overview' in l or 'summary' in l:
        return 'DASHBOARD', CONFIGS['DASHBOARD']
    
    # Config
    if any(x in l or x in p for x in ['config', 'setup', 'parameter', 'rule', 'template', 'mapping', 'matrix']):
        return 'CONFIGURATION', CONFIGS['CONFIGURATION']
        
    # Masters (Enhanced keyword list)
    if 'master' in l or 'directory' in l or 'profile' in l:
        return 'MASTER', CONFIGS['MASTER']
    if any(x in l or x in p for x in ['category', 'brand', 'tax', 'currenc', 'terms', 'bank', 'account', 'uom', 'measure', 'attribute', 'reason', 'code', 'template']):
        return 'MASTER', CONFIGS['SIMPLE_MASTER']
        
    # Default
    return 'TRANSACTION', CONFIGS['TRANSACTION']

def upsert_item(mid, label, path, parent_id, id_module_map, stack, is_parent=False):
    """Helper to update DB"""
    if not mid: return
    
    # Determine Module
    module = 'OTHER'
    if mid in MODULE_MAP:
        module = MODULE_MAP[mid]
    elif parent_id and parent_id in id_module_map:
        module = id_module_map[parent_id]
    else:
        # Fallback
        if path and '/admin' in path: module = 'ADMIN'
        elif path and '/retail' in path: module = 'RETAIL'
        elif path and '/operations' in path: module = 'RETAIL'
        elif path and '/crm' in path: module = 'CRM'
        elif path and '/finance' in path: module = 'FMS'
        elif path and '/hr' in path: module = 'HRM'
        elif path and '/setup' in path: module = 'SETUP'
    
    # Store for children
    id_module_map[mid] = module
    
    # Config
    vtype, config = get_view_type_and_config(label, path, is_parent)
    
    # Upsert
    db_id = mid.upper().replace('-', '_')
    parent_db_id = parent_id.upper().replace('-', '_') if parent_id else None
    
    parent_obj = None
    if parent_db_id:
        try:
            parent_obj = ERPMenuItem.objects.get(menu_id=parent_db_id)
        except ERPMenuItem.DoesNotExist:
            print(f"Warning: Parent {parent_db_id} not found for {db_id}")
    
    _, created = ERPMenuItem.objects.update_or_create(
        menu_id=db_id,
        defaults={
            'menu_name': label or mid,
            'module_name': module,
            'view_type': vtype,
            'applicable_toolbar_config': config,
            'route_path': path,
            'parent_menu': parent_obj,
            'is_active': True
        }
    )
    if 'company' in mid.lower() or 'setup' in mid.lower():
         print(f"DEBUG: {db_id} -> {module} (Parent: {parent_id})")

def process_menu_hierarchy():
    print("=" * 100)
    print("REGENERATING TOOLBAR REGISTRY (HIERARCHICAL STRUCTURAL FIX)")
    print("=" * 100)
    
    file_path = os.path.join(PROJECT_ROOT, 'frontend', 'src', 'app', 'menuConfig.ts')
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    stack = [] # Stack of ID strings
    id_module_map = {}
    
    last_id = None
    last_label = None
    last_path = None
    
    count_groups = 0
    count_leaves = 0
    
    for line in lines:
        line = line.strip()
        
        # Regex extraction
        id_match = re.search(r"id:\s*['\"]([^'\"]+)['\"]", line)
        if id_match:
            last_id = id_match.group(1)
            last_label = last_id
            last_path = None # Reset path
        
        label_match = re.search(r"label:\s*['\"]([^'\"]+)['\"]", line)
        if label_match: last_label = label_match.group(1)
            
        path_match = re.search(r"path:\s*['\"]([^'\"]+)['\"]", line)
        if path_match: last_path = path_match.group(1)
        
        # Check Children Start => Upsert PARENT
        if 'children: [' in line:
            if last_id:
                parent = stack[-1] if stack else None
                upsert_item(last_id, last_label, last_path, parent, id_module_map, stack, is_parent=True)
                count_groups += 1
                stack.append(last_id)
                last_id = None # Consumed
        
        # Check Object End => Upsert LEAF (if not consumed)
        if line.strip().endswith('},') or line.strip() == '}':
            if last_id:
                parent = stack[-1] if stack else None
                upsert_item(last_id, last_label, last_path, parent, id_module_map, stack, is_parent=False)
                count_leaves += 1
                last_id = None # Consumed

        # Check Children End => Pop Stack
        if line.startswith('],') or line == ']':
            if stack:
                stack.pop()

    print(f"Hierarchy Sync Complete.")
    print(f"  - Groups/Folders Created: {count_groups}")
    print(f"  - Leaf Items Created: {count_leaves}")
    print(f"  - Total: {count_groups + count_leaves}")

if __name__ == "__main__":
    process_menu_hierarchy()




