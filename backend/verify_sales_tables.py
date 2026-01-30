import sqlite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'sales_%' ORDER BY name")
tables = [row[0] for row in cursor.fetchall()]
for table in tables:
    print(table)
print(f'\nTotal: {len(tables)} sales tables created')




