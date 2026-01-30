from django.db import connection

def finalize_prep():
    with connection.cursor() as cursor:
        # 1. Rename common_unit_of_measure (which we renamed earlier) to unit_of_measure_legacy
        print("Renaming common_unit_of_measure -> unit_of_measure_legacy...")
        try:
            # Check if common_unit_of_measure exists (it should if prepare script ran)
            cursor.execute("ALTER TABLE common_unit_of_measure RENAME TO unit_of_measure_legacy")
            print("  Done.")
        except Exception as e:
            print(f"  Error (checking if unit_of_measure needs rename): {e}")
            try:
                 cursor.execute("ALTER TABLE unit_of_measure RENAME TO unit_of_measure_legacy")
                 print("  Renamed unit_of_measure -> unit_of_measure_legacy")
            except Exception as e2:
                 print(f"  Failed renaming to legacy: {e2}")

def copy_uom_data():
    with connection.cursor() as cursor:
        print("Copying data from unit_of_measure_legacy to common_unit_of_measure...")
        # Match columns strictly? 
        # Insert select * might fail if column order differs or new columns added.
        # But for now assume match.
        try:
            cursor.execute("INSERT INTO common_unit_of_measure SELECT * FROM unit_of_measure_legacy")
            print(f"  Copied {cursor.rowcount} rows.")
        except Exception as e:
            print(f"  Error copying data: {e}")

if __name__ == '__main__':
    # This script is split. Part 1 run BEFORE migrate. Part 2 run AFTER migrate domain.
    pass




