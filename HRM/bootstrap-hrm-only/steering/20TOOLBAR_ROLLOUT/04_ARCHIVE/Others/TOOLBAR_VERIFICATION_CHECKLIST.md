# ✅ TOOLBAR CONFIG VERIFICATION CHECKLIST

**Admin URL**: http://localhost:8000/admin/toolbar_control/toolbaritemproxy/  
**Date**: 2026-01-09  
**Status**: Ready for Manual Update

---

## 🎯 CRITICAL UPDATES NEEDED

### **Step 1: Search and Update UOM Entries**

Search: `UOM`

| Current Entry | Current Config | ✅ Correct Config | Action |
|---------------|----------------|-------------------|---------|
| **inventory_uom_setup** | `NESCKVDXRQF` | `NESCKVDXRQF` | ✅ NO CHANGE |
| **uom** | `NESCKVDXRQFX` | `NESCKVDXRQF` | ❌ Remove X |
| **UOM_SETUP** | `NRQFX` | `NESCKVDXRQF` | ❌ Add NESCKV |

**How to Update**:
1. Search "UOM" in admin
2. Find entry with config `NESCKVDXRQFX`
3. Click in config field, change to `NESCKVDXRQF`
4. Find entry with config `NRQFX`
5. Click in config field, change to `NESCKVDXRQF`
6. Click "Save" at bottom

---

### **Step 2: Update Item Master**

Search: `Item Master`

| Current Entry | Current Config | ✅ Correct Config | Action |
|---------------|----------------|-------------------|---------|
| **ITEM_MASTER** | `NESCKVDXRQFX` | `NESCKVDXRQFIO` | ❌ Change X to IO |
| **item-master** | `NESCKVDXRQFX` | `NESCKVDXRQFIO` | ❌ Change X to IO |

**How to Update**:
1. Search "Item Master" in admin
2. For each entry, change `NESCKVDXRQFX` to `NESCKVDXRQFIO`
3. Click "Save"

---

### **Step 3: Update Purchase Orders**

Search: `Purchase Order`

| Current Entry | Current Config | ✅ Correct Config | Action |
|---------------|----------------|-------------------|---------|
| **PURCHASE_ORDERS** | `NESCKPVDXRTJZ` | `NESCKZTJAVPMRDX1234QF` | ❌ REPLACE ENTIRE STRING |
| **purchase-orders** | `NESCKVDXRQFZTJAHO` | `NESCKZTJAVPMRDX1234QF` | ❌ REPLACE ENTIRE STRING |

**How to Update**:
1. Search "Purchase Order" in admin
2. For each entry, clear the field
3. Copy-paste: `NESCKZTJAVPMRDX1234QF`
4. Click "Save"

---

### **Step 4: Update Purchase Requisitions**

Search: `Purchase Requisition`

| Current Entry | Current Config | ✅ Correct Config | Action |
|---------------|----------------|-------------------|---------|
| **PURCHASE_REQUISITIONS** | `NESCKPVDXRTJZ` | `NESCKZTJAVPMRDX1234QF` | ❌ REPLACE ENTIRE STRING |
| **requisitions** | `NESCKVDXRQFZTJAHO` | `NESCKZTJAVPMRDX1234QF` | ❌ REPLACE ENTIRE STRING |

**How to Update**:
1. Search "Purchase Requisition" in admin
2. For each entry, clear the field
3. Copy-paste: `NESCKZTJAVPMRDX1234QF`
4. Click "Save"

---

### **Step 5: Update Customer Master**

Search: `Customer`

| Current Entry | Current Config | ✅ Correct Config | Action |
|---------------|----------------|-------------------|---------|
| **CUSTOMER_MASTER** | `NESCKVDXRQFX` | `NESCKVDXRQFIO` | ❌ Change X to IO |

**How to Update**:
1. Search "Customer" in admin
2. Change `NESCKVDXRQFX` to `NESCKVDXRQFIO`
3. Click "Save"

---

### **Step 6: Update Supplier Master**

Search: `Supplier`

| Current Entry | Current Config | ✅ Correct Config | Action |
|---------------|----------------|-------------------|---------|
| **SUPPLIER_MASTER** | `NESCKVDXRQFX` | `NESCKVDXRQFIO` | ❌ Change X to IO |
| **suppliers** | `NESCKVDXRQFIO` | `NESCKVDXRQFIO` | ✅ NO CHANGE |

**How to Update**:
1. Search "Supplier" in admin
2. Change `NESCKVDXRQFX` to `NESCKVDXRQFIO`
3. Click "Save"

---

### **Step 7: Update Sales Orders**

Search: `Sales Order`

| Current Entry | Current Config | ✅ Correct Config | Action |
|---------------|----------------|-------------------|---------|
| **SALES_ORDERS** | `NESCKPVDXRTJZ` | `NESCKZTJAVPMRDX1234QF` | ❌ REPLACE ENTIRE STRING |
| **orders** (Sales) | `NESCKVDXRQFZTJAHO` | `NESCKZTJAVPMRDX1234QF` | ❌ REPLACE ENTIRE STRING |

**How to Update**:
1. Search "Sales Order" in admin
2. For each entry, clear the field
3. Copy-paste: `NESCKZTJAVPMRDX1234QF`
4. Click "Save"

---

### **Step 8: Update Sales Invoices**

Search: `Sales Invoice`

| Current Entry | Current Config | ✅ Correct Config | Action |
|---------------|----------------|-------------------|---------|
| **SALES_INVOICES** | `NESCKPVDXRTJZ` | `NESCKZTJAVPMRDX1234QF` | ❌ REPLACE ENTIRE STRING |
| **invoices** (Sales) | `NESCKVDXRQFZTJAHO` | `NESCKZTJAVPMRDX1234QF` | ❌ REPLACE ENTIRE STRING |

**How to Update**:
1. Search "Sales Invoice" in admin
2. For each entry, clear the field
3. Copy-paste: `NESCKZTJAVPMRDX1234QF`
4. Click "Save"

---

## 📋 QUICK REFERENCE: CONFIG STRINGS TO COPY

```
Masters (Simple):        NESCKVDXRQF
Masters (Advanced):      NESCKVDXRQFIO
Transactions:            NESCKZTJAVPMRDX1234QF
Reports:                 VRXPYQFG
Configuration:           ESCKXR
```

---

## ✅ VERIFICATION AFTER UPDATE

After updating each section, verify in the toolbar explorer:

1. Open: `.steering/20TOOLBAR_ROLLOUT/01_ESSENTIAL/toolbar-explorer.html`
2. Click the screen you just updated
3. Verify the config string matches
4. Click VIEW Mode card - check buttons
5. Click CREATE Mode card - check buttons

---

## 🎯 COMPLETION CHECKLIST

- [ ] Step 1: UOM entries updated
- [ ] Step 2: Item Master updated
- [ ] Step 3: Purchase Orders updated
- [ ] Step 4: Purchase Requisitions updated
- [ ] Step 5: Customer Master updated
- [ ] Step 6: Supplier Master updated
- [ ] Step 7: Sales Orders updated
- [ ] Step 8: Sales Invoices updated
- [ ] All changes saved in admin
- [ ] Verified in toolbar explorer
- [ ] Tested in actual UOM page (http://localhost:5173/inventory/uoms)

---

**Estimated Time**: 10-15 minutes  
**Priority**: HIGH - Required for toolbar consistency

**Last Updated**: 2026-01-09 17:58 IST
