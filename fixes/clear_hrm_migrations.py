import sqlite3

db_path = 'backend/db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Delete hrm migrations
cursor.execute("DELETE FROM django_migrations WHERE app = 'hrm'")

conn.commit()
conn.close()
print("Successfully cleared hrm migrations from django_migrations")
