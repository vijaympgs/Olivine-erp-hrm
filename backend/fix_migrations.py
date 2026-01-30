import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings')
django.setup()

from django.db import connection

cursor = connection.cursor()
cursor.execute("DELETE FROM django_migrations WHERE app='company' AND name IN ('0009_customer', '0010_supplier')")
print('Migration records deleted')




