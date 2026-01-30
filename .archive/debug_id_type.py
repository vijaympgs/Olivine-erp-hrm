import os
import django
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings")
if not settings.configured:
    django.setup()

from core.org-structure.backend.company.models import ItemMaster
from Retail.backend.procurement.serializers import PurchaseRequisitionSerializer

print("--- DIAGNOSTICS START ---")
item = ItemMaster.objects.first()
print(f"First Item ID: {item.id} (Type: {type(item.id)})")
print(f"Item UUID (hex): {item.id.hex if hasattr(item.id, 'hex') else 'N/A'}")

data = {
    'lines': [{
        'item_id': str(item.id),
        'uom_id': '00000000-0000-0000-0000-000000000000', # Dummy valid UUID
        'requested_qty': 10
    }]
}

print(f"Testing Payload with ID: {data['lines'][0]['item_id']}")
ser = PurchaseRequisitionSerializer(data=data)
valid = ser.is_valid()
print(f"Validation: {valid}")
if not valid:
    print(f"Errors: {ser.errors}")

print("--- DIAGNOSTICS END ---")




