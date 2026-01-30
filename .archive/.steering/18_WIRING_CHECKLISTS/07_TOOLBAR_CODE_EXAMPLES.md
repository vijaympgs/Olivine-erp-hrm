# TOOLBAR IMPLEMENTATION - COMPLETE CODE EXAMPLES

**Purpose**: Complete, copy-paste code examples for implementing backend-driven toolbars  
**For**: Agent E (HRM/CRM Development)  
**Date**: 2026-01-09 20:05 IST  
**Status**: ✅ PRODUCTION READY

---

## 🎯 CRITICAL ARCHITECTURE RULE

### **ONE SCREEN = ONE DATABASE ENTRY**

```
❌ WRONG:
  ERPMenuItem #1: menu_id="employee-list", view_type="LIST_VIEW"
  ERPMenuItem #2: menu_id="EMPLOYEE_MASTER", view_type="MASTER"

✅ CORRECT:
  ERPMenuItem: menu_id="EMPLOYEE_MASTER", view_type="MASTER"
  
  Frontend handles BOTH:
    - List page: mode="VIEW"
    - Form page: mode="VIEW|CREATE|EDIT"
```

---

## 📋 PART 1: BACKEND SETUP

### **Step 1: Create ERPMenuItem Entry**

**Django Admin** (`http://localhost:8000/admin/`):

1. Navigate to: **Toolbar Control** → **ERP Menu Items**
2. Click **Add ERP Menu Item**
3. Fill in the form:

```
Menu ID: EMPLOYEE_MASTER
Menu Name: Employee Master
Module Name: HRM
Submodule Name: EMPLOYEE
View Type: MASTER
Route Path: /hrm/employees
Applicable Toolbar Config: NESCKVDXRQFIO
Is Active: ✓ (checked)
```

**Field Explanations**:
- `menu_id`: Uppercase snake case, matches frontend `viewId`
- `view_type`: MASTER, TRANSACTION, REPORT, DASHBOARD, or CONFIGURATION
- `applicable_toolbar_config`: Character string defining available actions

---

### **Step 2: Toolbar Configuration Strings**

**Choose based on screen type**:

#### **Masters (Simple)** - Basic CRUD
```
Config: NESCKVDXRQF
Actions: New, Edit, Save, Cancel, Clear, View, Delete, Exit, Refresh, Search, Filter

Example screens:
- Department
- Position  
- Leave Type
- Contact Category
```

#### **Masters (Advanced)** - With Import/Export
```
Config: NESCKVDXRQFIO
Actions: Above + Import, Export

Example screens:
- Employee Master
- Contact Master
- Account Master
```

#### **Transactions** - Full Workflow
```
Config: NESCKZTJAVPMRDX1234QF
Actions: New, Edit, Save, Cancel, Clear, Authorize, Submit, Reject, 
         Amend, View, Print, Email, Refresh, Delete, Exit, 
         First, Prev, Next, Last, Search, Filter

Example screens:
- Leave Request
- Attendance Adjustment
- Lead
- Opportunity
```

#### **Reports** - Read-Only
```
Config: VRXPYQFG
Actions: View, Refresh, Exit, Print, Export, Search, Filter, Generate

Example screens:
- Employee Directory Report
- Leave Balance Report
- Sales Pipeline Report
```

---

## 📋 PART 2: FRONTEND IMPLEMENTATION

### **Example 1: Employee Master (HRM)**

#### **File**: `frontend/apps/hrm/employee/pages/EmployeeSetup.tsx`

