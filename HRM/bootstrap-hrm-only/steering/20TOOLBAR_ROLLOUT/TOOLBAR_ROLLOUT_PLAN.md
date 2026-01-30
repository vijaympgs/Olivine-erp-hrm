# 🚀 **TOOLBAR ROLLOUT - MASTER IMPLEMENTATION PLAN**

**Objective**: Apply backend-driven toolbar to all Retail screens  
**Last Updated**: 2026-01-10 15:20 IST  
**Status**: Phase 2 In Progress - Item Master Implementation COMPLETE ✅  
**Owner**: Astra (Antigravity Engineering Agent)

---

## 📚 **QUICK NAVIGATION**

- **New to this project?** → Read `README.md` first
- **Need examples?** → See Gold Standard Examples section below
- **Ready to implement?** → Jump to your phase below
- **Need reference?** → Check `01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md`

---

## ✅ **PHASE 0: ARCHITECTURE & DOCUMENTATION** (COMPLETE)

### **Critical Foundation Work** - 2026-01-09
- **Status**: ✅ **COMPLETE**
- **Duration**: 2 hours

**Deliverables**:
1. ✅ **Architecture Clarification**
   - Established single-entry-per-screen rule
   - Removed "List View" entries from ERPMenuItem
   - Documented that list pages use `mode="VIEW"` with parent config
   
2. ✅ **Comprehensive Documentation**
   - `01_ESSENTIAL/ARCHITECTURE_CLARIFICATION.md` - Single-entry-per-screen explained
   - `01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md` - Character codes reference
   - `02_REFERENCE/MODE_BASED_FILTERING_TECHNICAL_REFERENCE.md` - How component filters buttons
   - `01_ESSENTIAL/BENCHMARK_STABILIZATION_COMPLETE.md` - Final verified state

3. ✅ **Backend Registry Cleanup**
   - All "List View" entries removed
   - Each screen has exactly ONE ERPMenuItem entry
   - Full config strings set for all screens

**Key Principle Established**:
> **One screen = One ERPMenuItem entry**  
> Frontend handles list vs form via `mode` prop, not separate database entries

---

## ✅ **PHASE 1: BENCHMARK STABILIZATION** (COMPLETE)

### **1.1 UOM Setup** - Simple Master Benchmark ✅
- **Status**: ✅ **STABILIZED & DOCUMENTED**
- **Config**: `NESCKVDXRQF` (11 characters)
- **menu_id**: `INVENTORY_UOM_SETUP`
- **view_type**: `MASTER`
- **Frontend**: `retail/frontend/inventory/pages/UOMSetup.tsx`
- **Documentation**: `04_ARCHIVE/UOM/` + Main folder manual (if exists)

**Features Verified**:
- ✅ Backend-driven toolbar (no hardcoded allowedActions)
- ✅ Mode-based visibility (buttons hidden, not disabled)
- ✅ In-place form swap (list ↔ form)
- ✅ Selection-first architecture (Edit/View/Delete require selection)
- ✅ Decoupled scrolling (fixed header, scrollable content)
- ✅ Surgical spacing (one-line gaps)
- ✅ Read-only view mode (all fields disabled)
- ✅ Filter panel toggle working
- ✅ Import/Export placeholders ready
- ✅ Exit navigation functional
- ✅ All keyboard shortcuts working (F2, F3, F5, F7, F8, ESC)
- ✅ VIEW mode: Shows 8 buttons (N, E, V, D, X, R, Q, F)
- ✅ CREATE mode: Shows 4 buttons (S, C, K, X)
- ✅ EDIT mode: Shows 4 buttons (S, C, K, X)
- ✅ VIEW_FORM mode: Shows 1 button (X)

**Use UOM as Gold Standard For**:
- Simple Master screens (single entity, no complex relationships)
- In-place form pattern
- Selection-first architecture
- Decoupled scrolling
- Read-only view mode

---

### **1.2 Purchase Order List** - Transaction Benchmark ✅
- **Status**: ✅ **STABILIZED**
- **Config**: `NESCKZTJAVPMRDX1234QF` (21 characters)
- **menu_id**: `PURCHASE_ORDERS`
- **view_type**: `TRANSACTION`
- **Frontend**: `retail/frontend/procurement/pages/PurchaseOrderListPage.tsx`

