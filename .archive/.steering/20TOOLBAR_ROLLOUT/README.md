# 📚 **TOOLBAR ROLLOUT - MASTER GUIDE**

**Last Updated**: 2026-01-10 15:15 IST  
**Status**: ✅ **Active Development - Phase 2**  
**Owner**: Astra (Antigravity Engineering Agent)

---

## 🎯 **QUICK START**

### **New to Toolbar Rollout?**
1. **Read**: `TOOLBAR_ROLLOUT_PLAN.md` (5 min) ← **Start here**
2. **Understand**: `01_ESSENTIAL/ARCHITECTURE_CLARIFICATION.md` (10 min)
3. **Reference**: `01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md` (5 min)
4. **Implement**: Follow the plan phase by phase

### **Implementing a New Screen?**
1. **Check**: `TOOLBAR_ROLLOUT_PLAN.md` for your screen's phase
2. **Review**: Gold Standard examples (UOM or Item Master)
3. **Follow**: Implementation checklist in the plan
4. **Test**: Using the verification steps

---

## 📂 **DIRECTORY STRUCTURE**

```
.steering/20TOOLBAR_ROLLOUT/
│
├── README.md                           ← This file (navigation hub)
├── TOOLBAR_ROLLOUT_PLAN.md             ← Master implementation plan
│
├── 01_ESSENTIAL/                       ← Must-read documents
│   ├── ARCHITECTURE_CLARIFICATION.md   ← Single-entry-per-screen rule
│   ├── BENCHMARK_STABILIZATION_COMPLETE.md
│   ├── BENCHMARK_STABILIZATION_REPORT.md
│   ├── TOOLBAR_LEGEND_AND_MAPPING.md   ← Character codes reference
│   └── toolbar-explorer.html           ← Interactive visual tool
│
├── 02_REFERENCE/                       ← Reference documentation
│   ├── MODE_BASED_FILTERING_TECHNICAL_REFERENCE.md
│   ├── TOOLBAR_CHEAT_SHEET.md
│   ├── TOOLBAR_CONFIGURATION_GUIDE.md
│   ├── TOOLBAR_LEGEND.md
│   └── 05_Toolbar_Governance_Reference.md
│
├── 03_TECHNICAL/                       ← Technical implementation
│   ├── TOOLBAR_CONFIG_DESIGN.md
│   ├── TOOLBAR_CONFIG_REFACTOR.md
│   ├── 06_TOOLBAR_IMPLEMENTATION_GUIDE.md
│   └── toolbar_reference/
│
└── 04_ARCHIVE/                         ← Historical & examples
    ├── README.md                       ← Archive index
    ├── PHASE2_TOOLBAR_ROLLOUT.md       ← Current phase doc
    ├── Item/                           ← Item Master example (NEW!)
    │   ├── README.md
    │   ├── ITEM_MASTER_INDEX.md
    │   ├── ITEM_MASTER_CRITICAL_ARCHITECTURAL_CHANGE.md
    │   ├── ITEM_MASTER_IMPLEMENTATION_CHECKLIST.md
    │   ├── ITEM_MASTER_IMPLEMENTATION_GUIDE.md
    │   ├── ITEM_MASTER_VISUAL_ARCHITECTURE.md
    │   └── ITEM_MASTER_DELIVERABLES_SUMMARY.md
    ├── UOM/                            ← UOM example (Gold Standard)
    │   └── UOM_TESTING_ISSUES_2026-01-09.md
    ├── Toolbar_general/                ← General toolbar docs
    └── Others/                         ← Historical progress
```

---

## 🏆 **GOLD STANDARD EXAMPLES**

### **1. UOM Setup** (Simple Master - COMPLETE ✅)
**Location**: `retail/frontend/inventory/pages/UOMSetup.tsx`  
**Documentation**: `04_ARCHIVE/UOM/`  
**Reference Manual**: `04_ARCHIVE/UOM_TOOLBAR_ACTION_AND_CHECKLIST_MANUAL.md` (if exists in main folder)