```typescript
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { MasterToolbar, MasterMode } from '@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven';

export const EmployeeSetup: React.FC = () => {
  const navigate = useNavigate();
  
  // State management
  const [employees, setEmployees] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [showFilterPanel, setShowFilterPanel] = useState(true);
  
  // Determine toolbar mode
  const getToolbarMode = (): MasterMode => {
    if (!showForm) return 'VIEW';
    return editingId ? 'EDIT' : 'CREATE';
  };
  
  // Handle toolbar actions
  const handleToolbarAction = (action: string) => {
    switch (action) {
      case 'new':
        setEditingId(null);
        setShowForm(true);
        break;
        
      case 'edit':
        if (selectedId && !showForm) {
          setEditingId(selectedId);
          setShowForm(true);
        }
        break;
        
      case 'save':
        if (showForm) {
          // Call your save logic here
          console.log('Saving employee...');
        }
        break;
        
      case 'cancel':
        setShowForm(false);
        setEditingId(null);
        break;
        
      case 'clear':
        if (showForm) {
          // Clear form fields
          console.log('Clearing form...');
        } else {
          // Clear filters
          setSelectedId(null);
        }
        break;
        
      case 'delete':
        if (selectedId && !showForm) {
          // Call delete logic
          console.log('Deleting employee:', selectedId);
        }
        break;
        
      case 'refresh':
        // Reload data
        console.log('Refreshing data...');
        break;
        
      case 'search':
        // Focus search input
        document.querySelector<HTMLInputElement>('input[type="text"]')?.focus();
        break;
        
      case 'filter':
        setShowFilterPanel(!showFilterPanel);
        break;
        
      case 'import':
        alert('Import functionality coming soon');
        break;
        
      case 'export':
        alert('Export functionality coming soon');
        break;
        
      case 'exit':
        navigate('/dashboard');
        break;
    }
  };
  
  return (
    <>
      {/* Toolbar - CRITICAL: No hardcoded allowedActions! */}
      <MasterToolbar
        viewId="EMPLOYEE_MASTER"  // Must match backend menu_id
        mode={getToolbarMode()}    // VIEW, CREATE, or EDIT
        onAction={handleToolbarAction}
        hasSelection={!!selectedId}
        showLabels={false}
        // ❌ DO NOT ADD: allowedActions={[...]}
      />
      
      <div className="page-container space-y-6">
        {/* Page header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-xl font-semibold text-[#201f1e]">
              Employee Directory
            </h1>
            <p className="text-sm text-[#605e5c]">
              Manage employee information
            </p>
          </div>
        </div>
        
        {/* Show form or list based on state */}
        {showForm ? (
          <div className="bg-white p-6 shadow-sm border border-gray-200">
            <h2 className="text-base font-semibold text-[#323130] mb-4">
              {editingId ? 'Edit Employee' : 'New Employee'}
            </h2>
            {/* Your form fields here */}
          </div>
        ) : (
          <>
            {/* Filter panel */}
            {showFilterPanel && (
              <div className="bg-white p-4 shadow-sm border border-gray-200">
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                  <input
                    type="text"
                    placeholder="Search employees..."
                    className="px-3 py-2 border border-gray-300 rounded-sm text-sm focus:border-[#0078d4] outline-none"
                  />
                  {/* More filters */}
                </div>
              </div>
            )}
            
            {/* Employee list table */}
            <div className="bg-white shadow-sm border border-gray-200">
              <table className="min-w-full">
                <thead className="bg-[#f3f2f1]">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-semibold text-[#605e5c] uppercase">
                      Employee ID
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-semibold text-[#605e5c] uppercase">
                      Name
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-semibold text-[#605e5c] uppercase">
                      Department
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-semibold text-[#605e5c] uppercase">
                      Status
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200">
                  {employees.map((emp: any) => (
                    <tr
                      key={emp.id}
                      className={`cursor-pointer transition-colors ${
                        selectedId === emp.id ? 'bg-blue-50' : 'hover:bg-[#f3f9ff]'
                      }`}
                      onClick={() => setSelectedId(emp.id)}
                    >
                      <td className="px-6 py-4 text-sm text-[#323130]">
                        {emp.employee_id}
                      </td>
                      <td className="px-6 py-4 text-sm text-[#323130]">
                        {emp.name}
                      </td>
                      <td className="px-6 py-4 text-sm text-[#323130]">
                        {emp.department}
                      </td>
                      <td className="px-6 py-4">
                        <span className="px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                          {emp.status}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </>
        )}
      </div>
    </>
  );
};
```

---

### **Example 2: Leave Request (HRM Transaction)**

#### **File**: `frontend/apps/hrm/leave/pages/LeaveRequestFormPage.tsx`