**Features Verified**:
- ✅ Hardcoded allowedActions removed
- ✅ Fully backend-driven
- ✅ List page uses `mode="VIEW"`
- ✅ VIEW mode: Shows 18 buttons
- ✅ CREATE mode: Shows 4 buttons (S, C, K, X)
- ✅ Workflow actions (Submit, Authorize, Reject)
- ✅ Document navigation (First, Prev, Next, Last)

**Use PO as Gold Standard For**:
- Transaction screens with workflow
- Document navigation
- Status-based button enabling
- Print/Email functionality

---

## 🚧 **PHASE 2: MASTER DATA ROLLOUT** (IN PROGRESS)

### **2A. CORE BUSINESS MASTERS** (P0 - Critical)

#### **2A.1 Item Master** - Complex Master 🚧
- **Status**: ✅ **IMPLEMENTED (Pending QA)**
- **Config**: `NESCKVDXRQFIO` (13 characters)
- **menu_id**: `ITEM_MASTER`
- **view_type**: `MASTER`
- **Frontend**: `retail/frontend/inventory/pages/ItemMasterSetup.tsx`
- **Documentation**: `04_ARCHIVE/Item/` (7 comprehensive documents)
- **Estimate**: 3-4 hours

**⚠️ CRITICAL ARCHITECTURAL CHANGE REQUIRED**:
Current implementation uses **MODAL/SLIDING WINDOW** pattern (`ItemModalWithVariants`).  
This is **INCOMPATIBLE** with toolbar architecture.

**Required Changes**:
1. ❌ **Remove**: `ItemModalWithVariants` component
2. ✅ **Create**: `ItemForm` component (in-place rendering)
3. ✅ **Implement**: In-place swap pattern (like UOM)
4. ✅ **Add**: Form ref for toolbar control
5. ✅ **Add**: Read-only view mode

**Documentation Package** (2,500 lines):
- `04_ARCHIVE/Item/ITEM_MASTER_INDEX.md` - Master navigation
- `04_ARCHIVE/Item/ITEM_MASTER_CRITICAL_ARCHITECTURAL_CHANGE.md` - **READ THIS FIRST**
- `04_ARCHIVE/Item/ITEM_MASTER_IMPLEMENTATION_GUIDE.md` - Step-by-step coding
- `04_ARCHIVE/Item/ITEM_MASTER_IMPLEMENTATION_CHECKLIST.md` - Comprehensive QA
- `04_ARCHIVE/Item/ITEM_MASTER_VISUAL_ARCHITECTURE.md` - Visual diagrams
- `04_ARCHIVE/Item/ITEM_MASTER_DELIVERABLES_SUMMARY.md` - Executive summary
- `04_ARCHIVE/Item/README.md` - Archive index

**Implementation Steps**:
1. **Read**: `04_ARCHIVE/Item/ITEM_MASTER_CRITICAL_ARCHITECTURAL_CHANGE.md` (15 min)
2. **Review**: `04_ARCHIVE/Item/ITEM_MASTER_IMPLEMENTATION_GUIDE.md` (15 min)
3. **Implement**: Follow 10-step guide (2-3 hours)
4. **Verify**: Use `04_ARCHIVE/Item/ITEM_MASTER_IMPLEMENTATION_CHECKLIST.md` (1 hour)

**Priority**: 🔴 **P0 - CRITICAL**

---

#### **2A.2 Customer Master** - Complex Master 🚧
- **Status**: ✅ **IMPLEMENTED (Pending QA)**
- **Config**: `NESCKVDXRQFIO` (13 characters)
- **menu_id**: `CUSTOMER_MASTER`
- **view_type**: `MASTER`
- **Estimate**: 2-3 hours

**Implementation Approach**:
- Use Item Master as template (similar complexity)
- Check if current implementation uses modal pattern
- If yes, apply same architectural change (modal → in-place swap)
- Follow Item Master implementation guide
- May include: Contact details, Credit limits, Payment terms, Addresses

**Priority**: 🔴 **P0 - CRITICAL**

---

