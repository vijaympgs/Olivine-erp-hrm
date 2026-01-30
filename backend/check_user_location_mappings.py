import sqlite3

conn = sqlite3.connect('backend/db.sqlite3')
cursor = conn.cursor()

# Check user_location_mappings structure
cursor.execute("PRAGMA table_info(user_location_mappings)")
columns = cursor.fetchall()

print("user_location_mappings table structure:")
for col in columns:
    print(f"  {col[1]} ({col[2]})")

# Check if there are any records
cursor.execute("SELECT COUNT(*) FROM user_location_mappings")
count = cursor.fetchone()[0]
print(f"\nTotal records: {count}")

# Sample data
if count > 0:
    cursor.execute("SELECT * FROM user_location_mappings LIMIT 5")
    rows = cursor.fetchall()
    print("\nSample data:")
    for row in rows:
        print(f"  {row}")

conn.close()
