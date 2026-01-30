from django.db import connection

def check_schema():
    with connection.cursor() as cursor:
        tables = ['unit_of_measure', 'common_unit_of_measure', 'procurement_purchaseorderline']
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

check_schema()




