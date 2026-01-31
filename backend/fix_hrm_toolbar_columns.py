#!/usr/bin/env python
"""Fix HRM toolbar columns - populate toolbar_list, toolbar_view, toolbar_edit, toolbar_create"""
import sqlite3

def fix_hrm_toolbar_columns():
    """Fix HRM toolbar columns based on view_type"""
    
    print("Fixing HRM Toolbar Columns")
    print("=" * 60)
    print()
    
    # Connect to database
    db_path = 'backend/db.sqlite3'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Define toolbar configurations by view_type
        toolbar_configs = {
            'MASTER': {
                'toolbar_list': 'NRQFVIOX',  # New, Refresh, Query, Filter, View, Import, Export, Exit
                'toolbar_view': 'X',         # Exit only
                'toolbar_edit': 'SCX',        # Save, Cancel, Exit
                'toolbar_create': 'SCX'      # Save, Cancel, Exit
            },
            'LIST': {
                'toolbar_list': 'NRQFVIOX',  # New, Refresh, Query, Filter, View, Import, Export, Exit
                'toolbar_view': 'X',         # Exit only
                'toolbar_edit': 'SCX',        # Save, Cancel, Exit
                'toolbar_create': 'SCX'      # Save, Cancel, Exit
            },
            'TRANSACTION': {
                'toolbar_list': 'NESCKZTJAVPMRDX1234QF',  # Full transaction toolbar
                'toolbar_view': 'X',
                'toolbar_edit': 'SCX',
                'toolbar_create': 'SCX'
            },
            'REPORT': {
                'toolbar_list': 'RPQFX',  # Refresh, Print, Query, Filter, Exit
                'toolbar_view': 'X',
                'toolbar_edit': 'SCX',
                'toolbar_create': 'SCX'
            }
        }
        
        # Get all HRM menu items
        cursor.execute("""
            SELECT id, menu_id, menu_name, view_type, 
                   toolbar_list, toolbar_view, toolbar_edit, toolbar_create
            FROM erp_menu_items
            WHERE module_name = 'HRM'
        """)
        hrm_items = cursor.fetchall()
        
        print(f"Found {len(hrm_items)} HRM menu items")
        print()
        
        updated_count = 0
        for item in hrm_items:
            item_id = item[0]
            menu_id = item[1]
            menu_name = item[2]
            view_type = item[3]
            current_list = item[4]
            current_view = item[5]
            current_edit = item[6]
            current_create = item[7]
            
            # Get toolbar config for this view_type
            config = toolbar_configs.get(view_type, toolbar_configs['MASTER'])
            
            # Check if update is needed
            needs_update = (
                current_list != config['toolbar_list'] or
                current_view != config['toolbar_view'] or
                current_edit != config['toolbar_edit'] or
                current_create != config['toolbar_create']
            )
            
            if needs_update:
                print(f"Updating: {menu_id} ({menu_name})")
                print(f"  View Type: {view_type}")
                print(f"  toolbar_list: {current_list} -> {config['toolbar_list']}")
                print(f"  toolbar_view: {current_view} -> {config['toolbar_view']}")
                print(f"  toolbar_edit: {current_edit} -> {config['toolbar_edit']}")
                print(f"  toolbar_create: {current_create} -> {config['toolbar_create']}")
                print()
                
                # Update the record
                cursor.execute("""
                    UPDATE erp_menu_items
                    SET toolbar_list = ?,
                        toolbar_view = ?,
                        toolbar_edit = ?,
                        toolbar_create = ?
                    WHERE id = ?
                """, (
                    config['toolbar_list'],
                    config['toolbar_view'],
                    config['toolbar_edit'],
                    config['toolbar_create'],
                    item_id
                ))
                
                updated_count += 1
            else:
                print(f"Skipping: {menu_id} ({menu_name}) - Already correct")
                print()
        
        conn.commit()
        
        print("=" * 60)
        print(f"Updated {updated_count} HRM menu items")
        print()
        
        # Verify updates
        print("Verification:")
        cursor.execute("""
            SELECT menu_id, menu_name, view_type, 
                   toolbar_list, toolbar_view, toolbar_edit, toolbar_create
            FROM erp_menu_items
            WHERE module_name = 'HRM'
            ORDER BY menu_name
        """)
        items = cursor.fetchall()
        
        for item in items:
            print(f"\n{item[0]} ({item[1]})")
            print(f"  View Type: {item[2]}")
            print(f"  toolbar_list: {item[3]}")
            print(f"  toolbar_view: {item[4]}")
            print(f"  toolbar_edit: {item[5]}")
            print(f"  toolbar_create: {item[6]}")
        
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    fix_hrm_toolbar_columns()
