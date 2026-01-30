
import csv
import re

def parse_markdown_plan(file_path):
    plan_items = {}
    current_item = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Detect start of a new item section (e.g., #### **2A.1 Item Master**)
            if line.startswith('#### '):
                # Save previous item if valid
                if 'menu_id' in current_item:
                    plan_items[current_item['menu_id']] = current_item
                current_item = {}
            
            # Parse menu_id
            match = re.search(r'- \*\*menu_id\*\*: `([^`]+)`', line)
            if match:
                current_item['menu_id'] = match.group(1)
                
            # Parse config
            match = re.search(r'- \*\*Config\*\*: `([^`]+)`', line)
            if match:
                current_item['config'] = match.group(1)
                
            # Parse view_type
            match = re.search(r'- \*\*view_type\*\*: `([^`]+)`', line)
            if match:
                current_item['view_type'] = match.group(1)

        # Save last item
        if 'menu_id' in current_item:
            plan_items[current_item['menu_id']] = current_item
            
    # Also parse simple lookups table if present (P2 section often uses tables)
    # Looking for table rows like: | **Tax Codes** | `TAX_CODES` | ...
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line and '`' in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) > 2:
                    # Try to extract menu_id from code block
                    menu_id_match = re.search(r'`([^`]+)`', line)
                    if menu_id_match:
                        menu_id = menu_id_match.group(1)
                        if menu_id not in plan_items:
                             # Assume simple master default if not explicitly detailed
                             plan_items[menu_id] = {
                                 'menu_id': menu_id,
                                 # We might not get config from table easily, but we know menu_id exists
                             }

    return plan_items

def verify_csv_against_plan(csv_path, plan_path):
    plan_items = parse_markdown_plan(plan_path)
    csv_items = {}
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['menu_id']:
                    csv_items[row['menu_id']] = row
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"Loaded {len(plan_items)} items from Plan")
    print(f"Loaded {len(csv_items)} items from CSV")
    print("-" * 50)

    # Check Plan items against CSV
    missing_in_csv = []
    mismatched_config = []
    
    for menu_id, plan_data in plan_items.items():
        if menu_id not in csv_items:
            missing_in_csv.append(menu_id)
        else:
            csv_data = csv_items[menu_id]
            # Check Config
            if 'config' in plan_data:
                # CSV config column name might vary, check standard name from export script
                csv_config = csv_data.get('applicable_toolbar_config', '')
                if csv_config != plan_data['config']:
                    mismatched_config.append({
                        'menu_id': menu_id,
                        'plan': plan_data['config'],
                        'csv': csv_config
                    })
    
    if missing_in_csv:
        print(f"\n❌ MISSING IN CSV (In Plan but not in DB): {len(missing_in_csv)}")
        for mid in missing_in_csv:
            print(f"  - {mid}")
    else:
        print("\n✅ All Plan items found in CSV")

    if mismatched_config:
        print(f"\n❌ CONFIG MISMATCHES: {len(mismatched_config)}")
        for m in mismatched_config:
            print(f"  - {m['menu_id']}: Plan='{m['plan']}' vs DB='{m['csv']}'")
    else:
        print("\n✅ All Configs match")

if __name__ == "__main__":
    verify_csv_against_plan('c:\\00mindra\\olivine-erp-platform\\ERP_Menu_Items_20260110_155048.csv', 'c:\\00mindra\\olivine-erp-platform\\.steering\\20TOOLBAR_ROLLOUT\\TOOLBAR_ROLLOUT_PLAN.md')



