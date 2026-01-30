from core.org-structure.backend.company import models as cm
from core.licensing.backend.business_entities import models as bem
from core.org-structure.backend.company.models import ItemMaster, OperationalSupplier, OperationalCustomer

print("="*70)
print("ARCHITECTURAL CORRECTION VALIDATION")
print("="*70)

# A. MODEL OWNERSHIP
print("\nA. MODEL OWNERSHIP & LOCATION")
print("-"*70)
print(f"  Category in company: {hasattr(cm, 'Category')}")
print(f"  Brand in company: {hasattr(cm, 'Brand')}")
print(f"  TaxClass in company: {hasattr(cm, 'TaxClass')}")
print(f"  ItemMaster in company: {hasattr(cm, 'ItemMaster')}")
print(f"  OperationalSupplier in company: {hasattr(cm, 'OperationalSupplier')}")
print(f"  OperationalCustomer in company: {hasattr(cm, 'OperationalCustomer')}")

be_models = [hasattr(bem, m) for m in ['Category', 'Brand', 'TaxClass', 'ItemMaster', 'Supplier', 'Customer']]
print(f"\n  Still in business_entities: {any(be_models)}")

# B. TABLE MAPPINGS
print("\nB. DATABASE TABLE INTEGRITY")
print("-"*70)
print(f"  ItemMaster table: {ItemMaster._meta.db_table}")
print(f"  Category table: {cm.Category._meta.db_table}")
print(f"  Brand table: {cm.Brand._meta.db_table}")
print(f"  TaxClass table: {cm.TaxClass._meta.db_table}")
print(f"  Supplier table: {OperationalSupplier._meta.db_table}")
print(f"  Customer table: {OperationalCustomer._meta.db_table}")

# C. APP LABELS
print("\nC. APP LABELS")
print("-"*70)
print(f"  ItemMaster app: {ItemMaster._meta.app_label}")
print(f"  Category app: {cm.Category._meta.app_label}")
print(f"  Supplier app: {OperationalSupplier._meta.app_label}")

# D. RECORD COUNTS
print("\nD. RECORD COUNTS")
print("-"*70)
print(f"  ItemMaster: {ItemMaster.objects.count()}")
print(f"  Suppliers: {OperationalSupplier.objects.count()}")
print(f"  Customers: {OperationalCustomer.objects.count()}")

print("\n" + "="*70)




