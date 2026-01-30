# 🎯 RETAIL MODULE - REVISED EXECUTION PLAN (Session 4)
**Date**: 2026-01-09 14:22 IST  
**Agent**: Astra  
**Status**: ⏳ **AWAITING APPROVAL**

---

## 📋 USER REQUIREMENTS

### **Critical Requirements from Viji**:
1. ✅ **Check all sidebar items are wired** - No item pending for wiring
2. ✅ **All UIs except POS Billing must use toolbar ONLY** - No command buttons

### **From toolbar-revisit-checklist.md**:
3. ✅ Update 4 menu items with correct toolbar strings
4. ✅ Verify mode-based behavior in existing pages
5. ✅ Test toolbar display (no scrolling, tooltips working)

---

## 🎯 REVISED EXECUTION PLAN

### **PHASE 1: SIDEBAR WIRING AUDIT** (2-3 hours) - **CRITICAL**

#### **1.1 Complete Sidebar Menu Audit** (60 min)
**Objective**: Verify 100% of sidebar menu items have corresponding UI implementations

**Tasks**:
- [ ] Extract all menu items from `menuConfig.ts`
- [ ] Cross-reference with `router.tsx` routes
- [ ] Identify any menu items without routes
- [ ] Identify any routes pointing to non-existent components
- [ ] Generate comprehensive wiring report

**Deliverable**: `SIDEBAR_WIRING_AUDIT_2026-01-09.md`

**Current Known Status** (from previous audit):
| Module | Total | Wired | Pending | % |
|--------|-------|-------|---------|---|
| Store Ops | 7 | 7 | 0 | 100% ✅ |
| Sales | 5 | 5 | 0 | 100% ✅ |
| Merchandising | 9 | 9 | 0 | 100% ✅ |
| Procurement | 11 | 11 | 0 | 100% ✅ |
| Customers | 3 | 3 | 0 | 100% ✅ |
| Inventory | 63 | 21 | **42** | 33% ⚠️ |

**Expected Outcome**: Confirm 42 Inventory UIs are the ONLY pending items

#### **1.2 Wire Any Missing Routes** (60 min)
**Objective**: Ensure every menu item has a valid route

**Tasks**:
- [ ] For each unwired menu item, create placeholder component
- [ ] Register route in `router.tsx`
- [ ] Add basic page structure with MasterToolbar
- [ ] Verify navigation works from sidebar

**Deliverable**: All sidebar items clickable and functional

#### **1.3 Update Implementation Tracker** (30 min)
**Objective**: Ensure RETAIL_IMPLEMENTATION_TRACKER.md is 100% accurate

**Tasks**:
- [ ] Update tracker with current wiring status
- [ ] Mark completed items as ✅
- [ ] Identify exact pending count
- [ ] Update percentage calculations

**Deliverable**: Updated `RETAIL_IMPLEMENTATION_TRACKER.md`

---

### **PHASE 2: COMMAND BUTTON ELIMINATION** (3-4 hours) - **CRITICAL**

#### **2.1 Comprehensive Button Audit** (90 min)
**Objective**: Identify ALL standalone command buttons across Retail module

**Scan Strategy**:
```powershell
# Search for common button patterns
Get-ChildItem -Path "frontend\apps\retail" -Recurse -Filter "*.tsx" | 
  Select-String -Pattern "Add New|Save|Cancel|Submit|Delete|Edit" |
  Where-Object { $_.Line -notmatch "MasterToolbar|handleToolbarAction" }
```

**Tasks**:
- [ ] Scan all Retail pages for standalone buttons
- [ ] Document each button found (file, line, type)
- [ ] Categorize: "Add New", "Save", "Cancel", "Submit", "Delete", "Edit"
- [ ] Create removal checklist

**Deliverable**: `COMMAND_BUTTON_AUDIT_2026-01-09.md`

**Exception**: POS Billing (`/operations/pos/pos`) - Can retain custom buttons

#### **2.2 Remove Standalone Buttons** (90 min)
**Objective**: Eliminate all command buttons, replace with toolbar-only pattern