#### **2A.3 Supplier Master** - Complex Master 🚧
- **Status**: ✅ **IMPLEMENTED (Pending QA)**
- **Config**: `NESCKVDXRQFIO` (13 characters)
- **menu_id**: `SUPPLIER_MASTER`
- **view_type**: `MASTER`
- **Estimate**: 2-3 hours

**Implementation Approach**:
- Use Item Master as template (similar complexity)
- Check if current implementation uses modal pattern
- If yes, apply same architectural change (modal → in-place swap)
- Follow Item Master implementation guide
- May include: Contact details, Payment terms, Tax details, Addresses

**Priority**: 🔴 **P0 - CRITICAL**

---

### **2B. ORGANIZATIONAL MASTERS** (P0 - Critical)

#### **2B.1 Company Master** - Configuration Master 🚧
- **Status**: ✅ **IMPLEMENTED (Pending QA)**
- **Config**: `NESCKVDXRQFIO` (13 characters) - Enabled New/Delete/Import/Export
- **menu_id**: `COMPANY`
- **view_type**: `MASTER`
- **Estimate**: 2 hours

**Special Considerations**:
- **Platform Only**: Can only be created/modified by Platform Superusers
- **No New/Delete**: Only Edit existing companies
- **Governance Flag**: This is a governance control, not licensing
- **Fields**: Company Name, Legal Name, Tax ID, Address, Logo, Settings

**Implementation Approach**:
- Different from standard masters (Edit-only mode)
- No "New" button (companies created via admin panel)
- No "Delete" button (deactivation only via admin)
- Focus on Edit, Save, Cancel, Clear, Exit, Refresh
- May need special permission checks

**Config Breakdown**:
- E = Edit (only action for selecting company)
- S = Save
- C = Cancel
- K = Clear
- X = Exit
- R = Refresh

**Priority**: 🔴 **P0 - CRITICAL**

---

#### **2B.2 Location Master** - Standard Master 🚧
- **Status**: ✅ **IMPLEMENTED (Pending QA)**
- **Config**: `NESCKVDXRQFIO` (13 characters) - Complete Master Data set
- **menu_id**: `LOCATIONS_SETUP`
- **view_type**: `MASTER`
- **Estimate**: 1.5 hours

**Implementation Approach**:
- Use UOM as template (simple master)
- Child of Company (belongs to one company)
- Fields: Location Code, Name, Type (Warehouse, Store, Office), Address, Active
- Standard CRUD operations

**Priority**: 🔴 **P0 - CRITICAL**

---

### **2C. ATTRIBUTE & CLASSIFICATION MASTERS** (P1 - High)

#### **2C.1 Attributes Master** - Standard Master ✅
- **Status**: ✅ **IMPLEMENTED (Pending QA)**
- **Config**: `NESCKVDXRQF` (11 characters)
- **menu_id**: `ATTRIBUTES`
- **view_type**: `MASTER`
- **Estimate**: 1.5 hours

**Implementation Approach**:
- Use UOM as template (simple master)
- Defines attribute definitions (e.g., "Color", "Size", "Material")
- Fields: Attribute Code, Name, Data Type (Text, Number, List), Required, Active
- Used by Item Master for variant attributes

**Priority**: 🟡 **P1 - HIGH**

---

#### **2C.2 Attribute Values Master** - Standard Master ✅
- **Status**: ✅ **IMPLEMENTED (Pending QA)**
- **Config**: `NESCKVDXRQF` (11 characters)
- **menu_id**: `ATTRIBUTE_VALUES`
- **view_type**: `MASTER`
- **Estimate**: 1.5 hours

**Implementation Approach**:
- Use UOM as template (simple master)
- Child of Attributes (belongs to one attribute)
- Defines possible values for list-type attributes
- Fields: Attribute (parent), Value Code, Value Name, Sort Order, Active
- Example: Attribute="Color", Values=["Red", "Blue", "Green"]

**Priority**: 🟡 **P1 - HIGH**

---

#### **2C.3 Product Attribute Templates** - Configuration Screen ✅
- **Status**: ✅ **IMPLEMENTED (Pending QA)**
- **Config**: `NESCKXR` (7 characters)
- **menu_id**: `ATTRIBUTE_TEMPLATES`
- **view_type**: `CONFIGURATION`
- **Estimate**: 1 hour

