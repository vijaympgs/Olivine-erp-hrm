import sqlite3

db_path = 'backend/db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [t[0] for t in cursor.fetchall()]

# More exhaustive list of HRM related tables
to_drop = [
    'employee_record', 'employee_address', 'department',
    'employee_profile', 'employee_skill', 'employee_document', 'skill_category',
    'organizational_unit', 'position', 'employee_position'
]

# Add any table that starts with hr_ or hrm_
to_drop.extend([t for t in tables if t.startswith('hr_') or t.startswith('hrm_')])

# Add any table that starts with hrm. (if any)
to_drop.extend([t for t in tables if t.startswith('hrm.')])

for table in set(to_drop):
    if table in tables:
        print(f"Dropping table {table}")
        cursor.execute(f"DROP TABLE \"{table}\"")

conn.commit()
conn.close()
print("Successfully dropped all HRM related tables")
