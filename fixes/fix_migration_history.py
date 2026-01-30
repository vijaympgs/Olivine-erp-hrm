import sqlite3
import datetime

db_path = 'backend/db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insert the missing dependency record
# (app, name, applied)
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
cursor.execute("INSERT INTO django_migrations (app, name, applied) VALUES (?, ?, ?)", 
               ('retail_domain', '0001_initial', now))

conn.commit()
conn.close()
print("Successfully inserted retail_domain.0001_initial into django_migrations")