```typescript
import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { MasterToolbar, MasterMode } from '@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven';

export const LeaveRequestFormPage: React.FC = () => {
  const navigate = useNavigate();
  const { id } = useParams();
  
  // State
  const [isNew, setIsNew] = useState(!id);
  const [isEditing, setIsEditing] = useState(false);
  const [leaveRequest, setLeaveRequest] = useState<any>(null);
  
  // Determine mode
  const getMode = (): MasterMode => {
    if (isNew) return 'CREATE';
    if (isEditing) return 'EDIT';
    return 'VIEW';
  };
  
  // Handle toolbar actions
  const handleToolbarAction = (action: string) => {
    switch (action) {
      case 'new':
        navigate('/hrm/leave-requests/new');
        break;
        
      case 'edit':
        setIsEditing(true);
        break;
        
      case 'save':
        // Save logic
        console.log('Saving leave request...');
        setIsEditing(false);
        setIsNew(false);
        break;
        
      case 'cancel':
        if (isNew) {
          navigate('/hrm/leave-requests');
        } else {
          setIsEditing(false);
        }
        break;
        
      case 'submit':
        // Submit for approval
        console.log('Submitting for approval...');
        break;
        
      case 'authorize':
        // Approve leave request
        console.log('Approving leave request...');
        break;
        
      case 'reject':
        // Reject leave request
        console.log('Rejecting leave request...');
        break;
        
      case 'print':
        window.print();
        break;
        
      case 'exit':
        navigate('/hrm/leave-requests');
        break;
    }
  };
  
  return (
    <>
      {/* Toolbar */}
      <MasterToolbar
        viewId="LEAVE_REQUEST"  // Must match backend menu_id
        mode={getMode()}
        onAction={handleToolbarAction}
        hasSelection={!!id}
        showLabels={false}
      />
      
      <div className="page-container space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-xl font-semibold text-[#201f1e]">
              {isNew ? 'New Leave Request' : `Leave Request #${id}`}
            </h1>
            <p className="text-sm text-[#605e5c]">
              {isNew ? 'Create a new leave request' : 'View or edit leave request'}
            </p>
          </div>
          
          {!isNew && leaveRequest && (
            <span className="px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-700">
              {leaveRequest.status}
            </span>
          )}
        </div>
        
        {/* Form */}
        <div className="bg-white p-6 shadow-sm border border-gray-200">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Employee */}
            <div>
              <label className="block text-xs font-semibold text-[#605e5c] uppercase mb-2">
                Employee *
              </label>
              <input
                type="text"
                disabled={!isNew && !isEditing}
                className="w-full px-3 py-2 border border-gray-300 rounded-sm text-sm focus:border-[#0078d4] outline-none disabled:bg-gray-50"
              />
            </div>
            
            {/* Leave Type */}
            <div>
              <label className="block text-xs font-semibold text-[#605e5c] uppercase mb-2">
                Leave Type *
              </label>
              <select
                disabled={!isNew && !isEditing}
                className="w-full px-3 py-2 border border-gray-300 rounded-sm text-sm focus:border-[#0078d4] outline-none disabled:bg-gray-50"
              >
                <option>Select leave type...</option>
                <option>Annual Leave</option>
                <option>Sick Leave</option>
                <option>Casual Leave</option>
              </select>
            </div>
            
            {/* From Date */}
            <div>
              <label className="block text-xs font-semibold text-[#605e5c] uppercase mb-2">
                From Date *
              </label>
              <input
                type="date"
                disabled={!isNew && !isEditing}
                className="w-full px-3 py-2 border border-gray-300 rounded-sm text-sm focus:border-[#0078d4] outline-none disabled:bg-gray-50"
              />
            </div>
            
            {/* To Date */}
            <div>
              <label className="block text-xs font-semibold text-[#605e5c] uppercase mb-2">
                To Date *
              </label>
              <input
                type="date"
                disabled={!isNew && !isEditing}
                className="w-full px-3 py-2 border border-gray-300 rounded-sm text-sm focus:border-[#0078d4] outline-none disabled:bg-gray-50"
              />
            </div>
            
            {/* Reason */}
            <div className="md:col-span-2">
              <label className="block text-xs font-semibold text-[#605e5c] uppercase mb-2">
                Reason *
              </label>
              <textarea
                rows={3}
                disabled={!isNew && !isEditing}
                className="w-full px-3 py-2 border border-gray-300 rounded-sm text-sm focus:border-[#0078d4] outline-none disabled:bg-gray-50"
              />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
```

---

## 📋 PART 3: BUTTON VISIBILITY RULES

### **How MasterToolbar Filters Buttons**

The component automatically shows/hides buttons based on `mode`:

#### **VIEW Mode** (List or viewing single record)
```
Shows: N, E, V, D, X, R, Q, F, Z, T, J, A, P, M, I, O, 1234
Hides: S, C, K

Logic: User is viewing, show navigation and actions, hide form controls
```

#### **CREATE Mode** (Creating new record)
```
Shows: S, C, K, X
Hides: N, E, V, D, R, Q, F, Z, T, J, A, P, M, I, O, 1234

Logic: User is creating, show only form controls
```

#### **EDIT Mode** (Editing existing record)
```
Shows: S, C, K, X
Hides: N, E, V, D, R, Q, F, Z, T, J, A, P, M, I, O, 1234