**Implementation Approach**:
- Toolbar-only pattern (no manual buttons)
- Modal-based form (existing pattern preserved)
- Mode switching (VIEW/CREATE/EDIT)
- Fields: Company, Code, Name, Mode, Version, Lines, Active
- All toolbar actions wired: Edit, Save, Cancel, Clear, Exit, Refresh

**Priority**: 🟡 **P1 - HIGH**

---


### **2E. LOOKUP MASTERS (P2 - Medium)**

#### **Simple Masters List** ⏸️
- **Config**: `NESCKVDXRQF` (11 characters) for all
- **Template**: Use UOM as exact template
- **Estimate**: 1 hour each

| Screen | menu_id | Status | Priority |
|--------|---------|--------|----------|
| **UOM Setup** | `INVENTORY_UOM_SETUP` | ✅ COMPLETE | - |
| **Reason Codes** | `REASON_CODES` | ✅ COMPLETE | - |
| **Brands** | `BRANDS` | ⏸️ PENDING | P2 |
| **Tax Codes** | `TAX_CODES` | ⏸️ PENDING | P2 |
| **Payment Terms** | `PAYMENT_TERMS` | ⏸️ PENDING | P2 |
| **Warehouses** | `WAREHOUSES` | ⏸️ PENDING | P2 |
| **Units** | `UNITS` | ⏸️ PENDING | P2 |

---

---

## 📊 **PHASE 2 SUMMARY**

### **Total Screens in Phase 2**: 18 screens

| Category | Screens | Estimate | Priority |
|----------|---------|----------|----------|
| **2A. Core Business** | 3 (Item, Customer, Supplier) | 8-10h | P0 |
| **2B. Organizational** | 2 (Company, Location) | 3-4h | P0 |
| **2C. Attributes** | 3 (Attributes, Values, Code) | 4-5h | P1 |
| **2D. Categories** | 1 (Product Categories) | 1.5h | P1 |
| **2E. Lookups** | 7 (Tax, Payment, etc.) | 7h | P2 |
| **TOTAL** | **16 screens** | **23-28h** | - |

### **Completed**: 3 screens (17%)
- ✅ UOM Setup
- ✅ Reason Codes
- ✅ Categories

### **In Progress**: 1 screen (6%)
- 🚧 Item Master (documentation complete)

### **Pending**: 11 screens (69%)
- Customer, Supplier (P0)
- Company, Location (P0)
- Attributes, Attribute Values, Code Master (P1)
- 7 simple lookups (P2)

---

## 🔄 **PHASE 3: TRANSACTIONS ROLLOUT** (PENDING)

### **3.1 Procurement** - Already Complete ✅
- ✅ Purchase Requisition
- ✅ Purchase Order

### **3.2 Sales** - Pending ⏸️
- **Estimate**: 6-8 hours total

| Screen | Config | Estimate | Priority |
|--------|--------|----------|----------|
| Sales Order | `NESCKZTJAVPMRDX1234QF` | 3h | P0 |
| Sales Invoice | `NESCKZTJAVPMRDX1234QF` | 3h | P0 |
| Sales Quote | `NESCKZTJAVPMRDX1234QF` | 2h | P1 |

**Additional Requirements**:
- Wire workflow endpoints (Submit, Authorize, Reject)
- Implement document navigation (First, Prev, Next, Last)
- Add Print/Email handlers
- Test status-based button enabling

**Implementation Approach**:
- Use Purchase Order as exact template
- Copy workflow logic
- Adjust for sales-specific fields

---

### **3.3 Inventory** - Pending ⏸️
- **Estimate**: 4-6 hours total

| Screen | Config | Estimate | Priority |
|--------|--------|----------|----------|
| Stock Adjustment | `NESCKZTJAVPMRDX1234QF` | 2h | P1 |
| Stock Transfer | `NESCKZTJAVPMRDX1234QF` | 2h | P1 |
| Stock Take | `NESCKZTJAVPMRDX1234QF` | 2h | P1 |

---

## 📊 **PHASE 4: REPORTS & DASHBOARDS** (PENDING)

**Estimate**: 4-6 hours total

| Screen | Config | Estimate | Priority |
|--------|--------|----------|----------|
| Stock Valuation | `VRXPYQFG` | 2h | P2 |
| Sales Analysis | `VRXPYQFG` | 2h | P2 |
| Aging Reports | `VRXPYQFG` | 2h | P2 |

