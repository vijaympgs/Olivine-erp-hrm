
import csv
import sys

def analyze_view_types(file_path):
    print(f"Analyzing {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # 1. Check for legacy 'LIST' types
    legacy_types = [r for r in rows if 'LIST' in r.get('view_type', '').upper()]
    if legacy_types:
        print(f"\n❌ FOUND {len(legacy_types)} LEGACY 'LIST' TYPES:")
        for r in legacy_types:
            print(f"  - {r['menu_id']}: {r['view_type']}")
    else:
        print("\n✅ No legacy 'LIST' view types found (Good).")

    # 2. Check for mismatches based on heuristic keywords
    print("\n🔍 Checking for potential misclassifications:")
    mismatches = []
    
    for r in rows:
        mid = r['menu_id'].upper()
        name = r['menu_name'].upper()
        vtype = r.get('view_type', '').upper()
        
        expected = None
        
        # Heuristics
        if 'DASHBOARD' in mid or 'DASHBOARD' in name:
            expected = 'DASHBOARD'
        elif 'REPORT' in mid or 'REPORT' in name or 'ANALYSIS' in mid:
            expected = 'REPORT'
        elif 'reconciliation' in name.lower() or 'approval' in name.lower():
            # Often transactions or specialized
            pass 
        
        # If we have a strong expectation and it mismatches
        if expected and vtype != expected:
            # Special exceptions
            if expected == 'REPORT' and vtype == 'MASTER': # e.g. "Inventory Reports" menu container might be marked Master?
                mismatches.append(f"{r['menu_id']} ({name}): Type='{vtype}', Expected='{expected}'")
            elif expected == 'DASHBOARD' and vtype != 'DASHBOARD':
                 mismatches.append(f"{r['menu_id']} ({name}): Type='{vtype}', Expected='{expected}'")

    if mismatches:
        for m in mismatches:
            print(f"  ? {m}")
    else:
        print("  - Heuristics check passed (Dashboards/Reports seem aligned).")

    # 3. List all distinct view types found
    distinct_types = set(r.get('view_type') for r in rows)
    print(f"\n📊 Distinct View Types in File: {sorted(list(distinct_types))}")

if __name__ == "__main__":
    analyze_view_types(r"c:\00mindra\olivine-erp-platform\ERP_Menu_Items_20260110_161145.csv")



