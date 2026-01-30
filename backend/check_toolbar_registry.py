import sqlite3

conn = sqlite3.connect('backend/db.sqlite3')
cursor = conn.cursor()

# Check toolbar controls for EMPLOYEE_RECORDS
cursor.execute("SELECT menu_id, toolbar_string FROM erp_toolbar_controls WHERE menu_id='EMPLOYEE_RECORDS'")
row = cursor.fetchone()

if row:
    print(f'Menu ID: {row[0]}')
    print(f'Toolbar String: {row[1]}')
else:
    print('No entry found in erp_toolbar_controls for EMPLOYEE_RECORDS')
    
    # Check if there are any toolbar controls entries
    cursor.execute("SELECT COUNT(*) FROM erp_toolbar_controls")
    count = cursor.fetchone()[0]
    print(f'\nTotal erp_toolbar_controls entries: {count}')
    
    # Show a few sample entries
    cursor.execute("SELECT menu_id, toolbar_string FROM erp_toolbar_controls LIMIT 5")
    print('\nSample erp_toolbar_controls entries:')
    for r in cursor.fetchall():
        print(f'  {r[0]}: {r[1]}')

conn.close()
