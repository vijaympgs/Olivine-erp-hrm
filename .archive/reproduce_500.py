import os
import django
from django.conf import settings

# Setup Django Environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings")
if not settings.configured:
    django.setup()

from django.contrib.auth import get_user_model
from Retail.backend.procurement.serializers import PurchaseRequisitionSerializer
from core.org-structure.backend.company.models import Company, Location, ItemMaster, UnitOfMeasure
from Retail.backend.procurement.models import PurchaseRequisition
import traceback

print("--- DIAGNOSTICS START ---")

try:
    # 1. Check Master Data
    User = get_user_model()
    u_obj = User.objects.first()
    c = Company.objects.filter(status='ACTIVE').first()
    l = Location.objects.filter(company=c, is_active=True).first() if c else None
    i = ItemMaster.objects.first()
    uom = UnitOfMeasure.objects.first()

    print(f"User: {u_obj} (ID: {u_obj.id if u_obj else 'None'})")
    print(f"Company: {c} (ID: {c.id if c else 'None'})")
    print(f"Location: {l} (ID: {l.id if l else 'None'})")
    print(f"Item: {i} ({i.id if i else 'None'})")
    print(f"UOM: {uom} ({uom.id if uom else 'None'})")

    # 2. Simulate Payload
    request_data = {
        'lines': []
    }

    if i and uom:
        request_data['lines'].append({
            'item_id': str(i.id),
            'uom_id': str(uom.id),
            'requested_qty': 10
        })

    print(f"Request Data: {request_data}")

    # 3. Simulate Serializer & Save
    serializer = PurchaseRequisitionSerializer(data=request_data)

    if serializer.is_valid():
        print("Validation: PASSED")
        # print(f"Validated Data: {serializer.validated_data}") # Can contain objects
        
        try:
            print("Attempting save with injection...")
            instance = serializer.save(
                company=c,
                requesting_location=l,
                requested_by=u_obj
            )
            print(f"Save: SUCCESS (ID: {instance.id}, PR: {instance.pr_number})")
        except Exception as e:
            print("!!! EXCEPTION DURING SAVE !!!")
            traceback.print_exc()
    else:
        print("Validation: FAILED")
        print(serializer.errors)

except Exception as e:
    print("!!! SETUP/PRE-SAVE EXCEPTION !!!")
    traceback.print_exc()

print("--- DIAGNOSTICS END ---")




