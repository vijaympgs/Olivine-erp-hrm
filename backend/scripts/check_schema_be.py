from django.db import connection

def check_schema_be():
    with connection.cursor() as cursor:
        tables = ['be_item_master']
        for table in tables:
            print(f"--- Schema for {table} ---")
            try:
                cursor.execute(f"PRAGMA table_info({table})")
                columns = cursor.fetchall()
                if columns:
                    for col in columns:
                        print(col)
                else:
                    print("Table not found.")
            except Exception as e:
                print(e)

check_schema_be()




