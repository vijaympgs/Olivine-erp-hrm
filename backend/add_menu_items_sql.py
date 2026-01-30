#!/usr/bin/env python
import os
import sqlite3
import sys

def add_missing_hrm_menu_items():
    """Add missing HRM menu items directly to database"""
    
    # Database path
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    
    if not os.path.exists(db_path):
        print(f"[ERROR] Database not found at: {db_path}")
        return
    
    print("ADDING MISSING HRM MENU ITEMS TO DATABASE")
    print("=" * 80)
    
    # Connect to database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Define the missing menu items
        missing_items = [
            {
                'menu_id': 'HRM_EMPLOYEE_SELF_SERVICE',
                'menu_name': 'Employee Self-Service',
                'view_type': 'MASTER',
                'applicable_toolbar_config': 'NESCKVDXRQF',
                'module_name': 'HRM',
                'is_active': 1,
                'route_path': '/hr/employees/self-service'
            },
            {
                'menu_id': 'HRM_DOCUMENT_MANAGEMENT',
                'menu_name': 'Document Management',
                'view_type': 'MASTER',
                'applicable_toolbar_config': 'NESCKVDXRQF',
                'module_name': 'HRM',
                'is_active': 1,
                'route_path': '/hr/employees/documents'
            },
            {
                'menu_id': 'HRM_EMPLOYEE_LIFECYCLE',
                'menu_name': 'Employee Lifecycle',
                'view_type': 'MASTER',
                'applicable_toolbar_config': 'NESCKVDXRQF',
                'module_name': 'HRM',
                'is_active': 1,
                'route_path': '/hr/employees/lifecycle'
            }
        ]
        
        # First, check what tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print("Available tables:")
        for table in tables:
            print(f"  {table[0]}")
        
        # Find the correct table name
        menu_table = None
        for table in tables:
            if 'menu' in table[0].lower() and 'item' in table[0].lower():
                menu_table = table[0]
                break
        
        if not menu_table:
            print("ERROR: No menu item table found!")
            conn.close()
            return
        
        print(f"\nUsing table: {menu_table}")
        
        # Check table structure
        cursor.execute(f"PRAGMA table_info({menu_table})")
        columns = cursor.fetchall()
        print("Table structure:")
        for col in columns:
            print(f"  {col[1]} - {col[2]}")
        
        # Check existing HRM items
        print("\nChecking existing HRM menu items...")
        cursor.execute(f"SELECT menu_id, menu_name FROM {menu_table} WHERE menu_id LIKE 'HRM%' ORDER BY menu_id")
        existing_items = cursor.fetchall()
        print(f"Found {len(existing_items)} existing HRM menu items:")
        for item in existing_items:
            print(f"  {item[0]} - {item[1]}")
        
        print("\nAdding missing menu items...")
        
        added_count = 0
        for item_data in missing_items:
            menu_id = item_data['menu_id']
            
            # Check if item already exists
            cursor.execute(f"SELECT menu_id FROM {menu_table} WHERE menu_id = ?", (menu_id,))
            if cursor.fetchone():
                print(f"[WARNING] {menu_id} already exists - skipping")
                continue
            
            # Insert the menu item
            try:
                cursor.execute(f"""
                    INSERT INTO {menu_table} 
                    (menu_id, menu_name, view_type, applicable_toolbar_config, module_name, is_active, route_path, toolbar_config, is_license_controlled, is_system_menu, menu_order, display_order, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
                """, (
                    item_data['menu_id'],
                    item_data['menu_name'],
                    item_data['view_type'],
                    item_data['applicable_toolbar_config'],
                    item_data['module_name'],
                    item_data['is_active'],
                    item_data['route_path'],
                    item_data['applicable_toolbar_config'],  # Also use for toolbar_config
                    0,  # is_license_controlled
                    0,  # is_system_menu
                    1,  # menu_order
                    1   # display_order
                ))
                print(f"[SUCCESS] Created {menu_id} - {item_data['menu_name']}")
                added_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to create {menu_id}: {str(e)}")
        
        # Commit changes
        conn.commit()
        print(f"\nSummary: Added {added_count} new menu items")
        
        # Verify all HRM items
        print("\nAll HRM menu items after update:")
        cursor.execute(f"SELECT menu_id, menu_name, view_type, is_active FROM {menu_table} WHERE menu_id LIKE 'HRM%' ORDER BY menu_id")
        all_items = cursor.fetchall()
        for item in all_items:
            status = "[ACTIVE]" if item[3] else "[INACTIVE]"
            print(f"  {status} {item[0]} - {item[1]} ({item[2]})")
        
        conn.close()
        
    except Exception as e:
        print(f"[ERROR] Database error: {str(e)}")

if __name__ == '__main__':
    add_missing_hrm_menu_items()