**Key Features**:
- Read-only mode (no CRUD operations)
- Export to Excel/PDF
- Print functionality
- Advanced filtering

**Config Breakdown**:
- V = View
- R = Refresh
- X = Exit
- P = Print
- Y = Export (Y for eXport alternative)
- Q = Search
- F = Filter
- G = Generate (report)

---

## ⚙️ **PHASE 5: CONFIGURATION SCREENS** (PENDING)

**Estimate**: 2-3 hours total

| Screen | Config | Estimate | Priority |
|--------|--------|----------|----------|
| Company Settings | `ESCKXR` | 1h | P2 |
| System Parameters | `ESCKXR` | 1h | P2 |
| User Preferences | `ESCKXR` | 1h | P3 |

**Key Features**:
- Edit-only mode (no New/Delete)
- Single record editing
- Save/Cancel only

**Config Breakdown**:
- E = Edit
- S = Save
- C = Cancel
- K = Clear
- X = Exit
- R = Refresh

---

## 📋 **IMPLEMENTATION CHECKLIST**

### **For Each Screen**:

#### **Backend Setup** (10 min):
- [ ] Verify `ERPMenuItem` exists in database
- [ ] Set correct `menu_id` (matches frontend `viewId`)
- [ ] Set `applicable_toolbar_config` based on screen type
- [ ] Set `module_name` = 'RETAIL'
- [ ] Set `view_type` (MASTER, TRANSACTION, REPORT, etc.)
- [ ] Set `route_path` (e.g., `/inventory/uoms`)
- [ ] Verify no duplicate entries exist

#### **Frontend Integration** (1-3 hours):
- [ ] **Check for modal pattern** - If exists, plan architectural change
- [ ] Import `MasterToolbar` component
- [ ] Set `viewId` to match backend `menu_id`
- [ ] Remove hardcoded `allowedActions` prop
- [ ] Add state management (showForm, editingId, selectedId, viewMode)
- [ ] Add `getToolbarMode()` helper function
- [ ] Implement `handleToolbarAction` switch-case for all actions
- [ ] Add form ref (`useRef`) for toolbar control
- [ ] Implement CRUD handlers (handleCreate, handleEdit, handleView, handleDelete)
- [ ] Implement form lifecycle handlers (handleFormSuccess, handleFormCancel)
- [ ] Add keyboard shortcuts (F2, F3, F5, F7, F8, ESC)
- [ ] Add filter panel toggle (if applicable)
- [ ] Add import/export handlers (if applicable)
- [ ] Implement decoupled scrolling (fixed header, scrollable content)
- [ ] Add hairline scrollbar styling
- [ ] Ensure surgical spacing (one-line gaps)

