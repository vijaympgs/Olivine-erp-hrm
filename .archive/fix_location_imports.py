"""
Automated Import Fixer - Legacy Location to Retail Domain
==========================================================

This script fixes all imports of Location from legacy paths to the new
Retail.backend.domain location.

Changes:
1. from core.org_structure.backend.company.models import ... Location ...
   → Split into two imports (Common.domain for others, Retail.backend.domain for Location)

2. from core.org_structure.backend.location.models.location import Location
   → from Retail.backend.domain.models import Location
"""

import os
import re

def fix_import_line(line):
    """Fix a single import line that includes Location"""
    # Pattern: from core.org_structure.backend.company.models import X, Y, Location, Z
    
    # Extract all imported items
    match = re.search(r'from core\.org_structure\.backend\.company\.models import (.+)', line)
    if not match:
        return line
    
    imports_str = match.group(1).strip()
    imports = [item.strip() for item in imports_str.split(',')]
    
    # Separate Location from others
    location_imports = [imp for imp in imports if 'Location' in imp]
    other_imports = [imp for imp in imports if 'Location' not in imp]
    
    result_lines = []
    
    # Add Common.domain import for ItemMaster, ItemVariant, etc.
    if other_imports:
        common_domain_items = []
        company_items = []
        
        for imp in other_imports:
            if any(x in imp for x in ['ItemMaster', 'ItemVariant', 'UnitOfMeasure', 'Supplier', 'Customer']):
                common_domain_items.append(imp)
            else:
                company_items.append(imp)
        
        if common_domain_items:
            result_lines.append(f"from common.domain.models import {', '.join(common_domain_items)}")
        if company_items:
            result_lines.append(f"from core.org_structure.backend.company.models import {', '.join(company_items)}")
    
    # Add Retail.backend.domain import for Location
    if location_imports:
        result_lines.append("from Retail.backend.domain.models import Location")
    
    return '\n'.join(result_lines)

def fix_file(filepath):
    """Fix all Location imports in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern 1: from core.org_structure.backend.location.models.location import Location
        content = re.sub(
            r'from core\.org_structure\.backend\.location\.models\.location import Location',
            'from Retail.backend.domain.models import Location',
            content
        )
        
        # Pattern 2: from core.org_structure.backend.company.models import ... (with Location)
        lines = content.split('\n')
        fixed_lines = []
        
        for line in lines:
            if 'from core.org_structure.backend.company.models import' in line and 'Location' in line:
                fixed = fix_import_line(line)
                fixed_lines.append(fixed)
            else:
                fixed_lines.append(line)
        
        content = '\n'.join(fixed_lines)
        
        # Only write if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

# Files to fix (from our scan)
files_to_fix = [
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\inventory\intercompany_models.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\pos\day_open\views.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\procurement\models.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\procurement\views.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\sales\services.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\sales\tests\test_6_1_sales_quotation.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\sales\tests\test_6_2_sales_order.py',
    # Test files
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\inventory\tests\test_5_3_stock_movements.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\inventory\tests\test_5_4_stock_adjustments.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\inventory\tests\test_5_5_physical_inventory.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\inventory\tests\test_5_6_inventory_valuation.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\inventory\tests\test_5_7_replenishment.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\inventory\tests\test_5_8_item_tracking.py',
    r'c:\00mindra\olivine-erp-platform\apps\retail\backend\inventory\tests\test_5_9_inventory_reports.py',
]

# Fix all files
print("Fixing Location imports in 14 backend files...")
fixed_count = 0
for filepath in files_to_fix:
    if os.path.exists(filepath):
        if fix_file(filepath):
            print(f"✅ Fixed: {os.path.basename(filepath)}")
            fixed_count += 1
        else:
            print(f"⏭️  Skipped (no changes): {os.path.basename(filepath)}")
    else:
        print(f"❌ Not found: {filepath}")

print(f"\n✅ Fixed {fixed_count} files")
print("🔄 Now run: python manage.py check")




