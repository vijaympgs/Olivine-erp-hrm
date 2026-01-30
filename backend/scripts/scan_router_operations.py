import os
import re

ROUTER_PATH = r'c:\00mindra\olivine-erp-platform\frontend\src\app\router.tsx'

def scan_router():
    print("=" * 100)
    print("SCANNING ROUTER FOR OPERATIONAL PAGES")
    print("=" * 100)
    
    with open(ROUTER_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract path and element from: { path: "...", element: <...> }
    # Using a simpler regex for extraction
    pattern = r'path:\s*[\'"]([^\'"]+)[\'"]\s*,\s*element:\s*<([^/\s>]+)'
    matches = re.findall(pattern, content)
    
    print(f"Found {len(matches)} operational routes.")
    
    # Filter for interesting ones: procurement, sales, inventory, finance, hr, pos, etc.
    ops = []
    for path, element in matches:
        if any(x in path for x in ['procurement', 'sales', 'inventory', 'finance', 'hr', 'pos', 'admin', 'setup', 'partners']):
            if ':' in path or '/new' in path: 
                vtype = 'TRANSACTION'
            elif 'report' in path.lower() or 'analysis' in path.lower():
                vtype = 'REPORT'
            elif 'dashboard' in path.lower():
                vtype = 'DASHBOARD'
            elif 'config' in path.lower() or 'setup' in path.lower() or 'settings' in path.lower():
                vtype = 'CONFIGURATION'
            else:
                vtype = 'LIST (SKIP)'
            
            ops.append((path, element, vtype))
            print(f"{path:40} | {element:30} | {vtype}")
            
    return ops

if __name__ == "__main__":
    scan_router()




