import sqlite3

conn = sqlite3.connect('backend/db.sqlite3')
cursor = conn.cursor()

# Find company-related tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%company%' ORDER BY name")
tables = cursor.fetchall()

print("Company-related tables:")
for table in tables:
    print(f"  - {table[0]}")

conn.close()
