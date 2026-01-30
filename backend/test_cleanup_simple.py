from rest_framework.test import APIClient
from core.org-structure.backend.company.models import ItemMaster, OperationalSupplier, OperationalCustomer
from core.licensing.backend.business_entities.models import Company
from django.contrib import admin

print("="*70)
print("POST-CLEANUP VERIFICATION TESTS")
print("="*70)

# TEST 1: Model Counts
print("\n📊 TEST 1: MODEL RECORD COUNTS")
print("-"*70)
company_count = Company.objects.count()
item_count = ItemMaster.objects.count()
supplier_count = OperationalSupplier.objects.count()
customer_count = OperationalCustomer.objects.count()

print(f"  Companies: {company_count}")
print(f"  ItemMaster: {item_count}")
print(f"  Suppliers: {supplier_count}")
print(f"  Customers: {customer_count}")

test1_pass = (company_count == 5 and item_count == 302 and 
              supplier_count == 145 and customer_count == 170)
print(f"\n  Result: {'✅ PASS' if test1_pass else '❌ FAIL'}")

# TEST 2: API Endpoints
print("\n🌐 TEST 2: API ENDPOINT TESTS")
print("-"*70)

client = APIClient()

# Test Supplier API
print("\n  A. Supplier Lookup API")
response = client.get('/api/suppliers/', {'status': 'ACTIVE'})
print(f"     Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    count = len(data) if isinstance(data, list) else len(data.get('results', []))
    print(f"     Count: {count} suppliers")
    supplier_api_pass = count > 0
    print(f"     Result: {'✅ PASS' if supplier_api_pass else '❌ FAIL'}")
else:
    supplier_api_pass = False
    print(f"     Result: ❌ FAIL")

# Test Item API
print("\n  B. Item Lookup API")
response2 = client.get('/api/items/')
print(f"     Status: {response2.status_code}")
if response2.status_code == 200:
    data2 = response2.json()
    count2 = len(data2) if isinstance(data2, list) else len(data2.get('results', []))
    print(f"     Count: {count2} items")
    item_api_pass = count2 > 0
    print(f"     Result: {'✅ PASS' if item_api_pass else '❌ FAIL'}")
else:
    item_api_pass = False
    print(f"     Result: ❌ FAIL")

# TEST 3: Admin Registration
print("\n🔧 TEST 3: DJANGO ADMIN REGISTRATION")
print("-"*70)

be_models = [m for m in admin.site._registry.keys() 
             if hasattr(m, '_meta') and m._meta.app_label == 'business_entities']
print(f"\n  business_entities: {len(be_models)} models")
for m in be_models:
    print(f"    - {m.__name__}")

company_models = [m for m in admin.site._registry.keys() 
                  if hasattr(m, '_meta') and m._meta.app_label == 'company']
print(f"\n  company: {len(company_models)} models")
for m in sorted(company_models, key=lambda x: x.__name__)[:5]:
    print(f"    - {m.__name__}")
if len(company_models) > 5:
    print(f"    ... and {len(company_models) - 5} more")

# SUMMARY
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
all_pass = test1_pass and supplier_api_pass and item_api_pass
print(f"  Model Counts: {'✅ PASS' if test1_pass else '❌ FAIL'}")
print(f"  Supplier API: {'✅ PASS' if supplier_api_pass else '❌ FAIL'}")
print(f"  Item API: {'✅ PASS' if item_api_pass else '❌ FAIL'}")
print(f"\n{'🎊 ALL TESTS PASSED!' if all_pass else '⚠️ SOME TESTS FAILED'}")
print("="*70)




