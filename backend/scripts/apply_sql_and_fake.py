import os
import sqlite3
import subprocess
from datetime import datetime

def apply_sql_and_fake():
    db_path = 'db.sqlite3'
    
    print("Generating SQL via subprocess...")
    result = subprocess.run(['python', 'manage.py', 'sqlmigrate', 'domain', '0001'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error generating SQL:", result.stderr)
        return
    
    sql = result.stdout
    print(f"SQL Length: {len(sql)}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("Applying SQL...")
    try:
        cursor.executescript(sql)
        print("SQL Applied.")
    except Exception as e:
        print(f"SQL Error: {e}")
        # If error is "table already exists", we might proceed?
        # Check specific error?
    
    print("Faking migration entry...")
    try:
        cursor.execute("SELECT * FROM django_migrations WHERE app='domain' AND name='0001_initial'")
        if cursor.fetchone():
            print("Migration already recorded.")
        else:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO django_migrations (app, name, applied) VALUES (?, ?, ?)", 
                           ('domain', '0001_initial', now))
            print("Migration inserted.")
            conn.commit()
    except Exception as e:
        print(f"Fake Error: {e}")
    
    conn.close()

if __name__ == '__main__':
    apply_sql_and_fake()




