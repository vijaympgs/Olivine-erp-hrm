# 📊 DATABASE SEED SCRIPTS ANALYSIS

**Date**: 2026-01-09 20:32 IST  
**Purpose**: Analysis of all seed scripts and correct execution order  
**Status**: ✅ COMPLETE

---

## 🔍 **SEED SCRIPTS FOUND**

### **Core/Essential Scripts** (Must Run):

1. **`seed_default_roles.py`**
   - Location: `core/auth_access/backend/user_management/management/commands/`
   - Purpose: Creates default user roles (Admin, BackOffice Manager, POS Manager, etc.)
   - Dependencies: None
   - **Run Order**: #1

2. **`seed_default_users.py`**
   - Location: `core/auth_access/backend/user_management/management/commands/`
   - Purpose: Creates test users with roles
   - Users: admin, boadmin, bouser, posadmin, posuser
   - Dependencies: Roles must exist
   - **Run Order**: #2

3. **`seed_data.py`**
   - Location: `core/org_structure/backend/company/management/commands/`
   - Purpose: **MAIN DATA SEED** - Creates:
     - Company (Mindra Retail Pvt Ltd)
     - Locations (5: HQ, Warehouse, 2 Stores, Online)
     - Attributes (10: Color, Size, Material, etc.)
     - Attribute Values (50+)
     - UOMs (10: PCS, KG, GM, MTR, etc.)
     - Items (3 with variants)
     - Customers (5)
     - Suppliers (5)
     - Terminals (3)
     - Price Lists
   - Dependencies: None
   - **Run Order**: #3

4. **`seed_masters.py`**
   - Location: `core/org_structure/backend/company/management/commands/`
   - Purpose: Creates:
     - Categories (~30 hierarchical)
     - Brands (~20)
   - Dependencies: Company must exist
   - **Run Order**: #4

5. **`seed_retail_menu_items.py`**
   - Location: `core/auth_access/backend/user_management/management/commands/`
   - Purpose: Creates ERPMenuItem entries (toolbar configs)
   - Dependencies: None
   - **Run Order**: #5

6. **`seed_toolbar_controls.py`**
   - Location: `backend/scripts/`
   - Purpose: Seeds toolbar control configurations
   - Dependencies: Menu items must exist
   - **Run Order**: #6

---

## ✅ **CORRECT EXECUTION ORDER**

```powershell
# 1. Reset database
Remove-Item backend\db.sqlite3
python backend\manage.py migrate

# 2. Create superuser
python backend\manage.py createsuperuser

# 3. Seed in order
python backend\manage.py seed_default_roles
python backend\manage.py seed_default_users
python backend\manage.py seed_data
python backend\manage.py seed_masters
python backend\manage.py seed_retail_menu_items
python backend\scripts\seed_toolbar_controls.py
```

---

## 📦 **WHAT GETS CREATED**

### **From `seed_data.py`**:
- ✅ 1 Company (Mindra Retail Pvt Ltd)
- ✅ 5 Locations (HQ, WH-BLR, STR-MG, STR-IND, ONLINE)
- ✅ 10 Attributes (COLOR, SIZE, MATERIAL, BRAND, etc.)
- ✅ 50+ Attribute Values
- ✅ 10 UOMs (PCS, KG, GM, MTR, CM, LTR, ML, BOX, PACK, PAIR)
- ✅ 3 Items with variants:
  - TSH-001: Cotton T-Shirt (4 variants)
  - JNS-001: Slim Jeans (3 variants)
  - SHT-001: Formal Shirt (2 variants)
- ✅ 5 Customers
- ✅ 5 Suppliers
- ✅ 3 Terminals
- ✅ 1 Price List with prices for all variants

### **From `seed_masters.py`**:
- ✅ ~30 Categories (hierarchical)
  - Level 1: Apparel, Electronics, Home, Food
  - Level 2: Men's Wear, Women's Wear, Mobile, Furniture, etc.
  - Level 3: Shirts, T-Shirts, Jeans, Smartphones, etc.