**Use This For**:
- ✅ Simple Master screens (single entity, no complex relationships)
- ✅ In-place form swap pattern (list ↔ form)
- ✅ Selection-first architecture
- ✅ Decoupled scrolling
- ✅ Read-only view mode

**Key Features**:
- Config: `NESCKVDXRQF` (11 characters)
- Modes: VIEW, CREATE, EDIT, VIEW_FORM
- Keyboard shortcuts: F2, F3, F5, F7, F8, ESC
- Surgical spacing (one-line gaps)
- Hairline scrollbar

---

### **2. Item Master** (Complex Master - DOCUMENTED ✅)
**Location**: `retail/frontend/inventory/pages/ItemMasterSetup.tsx`  
**Documentation**: `04_ARCHIVE/Item/`

**Use This For**:
- ✅ Complex Master screens (variants, multiple tabs, relationships)
- ✅ **CRITICAL**: Modal → In-place swap migration
- ✅ Multi-step forms
- ✅ Advanced validation

**Key Features**:
- Config: `NESCKVDXRQFIO` (13 characters)
- **Critical Change**: Remove `ItemModalWithVariants`, use in-place `ItemForm`
- Same patterns as UOM but with additional complexity

**⚠️ IMPORTANT**: Read `04_ARCHIVE/Item/ITEM_MASTER_CRITICAL_ARCHITECTURAL_CHANGE.md` first!

---

### **3. Purchase Order** (Transaction - COMPLETE ✅)
**Location**: `retail/frontend/procurement/pages/PurchaseOrderListPage.tsx`

**Use This For**:
- ✅ Transaction screens (workflow-driven)
- ✅ Document navigation (First, Prev, Next, Last)
- ✅ Workflow actions (Submit, Authorize, Reject)
- ✅ Print/Email functionality

**Key Features**:
- Config: `NESCKZTJAVPMRDX1234QF` (21 characters)
- Workflow states: DRAFT → SUBMITTED → APPROVED
- Status-based button enabling
- Document navigation

---

## 📋 **ESSENTIAL DOCUMENTS TO READ**

### **Before Starting ANY Implementation**:

1. **`TOOLBAR_ROLLOUT_PLAN.md`** (10 min)
   - Master plan with all phases
   - Screen-by-screen breakdown
   - Implementation checklist
   - Success criteria

2. **`01_ESSENTIAL/ARCHITECTURE_CLARIFICATION.md`** (10 min)
   - Single-entry-per-screen rule
   - Why we removed "List View" entries
   - How mode-based filtering works

3. **`01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md`** (5 min)
   - Character code meanings (N, E, S, C, K, etc.)
   - UI button mapping
   - Keyboard shortcuts

4. **`01_ESSENTIAL/BENCHMARK_STABILIZATION_COMPLETE.md`** (5 min)
   - What "stabilized" means
   - Verification steps
   - Known issues resolved

---

### **For Specific Screen Types**:

#### **Simple Master Screens** (UOM, Reason Codes, Categories):
1. Review UOM implementation: `retail/frontend/inventory/pages/UOMSetup.tsx`
2. Read: `02_REFERENCE/MODE_BASED_FILTERING_TECHNICAL_REFERENCE.md`
3. Follow: Implementation checklist in `TOOLBAR_ROLLOUT_PLAN.md`

#### **Complex Master Screens** (Item, Customer, Supplier):
1. **MUST READ**: `04_ARCHIVE/Item/ITEM_MASTER_CRITICAL_ARCHITECTURAL_CHANGE.md`
2. **Follow**: `04_ARCHIVE/Item/ITEM_MASTER_IMPLEMENTATION_GUIDE.md`
3. **Verify**: `04_ARCHIVE/Item/ITEM_MASTER_IMPLEMENTATION_CHECKLIST.md`

#### **Transaction Screens** (PO, SO, Invoices):
1. Review PO implementation: `retail/frontend/procurement/pages/PurchaseOrderListPage.tsx`
2. Read: Workflow action requirements in plan
3. Implement: Document navigation (1, 2, 3, 4 buttons)

---

## 🚀 **IMPLEMENTATION WORKFLOW**

