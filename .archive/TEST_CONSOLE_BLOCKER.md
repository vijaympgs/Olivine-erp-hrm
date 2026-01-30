# 🚨 TEST CONSOLE ISSUE - ROOT CAUSE IDENTIFIED

**Date**: 2026-01-02 20:10 IST  
**Status**: ⚠️ **BLOCKED BY MERGEABILITY MIGRATION**

---

## ❌ ISSUE SUMMARY

**Symptom**: Test Console shows "No components match filters" and "Failed to sync scripts: Internal Server Error"

**Root Cause**: `common.domain` Django app is not registered in `INSTALLED_APPS`

---

## 🔍 DIAGNOSIS

### **Error Chain**:
1. Test Console tries to load data from backend API
2. Backend tries to run Django management commands
3. Django system check fails with 41 model relation errors
4. All errors are: "Field defines a relation with model 'X', which is either not installed, or is abstract"
5. Models affected: `Customer`, `ItemMaster`, `ItemVariant`, `UnitOfMeasure`, `Location`

### **Why This Happens**:
- We updated Sales & Inventory models to import from `common.domain`
- But `common.domain` is NOT registered as a Django app
- Django doesn't recognize these models
- ForeignKey references fail

---

## ✅ SOLUTION REQUIRED

**We must complete the mergeability migration blocker resolution:**

### **Step 1: Create AppConfig**
```python
# common/domain/apps.py
from django.apps import AppConfig

class DomainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common.domain'
    label = 'domain'
    verbose_name = 'Common Domain Contracts'
```

### **Step 2: Register in INSTALLED_APPS**
```python
# backend/erp_core/settings.py
INSTALLED_APPS = [
    # ... existing apps ...
    'common.domain',  # Add this BEFORE retail apps
    # ... retail apps ...
]
```

### **Step 3: Create Migrations**
```bash
python manage.py makemigrations domain
python manage.py migrate domain
```

### **Step 4: Retry Test Console**
```bash
python manage.py update_test_scripts
# Then refresh browser at http://localhost:5173/test-console
```

---

## 📊 IMPACT

**Currently Broken**:
- ❌ Test Console (cannot load data)
- ❌ Django management commands (system check fails)
- ❌ Any backend operation that touches Sales/Inventory models
- ❌ Backend server likely not starting properly

**Will Be Fixed After Solution**:
- ✅ Test Console will load components
- ✅ Django system checks will pass
- ✅ Sales/Inventory APIs will work
- ✅ Mergeability migration will be complete

---

## 🎯 PRIORITY

**CRITICAL - BLOCKING ALL BACKEND OPERATIONS**

This must be resolved before:
- Test Console can work
- Sales module can be tested
- Any backend API can function properly

---

## 📝 RELATED DOCUMENTS

- `SALES_MIGRATION_VERIFICATION.md` - Original blocker identification
- `MERGEABILITY_COMPLETE.md` - Migration completion report
- `PHASE4_CLEANUP_PROGRESS.md` - Import updates progress

---

**Action Required**: Complete Django app registration for `common.domain`
