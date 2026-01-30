# MANUAL TESTING GUIDE - PO Lookups Verification

**Date**: 2025-12-23  
**Purpose**: Verify that Supplier and Item lookups display data correctly after architectural correction  
**Prerequisites**: Backend and frontend servers running

---

## 🎯 TEST OBJECTIVES

1. Verify Supplier Lookup displays 145 suppliers
2. Verify Item Lookup displays 302 items
3. Confirm data is being fetched from correct API endpoints
4. Ensure no errors in browser console

---

## 📋 TEST STEPS

### **STEP 1: Access the Application**

1. Open browser and navigate to: `http://localhost:5174`
2. **Login Credentials**:
   - Username: `admin`
   - Password: `admin123`
3. After login, you should see the main dashboard

---

### **STEP 2: Navigate to Purchase Order Form**

1. Click on **Procurement** in the sidebar
2. Click on **Purchase Orders**
3. Click **New** or **+ Create** button
4. You should now be on the Purchase Order form page
5. **URL should be**: `http://localhost:5174/procurement/purchase-orders/new`

---

### **STEP 3: Test Supplier Lookup**

#### **3A. Open Supplier Lookup**
- **Method 1**: Click the **"Lookup"** button next to the Supplier field
- **Method 2**: Press **F3** keyboard shortcut
- **Method 3**: Click on the supplier field itself (if clickable)

#### **3B. Verify Supplier Modal**
✅ **Expected Results**:
- Modal should slide in from the right side
- Title should say "Supplier Lookup"
- Search bar should be visible at the top
- **Should display suppliers** (not "No suppliers found")

#### **3C. Check Supplier Data**
✅ **What to verify**:
- **Count**: Should show approximately **145 suppliers**
- **Columns**: Should display Supplier Code, Supplier Name
- **Sample Data**: Look for suppliers like:
  - "Hindustan Unilever"
  - "Procter \u0026 Gamble"
  - "ITC Limited"
  - "Nestlé India"
  - "Britannia Industries"

#### **3D. Test Search**
1. Type "Unilever" in the search box
2. Results should filter to show matching suppliers
3. Clear search to see all suppliers again

#### **3E. Test Selection**
1. Click on any supplier row
2. Modal should close
3. Supplier name should appear in the PO form's supplier field

---

### **STEP 4: Test Item/Product Lookup**

#### **4A. Open Item Lookup**
- **Method 1**: Click the **"Add Item"** or **Product Lookup** button
- **Method 2**: Press **F1** keyboard shortcut

#### **4B. Verify Item Modal**
✅ **Expected Results**:
- Modal should slide in from the right side
- Title should say "Product Lookup"
- Search bar should be visible at the top
- **Should display items** (not "No items found")

#### **4C. Check Item Data**
✅ **What to verify**:
- **Count**: Should show approximately **302 items**
- **Columns**: Should display Item Code, Item Name, Price, Stock UOM
- **Sample Data**: Look for items like various products from the seed data

#### **4D. Test Search**
1. Type any keyword in the search box
2. Results should filter to show matching items
3. Clear search to see all items again

#### **4E. Test Selection**
1. Click on any item row
2. Modal should close
3. Item should be added to the PO lines table

---

### **STEP 5: Browser Console Verification**

1. Open **Browser Developer Tools** (F12)
2. Go to **Console** tab
3. **Check for errors**:
   - ❌ Should NOT see "No suppliers found"
   - ❌ Should NOT see "No items found"
   - ❌ Should NOT see 404 or 500 errors
   - ✅ Should see successful API calls to `/api/suppliers/` and `/api/items/`

4. Go to **Network** tab
5. Open Supplier Lookup again
6. **Verify API call**:
   - Request URL: `http://127.0.0.1:8000/api/suppliers/?status=ACTIVE`
   - Status: `200 OK`
   - Response should contain array of suppliers

7. Open Item Lookup
8. **Verify API call**:
   - Request URL: `http://127.0.0.1:8000/api/items/...`
   - Status: `200 OK`
   - Response should contain array of items

---

## ✅ SUCCESS CRITERIA

| Test | Expected Result | Pass/Fail |
|------|----------------|-----------|
| Supplier Lookup Opens | ✅ Modal opens without errors | ☐ |
| Supplier Data Displayed | ✅ Shows ~145 suppliers | ☐ |
| Supplier Search Works | ✅ Filters results correctly | ☐ |
| Supplier Selection Works | ✅ Populates PO form | ☐ |
| Item Lookup Opens | ✅ Modal opens without errors | ☐ |
| Item Data Displayed | ✅ Shows ~302 items | ☐ |
| Item Search Works | ✅ Filters results correctly | ☐ |
| Item Selection Works | ✅ Adds to PO lines | ☐ |
| No Console Errors | ✅ No errors in browser console | ☐ |
| API Calls Successful | ✅ 200 OK responses | ☐ |

---

## 🐛 TROUBLESHOOTING

### **Issue: "No suppliers found"**

**Possible Causes**:
1. Backend not running
2. API endpoint not accessible
3. Data not seeded

**Solutions**:
1. Check backend is running: `http://127.0.0.1:8000/api/suppliers/`
2. Run seed script: `python seed/seed_enterprise_masters.py`
3. Check browser console for errors

---

### **Issue: "No items found"**

**Possible Causes**:
1. ItemMaster data not accessible
2. API endpoint issue

**Solutions**:
1. Check backend: `http://127.0.0.1:8000/api/items/`
2. Verify in Django shell:
   ```python
   from domain.company.models import ItemMaster
   print(ItemMaster.objects.count())  # Should be 302
   ```

---

### **Issue: Modal doesn't open**

**Possible Causes**:
1. JavaScript error
2. Component not loaded

**Solutions**:
1. Check browser console for errors
2. Refresh the page (Ctrl+F5)
3. Clear browser cache

---

## 📸 SCREENSHOTS TO CAPTURE

Please capture screenshots of:
1. ✅ Supplier Lookup modal with data visible
2. ✅ Item Lookup modal with data visible
3. ✅ Browser Network tab showing successful API calls
4. ❌ Any errors encountered (if any)

---

## 📝 TEST REPORT TEMPLATE

After testing, please report:

```
TEST RESULTS - PO Lookups Verification
Date: [DATE]
Tester: [YOUR NAME]

SUPPLIER LOOKUP:
- Opens: [YES/NO]
- Data Count: [NUMBER]
- Sample Data: [LIST 3-5 SUPPLIERS]
- Search Works: [YES/NO]
- Selection Works: [YES/NO]
- Errors: [NONE / DESCRIBE]

ITEM LOOKUP:
- Opens: [YES/NO]
- Data Count: [NUMBER]
- Sample Data: [LIST 3-5 ITEMS]
- Search Works: [YES/NO]
- Selection Works: [YES/NO]
- Errors: [NONE / DESCRIBE]

OVERALL STATUS: [PASS / FAIL]
NOTES: [ANY ADDITIONAL OBSERVATIONS]
```

---

## 🎯 NEXT STEPS AFTER TESTING

### **If All Tests Pass** ✅:
1. Mark architectural correction as VERIFIED
2. Proceed with normal PO creation workflow
3. Test end-to-end PO creation and submission

### **If Tests Fail** ❌:
1. Document exact error messages
2. Check browser console for details
3. Verify backend logs
4. Report findings for investigation

---

**Testing Guide Created**: 2025-12-23 21:15 IST  
**Expected Test Duration**: 10-15 minutes  
**Difficulty**: Easy

**Good luck with testing!** 🚀
