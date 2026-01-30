from django.db import connection

def fix_all_uom_integrity():
    with connection.cursor() as cursor:
        uom_table = 'unit_of_measure' 
        
        tables_to_check = [
            'procurement_purchaseorderline',
            'procurement_purchaserequisitionline',
            'procurement_rfqline',
            'procurement_goodsreceiptline',
            'procurement_asnline'
        ]

        print(f"Using UOM Table: {uom_table}")
        
        for table in tables_to_check:
            print(f"Checking {table}...")
            # Check if table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=%s;", [table])
            if not cursor.fetchone():
                print(f"  Skipping {table} (not found)")
                continue

            # Check integrity
            query = f"""
                SELECT id, uom_id 
                FROM {table} 
                WHERE uom_id IS NOT NULL 
                AND uom_id NOT IN (SELECT id FROM {uom_table})
            """
            try:
                cursor.execute(query)
                bad_rows = cursor.fetchall()
                
                if bad_rows:
                    print(f"  Found {len(bad_rows)} rows with invalid UOM IDs.")
                    print("  IDs:", [r[0] for r in bad_rows])
                    print("  Fixing by setting UOM to NULL...")
                    update_query = f"""
                        UPDATE {table}
                        SET uom_id = NULL
                        WHERE uom_id IS NOT NULL 
                        AND uom_id NOT IN (SELECT id FROM {uom_table})
                    """
                    cursor.execute(update_query)
                    print(f"  Updated {cursor.rowcount} rows.")
                else:
                    print("  No integrity violations found.")
            except Exception as e:
                print(f"  Error checking {table}: {e}")

fix_all_uom_integrity()




