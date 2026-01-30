# QUICK MANUAL TESTING CHECKLIST

**Time Required**: 5 minutes  
**Date**: 2025-12-23

---

## ✅ DJANGO ADMIN SANITY CHECK (2 minutes)

### Step 1: Access Admin
- [ ] Navigate to: `http://127.0.0.1:8000/admin/`
- [ ] Login: `admin` / `admin123`

### Step 2: Check business_entities Section
- [ ] Find "BUSINESS_ENTITIES" section in sidebar
- [ ] Should show ONLY "Companies" (1 model)
- [ ] ❌ Should NOT show: Category, Brand, ItemMaster, Supplier, Customer, Location

### Step 3: Check COMPANY Section
- [ ] Find "COMPANY" section in sidebar
- [ ] Should show multiple models (11+):
  - [ ] Attributes
  - [ ] Attribute values
  - [ ] Brands
  - [ ] Categories
  - [ ] Customers
  - [ ] Item Masters
  - [ ] Locations
  - [ ] Price Lists
  - [ ] Product Attribute Templates
  - [ ] Suppliers
  - [ ] Tax Classes
  - [ ] Units of Measure

### Step 4: Quick Data Check
- [ ] Click "Item Masters" → Should show 302 records
- [ ] Click "Suppliers" → Should show 145 records
- [ ] Click "Customers" → Should show 170 records

**Result**: [ ] PASS / [ ] FAIL

---

## ✅ PO SUPPLIER LOOKUP TEST (1.5 minutes)

### Step 1: Navigate to PO Form
- [ ] Go to: `http://localhost:5174/procurement/purchase-orders/new`
- [ ] Or: Click Procurement → Purchase Orders → New

### Step 2: Open Supplier Lookup
- [ ] Click "Lookup" button next to Supplier field
- [ ] OR press `F3` keyboard shortcut

### Step 3: Verify Supplier Modal
- [ ] Modal opens from right side
- [ ] Shows "Supplier Lookup" title
- [ ] Displays list of suppliers (should see ~145)
- [ ] Search bar is visible

### Step 4: Test Search
- [ ] Type "Unilever" in search box
- [ ] Results filter to matching suppliers
- [ ] Clear search to see all suppliers again

### Step 5: Test Selection
- [ ] Click on any supplier row
- [ ] Modal closes
- [ ] Supplier name appears in PO form field

**Result**: [ ] PASS / [ ] FAIL

---

## ✅ PO ITEM LOOKUP TEST (1.5 minutes)

### Step 1: Open Item Lookup
- [ ] Click "Add Item" or Product Lookup button
- [ ] OR press `F1` keyboard shortcut

### Step 2: Verify Item Modal
- [ ] Modal opens from right side
- [ ] Shows "Product Lookup" or "Item Lookup" title
- [ ] Displays list of items (should see ~302)
- [ ] Search bar is visible

### Step 3: Test Search
- [ ] Type any keyword in search box
- [ ] Results filter to matching items
- [ ] Clear search to see all items again

### Step 4: Test Selection
- [ ] Click on any item row
- [ ] Modal closes
- [ ] Item is added to PO lines table

**Result**: [ ] PASS / [ ] FAIL

---

## 📊 QUICK SUMMARY

| Test | Status | Notes |
|------|--------|-------|
| Django Admin - business_entities | [ ] PASS / [ ] FAIL | |
| Django Admin - company | [ ] PASS / [ ] FAIL | |
| Supplier Lookup | [ ] PASS / [ ] FAIL | |
| Item Lookup | [ ] PASS / [ ] FAIL | |

**Overall Result**: [ ] ALL PASS / [ ] SOME FAILED

---

## 🐛 IF TESTS FAIL

### Supplier Lookup Shows "No suppliers found":
1. Check backend is running: `http://127.0.0.1:8000/api/suppliers/`
2. Check browser console for errors (F12)
3. Verify: `python manage.py shell -c "from domain.company.models import OperationalSupplier; print(OperationalSupplier.objects.count())"`

### Item Lookup Shows "No items found":
1. Check backend is running: `http://127.0.0.1:8000/api/items/`
2. Check browser console for errors (F12)
3. Verify: `python manage.py shell -c "from domain.company.models import ItemMaster; print(ItemMaster.objects.count())"`

### Admin Models Missing:
1. Restart Django server: `Ctrl+C` then `python manage.py runserver`
2. Clear browser cache: `Ctrl+Shift+Delete`
3. Check: `backend/domain/company/admin.py` exists

---

## ✅ EXPECTED RESULTS

If all tests pass, you should see:
- ✅ Django Admin properly organized (business_entities has 1 model, company has 11+)
- ✅ Supplier Lookup shows 145 suppliers
- ✅ Item Lookup shows 302 items
- ✅ Search functionality works in both lookups
- ✅ Selection populates the PO form correctly
- ✅ No console errors

---

**Testing Completed**: ___________  
**Tested By**: ___________  
**Overall Status**: [ ] PASS / [ ] FAIL
