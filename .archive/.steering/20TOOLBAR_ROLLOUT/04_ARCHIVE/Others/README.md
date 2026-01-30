# 📂 TOOLBAR ROLLOUT - DOCUMENTATION HUB

**Complete reference for backend-driven toolbar implementation**  
**Last Updated**: 2026-01-10 08:05 IST

---

## 🎯 **START HERE: NEW AGENT ONBOARDING**

### **⚡ QUICK_START_GUIDE.md** (5 minutes)
**Purpose**: Get started immediately with 3-step implementation  
**Use When**: "I need to implement toolbar on my first screen NOW"

**Contains**:
- 3-step implementation (Django + Frontend + Test)
- Config strings cheat sheet
- Top 15 character codes
- Mode behavior summary
- Troubleshooting tips

---

### **📖 TOOLBAR_IMPLEMENTATION_EXPLAINED.md** (20 minutes)
**Purpose**: Complete understanding of the toolbar system  
**Use When**: "I want to understand how this works end-to-end"

**Contains**:
1. **Backend Implementation**: Django master control with 4 real examples
2. **Mode-Based Control**: How VIEW/CREATE/EDIT modes work
3. **Complete Character Legend**: All 30+ toolbar actions explained
4. **Real Examples**: HRM Leave Application, Employee Master, Attendance Report

---

## 📚 **REFERENCE DOCUMENTATION**

### **📁 01_ESSENTIAL/** (Your Go-To Resources)

#### **1️⃣ TOOLBAR_LEGEND_AND_MAPPING.md**
**Purpose**: Character codes + UI screen classification  
**Use When**: "Which config string do I use for this screen?"

**Quick Answer**:
- Masters (Simple) → `NESCKVDXRQF`
- Masters (Advanced) → `NESCKVDXRQFIO`
- Transactions → `NESCKZTJAVPMRDX1234QF`
- Reports → `VRXPYQFG`
- Configuration → `ESCKXR`

---

#### **2️⃣ TOOLBAR_ROLLOUT_PLAN.md**
**Purpose**: Implementation plan with checklists  
**Use When**: "How do I implement toolbar on a new screen?"

**Contains**:
- 5 implementation phases
- Per-screen checklist (Backend + Frontend + Testing)
- Progress tracking (10% complete)
- Timeline and estimates

---

#### **3️⃣ toolbar-explorer.html** ✨
**Purpose**: Interactive visual tool  
**Use When**: "What does this toolbar look like?"

**How to Use**:
1. Open in browser
2. Click any screen in left sidebar
3. See toolbar preview, config string, and character breakdown

**Features**:
- Retail module tree navigation
- Live toolbar preview
- Character-by-character breakdown
- Action counts (Total, VIEW mode, CREATE mode)

---

## 📚 **REFERENCE DOCS**

### **📁 02_REFERENCE/** (Deep Dive)

| File | Purpose |
|------|---------|
| **TOOLBAR_CHEAT_SHEET.md** | One-page quick reference |
| **TOOLBAR_CONFIGURATION_GUIDE.md** | Complete guide with examples |
| **TOOLBAR_LEGEND.md** | Original legend (legacy) |
| **05_Toolbar_Governance_Reference.md** | Governance rules |

---

## 🔧 **TECHNICAL DOCS**

### **📁 03_TECHNICAL/** (Implementation Details)

