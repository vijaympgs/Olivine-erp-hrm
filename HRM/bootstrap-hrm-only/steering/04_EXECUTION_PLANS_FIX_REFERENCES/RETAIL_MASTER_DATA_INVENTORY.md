# COMPLETE RETAIL MASTER DATA LIST

**Purpose**: Comprehensive inventory of all master data pages in the Retail module requiring toolbar standardization  
**Date**: 2026-01-07 20:45 IST  
**Session**: Phase 4-5 Session 2 Planning

---

## 📊 **MASTER DATA CATEGORIES**

### **1. MERCHANDISING MASTERS** (Product Definition)

| Master | Path | Component | Template | Priority | Status |
|--------|------|-----------|----------|----------|--------|
| **Item Master** | `/inventory/item-master` | `ItemMasterSetup.tsx` | MST-M | HIGH | ⚠️ Needs Toolbar |
| **Attribute Definitions** | `/inventory/attributes` | `AttributeSetup.tsx` | MST-M | HIGH | ⚠️ Needs Toolbar |
| **Attribute Values** | `/inventory/attribute-values` | `AttributeValueSetup.tsx` | MST-S | MEDIUM | ⚠️ Needs Toolbar |
| **Attribute Templates** | `/inventory/attribute-templates` | `ProductAttributeTemplateSetup.tsx` | MST-M | MEDIUM | ⚠️ Needs Toolbar |
| **Price Lists** | `/inventory/price-lists` | `PriceListSetup.tsx` | MST-M | HIGH | ⚠️ Needs Toolbar |
| **Units of Measure (UOM)** | `/inventory/uoms` | `UOMSetup.tsx` | MST-S | HIGH | ⚠️ Needs Toolbar |

**Subtotal**: 6 masters

---

### **2. PARTNER MASTERS** (Customers & Suppliers)

| Master | Path | Component | Template | Priority | Status |
|--------|------|-----------|----------|----------|--------|
| **Customer Directory** | `/partners/customers` | `CustomerSetup.tsx` | MST-M | HIGH | ⚠️ Needs Toolbar |
| **Supplier/Vendor Directory** | `/partners/suppliers` | `SupplierSetup.tsx` | MST-M | HIGH | ⚠️ Needs Toolbar |
| **Customer Groups** | `/customers/groups` | `SimpleMasterSetup.tsx` | MST-S | MEDIUM | ⚠️ Needs Toolbar |
| **Loyalty Programs** | `/customers/loyalty` | `SimpleMasterSetup.tsx` | MST-S | MEDIUM | ⚠️ Needs Toolbar |

**Subtotal**: 4 masters

---

### **3. COMPANY & LOCATION MASTERS** (Organizational Structure)

| Master | Path | Component | Template | Priority | Status |
|--------|------|-----------|----------|----------|--------|
| **Company Settings** | `/setup/company` | `CompanySettings.tsx` | MST-M | HIGH | ⚠️ Needs Toolbar |
| **Location Setup** | `/setup/locations` | `LocationSetup.tsx` | MST-M | HIGH | ⚠️ Needs Toolbar |

**Subtotal**: 2 masters

---

### **4. CODE MASTERS** (Simple Masters via SimpleMasterSetup)

| Master | Path | Component | Template | Priority | Status |
|--------|------|-----------|----------|----------|--------|
| **Category** | `/setup/simple-masters` | `SimpleMasterSetup.tsx` | MST-S | HIGH | ⚠️ Needs Toolbar |
| **Brand** | `/setup/simple-masters` | `SimpleMasterSetup.tsx` | MST-S | HIGH | ⚠️ Needs Toolbar |
| **Tax Classes** | `/setup/simple-masters` | `SimpleMasterSetup.tsx` | MST-S | MEDIUM | ⚠️ Needs Toolbar |
| **Payment Methods** | `/setup/simple-masters` | `SimpleMasterSetup.tsx` | MST-S | MEDIUM | ⚠️ Needs Toolbar |

**Subtotal**: 4 masters (all use same component with dropdown selector)

---

### **5. INVENTORY CONFIGURATION MASTERS**

