# 📋 TOOLBAR CONFIG UPDATE GUIDE FOR DJANGO ADMIN

**Admin URL**: http://localhost:8000/admin/toolbar_control/toolbaritemproxy/

**Instructions**: Use the inline editing feature to update the "Applicable toolbar config" column

---

## 🎯 PRIORITY UPDATES (Fix These First)

### **Inventory Module**

| Item Name | Current Config | Correct Config | Type |
|-----------|----------------|----------------|------|
| **UOM Setup** (Master Data) | `NESCKVDXRQF` | `NESCKVDXRQF` | ✅ CORRECT |
| **Units of Measure** (List View) | `NESCKVDXRQFX` | `NESCKVDXRQF` | ❌ Remove X |
| **Unit of Measure Setup** (List View) | `NRQFX` | `NESCKVDXRQF` | ❌ Incomplete |
| **Item Master** (Master Data) | `NESCKVDXRQFZTJAHO` | `NESCKVDXRQFIO` | ❌ Wrong - should be Masters Advanced |
| **Item Master** (List View) | `NESCKVDXRQFZTJAHO` | `NESCKVDXRQFIO` | ❌ Wrong |

### **Procurement Module**

| Item Name | Current Config | Correct Config | Type |
|-----------|----------------|----------------|------|
| **Purchase Orders** (Transaction) | `NESCKPVDXRTJZ` | `NESCKZTJAVPMRDX1234QF` | ❌ Incomplete |
| **Purchase Orders** (List View) | `NESCKVDXRQFZTJAHO` | `NESCKZTJAVPMRDX1234QF` | ❌ Wrong |

---

## 📖 STANDARD CONFIGURATIONS REFERENCE

### **Masters (Simple)** - `NESCKVDXRQF`
**Use For**: UOM, Brands, Categories, Tax Classes, Reason Codes

**Characters**:
- N = New (F2)
- E = Edit (F3)
- S = Save (F8)
- C = Cancel (Esc)
- K = Clear (F5)
- V = View (F7)
- D = Delete (F4)
- X = Exit (Esc)
- R = Refresh (F9)
- Q = Search (Ctrl+F)
- F = Filter (Alt+F)

---

### **Masters (Advanced)** - `NESCKVDXRQFIO`
**Use For**: Item Master, Customer Master, Supplier Master

**All from Masters (Simple) PLUS**:
- I = Import (Ctrl+I)
- O = Export (Ctrl+E)

---

### **Transactions** - `NESCKZTJAVPMRDX1234QF`
**Use For**: Purchase Orders, Sales Orders, Invoices

**Characters**:
- N = New (F2)
- E = Edit (F3)
- S = Save (F8)
- C = Cancel (Esc)
- K = Clear (F5)
- Z = Authorize (F10)
- T = Submit (Alt+S)
- J = Reject (Alt+R)
- A = Amend (Alt+A)
- V = View (F7)
- P = Print (Ctrl+P)
- M = Email (Ctrl+M)
- R = Refresh (F9)
- D = Delete (F4)
- X = Exit (Esc)
- 1 = First (Home)
- 2 = Prev (PgUp)
- 3 = Next (PgDn)
- 4 = Last (End)
- Q = Search (Ctrl+F)
- F = Filter (Alt+F)

---

### **Transactions (Simple)** - `NESCKVDXRQF`
**Use For**: Stock Adjustments, Stock Transfers (no approval workflow)

**Same as Masters (Simple)**

---

### **Reports** - `VRXPYQFG`
**Use For**: Stock Valuation, Sales Analysis, Aging Reports

**Characters**:
- V = View (F7)
- R = Refresh (F9)
- X = Exit (Esc)
- P = Print (Ctrl+P)
- Y = Export (Ctrl+E)
- Q = Search (Ctrl+F)
- F = Filter (Alt+F)
- G = Settings (Alt+O)

---

### **Configuration** - `ESCKXR`
**Use For**: Company Settings, System Parameters

**Characters**:
- E = Edit (F3)
- S = Save (F8)
- C = Cancel (Esc)
- K = Clear (F5)
- X = Exit (Esc)
- R = Refresh (F9)

---

## 🔧 HOW TO UPDATE IN ADMIN

1. **Search for the item** using the search box
2. **Click in the "Applicable toolbar config" field**
3. **Clear the current value**
4. **Copy-paste the correct config** from this guide
5. **Click "Save" button** at the bottom of the page
6. **Verify** the change was saved

---

## ✅ VERIFICATION CHECKLIST

After updating, verify these screens work correctly:

### **UOM Setup**:
- [ ] VIEW mode shows: New, Edit, View, Delete, Refresh, Search, Filter, Exit
- [ ] CREATE mode shows: Save, Cancel, Clear, Exit
- [ ] Config string: `NESCKVDXRQF`

### **Item Master**:
- [ ] VIEW mode includes Import and Export buttons
- [ ] Config string: `NESCKVDXRQFIO`

### **Purchase Order**:
- [ ] VIEW mode shows workflow buttons (Authorize, Submit, Reject, Amend)
- [ ] VIEW mode shows navigation (First, Prev, Next, Last)
- [ ] Config string: `NESCKZTJAVPMRDX1234QF`

---

## 📊 COMPLETE RETAIL MODULE CONFIG MAP

| Screen | View Type | Config String |
|--------|-----------|---------------|
| **UOM Setup** | Master Data | `NESCKVDXRQF` |
| **Reason Codes** | Master Data | `NESCKVDXRQF` |
| **Categories** | Master Data | `NESCKVDXRQF` |
| **Brands** | Master Data | `NESCKVDXRQF` |
| **Attributes** | Master Data | `NESCKVDXRQF` |
| **Item Master** | Master Data | `NESCKVDXRQFIO` |
| **Customer Master** | Master Data | `NESCKVDXRQFIO` |
| **Supplier Master** | Master Data | `NESCKVDXRQFIO` |
| **Stock Movement** | Transaction | `NESCKVDXRQF` |
| **Stock Adjustment** | Transaction | `NESCKVDXRQF` |
| **Stock Transfer** | Transaction | `NESCKVDXRQF` |
| **Purchase Requisition** | Transaction | `NESCKZTJAVPMRDX1234QF` |
| **Purchase Order** | Transaction | `NESCKZTJAVPMRDX1234QF` |
| **Sales Order** | Transaction | `NESCKZTJAVPMRDX1234QF` |
| **Sales Invoice** | Transaction | `NESCKZTJAVPMRDX1234QF` |
| **Stock Valuation** | Report | `VRXPYQFG` |
| **Sales Analysis** | Report | `VRXPYQFG` |
| **Company Settings** | Configuration | `ESCKXR` |

---

**Last Updated**: 2026-01-09 17:54 IST  
**Reference**: `.steering/20TOOLBAR_ROLLOUT/01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md`
