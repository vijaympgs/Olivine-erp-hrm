#!/usr/bin/env python
"""
Master Data Verification Script
Checks if seed_data.py has been run and data exists
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings')
django.setup()

from core.licensing.backend.business_entities.models import Company
from core.org-structure.backend.company.models import (
    Location, UnitOfMeasure, Item, ItemVariant,
    OperationalSupplier as Supplier,
    OperationalCustomer as Customer,
    Attribute, AttributeValue
)

print("=" * 60)
print("MASTER DATA VERIFICATION REPORT")
print("=" * 60)

# Company
company_count = Company.objects.filter(status='ACTIVE').count()
print(f"\n1. Companies (Active): {company_count}")
if company_count > 0:
    for c in Company.objects.filter(status='ACTIVE')[:3]:
        print(f"   - {c.name} ({c.code})")

# Locations
location_count = Location.objects.filter(is_active=True).count()
print(f"\n2. Locations (Active): {location_count}")
if location_count > 0:
    for loc in Location.objects.filter(is_active=True)[:5]:
        print(f"   - {loc.name} ({loc.location_code}) - {loc.location_type}")

# Suppliers
supplier_count = Supplier.objects.filter(is_active=True).count()
print(f"\n3. Suppliers (Active): {supplier_count}")
if supplier_count > 0:
    for sup in Supplier.objects.filter(is_active=True)[:5]:
        print(f"   - {sup.supplier_name} ({sup.supplier_code})")

# Customers
customer_count = Customer.objects.filter(is_active=True).count()
print(f"\n4. Customers (Active): {customer_count}")

# Items
item_count = Item.objects.filter(status='ACTIVE').count()
print(f"\n5. Items (Active): {item_count}")
if item_count > 0:
    for item in Item.objects.filter(status='ACTIVE')[:5]:
        print(f"   - {item.item_name} ({item.item_code})")

# Item Variants
variant_count = ItemVariant.objects.count()
print(f"\n6. Item Variants: {variant_count}")

# UOMs
uom_count = UnitOfMeasure.objects.filter(is_active=True).count()
print(f"\n7. UOMs (Active): {uom_count}")
if uom_count > 0:
    for uom in UnitOfMeasure.objects.filter(is_active=True)[:5]:
        print(f"   - {uom.uom_name} ({uom.uom_code})")

# Attributes
attr_count = Attribute.objects.filter(is_active=True).count()
print(f"\n8. Attributes (Active): {attr_count}")

# Attribute Values
attrval_count = AttributeValue.objects.filter(is_active=True).count()
print(f"\n9. Attribute Values (Active): {attrval_count}")

print("\n" + "=" * 60)
print("READINESS ASSESSMENT")
print("=" * 60)

# Check against seed_data.py expectations
issues = []

if company_count < 1:
    issues.append("❌ Company: Expected ≥1, Found 0")
else:
    print("✅ Company: READY")

if location_count < 2:
    issues.append(f"❌ Locations: Expected ≥2, Found {location_count}")
else:
    print("✅ Locations: READY")

if supplier_count < 3:
    issues.append(f"❌ Suppliers: Expected ≥3, Found {supplier_count}")
else:
    print("✅ Suppliers: READY")

if item_count < 3:
    issues.append(f"❌ Items: Expected ≥3, Found {item_count}")
else:
    print("✅ Items: READY")

if variant_count < 9:
    issues.append(f"⚠️  Item Variants: Expected ≥9, Found {variant_count}")
else:
    print("✅ Item Variants: READY")

if uom_count < 5:
    issues.append(f"❌ UOMs: Expected ≥5, Found {uom_count}")
else:
    print("✅ UOMs: READY")

if issues:
    print("\n" + "=" * 60)
    print("ISSUES FOUND:")
    print("=" * 60)
    for issue in issues:
        print(issue)
    print("\n⚠️  RECOMMENDATION: Run 'python manage.py seed_data' to populate master data")
else:
    print("\n✅ ALL MASTER DATA READY FOR TESTING")

print("=" * 60)