| Master | Path | Component | Template | Priority | Status |
|--------|------|-----------|----------|----------|--------|
| **Reason Codes** | `/inventory/adjustments/reason-codes` | `ReasonCodeListPage.tsx` | MST-S | MEDIUM | ⚠️ Needs Toolbar |
| **Reorder Policies** | `/inventory/reorder-policies` | `ReorderPolicyListPage.tsx` | MST-M | MEDIUM | ⚠️ Needs Toolbar |
| **Inventory Setup** | `/inventory/setup` | `InventorySetup.tsx` | CFG-M | MEDIUM | ⚠️ Needs Toolbar |

**Subtotal**: 3 masters

---

### **6. POS MASTERS**

| Master | Path | Component | Template | Priority | Status |
|--------|------|-----------|----------|----------|--------|
| **POS Terminals/Registers** | `/operations/pos/terminal-configuration` | TBD | MST-M | MEDIUM | ⚠️ Needs Toolbar |

**Subtotal**: 1 master

---

## 📈 **SUMMARY BY PRIORITY**

### **HIGH PRIORITY** (Must-Have Toolbars)
1. Item Master
2. Attribute Definitions
3. Price Lists
4. UOM
5. Customer Directory
6. Supplier Directory
7. Company Settings
8. Location Setup
9. Category (Code Masters)
10. Brand (Code Masters)

**Total**: 10 masters

---

### **MEDIUM PRIORITY** (Should-Have Toolbars)
1. Attribute Values
2. Attribute Templates
3. Customer Groups
4. Loyalty Programs
5. Tax Classes
6. Payment Methods
7. Reason Codes
8. Reorder Policies
9. Inventory Setup
10. POS Terminals

**Total**: 10 masters

---

## 🎯 **GRAND TOTAL: 20 MASTER DATA PAGES**

---

## 📋 **IMPLEMENTATION APPROACH**

### **Phase 1: Core Merchandising & Partners** (Session 2)
**Estimated Time**: 4-6 hours

**Targets**:
1. Item Master (`ItemMasterSetup.tsx`)
2. UOM (`UOMSetup.tsx`)
3. Customer Directory (`CustomerSetup.tsx`)
4. Supplier Directory (`SupplierSetup.tsx`)
5. SimpleMasterSetup (Category, Brand, Customer Groups, Loyalty, Tax, Payment Methods)

**Deliverable**: 5 unique components + 1 shared component = 6 implementations

---

### **Phase 2: Company, Location & Configuration** (Session 3)
**Estimated Time**: 3-4 hours

**Targets**:
1. Company Settings (`CompanySettings.tsx`)
2. Location Setup (`LocationSetup.tsx`)
3. Attribute Definitions (`AttributeSetup.tsx`)
4. Attribute Values (`AttributeValueSetup.tsx`)
5. Attribute Templates (`ProductAttributeTemplateSetup.tsx`)
6. Price Lists (`PriceListSetup.tsx`)

**Deliverable**: 6 implementations

---

### **Phase 3: Inventory Config & POS** (Session 4)
**Estimated Time**: 2-3 hours

**Targets**:
1. Reason Codes (`ReasonCodeListPage.tsx`)
2. Reorder Policies (`ReorderPolicyListPage.tsx`)
3. Inventory Setup (`InventorySetup.tsx`)
4. POS Terminals (TBD)

**Deliverable**: 4 implementations

---

## 🔧 **TOOLBAR SPECIFICATION FOR MASTERS**

### **Standard Master Toolbar Actions**:
- **F1**: New (create new record)
- **F2**: Save (save current record)
- **F3**: Delete (delete selected record)
- **F4**: Refresh (reload data)
- **F5**: Export (export to Excel/CSV)
- **F6**: Import (import from Excel/CSV)
- **F7**: Search (focus search box)
- **F8**: Filter (toggle filter panel)
- **ESC**: Cancel/Close

### **Component Design**:
- Create `MasterToolbar` component (or adapt `TransactionToolbar`)
- Consistent visual styling with existing toolbars
- Status-based disabled actions
- Sticky positioning at top

---

## ✅ **SUCCESS CRITERIA**

**Phase 4-5 will be COMPLETE when**:
- ✅ All 20 master data pages have standardized toolbars
- ✅ Keyboard shortcuts work consistently (F1-F12)
- ✅ Visual consistency across all masters
- ✅ All implementations follow `18_WIRING_CHECKLISTS/MASTER_DATA_WIRING.md`
- ✅ Documentation updated

---

**Next Session**: Start with Phase 1 (Core Merchandising & Partners) - 5 unique components + SimpleMasterSetup
