import sqlite3

def add_mode_specific_toolbar_columns():
    """Add mode-specific toolbar columns to erp_menu_items table"""
    
    conn = sqlite3.connect('backend/db.sqlite3')
    cursor = conn.cursor()
    
    print("Adding mode-specific toolbar columns to erp_menu_items table...")
    
    # Add the four new columns
    columns = [
        ("toolbar_list", "VARCHAR(100)"),
        ("toolbar_view", "VARCHAR(100)"),
        ("toolbar_edit", "VARCHAR(100)"),
        ("toolbar_create", "VARCHAR(100)")
    ]
    
    for col_name, col_type in columns:
        try:
            cursor.execute(f"ALTER TABLE erp_menu_items ADD COLUMN {col_name} {col_type}")
            print(f"[OK] Added column: {col_name}")
        except sqlite3.OperationalError as e:
            if "duplicate column name" in str(e):
                print(f"[WARN] Column already exists: {col_name}")
            else:
                print(f"[ERROR] Error adding column {col_name}: {e}")
                conn.close()
                return
    
    conn.commit()
    conn.close()
    print("\n[OK] Mode-specific toolbar columns added successfully!")

if __name__ == "__main__":
    add_mode_specific_toolbar_columns()
