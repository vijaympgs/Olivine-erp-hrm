import os
import re

TRACKER_PATH = r'c:\00mindra\olivine-erp-platform\.steering\04_EXECUTION_PLANS_FIX_REFERENCES\RETAIL_IMPLEMENTATION_TRACKER.md'

def get_suggested_type(feature_name):
    name = feature_name.lower()
    if any(x in name for x in ['report', 'analysis', 'valuation', 'dead stock', 'aging']):
        return 'REPORT'
    if any(x in name for x in ['dashboard', 'overview', 'monitor', 'summary', 'trends']):
        return 'DASHBOARD'
    if any(x in name for x in ['setup', 'configuration', 'parameter', 'settings']):
        return 'CONFIGURATION'
    if any(x in name for x in ['master', 'catalog', 'hierarchy', 'uom', 'directory']):
        return 'MASTER'
    if any(x in name for x in ['entry', 'checkout', 'register']):
        return 'TRANSACTION'
    if any(x in name for x in ['history', 'list', 'management', 'bills', 'payments', 'compliance', 'returns', 'receipts', 'orders', 'invoices', 'quotes', 'requisitions', 'rfqs', 'asns']):
        return 'LIST'
    
    return 'LIST'

def update_tracker():
    with open(TRACKER_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_table = False
    header_found = False
    
    for line in lines:
        if line.strip().startswith('|') and '| Feature |' in line:
            in_table = True
            header_found = True
            # Add Type column
            parts = [p.strip() for p in line.split('|')]
            # parts[0] is empty, parts[1] is Feature, parts[2] is Path ...
            parts.insert(2, ' Type ')
            new_lines.append('|' + '|'.join(parts[1:-1]) + '|\n')
            continue
        
        if in_table and line.strip().startswith('|') and '---' in line:
            parts = [p.strip() for p in line.split('|')]
            parts.insert(2, '------')
            new_lines.append('|' + '|'.join(parts[1:-1]) + '|\n')
            continue

        if in_table and line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|')]
            feature_name = parts[1].strip()
            # If it's a data row (not header/separator)
            if feature_name and feature_name not in ['Feature', 'Category', 'Module']:
                suggested_type = get_suggested_type(feature_name)
                parts.insert(2, f' {suggested_type:10} ')
                new_lines.append('|' + '|'.join(parts[1:-1]) + '|\n')
            else:
                new_lines.append(line)
            continue
        
        if not line.strip().startswith('|'):
            in_table = False
            header_found = False
        
        new_lines.append(line)

    with open(TRACKER_PATH, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    update_tracker()
    print("Tracker updated with Type column.")