Logic: User is editing, show only form controls
```

---

## 📋 PART 4: COMPLETE CHARACTER REFERENCE

```
N - New (F2)
E - Edit (F3)
S - Save (F8)
C - Cancel (Esc)
K - Clear (F5)
V - View (F7)
D - Delete (F4)
X - Exit (Esc)
R - Refresh (F9)
Q - Search (Ctrl+F)
F - Filter (Alt+F)
Z - Authorize (F10)
T - Submit (Alt+S)
J - Reject (Alt+R)
A - Amend (Alt+A)
P - Print (Ctrl+P)
M - Email (Ctrl+M)
I - Import (Ctrl+I)
O - Export (Ctrl+E)
1 - First (Home)
2 - Prev (PgUp)
3 - Next (PgDn)
4 - Last (End)
Y - Generate (Alt+G) - For reports
G - Attachments (Alt+U)
B - Notes (Alt+N)
? - Help (F1)
```

---

## 📋 PART 5: COMMON PATTERNS

### **Pattern 1: Simple Master (Department, Position)**

**Backend**:
```
menu_id: DEPARTMENT_MASTER
view_type: MASTER
config: NESCKVDXRQF
```

**Frontend**:
```typescript
<MasterToolbar 
  viewId="DEPARTMENT_MASTER" 
  mode={showForm ? (editingId ? 'EDIT' : 'CREATE') : 'VIEW'}
  onAction={handleAction}
/>
```

---

### **Pattern 2: Advanced Master (Employee, Contact)**

**Backend**:
```
menu_id: CONTACT_MASTER
view_type: MASTER
config: NESCKVDXRQFIO
```

**Frontend**: Same as Pattern 1, component automatically shows Import/Export buttons

---

### **Pattern 3: Transaction (Leave, Lead)**

**Backend**:
```
menu_id: LEAD
view_type: TRANSACTION
config: NESCKZTJAVPMRDX1234QF
```

**Frontend**:
```typescript
<MasterToolbar 
  viewId="LEAD" 
  mode={isNew ? 'CREATE' : isEditing ? 'EDIT' : 'VIEW'}
  onAction={handleAction}
/>
```

---

## ✅ CHECKLIST FOR AGENT E

### **For Each Screen**:

#### **Backend**:
- [ ] Create ONE ERPMenuItem entry (not separate list/form entries)
- [ ] Set `menu_id` in UPPERCASE_SNAKE_CASE
- [ ] Set `view_type` (MASTER, TRANSACTION, REPORT, etc.)
- [ ] Set `applicable_toolbar_config` based on screen type
- [ ] Set `route_path` to match frontend route

#### **Frontend**:
- [ ] Import `MasterToolbar` from correct path
- [ ] Set `viewId` to match backend `menu_id` EXACTLY
- [ ] Implement `getMode()` function returning VIEW/CREATE/EDIT
- [ ] Implement `handleToolbarAction()` for all actions
- [ ] **DO NOT** add `allowedActions` prop
- [ ] Add state for `showForm`, `editingId`, `selectedId`
- [ ] Add filter panel toggle state (if applicable)

#### **Testing**:
- [ ] VIEW mode shows correct buttons
- [ ] CREATE mode shows only S, C, K, X
- [ ] EDIT mode shows only S, C, K, X
- [ ] All keyboard shortcuts work
- [ ] Filter toggle works
- [ ] Exit navigation works

---

## 🚨 COMMON MISTAKES TO AVOID

### **❌ MISTAKE 1: Creating Separate List View Entry**
```
❌ WRONG:
ERPMenuItem(menu_id="employee-list", view_type="LIST_VIEW")
ERPMenuItem(menu_id="EMPLOYEE_MASTER", view_type="MASTER")

✅ CORRECT:
ERPMenuItem(menu_id="EMPLOYEE_MASTER", view_type="MASTER")
Frontend handles list with mode="VIEW"
```

### **❌ MISTAKE 2: Hardcoding allowedActions**
```
❌ WRONG:
<MasterToolbar 
  viewId="EMPLOYEE_MASTER"
  allowedActions={['new', 'edit', 'save']}  // ❌ Don't do this!
/>

✅ CORRECT:
<MasterToolbar 
  viewId="EMPLOYEE_MASTER"
  mode={getMode()}  // Backend drives actions
/>
```

### **❌ MISTAKE 3: Wrong viewId Case**
```
❌ WRONG:
Backend: menu_id="EMPLOYEE_MASTER"
Frontend: viewId="employee_master"  // ❌ Case mismatch!

✅ CORRECT:
Backend: menu_id="EMPLOYEE_MASTER"
Frontend: viewId="EMPLOYEE_MASTER"  // ✅ Exact match
```

---

## 📞 NEED HELP?

**Questions**:
1. "Which config string should I use?" → Check Part 2 above
2. "How do I handle workflow actions?" → See Leave Request example
3. "What if buttons don't show?" → Check viewId matches menu_id exactly
4. "Can I add custom buttons?" → No, use standard config characters only

---

**Status**: ✅ READY FOR USE  
**Last Updated**: 2026-01-09 20:05 IST  
**For**: Agent E (HRM/CRM Development)
