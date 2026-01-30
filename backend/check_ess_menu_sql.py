import os
import sys
import sqlite3

def check_ess_menu_item():
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # First, check what tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print("=== Available Tables ===")
        for table in tables:
            print(f"- {table[0]}")
        print()
        
        # Look for menu item tables
        menu_table = None
        for table in tables:
            if 'menu' in table[0].lower() and 'item' in table[0].lower():
                menu_table = table[0]
                break
        
        if not menu_table:
            print("❌ No menu item table found!")
            return
            
        print(f"Using table: {menu_table}")
        print()
        
        # Check if ESS menu item exists
        cursor.execute("""
            SELECT menu_id, menu_name, route_path, toolbar_config, 
                   applicable_toolbar_config, component_name, view_type, is_active
            FROM erp_menu_items 
            WHERE menu_id = 'HRM_EMPLOYEE_SELF_SERVICE'
        """)
        
        ess_menu = cursor.fetchone()
        
        if ess_menu:
            print("=== Current ESS Menu Item Configuration ===")
            print(f"Menu ID: {ess_menu[0]}")
            print(f"Menu Name: {ess_menu[1]}")
            print(f"Route Path: {ess_menu[2]}")
            print(f"Toolbar Config: {ess_menu[3]}")
            print(f"Applicable Toolbar Config: {ess_menu[4]}")
            print(f"Component Name: {ess_menu[5]}")
            print(f"View Type: {ess_menu[6]}")
            print(f"Is Active: {ess_menu[7]}")
            print()
            
            # Check if toolbar config is properly set
            if not ess_menu[3]:
                print("❌ Toolbar Config is EMPTY - needs to be updated")
                
                # Update the toolbar config
                cursor.execute("""
                    UPDATE erp_menu_items 
                    SET toolbar_config = 'NESCKVDXRQF',
                        applicable_toolbar_config = 'NESCKVDXRQF'
                    WHERE menu_id = 'HRM_EMPLOYEE_SELF_SERVICE'
                """)
                conn.commit()
                print("✅ Toolbar Config updated successfully!")
            else:
                print(f"✅ Toolbar Config: {ess_menu[3]}")
                
        else:
            print("❌ ESS menu item not found! Creating new entry...")
            
            # Find HRM parent menu
            cursor.execute("""
                SELECT id FROM erp_menu_items 
                WHERE menu_id = 'HRM'
            """)
            hrm_parent = cursor.fetchone()
            
            if not hrm_parent:
                print("❌ HRM parent menu not found!")
                return
            
            # Create ESS menu item
            cursor.execute("""
                INSERT INTO erp_menu_items 
                (menu_id, menu_name, route_path, toolbar_config, applicable_toolbar_config,
                 component_name, view_type, parent_id, sort_order, is_active, icon, created_at, updated_at)
                VALUES 
                ('HRM_EMPLOYEE_SELF_SERVICE', 'Employee Self Service', '/hr/employees/self-service',
                 'NESCKVDXRQF', 'NESCKVDXRQF', 'EmployeeSelfService', 'ESS',
                 ?, 15, 1, 'User', datetime('now'), datetime('now'))
            """, (hrm_parent[0],))
            
            conn.commit()
            print("✅ ESS menu item created successfully!")
            print("Menu ID: HRM_EMPLOYEE_SELF_SERVICE")
            print("Menu Name: Employee Self Service")
            print("Route Path: /hr/employees/self-service")
            print("Toolbar Config: NESCKVDXRQF")
        
        # Show available toolbar controls
        print("\n=== Available Toolbar Controls ===")
        cursor.execute("""
            SELECT control_id, control_name, control_type 
            FROM erp_toolbar_controls
            WHERE control_id IN ('N', 'E', 'S', 'C', 'K', 'V', 'D', 'X', 'R', 'Q', 'F')
            ORDER BY control_id
        """)
        
        controls = cursor.fetchall()
        for control in controls:
            print(f"{control[0]}: {control[1]} ({control[2]})")
        
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_ess_menu_item()
