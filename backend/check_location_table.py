import sqlite3

conn = sqlite3.connect('backend/db.sqlite3')
cursor = conn.cursor()

# Check for location tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%location%'")
tables = cursor.fetchall()

print("Location-related tables:")
for table in tables:
    print(f"  - {table[0]}")

if not tables:
    print("  No location tables found!")

conn.close()
