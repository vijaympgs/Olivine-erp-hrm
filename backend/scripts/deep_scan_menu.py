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

MENU_CONFIG_PATH = os.path.join(PROJECT_ROOT, 'frontend', 'src', 'app', 'menuConfig.ts')

# Standard configuration strings
CONFIGS = {
    'MASTER': 'NESCKVDXRQFIO',
    'TRANSACTION': 'NESCKZTJAVPMRDX1234QF',
    'REPORT': 'VRXPYQFG',
    'DASHBOARD': 'VRXQFG',
    'LIST': 'NRQFX',
    'CONFIGURATION': 'ESCKXR',
}

def get_view_type(name, path):
    name = name.lower()
    path = path.lower()
    
    if any(x in name for x in ['report', 'analysis', 'valuation', 'register', 'aging', 'trends']):
        return 'REPORT'
    if any(x in name for x in ['dashboard', 'overview', 'monitor', 'summary', 'health score']):
        return 'DASHBOARD'
    if any(x in name for x in ['setup', 'config', 'settings', 'rules', 'parameters', 'definitions', 'methodology', 'preferences']):
        return 'CONFIGURATION'
    if any(x in name for x in ['master', 'catalog', 'hierarchy', 'directory', 'profiles', 'uom', 'template', 'employee', 'customer', 'vendor', 'supplier']):
        return 'MASTER'
    
    return 'TRANSACTION'

def get_module(path):
    path = path.lower()
    if path.startswith('/retail') or path.startswith('/inventory') or path.startswith('/procurement') or path.startswith('/sales') or path.startswith('/pos'):
        return 'RETAIL'
    if path.startswith('/finance'):
        return 'FMS'
    if path.startswith('/crm'):
        return 'CRM'
    if path.startswith('/hr'):
        return 'HRM'
    if path.startswith('/admin'):
        return 'ADMIN'
    if path.startswith('/setup'):
        return 'SETUP'
    return 'SYSTEM'

def deep_scan_and_regenerate():
    print("=" * 100)
    print("DEEP SCAN REGENERATION OF TOOLBAR REGISTRY")
    print("=" * 100)

    with open(MENU_CONFIG_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all objects with id, label, and path
    # Look for patterns like: { id: '...', label: '...', ..., path: '...' }
    # This regex is a bit loose but should catch most leaf nodes
    items = []
    # Match the block { id: ..., label: ..., path: ... }
    # We use a non-greedy match for the block content
    pattern = r'\{\s*id:\s*[\'"]([^\'"]+)[\'"]\s*,\s*label:\s*[\'"]([^\'"]+)[\'"]\s*,.*?path:\s*[\'"]([^\'"]+)[\'"]\s*.*?\}'
    matches = re.findall(pattern, content, re.DOTALL)
    
    print(f"Found {len(matches)} leaf items in menuConfig.ts")

    updated = 0
    created = 0
    
    for mid, label, path in matches:
        # Determine module
        module = get_module(path)
        
        # Determine type
        vtype = get_view_type(label, path)
        
        # Determine Toolbar ID
        toolbar_id = mid.upper().replace('-', '_')
        
        config = CONFIGS.get(vtype, CONFIGS['TRANSACTION'])
        
        obj, ok = ERPMenuItem.objects.update_or_create(
            menu_id=toolbar_id,
            defaults={
                'menu_name': label,
                'view_type': vtype,
                'module_name': module,
                'applicable_toolbar_config': config,
                'route_path': path,
                'is_active': True
            }
        )
        if ok: created += 1
        else: updated += 1
        
    print(f"\nCompleted Deep Scan.")
    print(f"Total Created: {created}")
    print(f"Total Updated: {updated}")
    print(f"Total Model Items: {ERPMenuItem.objects.count()}")
    print("=" * 100)

if __name__ == "__main__":
    deep_scan_and_regenerate()