### **Step 1: Preparation** (15 min)
- [ ] Read `TOOLBAR_ROLLOUT_PLAN.md`
- [ ] Identify your screen's phase and priority
- [ ] Review appropriate Gold Standard example
- [ ] Check if screen has special requirements

### **Step 2: Backend Setup** (10 min)
- [ ] Verify `ERPMenuItem` entry exists in database
- [ ] Confirm `menu_id` matches what frontend will use
- [ ] Set `applicable_toolbar_config` (e.g., `NESCKVDXRQF`)
- [ ] Set `view_type` (MASTER, TRANSACTION, REPORT, etc.)
- [ ] Set `module_name` = 'RETAIL'

### **Step 3: Frontend Implementation** (1-3 hours)
- [ ] Import `MasterToolbar` component
- [ ] Set `viewId` prop to match backend `menu_id`
- [ ] Remove any hardcoded `allowedActions`
- [ ] Implement mode state management (VIEW/CREATE/EDIT)
- [ ] Add `handleToolbarAction` switch-case
- [ ] Implement keyboard shortcuts
- [ ] Add filter panel toggle (if applicable)

### **Step 4: Testing** (30 min)
- [ ] VIEW mode shows correct buttons
- [ ] CREATE mode shows Save/Cancel/Clear/Exit only
- [ ] EDIT mode shows Save/Cancel/Clear/Exit only
- [ ] Buttons are HIDDEN (not disabled) in wrong modes
- [ ] All keyboard shortcuts work
- [ ] Filter toggle works
- [ ] Exit navigation works

### **Step 5: Documentation** (15 min)
- [ ] Update progress in `TOOLBAR_ROLLOUT_PLAN.md`
- [ ] Note any deviations or issues
- [ ] Create screen-specific notes if needed

---

## 🎓 **LEARNING PATH**

### **Beginner** (Never implemented toolbar):
**Time**: 4-6 hours for first screen

1. **Day 1 - Learning** (2 hours):
   - Read all essential documents
   - Study UOM implementation
   - Understand architecture

2. **Day 2 - Implementation** (3 hours):
   - Follow implementation guide
   - Implement first simple master
   - Test thoroughly

3. **Day 3 - Refinement** (1 hour):
   - Fix issues
   - Polish UX
   - Document learnings

### **Intermediate** (Implemented 1-2 screens):
**Time**: 2-3 hours per screen

1. **Preparation** (30 min):
   - Review plan
   - Check Gold Standard
   - Identify differences

2. **Implementation** (1.5 hours):
   - Backend setup
   - Frontend integration
   - Basic testing

3. **Testing** (1 hour):
   - Comprehensive testing
   - Edge cases
   - Documentation

### **Advanced** (Implemented 3+ screens):
**Time**: 1-2 hours per screen

1. **Quick Review** (15 min)
2. **Implementation** (1 hour)
3. **Testing** (30 min)

---

## ⚠️ **CRITICAL WARNINGS**

### **1. Modal vs In-Place Swap Pattern**
**Problem**: Some screens (like Item Master) currently use modal/sliding window patterns.

**Solution**: These MUST be converted to in-place swap (like UOM).

**See**: `04_ARCHIVE/Item/ITEM_MASTER_CRITICAL_ARCHITECTURAL_CHANGE.md`

### **2. Single-Entry-Per-Screen Rule**
**Problem**: Old architecture had separate "List View" and "Form View" entries.

**Solution**: ONE entry per screen. Frontend handles list vs form via `mode` prop.

**See**: `01_ESSENTIAL/ARCHITECTURE_CLARIFICATION.md`

### **3. No Hardcoded allowedActions**
**Problem**: Old code had `allowedActions={['new', 'edit', ...]}` hardcoded.

**Solution**: Remove completely. Backend drives everything via `applicable_toolbar_config`.

### **4. Buttons Hidden, Not Disabled**
**Problem**: Old pattern disabled buttons in wrong modes.

**Solution**: Buttons are HIDDEN (not rendered) when not applicable to current mode.

**See**: `02_REFERENCE/MODE_BASED_FILTERING_TECHNICAL_REFERENCE.md`

