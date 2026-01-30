# 🎯 TOOLBAR IMPLEMENTATION - COMPLETE GUIDE

**For**: Agent E (HRM/CRM Implementation)  
**From**: Astra (Retail/FMS - Toolbar Architecture Owner)  
**Date**: 2026-01-10  
**Status**: ⚡ ACTIVE AUTHORITY

---

## 📋 TABLE OF CONTENTS

1. [Backend Implementation - Django Master Control](#1-backend-implementation---django-master-control)
2. [Mode-Based Button Control](#2-mode-based-button-control)
3. [Complete Character Legend](#3-complete-character-legend)
4. [Implementation Examples](#4-implementation-examples)

---

# 1. BACKEND IMPLEMENTATION - DJANGO MASTER CONTROL

## 🎯 **The Architecture**

The toolbar system uses a **Backend-Driven Configuration** approach where Django controls which buttons appear on each screen through a simple character-based string.

### **Core Model: `ERPMenuItem`**

Located in: `backend/domain/master/models.py`

```python
class ERPMenuItem(models.Model):
    """
    Master registry for all UI screens and their toolbar configurations.
    Each screen has ONE entry with a configuration string.
    """
    menu_id = models.CharField(max_length=100, unique=True)
    # Example: "UOM_SETUP", "PURCHASE_ORDERS", "CUSTOMER_MASTER"
    
    name = models.CharField(max_length=200)
    # Example: "Units of Measure", "Purchase Orders", "Customer Master"
    
    view_type = models.CharField(max_length=50, choices=[
        ('MASTER', 'Master Data'),
        ('TRANSACTION', 'Transaction'),
        ('REPORT', 'Report'),
        ('DASHBOARD', 'Dashboard'),
        ('CONFIGURATION', 'Configuration'),
    ])
    
    applicable_toolbar_config = models.CharField(max_length=100)
    # THIS IS THE KEY FIELD - Character-based configuration string
    # Example: "NESCKVDXRQF" or "NESCKZTJAVPMRDX1234QF"
    
    module = models.CharField(max_length=50)
    # Example: "RETAIL", "FMS", "HRM", "CRM"
    
    is_active = models.BooleanField(default=True)
```

---

## 📊 **The 4 Key Records Example**

Here are 4 real examples from our Retail implementation showing how different screen types are configured:

### **Example 1: UOM Setup (Simple Master)**
```python
{
    "menu_id": "UOM_SETUP",
    "name": "Units of Measure",
    "view_type": "MASTER",
    "applicable_toolbar_config": "NESCKVDXRQF",
    "module": "RETAIL",
    "is_active": True
}
```

**Breakdown of `NESCKVDXRQF`**:
- `N` = New (F2)
- `E` = Edit (F3)
- `S` = Save (F8)
- `C` = Cancel (Esc)
- `K` = Clear (F5)
- `V` = View (F7)
- `D` = Delete (F4)
- `X` = Exit (Esc)
- `R` = Refresh (F9)
- `Q` = Search (Ctrl+F)
- `F` = Filter (Alt+F)

**Result**: 11 buttons available for UOM Setup screen

---

### **Example 2: Item Master (Advanced Master)**
```python
{
    "menu_id": "ITEM_MASTER",
    "name": "Item Master",
    "view_type": "MASTER",
    "applicable_toolbar_config": "NESCKVDXRQFIO",
    "module": "RETAIL",
    "is_active": True
}
```

**Breakdown of `NESCKVDXRQFIO`**:
- All from UOM Setup (`NESCKVDXRQF`) PLUS:
- `I` = Import (Ctrl+I)
- `O` = Export (Ctrl+E)

**Result**: 13 buttons available for Item Master screen

---

### **Example 3: Purchase Order (Transaction)**
```python
{
    "menu_id": "PURCHASE_ORDERS",
    "name": "Purchase Orders",
    "view_type": "TRANSACTION",
    "applicable_toolbar_config": "NESCKZTJAVPMRDX1234QF",
    "module": "RETAIL",
    "is_active": True
}
```

**Breakdown of `NESCKZTJAVPMRDX1234QF`**:
- `N` = New (F2)
- `E` = Edit (F3)
- `S` = Save (F8)
- `C` = Cancel (Esc)
- `K` = Clear (F5)
- `Z` = Authorize (F10)
- `T` = Submit (Alt+S)
- `J` = Reject (Alt+R)
- `A` = Amend (Alt+A)
- `V` = View (F7)
- `P` = Print (Ctrl+P)
- `M` = Email (Ctrl+M)
- `R` = Refresh (F9)
- `D` = Delete (F4)
- `X` = Exit (Esc)
- `1` = First Record (Home)
- `2` = Previous Record (PgUp)
- `3` = Next Record (PgDn)
- `4` = Last Record (End)
- `Q` = Search (Ctrl+F)
- `F` = Filter (Alt+F)

**Result**: 21 buttons available for Purchase Order screen

---

### **Example 4: Stock Valuation Report (Report)**
```python
{
    "menu_id": "STOCK_VALUATION_REPORT",
    "name": "Stock Valuation Report",
    "view_type": "REPORT",
    "applicable_toolbar_config": "VRXPYQFG",
    "module": "RETAIL",
    "is_active": True
}
```

**Breakdown of `VRXPYQFG`**:
- `V` = View (F7)
- `R` = Refresh (F9)
- `X` = Exit (Esc)
- `P` = Print (Ctrl+P)
- `Y` = Export (Ctrl+E)
- `Q` = Search (Ctrl+F)
- `F` = Filter (Alt+F)
- `G` = Settings (Alt+O)

**Result**: 8 buttons available for Stock Valuation Report screen

---

## 🔧 **How to Add a New Screen**

### **Step 1: Create Django Admin Entry**

1. Go to Django Admin: `http://localhost:8000/admin/`
2. Navigate to: **Toolbar Control** → **ERP Menu Items**
3. Click **Add ERP Menu Item**
4. Fill in the fields:

```
Menu ID: HRM_LEAVE_APPLICATION
Name: Leave Application
View Type: TRANSACTION
Applicable Toolbar Config: NESCKZTJAVPMRDX1234QF
Module: HRM
Is Active: ✓ (checked)
```

5. Click **Save**

### **Step 2: Verify in Database**

The record is now available via API endpoint:
```
GET /api/toolbar-config/?menu_id=HRM_LEAVE_APPLICATION
```

Response:
```json
{
  "menu_id": "HRM_LEAVE_APPLICATION",
  "name": "Leave Application",
  "view_type": "TRANSACTION",
  "applicable_toolbar_config": "NESCKZTJAVPMRDX1234QF",
  "module": "HRM",
  "is_active": true
}
```

---

## 📋 **Standard Configuration Strings by Screen Type**

| Screen Type | Config String | Use Case | Example Screens |
|-------------|---------------|----------|-----------------|
| **Masters (Simple)** | `NESCKVDXRQF` | Basic CRUD operations | UOM, Brands, Categories, Tax Classes |
| **Masters (Advanced)** | `NESCKVDXRQFIO` | CRUD + Import/Export | Item Master, Customers, Suppliers, Employees |
| **Transactions** | `NESCKZTJAVPMRDX1234QF` | Full workflow with approvals | Purchase Orders, Sales Orders, Invoices, Leave Applications |
| **Reports** | `VRXPYQFG` | Read-only with export | Stock Reports, Sales Analysis, Attendance Reports |
| **Configuration** | `ESCKXR` | Settings screens | Company Settings, System Parameters |
| **Transaction (Simple)** | `NESCKVDXRQF` | No approval workflow | Stock Adjustments, Stock Transfers |

---

# 2. MODE-BASED BUTTON CONTROL

## 🎯 **The Three Modes**

The frontend toolbar component uses a `mode` prop to control which buttons are visible. This is the **KEY CONCEPT** that makes the system work.

### **Mode 1: VIEW Mode**
**When**: User is viewing/browsing records (list or detail view)  
**Purpose**: Allow navigation, searching, and initiating actions

**Visible Buttons**:
- ✅ New (N)
- ✅ Edit (E)
- ✅ View (V)
- ✅ Delete (D)
- ✅ Refresh (R)
- ✅ Search (Q)
- ✅ Filter (F)
- ✅ Import (I)
- ✅ Export (O)
- ✅ Print (P)
- ✅ Email (M)
- ✅ Authorize (Z)
- ✅ Submit (T)
- ✅ Reject (J)
- ✅ Amend (A)
- ✅ Navigation (1,2,3,4)
- ✅ Exit (X)

**Hidden Buttons**:
- ❌ Save (S)
- ❌ Cancel (C)
- ❌ Clear (K)

**Why**: In VIEW mode, there's nothing to save or cancel, so these buttons are hidden.

---

### **Mode 2: CREATE Mode**
**When**: User is creating a new record  
**Purpose**: Focus on saving or canceling the new record

**Visible Buttons**:
- ✅ Save (S)
- ✅ Cancel (C)
- ✅ Clear (K)
- ✅ Exit (X)
- ✅ Help (?)
- ✅ Notes (B)
- ✅ Attach (G)

**Hidden Buttons**:
- ❌ New (N)
- ❌ Edit (E)
- ❌ View (V)
- ❌ Delete (D)
- ❌ Refresh (R)
- ❌ Search (Q)
- ❌ Filter (F)
- ❌ All workflow buttons (Z, T, J, A)
- ❌ All navigation buttons (1, 2, 3, 4)

**Why**: When creating a record, user should focus on completing the form. Navigation and other actions could cause data loss.

---

### **Mode 3: EDIT Mode**
**When**: User is editing an existing record  
**Purpose**: Focus on saving or canceling changes

**Visible Buttons**:
- ✅ Save (S)
- ✅ Cancel (C)
- ✅ Clear (K)
- ✅ Exit (X)
- ✅ Help (?)
- ✅ Notes (B)
- ✅ Attach (G)

**Hidden Buttons**:
- ❌ New (N)
- ❌ Edit (E)
- ❌ View (V)
- ❌ Delete (D)
- ❌ Refresh (R)
- ❌ Search (Q)
- ❌ Filter (F)
- ❌ All workflow buttons (Z, T, J, A)
- ❌ All navigation buttons (1, 2, 3, 4)

**Why**: Same as CREATE mode - focus on completing the edit without distractions.

---

## 🔄 **Mode Transition Flow**

```
┌─────────────────────────────────────────────────────────────┐
│                      LIST PAGE (VIEW Mode)                   │
│  Toolbar: [New] [Refresh] [Search] [Filter] [Exit]         │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Click "New" (N)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   FORM PAGE (CREATE Mode)                    │
│  Toolbar: [Save] [Cancel] [Clear] [Exit]                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Click "Save" (S)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   FORM PAGE (VIEW Mode)                      │
│  Toolbar: [Edit] [Delete] [Print] [Authorize] [Exit]       │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Click "Edit" (E)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   FORM PAGE (EDIT Mode)                      │
│  Toolbar: [Save] [Cancel] [Clear] [Exit]                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Click "Cancel" (C)
                              ▼
                        Back to VIEW Mode
```

---

## 💻 **Frontend Implementation**

### **Component Usage**

```tsx
import { MasterToolbar, MasterMode } from "@/components/MasterToolbarConfigDriven";
import { useState } from "react";

export const LeaveApplicationPage = () => {
  // State to track current mode
  const [mode, setMode] = useState<MasterMode>('VIEW');
  const [selectedId, setSelectedId] = useState<number | null>(null);

  // Handler for toolbar actions
  const handleToolbarAction = (actionId: string) => {
    switch (actionId) {
      case 'new':
        setMode('CREATE');
        setSelectedId(null);
        break;

      case 'edit':
        if (selectedId) {
          setMode('EDIT');
        }
        break;

      case 'save':
        // Save logic here
        saveLeaveApplication();
        setMode('VIEW');
        break;

      case 'cancel':
        setMode('VIEW');
        break;

      case 'delete':
        if (selectedId) {
          deleteLeaveApplication(selectedId);
        }
        break;

      case 'refresh':
        refreshData();
        break;

      case 'exit':
        navigate('/hrm/dashboard');
        break;

      // ... other actions
    }
  };

  return (
    <div className="page-container">
      {/* Toolbar - automatically shows/hides buttons based on mode */}
      <MasterToolbar
        viewId="HRM_LEAVE_APPLICATION"  // Must match Django menu_id
        mode={mode}                      // Current mode (VIEW/CREATE/EDIT)
        onAction={handleToolbarAction}   // Action handler
      />

      {/* Page content */}
      <div className="content">
        {mode === 'VIEW' && <LeaveApplicationList />}
        {mode === 'CREATE' && <LeaveApplicationForm />}
        {mode === 'EDIT' && <LeaveApplicationForm id={selectedId} />}
      </div>
    </div>
  );
};
```

---

## 🎨 **Visual Example: UOM Setup**

### **Scenario 1: List Page (VIEW Mode)**

```tsx
<MasterToolbar viewId="UOM_SETUP" mode="VIEW" />
```

**Visible Buttons**:
```
[New] [Refresh] [Search] [Filter] [Exit]
```

**Config String**: `NESCKVDXRQF`  
**Filtered to**: `N`, `R`, `Q`, `F`, `X` (only list-relevant actions)

---

### **Scenario 2: Creating New UOM (CREATE Mode)**

```tsx
<MasterToolbar viewId="UOM_SETUP" mode="CREATE" />
```

**Visible Buttons**:
```
[Save] [Cancel] [Clear] [Exit]
```

**Config String**: `NESCKVDXRQF`  
**Filtered to**: `S`, `C`, `K`, `X` (only form-edit actions)

---

### **Scenario 3: Viewing UOM Details (VIEW Mode)**

```tsx
<MasterToolbar viewId="UOM_SETUP" mode="VIEW" />
```

**Visible Buttons**:
```
[Edit] [Delete] [View] [Exit]
```

**Config String**: `NESCKVDXRQF`  
**Filtered to**: `E`, `D`, `V`, `X` (only detail-view actions)

---

### **Scenario 4: Editing UOM (EDIT Mode)**

```tsx
<MasterToolbar viewId="UOM_SETUP" mode="EDIT" />
```

**Visible Buttons**:
```
[Save] [Cancel] [Clear] [Exit]
```

**Config String**: `NESCKVDXRQF`  
**Filtered to**: `S`, `C`, `K`, `X` (same as CREATE mode)

---

# 3. COMPLETE CHARACTER LEGEND

## 📖 **Full Character Reference**

### **CRUD Operations**

| Code | Action | Shortcut | Icon | Color | Description | Visible In |
|------|--------|----------|------|-------|-------------|------------|
| **N** | New | F2 | ➕ | Blue | Create new record | VIEW |
| **E** | Edit | F3 | ✏️ | Blue | Edit selected record | VIEW |
| **S** | Save | F8 | 💾 | Green | Save current changes | CREATE, EDIT |
| **C** | Cancel | Esc | ❌ | Gray | Discard changes | CREATE, EDIT |
| **K** | Clear | F5 | 🔄 | Amber | Clear form fields | CREATE, EDIT |
| **V** | View | F7 | 👁️ | Indigo | View record details | VIEW |
| **D** | Delete | F4 | 🗑️ | Red | Delete selected record | VIEW |

---

### **Navigation & Search**

| Code | Action | Shortcut | Icon | Color | Description | Visible In |
|------|--------|----------|------|-------|-------------|------------|
| **X** | Exit | Esc | 🚪 | Gray | Exit current screen | ALL |
| **R** | Refresh | F9 | 🔃 | Cyan | Reload data | VIEW |
| **Q** | Search | Ctrl+F | 🔍 | Gray | Open search dialog | VIEW |
| **F** | Filter | Alt+F | ⚡ | Gray | Toggle filter panel | VIEW |
| **1** | First | Home | ⏮️ | Gray | Go to first record | VIEW |
| **2** | Previous | PgUp | ◀️ | Gray | Go to previous record | VIEW |
| **3** | Next | PgDn | ▶️ | Gray | Go to next record | VIEW |
| **4** | Last | End | ⏭️ | Gray | Go to last record | VIEW |

---

### **Data Operations**

| Code | Action | Shortcut | Icon | Color | Description | Visible In |
|------|--------|----------|------|-------|-------------|------------|
| **I** | Import | Ctrl+I | ⬆️ | Violet | Import data from file | VIEW |
| **O** | Export | Ctrl+E | ⬇️ | Indigo | Export data to file | VIEW |
| **Y** | Export (Alt) | Ctrl+E | ⬇️ | Indigo | Alternative export | VIEW |
| **L** | Clone | Ctrl+Shift+C | 📋 | Blue | Duplicate record | VIEW |

---

### **Workflow & Approval**

| Code | Action | Shortcut | Icon | Color | Description | Visible In |
|------|--------|----------|------|-------|-------------|------------|
| **Z** | Authorize | F10 | ✅ | Green | Approve/authorize document | VIEW |
| **T** | Submit | Alt+S | 📤 | Blue | Submit for approval | VIEW |
| **J** | Reject | Alt+R | 🚫 | Red | Reject document | VIEW |
| **A** | Amend | Alt+A | 📝 | Orange | Modify authorized document | VIEW |
| **H** | Hold | Alt+H | ⏸️ | Yellow | Put document on hold | VIEW |
| **W** | Void | Alt+V | ⛔ | Red | Void/cancel document | VIEW |

---

### **Document Operations**

| Code | Action | Shortcut | Icon | Color | Description | Visible In |
|------|--------|----------|------|-------|-------------|------------|
| **P** | Print | Ctrl+P | 🖨️ | Purple | Print document | VIEW |
| **M** | Email | Ctrl+M | 📧 | Sky | Send via email | VIEW |

---

### **Tools & Utilities**

| Code | Action | Shortcut | Icon | Color | Description | Visible In |
|------|--------|----------|------|-------|-------------|------------|
| **B** | Notes | Alt+N | 📝 | Yellow | Add/view notes | ALL |
| **G** | Attach | Alt+U | 📎 | Gray | Attach files | ALL |
| **?** | Help | F1 | ❓ | Blue | Show help | ALL |
| **U** | Settings | Alt+O | ⚙️ | Gray | Configure settings | VIEW |

---

## 🎯 **Standard Configuration Patterns**

### **Pattern 1: Simple Master (11 buttons)**
```
NESCKVDXRQF
```
**Use For**: UOM, Brands, Categories, Tax Classes, Departments, Designations

**Buttons**: New, Edit, Save, Cancel, Clear, View, Delete, Exit, Refresh, Search, Filter

---

### **Pattern 2: Advanced Master (13 buttons)**
```
NESCKVDXRQFIO
```
**Use For**: Item Master, Customers, Suppliers, Employees, Locations

**Buttons**: All from Simple Master + Import, Export

---

### **Pattern 3: Full Transaction (21 buttons)**
```
NESCKZTJAVPMRDX1234QF
```
**Use For**: Purchase Orders, Sales Orders, Invoices, Leave Applications, Expense Claims

**Buttons**: New, Edit, Save, Cancel, Clear, Authorize, Submit, Reject, Amend, View, Print, Email, Refresh, Delete, Exit, First, Previous, Next, Last, Search, Filter

---

### **Pattern 4: Simple Transaction (11 buttons)**
```
NESCKVDXRQF
```
**Use For**: Stock Adjustments, Stock Transfers, Attendance Entries

**Buttons**: Same as Simple Master (no approval workflow)

---

### **Pattern 5: Report (8 buttons)**
```
VRXPYQFG
```
**Use For**: Stock Reports, Sales Analysis, Attendance Reports, Payroll Reports

**Buttons**: View, Refresh, Exit, Print, Export, Search, Filter, Settings

---

### **Pattern 6: Configuration (6 buttons)**
```
ESCKXR
```
**Use For**: Company Settings, System Parameters, User Preferences

**Buttons**: Edit, Save, Cancel, Clear, Exit, Refresh

---

# 4. IMPLEMENTATION EXAMPLES

## 📋 **Example 1: HRM Leave Application (Full Transaction)**

### **Step 1: Backend Setup**

Create Django Admin entry:
```python
{
    "menu_id": "HRM_LEAVE_APPLICATION",
    "name": "Leave Application",
    "view_type": "TRANSACTION",
    "applicable_toolbar_config": "NESCKZTJAVPMRDX1234QF",
    "module": "HRM",
    "is_active": True
}
```

---

### **Step 2: Frontend Implementation**

```tsx
// File: frontend/apps/hrm/leave/pages/LeaveApplication.tsx

import { useState } from 'react';
import { MasterToolbar, MasterMode } from '@/components/MasterToolbarConfigDriven';
import { useNavigate } from 'react-router-dom';

export const LeaveApplicationPage = () => {
  const [mode, setMode] = useState<MasterMode>('VIEW');
  const [selectedId, setSelectedId] = useState<number | null>(null);
  const navigate = useNavigate();

  const handleToolbarAction = (actionId: string) => {
    switch (actionId) {
      case 'new':
        setMode('CREATE');
        setSelectedId(null);
        break;

      case 'edit':
        if (selectedId) {
          setMode('EDIT');
        } else {
          alert('Please select a record to edit');
        }
        break;

      case 'save':
        // Save logic
        if (mode === 'CREATE') {
          createLeaveApplication();
        } else if (mode === 'EDIT') {
          updateLeaveApplication(selectedId);
        }
        setMode('VIEW');
        break;

      case 'cancel':
        setMode('VIEW');
        break;

      case 'clear':
        // Clear form fields
        clearForm();
        break;

      case 'delete':
        if (selectedId) {
          if (confirm('Are you sure you want to delete this leave application?')) {
            deleteLeaveApplication(selectedId);
          }
        }
        break;

      case 'view':
        if (selectedId) {
          viewLeaveApplication(selectedId);
        }
        break;

      case 'submit':
        if (selectedId) {
          submitLeaveApplication(selectedId);
        }
        break;

      case 'authorize':
        if (selectedId) {
          authorizeLeaveApplication(selectedId);
        }
        break;

      case 'reject':
        if (selectedId) {
          rejectLeaveApplication(selectedId);
        }
        break;

      case 'print':
        if (selectedId) {
          printLeaveApplication(selectedId);
        }
        break;

      case 'refresh':
        refreshData();
        break;

      case 'search':
        openSearchDialog();
        break;

      case 'filter':
        toggleFilterPanel();
        break;

      case 'exit':
        navigate('/hrm/dashboard');
        break;

      default:
        console.log('Unhandled action:', actionId);
    }
  };

  return (
    <div className="page-container">
      {/* Toolbar */}
      <MasterToolbar
        viewId="HRM_LEAVE_APPLICATION"
        mode={mode}
        onAction={handleToolbarAction}
      />

      {/* Content */}
      <div className="content">
        {mode === 'VIEW' && (
          <LeaveApplicationList
            onSelect={setSelectedId}
            selectedId={selectedId}
          />
        )}
        {mode === 'CREATE' && (
          <LeaveApplicationForm
            onSave={() => setMode('VIEW')}
            onCancel={() => setMode('VIEW')}
          />
        )}
        {mode === 'EDIT' && (
          <LeaveApplicationForm
            id={selectedId}
            onSave={() => setMode('VIEW')}
            onCancel={() => setMode('VIEW')}
          />
        )}
      </div>
    </div>
  );
};
```

---

### **Step 3: Toolbar Behavior**

**When page loads (VIEW mode)**:
```
Toolbar shows: [New] [Refresh] [Search] [Filter] [Exit]
User sees: List of leave applications
```

**User clicks "New" button**:
```
Mode changes to: CREATE
Toolbar shows: [Save] [Cancel] [Clear] [Exit]
User sees: Empty leave application form
```

**User fills form and clicks "Save"**:
```
Mode changes to: VIEW
Toolbar shows: [Edit] [Delete] [Submit] [Authorize] [Print] [Exit]
User sees: Saved leave application details
```

**User clicks "Edit" button**:
```
Mode changes to: EDIT
Toolbar shows: [Save] [Cancel] [Clear] [Exit]
User sees: Editable leave application form
```

---

## 📋 **Example 2: HRM Employee Master (Advanced Master)**

### **Step 1: Backend Setup**

```python
{
    "menu_id": "HRM_EMPLOYEE_MASTER",
    "name": "Employee Master",
    "view_type": "MASTER",
    "applicable_toolbar_config": "NESCKVDXRQFIO",
    "module": "HRM",
    "is_active": True
}
```

---

### **Step 2: Frontend Implementation**

```tsx
// File: frontend/apps/hrm/employee/pages/EmployeeMaster.tsx

import { useState } from 'react';
import { MasterToolbar, MasterMode } from '@/components/MasterToolbarConfigDriven';

export const EmployeeMasterPage = () => {
  const [mode, setMode] = useState<MasterMode>('VIEW');
  const [selectedId, setSelectedId] = useState<number | null>(null);

  const handleToolbarAction = (actionId: string) => {
    switch (actionId) {
      case 'new':
        setMode('CREATE');
        break;

      case 'edit':
        if (selectedId) setMode('EDIT');
        break;

      case 'save':
        saveEmployee();
        setMode('VIEW');
        break;

      case 'cancel':
        setMode('VIEW');
        break;

      case 'delete':
        if (selectedId) deleteEmployee(selectedId);
        break;

      case 'import':
        openImportDialog();
        break;

      case 'export':
        exportEmployees();
        break;

      case 'refresh':
        refreshData();
        break;

      case 'exit':
        navigate('/hrm/dashboard');
        break;

      // ... other actions
    }
  };

  return (
    <div className="page-container">
      <MasterToolbar
        viewId="HRM_EMPLOYEE_MASTER"
        mode={mode}
        onAction={handleToolbarAction}
      />

      <div className="content">
        {/* Employee list or form based on mode */}
      </div>
    </div>
  );
};
```

---

## 📋 **Example 3: HRM Attendance Report (Report)**

### **Step 1: Backend Setup**

```python
{
    "menu_id": "HRM_ATTENDANCE_REPORT",
    "name": "Attendance Report",
    "view_type": "REPORT",
    "applicable_toolbar_config": "VRXPYQFG",
    "module": "HRM",
    "is_active": True
}
```

---

### **Step 2: Frontend Implementation**

```tsx
// File: frontend/apps/hrm/reports/pages/AttendanceReport.tsx

import { MasterToolbar } from '@/components/MasterToolbarConfigDriven';

export const AttendanceReportPage = () => {
  const handleToolbarAction = (actionId: string) => {
    switch (actionId) {
      case 'view':
        generateReport();
        break;

      case 'refresh':
        refreshReport();
        break;

      case 'print':
        printReport();
        break;

      case 'export':
        exportToExcel();
        break;

      case 'search':
        openSearchDialog();
        break;

      case 'filter':
        toggleFilterPanel();
        break;

      case 'settings':
        openReportSettings();
        break;

      case 'exit':
        navigate('/hrm/dashboard');
        break;
    }
  };

  return (
    <div className="page-container">
      <MasterToolbar
        viewId="HRM_ATTENDANCE_REPORT"
        mode="VIEW"  // Reports are always in VIEW mode
        onAction={handleToolbarAction}
      />

      <div className="content">
        {/* Report content */}
      </div>
    </div>
  );
};
```

**Note**: Reports are ALWAYS in VIEW mode since they're read-only.

---

## ✅ **Quick Reference Checklist**

### **For Each New Screen:**

- [ ] **Step 1**: Create `ERPMenuItem` entry in Django Admin
  - [ ] Set unique `menu_id` (e.g., `HRM_LEAVE_APPLICATION`)
  - [ ] Choose appropriate `view_type` (MASTER/TRANSACTION/REPORT)
  - [ ] Set correct `applicable_toolbar_config` string
  - [ ] Set `module` (HRM/CRM)
  - [ ] Set `is_active = True`

- [ ] **Step 2**: Import `MasterToolbar` in frontend component
  - [ ] Add `mode` state variable
  - [ ] Create `handleToolbarAction` function
  - [ ] Add `<MasterToolbar>` component with correct `viewId`

- [ ] **Step 3**: Implement mode transitions
  - [ ] New → CREATE mode
  - [ ] Edit → EDIT mode
  - [ ] Save → VIEW mode
  - [ ] Cancel → VIEW mode

- [ ] **Step 4**: Test all toolbar buttons
  - [ ] Verify buttons appear/hide based on mode
  - [ ] Test all action handlers
  - [ ] Verify keyboard shortcuts work

---

## 🎯 **Key Takeaways**

1. **One Entry Per Screen**: Each screen has ONE `ERPMenuItem` entry, not separate entries for list/form views

2. **Character-Based Config**: Backend provides a string like `NESCKVDXRQF`, frontend parses it

3. **Mode Controls Visibility**: The `mode` prop (VIEW/CREATE/EDIT) determines which buttons show

4. **Standard Patterns**: Use predefined config strings for consistency:
   - Simple Master: `NESCKVDXRQF`
   - Advanced Master: `NESCKVDXRQFIO`
   - Transaction: `NESCKZTJAVPMRDX1234QF`
   - Report: `VRXPYQFG`

5. **Mode Transitions**: Always manage mode state in your component:
   - New → CREATE
   - Edit → EDIT
   - Save/Cancel → VIEW

---

**Document Owner**: Astra (Retail/FMS)  
**For**: Agent E (HRM/CRM)  
**Status**: ⚡ ACTIVE AUTHORITY  
**Version**: 1.0  
**Date**: 2026-01-10
