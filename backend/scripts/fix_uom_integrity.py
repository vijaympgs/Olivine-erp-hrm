from django.db import connection

def fix_uom_integrity():
    with connection.cursor() as cursor:
        uom_table = 'unit_of_measure' 
        pol_table = 'procurement_purchaseorderline'

        print(f"Using UOM Table: {uom_table}")
        print(f"Using POL Table: {pol_table}")
        
        # 1. Check for bad integrity
        query = f"""
            SELECT id, uom_id 
            FROM {pol_table} 
            WHERE uom_id IS NOT NULL 
            AND uom_id NOT IN (SELECT id FROM {uom_table})
        """
        try:
            cursor.execute(query)
            bad_rows = cursor.fetchall()
            print(f"Found {len(bad_rows)} rows with invalid UOM IDs.")

            if bad_rows:
                print("IDs:", [r[0] for r in bad_rows])
                print("Fixing by setting UOM to NULL...")
                update_query = f"""
                    UPDATE {pol_table}
                    SET uom_id = NULL
                    WHERE uom_id IS NOT NULL 
                    AND uom_id NOT IN (SELECT id FROM {uom_table})
                """
                cursor.execute(update_query)
                print(f"Updated {cursor.rowcount} rows.")
            else:
                print("No integrity violations found.")
        except Exception as e:
            print(f"Error: {e}")

fix_uom_integrity()




