# ARCHITECTURAL LOCK - QUICK REFERENCE

## 🔒 THE RULE (NON-NEGOTIABLE)

```
business_entities = LICENSING METADATA ONLY
company = OPERATIONAL MASTERS ONLY
```

**NO EXCEPTIONS. NO INTERPRETATION.**

---

## 📋 OPERATIONAL MODELS (Use domain.company)

### Canonical Models in `domain.company.models`:

| Model | Purpose | DB Table | Records |
|-------|---------|----------|---------|
| `Category` | Product categories | `be_category` | 7 |
| `Brand` | Product brands | `be_brand` | 21 |
| `TaxClass` | Tax classifications | `be_tax_class` | 5 |
| `ItemMaster` | **CANONICAL ITEM MODEL** | `be_item_master` | 302 |
| `OperationalSupplier` | Suppliers (alias: `Supplier`) | `be_supplier` | 145 |
| `OperationalCustomer` | Customers (alias: `Customer`) | `be_customer` | 170 |
| `Location` | Store/warehouse locations | `be_location` | 28 |
| `Attribute` | Product attributes | `be_attribute` | - |
| `AttributeValue` | Attribute values | `be_attribute_value` | - |
| `UnitOfMeasure` | Units of measure | `be_uom` | - |
| `PriceList` | Price lists | `be_price_list` | - |

---

## ✅ CORRECT IMPORT PATTERNS

### ✅ Seeds, APIs, Services, Admin:
```python
from domain.business_entities.models import Company  # ONLY for licensing
from domain.company.models import (
    ItemMaster,
    Category,
    Brand,
    TaxClass,
    Location,
    OperationalSupplier as Supplier,
    OperationalCustomer as Customer,
    # ... other operational models
)
```

### ❌ WRONG (DO NOT DO THIS):
```python
# ❌ NEVER import operational models from business_entities
from domain.business_entities.models import (
    ItemMaster,  # ❌ WRONG
    Supplier,    # ❌ WRONG
    Customer,    # ❌ WRONG
    Category,    # ❌ WRONG
)
```

---

## 🚫 DEPRECATED MODELS

### In `domain.company.models`:
- ❌ `Item` - DEPRECATED (use `ItemMaster`)
- ❌ `Supplier` (legacy) - DEPRECATED (use `OperationalSupplier`)
- ❌ `Customer` (legacy) - DEPRECATED (use `OperationalCustomer`)

### In `domain.business_entities.models`:
- ⚠️ Operational models still exist but are DEPRECATED
- ⚠️ DO NOT USE - they will be removed in future cleanup

---

## 📊 ITEM MODEL DECISION

**CANONICAL ITEM MODEL**: `ItemMaster` (domain.company)

| Model | Status | Records | Purpose |
|-------|--------|---------|---------|
| `ItemMaster` | ✅ CANONICAL | 302 | **USE THIS** |
| `Item` | ❌ DEPRECATED | 0 | Legacy, will be removed |

**Why ItemMaster?**
- Has actual data (302 records)
- Used by procurement, inventory, POS
- Seed script uses it
- Extensive relationships

---

## 🔧 AFFECTED MODULES

### Updated Files:
1. `backend/domain/company/models.py` - Added operational models
2. `backend/domain/company/views.py` - Updated imports
3. `seed/seed_enterprise_masters.py` - Updated imports

### Modules Using ItemMaster:
- ✅ Procurement (`domain.procurement`)
- ✅ Inventory (`domain.inventory`)
- ✅ POS (`domain.pos`)
- ✅ Sales (`domain.sales`)

---

## 🎯 VERIFICATION COMMANDS

### Check Model Location:
```python
from domain.company.models import ItemMaster, OperationalSupplier
print(f"ItemMaster app: {ItemMaster._meta.app_label}")  # Should be 'company'
print(f"ItemMaster table: {ItemMaster._meta.db_table}")  # Should be 'be_item_master'
print(f"ItemMaster count: {ItemMaster.objects.count()}")  # Should be 302
```

### Check API Endpoints:
```bash
curl http://localhost:8000/api/suppliers/?status=ACTIVE
curl http://localhost:8000/api/items/
```

---

## 📝 FUTURE CLEANUP TASKS

1. **Remove deprecated models from `business_entities/models.py`**
   - Category, Brand, TaxClass, ItemMaster, Supplier, Customer
   - LOW RISK (not used anywhere)

2. **Remove legacy models from `company/models.py`**
   - Legacy Item, Supplier, Customer
   - MEDIUM RISK (check for any remaining references)

3. **Update Django Admin**
   - Register operational models in `company/admin.py`
   - Remove from `business_entities/admin.py`

---

## 🚨 CRITICAL REMINDERS

1. **NEVER** import operational models from `business_entities`
2. **ALWAYS** use `ItemMaster` (not `Item`)
3. **ALWAYS** use `OperationalSupplier`/`OperationalCustomer` (aliased as Supplier/Customer)
4. **Company** is the ONLY model that should be in `business_entities` (for licensing)
5. **NO** table renaming (keep `be_*` prefixes)
6. **NO** data migration needed (same tables)

---

## 📞 ESCALATION

If you encounter:
- Imports from `business_entities` for operational models
- References to deprecated `Item` model
- Confusion about which model to use

**STOP. ASK. DO NOT GUESS.**

**Authority**: Viji  
**Agent Role**: Executor ONLY

---

**Last Updated**: 2025-12-23  
**Status**: LOCKED - NO CHANGES WITHOUT APPROVAL
