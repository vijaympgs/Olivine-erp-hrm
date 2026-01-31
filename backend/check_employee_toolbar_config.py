#!/usr/bin/env python
"""Check Employee Records toolbar configuration in database"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
django.setup()

from django.db import connection

def check_employee_toolbar():
    """Check Employee Records toolbar configuration"""
    
    print("🔍 Checking Employee Records Toolbar Configuration")
    print("=" * 60)
    print()
    
    with connection.cursor() as cursor:
        # Check if erp_menu_items table exists
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name LIKE '%menu%'
        """)
        tables = cursor.fetchall()
        
        print("📋 Available menu-related tables:")
        for table in tables:
            print(f"  - {table[0]}")
        print()
        
        # Check for erp_menu_items table
        if ('erp_menu_items',) in tables:
            print("✅ Found erp_menu_items table")
            print()
            
            # Check table structure
            cursor.execute("PRAGMA table_info(erp_menu_items)")
            columns = cursor.fetchall()
            
            print("📊 Table Structure:")
            for col in columns:
                print(f"  - {col[1]} ({col[2]})")
            print()
            
            # Check for Employee Records entry
            cursor.execute("""
                SELECT menu_id, menu_name, module_name, view_type, 
                       applicable_toolbar_config, toolbar_list, toolbar_view, 
                       toolbar_edit, toolbar_create, route_path
                FROM erp_menu_items
                WHERE menu_id LIKE '%EMPLOYEE%' OR menu_name LIKE '%EMPLOYEE%'
            """)
            employee_items = cursor.fetchall()
            
            if employee_items:
                print("📋 Employee Records Entries:")
                for item in employee_items:
                    print(f"\n  Menu ID: {item[0]}")
                    print(f"  Menu Name: {item[1]}")
                    print(f"  Module: {item[2]}")
                    print(f"  View Type: {item[3]}")
                    print(f"  Applicable Toolbar Config: {item[4]}")
                    print(f"  Toolbar List: {item[5]}")
                    print(f"  Toolbar View: {item[6]}")
                    print(f"  Toolbar Edit: {item[7]}")
                    print(f"  Toolbar Create: {item[8]}")
                    print(f"  Route Path: {item[9]}")
                    print()
            else:
                print("❌ No Employee Records entries found")
                print()
                
                # Check all menu items
                cursor.execute("""
                    SELECT menu_id, menu_name, module_name 
                    FROM erp_menu_items
                    LIMIT 10
                """)
                all_items = cursor.fetchall()
                
                print("📋 Sample Menu Items:")
                for item in all_items:
                    print(f"  - {item[0]}: {item[1]} ({item[2]})")
                print()
        else:
            print("❌ erp_menu_items table not found")
            print()
            
            # Check for other possible table names
            cursor.execute("""
                SELECT name FROM sqlite_master 
                WHERE type='table' AND name LIKE '%item%'
            """)
            item_tables = cursor.fetchall()
            
            print("📋 Available item-related tables:")
            for table in item_tables:
                print(f"  - {table[0]}")
            print()

if __name__ == "__main__":
    check_employee_toolbar()