**For Each Page**:
- [ ] Remove button JSX elements
- [ ] Ensure MasterToolbar is present
- [ ] Verify `handleToolbarAction()` handles the action
- [ ] Test functionality still works via toolbar
- [ ] Verify keyboard shortcuts work (F2, F3, F8, etc.)

**Pattern to Follow**:
```tsx
// ❌ REMOVE THIS
<button onClick={handleCreate} className="...">
  <Plus /> Add New
</button>

// ✅ ENSURE THIS EXISTS
<MasterToolbar 
  viewId="ITEM_MASTER" 
  mode={mode} 
  onAction={handleToolbarAction} 
/>
```

**Deliverable**: 100% toolbar-only compliance (except POS Billing)

#### **2.3 Verification Testing** (60 min)
**Objective**: Ensure all CRUD operations still work via toolbar

**Test Each Modified Page**:
- [ ] New (F2) - Opens create form
- [ ] Edit (F3) - Opens edit form
- [ ] Save (F8) - Saves data
- [ ] Cancel (ESC) - Cancels operation
- [ ] Delete (F4) - Deletes record
- [ ] Refresh (F9) - Reloads data
- [ ] Exit (ESC) - Navigates back

**Deliverable**: All pages functional with toolbar-only pattern

---

### **PHASE 3: TOOLBAR CONFIGURATION CLEANUP** (1-2 hours)

#### **3.1 Update Menu Item Toolbar Strings** (45 min)
**Objective**: Apply correct toolbar configs per `toolbar-revisit-checklist.md`

**Django Admin Updates** (`ERPMenuItem.applicable_toolbar_config`):
- [ ] `MOVEMENT_TYPES` → `NRQFX` (List view)
- [ ] `VALUATION_METHODS` → `VRX` (View, Refresh, Exit only)
- [ ] `INV_PARAMETERS` → `ESCKXR` (Edit-focused config)
- [ ] `APPROVAL_RULES` → `NRQFX` (List view)

**Process**:
1. Access Django Admin → Toolbar Control → Items
2. Search for each menu_id
3. Update `applicable_toolbar_config` field
4. Save changes
5. Test frontend reflects changes

**Deliverable**: 4 menu items updated with correct strings

#### **3.2 Verify Mode-Based Behavior** (45 min)
**Objective**: Ensure toolbar buttons enable/disable correctly per mode

**Test Matrix**:
| Mode | Enabled Buttons | Disabled Buttons |
|------|----------------|------------------|
| **VIEW** | N, E, V, P, M, R, Y, I, Q, F, 1234, BGW, ?, X | S, C, K, T, J, H, O |
| **CREATE** | S, C, K, ?, BGW | N, E, D, V, P, M, R, Y, I, Q, F, 1234, X |
| **EDIT** | S, C, K, ?, BGW | N, E, D, V, P, M, R, Y, I, Q, F, 1234, X |

**Test Pages**:
- [ ] UOMSetup.tsx
- [ ] ReasonCodeListPage.tsx
- [ ] InventorySetup.tsx
- [ ] ItemMasterSetup.tsx
- [ ] CustomerSetup.tsx

**Deliverable**: Mode transitions working correctly

#### **3.3 UI/UX Refinements** (30 min)
**Objective**: Ensure toolbar displays properly

**Checks**:
- [ ] All buttons visible in single line (no horizontal scroll)
- [ ] Tooltips appear on hover for all 29 buttons
- [ ] Icons consistent across all modules
- [ ] Button separators visible between groups
- [ ] Keyboard shortcuts displayed in tooltips

**Deliverable**: Polished toolbar UX

---

### **PHASE 4: INVENTORY UI DEVELOPMENT** (26 hours) - **ONLY AFTER PHASES 1-3**

