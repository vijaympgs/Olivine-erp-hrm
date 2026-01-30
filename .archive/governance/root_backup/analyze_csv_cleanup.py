
import csv
import sys

def analyze_csv(file_path):
    print(f"Analyzing {file_path}...")
    
    entries = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                entries.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"Total entries: {len(entries)}")
    
    # Check for "List" in name or ID
    list_items = []
    for e in entries:
        if 'List' in e['menu_name'] or '_LIST' in e['menu_id']:
            list_items.append(f"{e['menu_id']} ({e['menu_name']})")
            
    if list_items:
        print("\n⚠️ Items containing 'List':")
        for i in list_items:
            print(f"  - {i}")
    else:
        print("\n✅ No items containing 'List' found.")

    # Check for potential duplicates (e.g. UOM_SETUP and UOM_LIST)
    # We can group by some base name heuristic
    print("\n🔍 Checking for potential duplicates (base name match):")
    
    # Heuristic: split by _ and take first word? No, "ITEM_MASTER" vs "ITEM_GROUP".
    # Let's just look at specific known problem areas from yesterday.
    
    known_keys = ['UOM', 'ITEM', 'CUSTOMER', 'SUPPLIER', 'PO', 'PURCHASE']
    for key in known_keys:
        matches = [e['menu_id'] for e in entries if key in e['menu_id']]
        if len(matches) > 1:
            print(f"  {key}: {matches}")

analyze_csv('ERP_Menu_Items_20260110_155048.csv')