#### **Testing** (30 min):
- [ ] VIEW mode shows correct buttons
- [ ] CREATE mode shows Save/Cancel/Clear/Exit only
- [ ] EDIT mode shows Save/Cancel/Clear/Exit only
- [ ] VIEW_FORM mode shows Exit only (read-only)
- [ ] Buttons are HIDDEN (not disabled) in irrelevant modes
- [ ] Selection-first works (Edit/View/Delete require selection)
- [ ] Clicking row only selects (doesn't open form)
- [ ] Edit button opens form with data
- [ ] View button opens read-only form
- [ ] Save button creates/updates record
- [ ] Cancel button closes form without saving
- [ ] Clear button resets form
- [ ] Filter toggle works
- [ ] Exit navigation works
- [ ] All keyboard shortcuts work (F2, F3, F5, F7, F8, ESC)
- [ ] Decoupled scrolling works (header fixed, content scrolls)
- [ ] No console errors
- [ ] No TypeScript errors

---

## 🏆 **GOLD STANDARD EXAMPLES**

### **1. UOM Setup** (Simple Master)
**Location**: `retail/frontend/inventory/pages/UOMSetup.tsx`  
**Documentation**: `04_ARCHIVE/UOM/`  
**Config**: `NESCKVDXRQF`

**Use For**:
- Simple Master screens
- In-place form swap pattern
- Selection-first architecture
- Decoupled scrolling
- Read-only view mode

**Key Patterns**:
```typescript
// State management
const [showForm, setShowForm] = useState(false);
const [editingId, setEditingId] = useState<string | null>(null);
const [selectedItemId, setSelectedItemId] = useState<string | null>(null);
const [viewMode, setViewMode] = useState(false);
const formRef = useRef<any>(null);

// Mode helper
const getToolbarMode = (): MasterMode => {
  if (!showForm) return 'VIEW';
  if (viewMode) return 'VIEW_FORM';
  return editingId ? 'EDIT' : 'CREATE';
};

// Toolbar integration
<MasterToolbar
  viewId="INVENTORY_UOM_SETUP"
  mode={getToolbarMode()}
  onAction={handleToolbarAction}
  hasSelection={!!selectedItemId}
/>

// Conditional rendering (list OR form, never both)
{showForm ? (
  <UOMForm ref={formRef} itemId={editingId} readOnly={viewMode} />
) : (
  <table>...</table>
)}
```

---

### **2. Item Master** (Complex Master)
**Location**: `retail/frontend/inventory/pages/ItemMasterSetup.tsx`  
**Documentation**: `04_ARCHIVE/Item/` (7 documents)  
**Config**: `NESCKVDXRQFIO`

**⚠️ CRITICAL**: Current implementation uses modal pattern - MUST be changed!

**Use For**:
- Complex Master screens
- Multi-step forms
- Screens with variants/relationships
- **Modal → In-place swap migration**

**Must Read**:
- `04_ARCHIVE/Item/ITEM_MASTER_CRITICAL_ARCHITECTURAL_CHANGE.md`
- `04_ARCHIVE/Item/ITEM_MASTER_IMPLEMENTATION_GUIDE.md`

---

### **3. Purchase Order** (Transaction)
**Location**: `retail/frontend/procurement/pages/PurchaseOrderListPage.tsx`  
**Config**: `NESCKZTJAVPMRDX1234QF`

**Use For**:
- Transaction screens
- Workflow-driven documents
- Document navigation
- Print/Email functionality

**Key Patterns**:
- Workflow actions (Submit, Authorize, Reject)
- Status-based button enabling
- Document navigation (1, 2, 3, 4 buttons)

---

## 🎯 **SUCCESS CRITERIA**

### **Per Screen**:
- ✅ Toolbar driven by backend configuration
- ✅ No hardcoded `allowedActions`
- ✅ Mode transitions work correctly
- ✅ Buttons hidden (not disabled) when irrelevant
- ✅ All keyboard shortcuts functional
- ✅ Filter/Import/Export implemented (where applicable)
- ✅ Consistent with Gold Standard examples
- ✅ No console errors or TypeScript errors

### **Overall Project**:
- ✅ All Retail screens use `MasterToolbar`
- ✅ Consistent UX across all screens
- ✅ Backend registry 100% accurate
- ✅ Zero hardcoded toolbar configurations
- ✅ Documentation complete and up-to-date

---

## 📊 **OVERALL PROGRESS TRACKING**

### **Completed**: 7 screens (10%)
- ✅ Phase 0: Architecture & Documentation
- ✅ Phase 1: Benchmarks
  - UOM Setup (Simple Master)
  - Purchase Order (Transaction)
- ✅ Reason Codes (Simple Master)
- ✅ Categories (Simple Master)
- ✅ Purchase Requisition (Transaction)

### **In Progress**: 1 screen (1%)
- 🚧 Item Master (documentation complete, implementation pending)

### **Pending**: ~62 screens (89%)

**Phase 2 - Master Data** (14 pending):
- **P0**: Customer, Supplier, Company, Location (4 screens)
- **P1**: Attributes, Attribute Values, Code Master, Employee (4 screens)
- **P2**: Tax Codes, Payment Terms, Warehouses, Departments, Brands, Units (6 screens)

**Phase 3 - Transactions** (8 pending):
- Sales Orders, Invoices, Quotes (3 screens)
- Stock Adjustments, Transfers, Takes (3 screens)
- Other transactions (2 screens)

**Phase 4 - Reports** (6 pending):
- Stock Valuation, Sales Analysis, Aging Reports, etc.

**Phase 5 - Configuration** (3 pending):
- Company Settings, System Parameters, User Preferences

**Total Estimated**: ~70 screens across all phases

---

## 🔧 **TOOLS & RESOURCES**

### **Documentation**:
1. `README.md` - This folder's navigation hub
2. `01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md` - Character codes
3. `01_ESSENTIAL/ARCHITECTURE_CLARIFICATION.md` - Core architecture
4. `02_REFERENCE/MODE_BASED_FILTERING_TECHNICAL_REFERENCE.md` - How filtering works
5. `04_ARCHIVE/Item/` - Complete Item Master package
6. `04_ARCHIVE/UOM/` - UOM reference materials

### **Interactive Tools**:
- `01_ESSENTIAL/toolbar-explorer.html` - Visual toolbar configuration builder

### **Backend Scripts**:
- `backend/scripts/verify_uom_toolbar.py` - Verify menu entries
- `backend/scripts/seed_toolbar_controls.py` - Seed toolbar controls
- `backend/scripts/fix_benchmarks.py` - Fix benchmark configurations

### **Frontend Components**:
- `frontend/core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven.tsx` - Main toolbar
- `frontend/src/hooks/useToolbarConfig.ts` - Toolbar configuration hook

---

## 📅 **TIMELINE**

| Phase | Duration | Start | End | Status |
|-------|----------|-------|-----|--------|
| Phase 0: Architecture & Docs | 2h | 2026-01-09 | 2026-01-09 | ✅ COMPLETE |
| Phase 1: Benchmarks | 3h | 2026-01-09 | 2026-01-09 | ✅ COMPLETE |
| Phase 2: Master Data | 26-31h | 2026-01-10 | TBD | 🚧 IN PROGRESS |
| Phase 3: Transactions | 10h | TBD | TBD | ⏸️ PENDING |
| Phase 4: Reports | 6h | TBD | TBD | ⏸️ PENDING |
| Phase 5: Configuration | 3h | TBD | TBD | ⏸️ PENDING |
| **TOTAL** | **50-55h** | | | **10% Complete** |

### **Phase 2 Breakdown** (26-31 hours):
- **Week 1** (10-12h): Item, Customer, Supplier, Company, Location
- **Week 2** (8-10h): Attributes, Attribute Values, Code Master, Employee
- **Week 3** (8-9h): Simple Lookups (Tax, Payment, Warehouses, etc.)

---

## 📝 **NEXT SESSION PRIORITIES**

### **Immediate** (Next 4-6 hours):
1. **Item Master Implementation** (3-4 hours)
   - Read critical architectural change document
   - Implement modal → in-place swap migration
   - Follow implementation guide
   - Verify with checklist

2. **Customer Master** (2-3 hours)
   - Check for modal pattern
   - Apply Item Master template
   - Implement and test

### **This Week** (Next 8-12 hours):
3. **Supplier Master** (2-3 hours)
4. **Employee Master** (2-3 hours)
5. **Simple Masters** (2-3 hours)
   - Tax Codes
   - Payment Terms
   - Warehouses

### **Next Week** (12-16 hours):
6. **Sales Transactions** (6-8 hours)
   - Sales Order
   - Sales Invoice
   - Sales Quote

7. **Inventory Transactions** (4-6 hours)
   - Stock Adjustment
   - Stock Transfer
   - Stock Take

---

## ⚠️ **CRITICAL NOTES**

1. **Modal Pattern**: Several screens currently use modal/sliding window patterns. These MUST be converted to in-place swap (like UOM). See Item Master documentation for migration guide.

2. **Single Entry Rule**: Each screen has exactly ONE ERPMenuItem entry. Frontend handles list vs form via `mode` prop.

3. **No Hardcoded Actions**: Remove ALL `allowedActions` props. Backend drives everything.

4. **Buttons Hidden, Not Disabled**: Buttons are HIDDEN (not rendered) when not applicable to current mode.

5. **Selection First**: Edit, View, and Delete buttons require a row to be selected first.

---

**Status**: ⚡ **ACTIVE - Phase 2 In Progress**  
**Owner**: Astra (Antigravity Engineering Agent)  
**Last Updated**: 2026-01-10 15:20 IST

---

**Ready to implement? Start with `README.md` for navigation, then follow this plan phase by phase!** 🚀
