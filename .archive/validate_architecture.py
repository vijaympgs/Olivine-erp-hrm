#!/usr/bin/env python
"""
ARCHITECTURAL CORRECTION VALIDATION SCRIPT
Validates that operational models have been correctly moved from business_entities to company
"""
import os
import sys
import django

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'backend'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_core.settings.dev")
django.setup()

from domain.company import models as cm
from domain.business_entities import models as bem

print("="*70)
print("ARCHITECTURAL CORRECTION VALIDATION")
print("="*70)

# A. MODEL OWNERSHIP & LOCATION
print("\nA. MODEL OWNERSHIP & LOCATION")
print("-"*70)
company_models = {
    'Category': hasattr(cm, 'Category'),
    'Brand': hasattr(cm, 'Brand'),
    'TaxClass': hasattr(cm, 'TaxClass'),
    'ItemMaster': hasattr(cm, 'ItemMaster'),
    'OperationalSupplier': hasattr(cm, 'OperationalSupplier'),
    'OperationalCustomer': hasattr(cm, 'OperationalCustomer'),
}

for model, exists in company_models.items():
    status = "✅ PASS" if exists else "❌ FAIL"
    print(f"  ☐ {model} in domain.company: {status}")

# Check if still in business_entities
be_operational = []
for model in ['Category', 'Brand', 'TaxClass', 'ItemMaster', 'Supplier', 'Customer']:
    if hasattr(bem, model):
        be_operational.append(model)

if be_operational:
    print(f"\n  ❌ FAIL: These models still exist in business_entities: {be_operational}")
else:
    print(f"\n  ✅ PASS: NO operational models remain in business_entities")

# B. DATABASE TABLE INTEGRITY
print("\nB. DATABASE TABLE INTEGRITY")
print("-"*70)
table_mappings = {
    'ItemMaster': 'be_item_master',
    'Category': 'be_category',
    'Brand': 'be_brand',
    'TaxClass': 'be_tax_class',
    'OperationalSupplier': 'be_supplier',
    'OperationalCustomer': 'be_customer',
}

for model_name, expected_table in table_mappings.items():
    model_class = getattr(cm, model_name)
    actual_table = model_class._meta.db_table
    status = "✅ PASS" if actual_table == expected_table else f"❌ FAIL (got {actual_table})"
    print(f"  ☐ {model_name} → {expected_table}: {status}")

# C. APP LABELS
print("\nC. APP LABELS")
print("-"*70)
for model_name in table_mappings.keys():
    model_class = getattr(cm, model_name)
    app_label = model_class._meta.app_label
    status = "✅ PASS" if app_label == 'company' else f"❌ FAIL (got {app_label})"
    print(f"  ☐ {model_name} app_label='company': {status}")

# D. RECORD COUNTS
print("\nD. RUNTIME VERIFICATION - RECORD COUNTS")
print("-"*70)
from domain.company.models import ItemMaster, OperationalSupplier, OperationalCustomer

counts = {
    'ItemMaster': ItemMaster.objects.count(),
    'OperationalSupplier': OperationalSupplier.objects.count(),
    'OperationalCustomer': OperationalCustomer.objects.count(),
}

for model, count in counts.items():
    print(f"  {model}: {count} records")

# E. SEED SCRIPT VALIDATION
print("\nE. SEED SCRIPT IMPORTS")
print("-"*70)
seed_file = os.path.join(BASE_DIR, 'seed', 'seed_enterprise_masters.py')
with open(seed_file, 'r') as f:
    seed_content = f.read()

has_be_import = 'from domain.business_entities.models import (' in seed_content and \
                ('ItemMaster' in seed_content.split('from domain.business_entities.models import (')[1].split(')')[0] or
                 'Supplier' in seed_content.split('from domain.business_entities.models import (')[1].split(')')[0] or
                 'Customer' in seed_content.split('from domain.business_entities.models import (')[1].split(')')[0])

has_company_import = 'from domain.company.models import (' in seed_content

if has_be_import:
    print(f"  ❌ FAIL: Seed script still imports operational models from business_entities")
else:
    print(f"  ✅ PASS: Seed script does NOT import operational models from business_entities")

if has_company_import:
    print(f"  ✅ PASS: Seed script imports from domain.company.models")
else:
    print(f"  ❌ FAIL: Seed script missing domain.company.models import")

# FINAL SUMMARY
print("\n" + "="*70)
print("VALIDATION SUMMARY")
print("="*70)
all_pass = all(company_models.values()) and not be_operational and \
           all(getattr(cm, m)._meta.db_table == t for m, t in table_mappings.items()) and \
           not has_be_import and has_company_import

if all_pass:
    print("✅ ALL CHECKS PASSED - ARCHITECTURAL CORRECTION COMPLETE")
else:
    print("❌ SOME CHECKS FAILED - REVIEW REQUIRED")

print(f"\nFinal Record Counts:")
print(f"  - ItemMaster: {counts['ItemMaster']}")
print(f"  - Suppliers: {counts['OperationalSupplier']}")
print(f"  - Customers: {counts['OperationalCustomer']}")
print("="*70)




