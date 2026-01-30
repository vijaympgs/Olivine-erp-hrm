# 🚧 DJANGO APP REGISTRATION - BLOCKED BY IMPORT CLEANUP

**Date**: 2026-01-02 20:30 IST  
**Status**: 🔴 **BLOCKED - 22 Files Need Import Updates**

---

## ✅ PROGRESS SO FAR

1. ✅ Created `common.domain` Django app
2. ✅ Created `apps.retail.backend.domain` Django app  
3. ✅ Registered both in INSTALLED_APPS
4. ✅ Fixed circular imports with string ForeignKey references
5. ✅ Commented out legacy Location model in `core.org_structure.backend.company.models`
6. ✅ Fixed 5 import references manually

## ❌ CURRENT BLOCKER

**22 files still importing Location from legacy paths:**

### Backend Files (12):
1. `apps/retail/backend/inventory/intercompany_models.py`
2. `apps/retail/backend/inventory/tests/test_5_3_stock_movements.py`
3. `apps/retail/backend/inventory/tests/test_5_4_stock_adjustments.py`
4. `apps/retail/backend/inventory/tests/test_5_5_physical_inventory.py`
5. `apps/retail/backend/inventory/tests/test_5_6_inventory_valuation.py`
6. `apps/retail/backend/inventory/tests/test_5_7_replenishment.py`
7. `apps/retail/backend/inventory/tests/test_5_8_item_tracking.py`
8. `apps/retail/backend/inventory/tests/test_5_9_inventory_reports.py`
9. `apps/retail/backend/pos/day_open/views.py`
10. `apps/retail/backend/procurement/models.py`
11. `apps/retail/backend/procurement/views.py`
12. `apps/retail/backend/sales/services.py`

### Test Files (2):
13. `apps/retail/backend/sales/tests/test_6_1_sales_quotation.py`
14. `apps/retail/backend/sales/tests/test_6_2_sales_order.py`

### Duplicate/Frontend Files (8 - likely duplicates):
15-22. Various `core/auth_access` and `frontend` duplicates

---

## 🎯 SOLUTION OPTIONS

### Option A: Automated Script (RECOMMENDED)
Create a Python script to automatically update all imports:
- Find: `from core.org_structure.backend.company.models import.*Location`
- Replace with: `from apps.retail.backend.domain.models import Location`
- Also update: `from core.org_structure.backend.location`

### Option B: Manual Updates
Update each file individually (time-consuming, error-prone)

### Option C: Defer to Next Session
Document the blocker and continue in next session with fresh context

---

## 📊 IMPACT

**Currently Working**:
- ✅ Django app registration (both apps registered)
- ✅ Model definitions (no conflicts)
- ✅ String ForeignKey references

**Still Blocked**:
- ❌ Django system check (ImportError on first file with legacy import)
- ❌ Test Console
- ❌ Backend server startup
- ❌ Any backend operations

---

## ⏭️ RECOMMENDED NEXT STEP

**Create automated import update script** to fix all 22 files at once:

```python
import os
import re

def fix_location_imports(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern 1: from core.org_structure.backend.company.models import ... Location ...
    content = re.sub(
        r'from core\.org_structure\.backend\.company\.models import ([^\\n]*Location[^\\n]*)',
        lambda m: fix_import_line(m.group(0)),
        content
    )
    
    # Pattern 2: from core.org_structure.backend.location
    content = re.sub(
        r'from core\.org_structure\.backend\.location[^\\n]*',
        'from apps.retail.backend.domain.models import Location',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
```

**Estimated Time**: 10 minutes to create + test script, 2 minutes to run

---

**Status**: 🟡 **AWAITING DECISION - Automated fix or manual?**