#### **4A: Dashboard & Analytics** (12 UIs, 6 hours)
| # | Component | Path | Toolbar Config | Time |
|---|-----------|------|----------------|------|
| 1 | StockByLocationPage | `/inventory/levels/by-location` | `NEVZPM1234RDQX` | 45min |
| 2 | StockValuationDashboard | `/inventory/levels/valuation` | `NEVPM1234RDX` | 45min |
| 3 | MovementTrendsAnalytics | `/inventory/movements/trends` | `NEVPM1234RDX` | 45min |
| 4 | AlertsNotificationsPage | `/inventory/alerts` | `NEVZPM1234RDX` | 45min |
| 5 | StockByCategoryPage | `/inventory/levels/by-category` | `NEVZPM1234RDQX` | 30min |
| 6 | StockByBatchSerialPage | `/inventory/levels/by-batch` | `NEVZPM1234RDQX` | 30min |
| 7 | LowStockAlertsPage | `/inventory/alerts/low-stock` | `NEVZPM1234RDX` | 30min |
| 8 | OverstockAlertsPage | `/inventory/alerts/overstock` | `NEVZPM1234RDX` | 30min |
| 9 | StockAgingAnalysisPage | `/inventory/levels/aging` | `NEVPM1234RDX` | 45min |
| 10 | GoodsReceiptViewPage | `/inventory/movements/receipts` | `NEVPM1234RDX` | 30min |
| 11 | GoodsIssueViewPage | `/inventory/movements/issues` | `NEVPM1234RDX` | 30min |
| 12 | MovementReportsPage | `/inventory/movements/reports` | `NEPM1234RDX` | 30min |

#### **4B-4G: Remaining Phases** (30 UIs, 20 hours)
- **4B**: Physical Inventory (6 UIs, 4 hours)
- **4C**: Replenishment (4 UIs, 3 hours)
- **4D**: Batch & Serial (2 UIs, 2 hours)
- **4E**: Reports (7 UIs, 4 hours)
- **4F**: Valuation (4 UIs, 3 hours)
- **4G**: Miscellaneous (7 UIs, 4 hours)

**Full Details**: See `.steering/04_EXECUTION_PLANS/RETAIL_PHASE4_EXECUTION_PLAN.md`

---

## 📊 EXECUTION TIMELINE

### **Recommended Session Breakdown**:

**Session 4A** (6-8 hours):
- Phase 1: Sidebar Wiring Audit (2-3 hours)
- Phase 2: Command Button Elimination (3-4 hours)
- Phase 3: Toolbar Configuration Cleanup (1-2 hours)

**Session 4B** (6 hours):
- Phase 4A: Dashboard & Analytics (12 UIs)

**Session 4C** (7 hours):
- Phase 4B: Physical Inventory (6 UIs)
- Phase 4C: Replenishment (4 UIs)

**Session 4D** (6 hours):
- Phase 4D: Batch & Serial (2 UIs)
- Phase 4E: Reports (7 UIs)

**Session 4E** (7 hours):
- Phase 4F: Valuation (4 UIs)
- Phase 4G: Miscellaneous (7 UIs)

**Total Estimated Time**: 32-34 hours across 5 sessions

---

## ✅ SUCCESS CRITERIA

### **Phase 1 Complete When**:
- [ ] 100% of sidebar menu items have routes
- [ ] All menu items navigate to valid pages
- [ ] RETAIL_IMPLEMENTATION_TRACKER.md is accurate

### **Phase 2 Complete When**:
- [ ] Zero standalone command buttons (except POS Billing)
- [ ] All pages use MasterToolbar exclusively
- [ ] All CRUD operations work via toolbar
- [ ] All keyboard shortcuts functional

### **Phase 3 Complete When**:
- [ ] 4 menu items have correct toolbar strings
- [ ] Mode-based behavior verified on 5+ pages
- [ ] Toolbar displays properly (no scroll, tooltips work)

### **Phase 4 Complete When**:
- [ ] All 42 Inventory UIs created
- [ ] All routes registered
- [ ] All toolbar configs set
- [ ] Retail Module = 100% UI Complete

---

## 🚀 NEXT STEPS

**Immediate Action**: Await your approval to proceed with:
1. **Phase 1**: Sidebar Wiring Audit (2-3 hours)
2. **Phase 2**: Command Button Elimination (3-4 hours)
3. **Phase 3**: Toolbar Configuration Cleanup (1-2 hours)

**After Phases 1-3 Complete**: Proceed with Phase 4 (Inventory UI Development)

---

**Prepared By**: Astra  
**Date**: 2026-01-09 14:22 IST  
**Status**: ⏳ **AWAITING YOUR APPROVAL TO PROCEED**