- ✅ ~20 Brands (Nike, Adidas, Samsung, Apple, etc.)

### **From `seed_default_users.py`**:
- ✅ admin / admin123 (System Administrator)
- ✅ boadmin / boadmin123 (Back Office Manager)
- ✅ bouser / bouser123 (Back Office User)
- ✅ posadmin / posadmin123 (POS Manager)
- ✅ posuser / posuser123 (POS User)

---

## 🚀 **AUTOMATED SCRIPT CREATED**

**File**: `scripts/reset_and_seed_database.ps1`

**What it does**:
1. ✅ Backs up existing database
2. ✅ Deletes old database
3. ✅ Runs migrations
4. ✅ Creates superuser
5. ✅ Seeds all data in correct order
6. ✅ Shows summary

**How to run**:
```powershell
cd c:\00mindra\olivine-erp-platform
.\scripts\reset_and_seed_database.ps1
```

---

## 📊 **EXPECTED RESULT**

After running the script, you should have:

### **Database Tables**:
- ✅ All migrations applied
- ✅ All tables created
- ✅ No missing table errors

### **Demo Data**:
- ✅ 1 Company
- ✅ 5 Locations
- ✅ 10 UOMs
- ✅ 3 Items (9 variants total)
- ✅ 5 Customers
- ✅ 5 Suppliers
- ✅ ~30 Categories
- ✅ ~20 Brands
- ✅ 5 Test users

### **Toolbar Configs**:
- ✅ ERPMenuItem entries for all screens
- ✅ Toolbar control configurations
- ✅ UOM Setup: `INVENTORY_UOM_SETUP` / `NESCKVDXRQF`
- ✅ Purchase Orders: `PURCHASE_ORDERS` / `NESCKZTJAVPMRDX1234QF`

---

## 🧪 **TESTING AFTER SEED**

### **Test 1: Django Admin**
```
URL: http://localhost:8000/admin/
Login: admin / admin123
Check: Company, Locations, UOMs, Items, Customers, Suppliers
```

### **Test 2: UOM Setup**
```
URL: http://localhost:3000/inventory/uoms
Expected: List of 10 UOMs
Toolbar: Should show VIEW mode buttons only
```

### **Test 3: Purchase Orders**
```
URL: http://localhost:3000/procurement/purchase-orders
Expected: Empty list (no POs yet)
Toolbar: Should show VIEW mode buttons only
```

### **Test 4: Item Master**
```
URL: http://localhost:3000/inventory/items
Expected: List of 3 items with 9 variants
Toolbar: Should show VIEW mode buttons only
```

---

## ⚠️ **IMPORTANT NOTES**

1. **Duplicate Paths**: There are duplicate seed files in multiple locations:
   - `core/auth-access/` vs `core/auth_access/`
   - `core/org-structure/` vs `core/org_structure/`
   - `frontend/core/` copies
   
   **Use**: The ones in `core/` (without `frontend/` prefix)

2. **Empty Scripts**: `backend/scripts/seed_demo_data.py` is empty - ignore it

3. **Order Matters**: Must run in the order specified above

4. **Superuser**: Script creates `admin/admin123` automatically

---

## 🎯 **NEXT STEPS**

1. **Run the script**:
   ```powershell
   .\scripts\reset_and_seed_database.ps1
   ```

2. **Start Django server**:
   ```powershell
   python backend\manage.py runserver
   ```

3. **Start frontend**:
   ```powershell
   cd frontend
   npm run dev
   ```

4. **Test UOM page**:
   - Navigate to `/inventory/uoms`
   - Test toolbar buttons
   - Test CREATE mode (click New)
   - Verify Exit button is hidden in CREATE mode

5. **Test Purchase Orders**:
   - Navigate to `/procurement/purchase-orders`
   - Test toolbar buttons

---

**Status**: ✅ ANALYSIS COMPLETE  
**Script**: ✅ READY TO RUN  
**Next**: Run `reset_and_seed_database.ps1`
