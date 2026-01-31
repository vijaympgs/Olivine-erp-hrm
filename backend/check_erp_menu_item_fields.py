#!/usr/bin/env python
"""Check ERPMenuItem model fields"""
import sqlite3

def check_fields():
    """Check ERPMenuItem table structure"""
    
    print("Checking ERPMenuItem Table Structure")
    print("=" * 60)
    print()
    
    # Connect to database
    db_path = 'backend/db.sqlite3'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check table structure
        cursor.execute("PRAGMA table_info(erp_menu_items)")
        columns = cursor.fetchall()
        
        print("Table Columns:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        print()
        
        # Get sample data
        cursor.execute("SELECT * FROM erp_menu_items LIMIT 1")
        sample = cursor.fetchone()
        
        if sample:
            print("Sample Data (first row):")
            for i, col in enumerate(columns):
                print(f"  {col[1]}: {sample[i]}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    check_fields()
