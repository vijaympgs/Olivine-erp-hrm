import os
import django
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings")
if not settings.configured:
    django.setup()

from Retail.backend.procurement.serializers import PurchaseRequisitionSerializer
from core.org-structure.backend.company.models import ItemMaster, UnitOfMeasure
from django.contrib.auth import get_user_model
import json

print("--- FINAL VERIFICATION START ---")

# 1. Fetch proper integer ID item
try:
    item = ItemMaster.objects.first()
    uom = UnitOfMeasure.objects.first() # Get valid UOM
    print(f"Item ID: {item.id}")
    print(f"UOM ID: {uom.id}")

    # 2. Simulate sanitized payload
    payload = {
        'date': '2025-12-25',
        'required_by_date': '2025-12-30',
        'priority': 'NORMAL',
        'status': 'DRAFT',
        'remarks': 'Backend Verification Test',
        # Context (omitted => injected)
        'lines': [
            {
                'item_id': str(item.id), # "1"
                'uom_id': str(uom.id),   # "1"
                'requested_qty': 5,
                'required_by_date': '2025-12-30',
                # 'item_variant': omitted
            }
        ]
    }

    print(f"Payload: {payload}")

    serializer = PurchaseRequisitionSerializer(data=payload)
    if serializer.is_valid():
        try:
            # Simulate perform_create injection logic
            from core.licensing.backend.business_entities.models import Company
            from core.org-structure.backend.company.models import Location
            
            company = Company.objects.filter(status='ACTIVE').first() 
            location = Location.objects.filter(company=company, is_active=True).first()
            user = get_user_model().objects.first()
            
            print(f"Injecting: Company={company}, Location={location}, User={user}")

            pr = serializer.save(
                company=company,
                requesting_location=location,
                requested_by=user
            )
            print(f"SUCCESS! Created PR: {pr.pr_number}")
        except Exception as e:
            print("FAILED SAVE (500)!")
            import traceback
            traceback.print_exc()
    else:
        print("FAILED VALIDATION (400)!")
        print(serializer.errors)

except Exception as e:
    print("Setup Error:")
    import traceback
    traceback.print_exc()

print("--- FINAL VERIFICATION END ---")




