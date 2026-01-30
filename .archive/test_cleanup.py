#!/usr/bin/env python
"""
POST-CLEANUP VERIFICATION TESTS
Tests API endpoints and Django Admin after architectural cleanup
"""
import os
import sys
import django

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'backend'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.dev")
django.setup()

from rest_framework.test import APIClient
from domain.company.models import ItemMaster, OperationalSupplier, OperationalCustomer
from domain.business_entities.models import Company

print("="*70)
print("POST-CLEANUP VERIFICATION TESTS")
print("="*70)

# TEST 1: Model Counts
print("\n📊 TEST 1: MODEL RECORD COUNTS")
print("-"*70)
try:
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
except Exception as e:
    print(f"  ❌ ERROR: {e}")
    test1_pass = False

# TEST 2: API Endpoints
print("\n🌐 TEST 2: API ENDPOINT TESTS")
print("-"*70)

client = APIClient()

# Test Supplier API
print("\n  A. Supplier Lookup API (/api/suppliers/)")
try:
    response = client.get('/api/suppliers/', {'status': 'ACTIVE'})
    status_code = response.status_code
    
    if status_code == 200:
        data = response.json()
        count = len(data) if isinstance(data, list) else len(data.get('results', []))
        print(f"     Status: {status_code} OK")
        print(f"     Count: {count} suppliers")
        
        if count > 0:
            first_supplier = data[0] if isinstance(data, list) else data.get('results', [{}])[0]
            print(f"     Sample: {first_supplier.get('supplier_name', 'N/A')}")
        
        supplier_api_pass = count > 0
        print(f"     Result: {'✅ PASS' if supplier_api_pass else '❌ FAIL'}")
    else:
        print(f"     Status: {status_code} ERROR")
        print(f"     Result: ❌ FAIL")
        supplier_api_pass = False
except Exception as e:
    print(f"     ❌ ERROR: {e}")
    supplier_api_pass = False

# Test Item API
print("\n  B. Item Lookup API (/api/items/)")
try:
    response = client.get('/api/items/')
    status_code = response.status_code
    
    if status_code == 200:
        data = response.json()
        count = len(data) if isinstance(data, list) else len(data.get('results', []))
        print(f"     Status: {status_code} OK")
        print(f"     Count: {count} items")
        
        if count > 0:
            first_item = data[0] if isinstance(data, list) else data.get('results', [{}])[0]
            print(f"     Sample: {first_item.get('item_name', 'N/A')}")
        
        item_api_pass = count > 0
        print(f"     Result: {'✅ PASS' if item_api_pass else '❌ FAIL'}")
    else:
        print(f"     Status: {status_code} ERROR")
        print(f"     Result: ❌ FAIL")
        item_api_pass = False
except Exception as e:
    print(f"     ❌ ERROR: {e}")
    item_api_pass = False

# TEST 3: Admin Registration Check
print("\n🔧 TEST 3: DJANGO ADMIN REGISTRATION")
print("-"*70)

from django.contrib import admin

# Check business_entities admin
print("\n  A. business_entities Admin:")
be_models = [model for model in admin.site._registry.keys() 
             if hasattr(model, '_meta') and model._meta.app_label == 'business_entities']
print(f"     Registered models: {len(be_models)}")
for model in be_models:
    print(f"       - {model.__name__}")

# Should only have Company
be_admin_pass = len(be_models) == 1 and any(m.__name__ == 'Company' for m in be_models)
print(f"     Result: {'✅ PASS (Only Company)' if be_admin_pass else '❌ FAIL'}")

# Check company admin
print("\n  B. company Admin:")
company_models = [model for model in admin.site._registry.keys() 
                  if hasattr(model, '_meta') and model._meta.app_label == 'company']
print(f"     Registered models: {len(company_models)}")
for model in sorted(company_models, key=lambda m: m.__name__):
    print(f"       - {model.__name__}")

# Should have multiple operational models
company_admin_pass = len(company_models) >= 10
print(f"     Result: {'✅ PASS (Multiple operational models)' if company_admin_pass else '❌ FAIL'}")

# FINAL SUMMARY
print("\n" + "="*70)
print("FINAL TEST SUMMARY")
print("="*70)

all_tests = [
    ("Model Record Counts", test1_pass),
    ("Supplier API", supplier_api_pass),
    ("Item API", item_api_pass),
    ("business_entities Admin", be_admin_pass),
    ("company Admin", company_admin_pass),
]

passed = sum(1 for _, result in all_tests if result)
total = len(all_tests)

for test_name, result in all_tests:
    status = "✅ PASS" if result else "❌ FAIL"
    print(f"  {test_name}: {status}")

print(f"\nOverall: {passed}/{total} tests passed")

if passed == total:
    print("\n🎊 ALL TESTS PASSED - CLEANUP SUCCESSFUL! 🎊")
else:
    print(f"\n⚠️ {total - passed} test(s) failed - Review required")

print("="*70)




