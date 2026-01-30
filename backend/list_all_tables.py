import sqlite3

conn = sqlite3.connect('backend/db.sqlite3')
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
tables = cursor.fetchall()

print(f"Total tables: {len(tables)}\n")
print("All tables:")
for table in tables:
    print(f"  - {table[0]}")

conn.close()
