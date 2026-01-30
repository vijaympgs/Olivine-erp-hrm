# DOMAIN OWNERSHIP MIGRATION PLAN
**Date**: 2026-01-02 19:21 IST  
**Status**: AUTHORIZED EXECUTION  
**Authority**: Final Architectural Authority

---

## 🎯 OBJECTIVE
Establish clear domain ownership boundaries to enable app mergeability via copy-paste.

---

## 📋 DOMAIN OWNERSHIP DECISIONS (LOCKED)

### **Platform-Level (common/domain/)**
Models shared across ALL apps:
- ✅ **Company** - Licensing entity (all apps)
- ✅ **Customer** - Minimal shared contract (Retail + CRM)
- ✅ **ItemMaster** - Product catalog (Retail + FMS)
- ✅ **ItemVariant** - SKU/Variant (Retail + FMS)
- ✅ **Supplier** - Vendor entity (Retail + FMS)
- ✅ **UnitOfMeasure** - Measurement units (Retail + FMS)

### **Retail-Exclusive (retail/backend/domain/)**
Models owned ONLY by Retail:
- ✅ **Location** - Store/Warehouse (RETAIL ONLY)
- ⚠️ **RetailCustomer** - Retail-specific customer extensions (credit, pricing, loyalty)
- ⚠️ **RetailItem** - Retail-specific item extensions (pricing, inventory)

### **HRM-Exclusive (hrm/backend/domain/)**
- Employee, Department, Position
- ❌ NO Location references allowed

### **CRM-Exclusive (crm/backend/domain/)**
- Lead, Opportunity, Account
- ⚠️ CRMAccount extends common.Customer
- ❌ NO Location references allowed

### **FMS-Exclusive (fms/backend/domain/)**
- GL Account, Journal Entry
- Uses common.ItemMaster for valuation
- ❌ NO Location references allowed

---

## 🚨 CRITICAL RULES

### **Rule 1: Location Isolation**
```
Location is RETAIL-OWNED.
HRM, CRM, FMS MUST NOT reference Location.
All non-Retail apps operate at COMPANY level only.
```

### **Rule 2: Minimal Common Contracts**
```
common/domain/ models MUST be:
- Minimal (identity + company linkage only)
- Abstract where possible
- NO app-specific logic
- NO Location references
```

### **Rule 3: Extension Pattern**
```python
# CORRECT: Retail extends common Customer
class RetailCustomer(Customer):
    location = ForeignKey(Location)  # Retail-specific
    credit_limit = DecimalField()     # Retail-specific

# WRONG: Common Customer has Location
class Customer(models.Model):
    location = ForeignKey(Location)  # ❌ Breaks HRM/CRM
```

---

## 📂 CURRENT STATE ANALYSIS

### **Current Location**
```
core/org_structure/backend/location/models/location.py
└── Location model (145 lines)

Used by:
- apps/retail/backend/sales/models.py
- apps/retail/backend/inventory/models.py
- apps/retail/backend/procurement/models.py
- apps/retail/backend/pos/models.py
```

### **Current Customer**
```
core/org_structure/backend/company/models.py
└── Customer model (Line 654-710)
    ├── Legacy/Deprecated warning
    ├── Read-only manager
    └── References: BusinessEntityCompany
```

### **Current ItemMaster (Item)**
```
core/org_structure/backend/company/models.py
└── Item model (Line 441-485)
    ├── References: BusinessEntityCompany, UnitOfMeasure
    └── Used by: Retail (sales, inventory, procurement)
```

---

## ✅ EXECUTION PHASES

### **PHASE 1: Create Common Domain Layer** ✅ IN PROGRESS
**Status**: Creating `common/domain/models.py`

**Actions**:
1. Create `common/__init__.py`
2. Create `common/domain/__init__.py`
3. Create `common/domain/models.py` with minimal contracts:
   - Company (reference to existing)
   - Customer (minimal base)
   - ItemMaster (minimal base)
   - ItemVariant (minimal base)
   - Supplier (minimal base)
   - UnitOfMeasure (minimal base)

---

### **PHASE 2: Move Location to Retail** ⏳ NEXT
**Status**: Pending Phase 1 completion

**Actions**:
1. Create `retail/backend/domain/__init__.py`
2. Create `retail/backend/domain/models.py`
3. Move Location model from `core/org_structure/` to `retail/backend/domain/`
4. Update all Retail imports:
   - `apps/retail/backend/sales/models.py`
   - `apps/retail/backend/inventory/models.py`
   - `apps/retail/backend/procurement/models.py`
   - `apps/retail/backend/pos/models.py`
5. Verify ZERO Location references in:
   - `apps/hrm/backend/`
   - `apps/crm/backend/`
   - `apps/fms/backend/`

---

### **PHASE 3: Update Retail Imports** ⏳ PENDING
**Status**: After Phase 2

**Actions**:
1. Update Sales models to import from `common.domain` and `retail.backend.domain`
2. Update Inventory models
3. Update Procurement models
4. Update POS models
5. Run migrations

---

### **PHASE 4: Cleanup Core** ⏳ PENDING
**Status**: After Phase 3 verification

**Actions**:
1. Remove `core/org_structure/backend/location/` (after Location migration)
2. Mark legacy models in `core/org_structure/backend/company/models.py` as deprecated
3. Update documentation

---

## 🔍 VERIFICATION CHECKLIST

### **Mergeability Test**
```bash
# Test 1: Copy Retail app
cp -r apps/retail/ /tmp/test-merge/retail/
cp -r common/ /tmp/test-merge/common/

# Test 2: Verify imports work
cd /tmp/test-merge/
python -c "from retail.backend.sales.models import SalesQuote"
# Should succeed

# Test 3: Verify Location isolation
grep -r "from.*location" apps/hrm/backend/
grep -r "from.*location" apps/crm/backend/
grep -r "from.*location" apps/fms/backend/
# Should return ZERO results
```

---

## 📊 IMPACT ANALYSIS

### **Files to Modify**
| Category | Count | Effort |
|----------|-------|--------|
| Create common/domain/ | 3 files | LOW |
| Move Location to retail/ | 1 file | LOW |
| Update Retail imports | 20+ files | MEDIUM |
| Update migrations | 5+ files | MEDIUM |
| Cleanup core/ | 2 files | LOW |

**Total Estimated Effort**: 2-3 hours

---

## 🛑 STOP CONDITIONS

**STOP after**:
1. ✅ Common domain layer created
2. ✅ Location moved to Retail
3. ✅ All Retail imports updated
4. ✅ Zero Location leakage verified
5. ✅ Mergeability test passes

**WAIT for explicit approval** before:
- Restructuring root folders (`apps/` → root level)
- Frontend service migration
- Database schema changes

---

**End of Migration Plan** 📋