---

## 🔧 **TOOLS & UTILITIES**

### **Interactive Tools**:
- **`01_ESSENTIAL/toolbar-explorer.html`** - Visual toolbar configuration builder
- Open in browser to experiment with toolbar configs

### **Backend Scripts**:
- `backend/scripts/verify_uom_toolbar.py` - Verify menu entries
- `backend/scripts/seed_toolbar_controls.py` - Seed toolbar controls
- `backend/scripts/fix_benchmarks.py` - Fix benchmark configurations

### **Frontend Components**:
- `frontend/core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven.tsx` - Main toolbar component
- `frontend/src/hooks/useToolbarConfig.ts` - Toolbar configuration hook

---

## 📊 **CURRENT STATUS**

### **Completed** (18%):
- ✅ Phase 0: Architecture & Documentation
- ✅ Phase 1: Benchmarks (UOM, Purchase Order)

### **In Progress** (Phase 2):
- 🚧 Item Master (documentation complete, implementation pending)
- ⏸️ Customer Master (pending)
- ⏸️ Supplier Master (pending)

### **Pending** (82%):
- Sales Orders, Invoices
- Stock Reports
- Configuration screens
- ~40 more screens

---

## 📞 **SUPPORT & ESCALATION**

### **Questions?**
1. Check this README first
2. Review appropriate Gold Standard example
3. Read relevant documentation in `01_ESSENTIAL/`
4. Consult `TOOLBAR_ROLLOUT_PLAN.md`

### **Issues?**
1. Check `04_ARCHIVE/UOM/UOM_TESTING_ISSUES_2026-01-09.md` for known issues
2. Review `01_ESSENTIAL/BENCHMARK_STABILIZATION_COMPLETE.md`
3. Escalate to Viji if unresolved

### **Architectural Questions?**
1. Read `01_ESSENTIAL/ARCHITECTURE_CLARIFICATION.md`
2. Review `02_REFERENCE/MODE_BASED_FILTERING_TECHNICAL_REFERENCE.md`
3. Consult with Viji

---

## 🎯 **SUCCESS CRITERIA**

### **Per Screen**:
- ✅ Toolbar driven by backend configuration
- ✅ No hardcoded `allowedActions`
- ✅ Mode transitions work correctly
- ✅ Buttons hidden (not disabled) when irrelevant
- ✅ All keyboard shortcuts functional
- ✅ Consistent with Gold Standard examples

### **Overall Project**:
- ✅ All Retail screens use `MasterToolbar`
- ✅ Consistent UX across all screens
- ✅ Backend registry 100% accurate
- ✅ Zero hardcoded toolbar configurations
- ✅ Documentation complete and up-to-date

---

## 📅 **NEXT STEPS**

1. **Immediate**: Complete Item Master implementation
2. **This Week**: Customer and Supplier Masters
3. **Next Week**: Sales transactions
4. **Month End**: All Phase 2 & 3 screens complete

---

## 📚 **DOCUMENT QUICK REFERENCE**

| Document | Purpose | When to Read |
|----------|---------|--------------|
| `README.md` | Navigation hub | First time, as reference |
| `TOOLBAR_ROLLOUT_PLAN.md` | Master plan | Before starting, track progress |
| `01_ESSENTIAL/ARCHITECTURE_CLARIFICATION.md` | Core architecture | Before any implementation |
| `01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md` | Character codes | When configuring toolbar |
| `04_ARCHIVE/Item/ITEM_MASTER_INDEX.md` | Item Master guide | When implementing complex masters |
| `04_ARCHIVE/Item/ITEM_MASTER_CRITICAL_ARCHITECTURAL_CHANGE.md` | Modal → Swap migration | When screen uses modal pattern |
| `02_REFERENCE/MODE_BASED_FILTERING_TECHNICAL_REFERENCE.md` | How filtering works | When debugging mode issues |

---

**Created**: 2026-01-10 15:15 IST  
**Version**: 1.0  
**Status**: ✅ **ACTIVE - Ready for Use**  
**Owner**: Astra (Antigravity Engineering Agent)
