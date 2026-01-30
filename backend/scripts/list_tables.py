from django.db import connection

def list_tables():
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("All Tables:")
        for t in sorted([t[0] for t in tables]):
            print(t)

list_tables()