| File/Folder | Purpose |
|-------------|---------|
| **06_TOOLBAR_IMPLEMENTATION_GUIDE.md** | Step-by-step implementation |
| **TOOLBAR_CONFIG_DESIGN.md** | Design decisions |
| **TOOLBAR_CONFIG_REFACTOR.md** | Refactoring notes |
| **toolbar_reference/** | Code samples and demos |

---

## 📜 **ARCHIVE**

### **📁 04_ARCHIVE/** (Historical)

Phase completion docs, investigations, and old implementations.

---

## 🔤 **CONFIG STRINGS AT A GLANCE**

```
Masters (Simple)      | NESCKVDXRQF              | Basic CRUD
Masters (Advanced)    | NESCKVDXRQFIO            | With Import/Export
Transactions          | NESCKZTJAVPMRDX1234QF    | Full Workflow
Reports               | VRXPYQFG                 | Read-only
Configuration         | ESCKXR                   | Edit-only
Transaction (Simple)  | NESCKVDXRQF              | No Approval
```

---

## 📁 **DIRECTORY STRUCTURE**

```
20TOOLBAR_ROLLOUT/
│
├── README.md (this file)
│
├── 01_ESSENTIAL/ ⭐ START HERE
│   ├── TOOLBAR_LEGEND_AND_MAPPING.md
│   ├── TOOLBAR_ROLLOUT_PLAN.md
│   └── toolbar-explorer.html
│
├── 02_REFERENCE/ 📚 DEEP DIVE
│   ├── TOOLBAR_CHEAT_SHEET.md
│   ├── TOOLBAR_CONFIGURATION_GUIDE.md
│   ├── TOOLBAR_LEGEND.md
│   └── 05_Toolbar_Governance_Reference.md
│
├── 03_TECHNICAL/ 🔧 IMPLEMENTATION
│   ├── 06_TOOLBAR_IMPLEMENTATION_GUIDE.md
│   ├── TOOLBAR_CONFIG_DESIGN.md
│   ├── TOOLBAR_CONFIG_REFACTOR.md
│   └── toolbar_reference/
│       ├── TOOLBAR_GOVERNANCE_EXPLAINED.md
│       ├── toolbar-demo.html
│       └── toolbar_config.json
│
└── 04_ARCHIVE/ 📜 HISTORICAL
    ├── PHASE1_MASTER_TOOLBAR_COMPLETE.md
    ├── PHASE2_TOOLBAR_ROLLOUT.md
    ├── TOOLBAR_IMPLEMENTATION_COMPLETE.md
    └── (other historical docs)
```

---

## 🚀 **QUICK START GUIDE**

### **For Quick Lookup** (30 seconds):
```
1. Open 01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md
2. Find your screen type in the table
3. Copy the config string
```

### **For Implementation** (5 minutes):
```
1. Open 01_ESSENTIAL/TOOLBAR_ROLLOUT_PLAN.md
2. Follow the per-screen checklist
3. Test using success criteria
```

### **For Visual Understanding** (2 minutes):
```
1. Open 01_ESSENTIAL/toolbar-explorer.html in browser
2. Click any screen in left sidebar
3. See toolbar preview and breakdown
```

---

## ✅ **CURRENT STATUS**

### **Completed** (5 screens - 10%):
- ✅ UOM Setup (Gold Standard)
- ✅ Reason Codes
- ✅ Purchase Requisition
- ✅ Purchase Order
- ✅ Categories

### **Next Priority** (P0):
- 🚧 Item Master
- 🚧 Customer Master
- 🚧 Supplier Master

---

## 🎯 **RECOMMENDED WORKFLOW**

### **First Time**:
1. Read `01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md` (5 min)
2. Open `01_ESSENTIAL/toolbar-explorer.html` (2 min)
3. Click through different screen types to understand

### **During Implementation**:
1. Use `01_ESSENTIAL/TOOLBAR_ROLLOUT_PLAN.md` checklist
2. Reference `01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md` for config strings
3. Verify with `01_ESSENTIAL/toolbar-explorer.html`

### **For Deep Dive**:
1. Read `02_REFERENCE/TOOLBAR_CONFIGURATION_GUIDE.md`
2. Review `03_TECHNICAL/06_TOOLBAR_IMPLEMENTATION_GUIDE.md`

---

## 📞 **QUICK HELP**

**Q**: "Which config for Customer Master?"  
**A**: `NESCKVDXRQFIO` (Masters - Advanced)

**Q**: "Which config for Tax Class?"  
**A**: `NESCKVDXRQF` (Masters - Simple)

**Q**: "Which config for Sales Order?"  
**A**: `NESCKZTJAVPMRDX1234QF` (Transactions)

**Q**: "Which config for Stock Report?"  
**A**: `VRXPYQFG` (Reports)

---

## 🔗 **RELATED RESOURCES**

### **Backend**:
- `backend/scripts/verify_uom_toolbar.py` - Verify menu entries
- `backend/scripts/seed_toolbar_controls.py` - Seed controls

### **Frontend**:
- `frontend/core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven.tsx`
- `frontend/src/hooks/useToolbarConfig.ts`

### **Reference Implementation**:
- `retail/frontend/inventory/pages/UOMSetup.tsx` (Gold Standard)

---

**Owner**: Astra (ERP Platform Development)  
**Status**: ⚡ ACTIVE  
**Version**: 2.0 (Organized Structure)
