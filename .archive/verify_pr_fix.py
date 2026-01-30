from Retail.backend.procurement.serializers import PurchaseRequisitionSerializer
from core.org-structure.backend.company.models import ItemMaster, UnitOfMeasure, Company, Location

# Check DB state
c = Company.objects.filter(is_active=True).first()
l = Location.objects.filter(company=c, is_active=True).first() if c else None
i = ItemMaster.objects.first()
u = UnitOfMeasure.objects.first()

print(f"DEBUG: Company={c}, Location={l}, Item={i}, UOM={u}")

if i and u:
    data = {'lines': [{'item_id': str(i.id), 'uom_id': str(u.id), 'requested_qty': 10}]}
    # Note: company/location/requested_by are not in data, expecting serializer to allow this (required=False or read_only)
    ser = PurchaseRequisitionSerializer(data=data)
    is_valid = ser.is_valid()
    print(f"VALIDATION_RESULT: {is_valid}")
    if not is_valid:
        print(f"ERRORS: {ser.errors}")
else:
    print("ERROR: Missing seed data (Item or UOM)")




