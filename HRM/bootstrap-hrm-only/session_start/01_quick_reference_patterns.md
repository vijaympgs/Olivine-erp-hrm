# QUICK REFERENCE PATTERNS - Session Startup File

**Purpose**: UI standards, code patterns, and common templates  
**Last Updated**: January 30, 2026

---

## 1. UI TYPOGRAPHY STANDARDS

### L1 - Page Titles
```tsx
<h1 className="text-xl font-semibold text-[#201f1e]">
    Employee Directory
</h1>
```
- Font Size: `20px` / `text-xl`
- Font Weight: `600` / `font-semibold`
- Color: `#201f1e` (dark gray)

### L2 - Section Headers
```tsx
<h2 className="text-base font-semibold text-[#323130]">
    Personal Information
</h2>
```
- Font Size: `16px` / `text-base`
- Font Weight: `600` / `font-semibold`
- Color: `#323130` (medium gray)

### L3 - Field Labels
```tsx
<label className="text-xs font-semibold text-[#605e5c] uppercase">
    Employee Name *
</label>
```
- Font Size: `12px` / `text-xs`
- Font Weight: `600` / `font-semibold`
- Color: `#605e5c` (gray)
- Text Transform: `uppercase`

### L4 - Body Text
```tsx
<p className="text-sm text-[#323130]">
    Regular content text
</p>
```
- Font Size: `14px` / `text-sm`
- Color: `#323130` (medium gray)

---

## 2. FORM ELEMENTS

### Text Input (Standard)
```tsx
<input 
    type="text" 
    className="w-full px-3 py-2 border border-gray-300 rounded-sm text-sm focus:border-[#0078d4] focus:ring-1 focus:ring-[#0078d4] outline-none" 
/>
```
- Font Size: `14px` / `text-sm`
- Padding: `px-3 py-2` (12px horizontal, 8px vertical)
- Border: `1px solid #d1d1d1` / `border-gray-300`
- Border Radius: `2px` / `rounded-sm`
- Focus Border: `#0078d4` (blue)
- Focus Ring: `1px solid #0078d4`

### Select Dropdown (LOV)
```tsx
<select className="w-full px-3 py-2 border border-gray-300 rounded-sm text-sm focus:border-[#0078d4] outline-none">
    <option>Select Department...</option>
</select>
```
- Font Size: `14px` / `text-sm`
- Padding: `px-3 py-2`
- Border: `1px solid #d1d1d1` / `border-gray-300`
- Focus Border: `#0078d4` (blue)

### Checkbox
```tsx
<label className="flex items-center gap-2">
    <input 
        type="checkbox" 
        className="w-4 h-4 text-[#0078d4] border-gray-300 rounded focus:ring-[#0078d4]" 
    />
    <span className="text-sm text-[#323130]">Active</span>
</label>
```
- Checkbox Size: `16px` / `w-4 h-4`
- Checked Color: `#0078d4` (blue)
- Border: `1px solid #d1d1d1` / `border-gray-300`
- Label Font Size: `14px` / `text-sm`
- Label Color: `#323130` (medium gray)

### Radio Button
```tsx
<label className="flex items-center gap-2">
    <input 
        type="radio" 
        className="w-4 h-4 text-[#0078d4] border-gray-300 focus:ring-[#0078d4]" 
    />
    <span className="text-sm text-[#323130]">Full-time</span>
</label>
```
- Radio Size: `16px` / `w-4 h-4`
- Checked Color: `#0078d4` (blue)
- Border: `1px solid #d1d1d1` / `border-gray-300`
- Label Font Size: `14px` / `text-sm`
- Label Color: `#323130` (medium gray)

---

## 3. BUTTONS

### Primary Button
```tsx
<button 
    style={{ 
        backgroundColor: 'var(--button-primary-bg)', /* #ff6600 */
        color: 'var(--button-primary-text)' /* #ffffff */
    }} 
    className="px-3 py-1.5 font-medium rounded-sm" 
>
    Save
</button>
```
- Background: `#ff6600` (orange) / `var(--button-primary-bg)`
- Text Color: `#ffffff` (white) / `var(--button-primary-text)`
- Hover Background: `#e65c00` (darker orange) / `var(--button-primary-hover-bg)`
- Font Size: `14px` / `text-sm`
- Font Weight: `500` / `font-medium`
- Padding: `px-3 py-1.5` (12px horizontal, 6px vertical)
- Border Radius: `2px` / `rounded-sm`

### Secondary Button
```tsx
<button className="px-3 py-1.5 hover:bg-[#edebe9] rounded-sm text-[#323130] font-medium">
    Cancel
</button>
```
- Background: `transparent`
- Text Color: `#323130` (medium gray)
- Hover Background: `#edebe9` (light gray)
- Font Size: `14px` / `text-sm`
- Font Weight: `500` / `font-medium`
- Padding: `px-3 py-1.5`
- Border Radius: `2px` / `rounded-sm`

---

## 4. STATUS BADGES

```tsx
<span className="px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
    ACTIVE
</span>
```

**Status Colors:**
- **ACTIVE**: `bg-green-100 text-green-800`
- **PENDING**: `bg-yellow-100 text-yellow-700`
- **APPROVED**: `bg-blue-100 text-blue-700`
- **REJECTED**: `bg-red-100 text-red-700`
- **DRAFT**: `bg-gray-100 text-gray-700`

---

## 5. COLOR PALETTE

### Primary Colors
```css
--primary-blue: #0078d4      /* Links, focus states */
--primary-orange: #ff6600    /* Primary buttons */
```

### Text Colors
```css
--text-dark: #201f1e         /* Page titles */
--text-medium: #323130       /* Body text */
--text-gray: #605e5c         /* Labels */
--text-light: #a19f9d        /* Placeholder */
```

### Background Colors
```css
--bg-white: #ffffff          /* Cards, modals */
--bg-light: #faf9f8          /* Page background */
--bg-gray: #f3f2f1           /* Table headers */
--bg-blue-light: #f3f9ff     /* Row hover */
```

### Border Colors
```css
--border-light: #edebe9      /* Card borders */
--border-medium: #d1d1d1     /* Input borders */
--border-focus: #0078d4      /* Focus state */
```

---

## 6. TOOLBAR ARCHITECTURE

### ⚠️ CRITICAL: Toolbar Configuration Source

**Toolbar configuration is stored in the `erp_menu_items` table in the database**

Four mode-specific columns:
- `toolbar_list` - LIST mode (e.g., 'NRQFVIOX')
- `toolbar_view` - VIEW mode (e.g., 'X')
- `toolbar_edit` - EDIT mode (e.g., 'SCX')
- `toolbar_create` - CREATE mode (e.g., 'SCX')

### Character Codes
- N = New, E = Edit, R = Refresh, Q = Query/Search, F = Filter, X = Exit
- V = View, D = Delete, I = Import, O = Export, L = Clone
- B = Notes, U = Attach, G = Help, S = Save, C = Cancel, K = Clear
- A = Authorize, T = Submit, J = Reject, W = Amend, P = Print, M = Email
- 1 = First, 2 = Previous, 3 = Next, 4 = Last, H = Hold, Z = Void

### Frontend Implementation Pattern
```typescript
// In useToolbarConfig.ts or similar hook
const ERP_MENU_ITEMS = {
  'EMPLOYEE_RECORDS': {
    toolbar_list: 'NRQFVIOX',
    toolbar_view: 'X',
    toolbar_edit: 'SCX',
    toolbar_create: 'SCX',
  },
  // Add more menu items as needed
};

// Get mode-specific config
const modeColumn = `toolbar_${mode.toLowerCase()}`;
const toolbarConfig = menuItem[modeColumn];

// Parse character codes to action IDs
const actions = parseConfigString(toolbarConfig);
```

### ⚠️ DEADEND WARNING
If you find yourself creating a backend API for toolbar permissions, **STOP IMMEDIATELY**. This is the wrong approach. The toolbar configuration must come from the ERP Menu Item table that's already loaded in the app.

---

## 7. WIRING CHECKLISTS SUMMARY

### Master Data Wiring (11 Phases)
Use for: Employee Master, Department, Position, Contact, Account, etc.

1. Backend Model & Serializer
2. Backend ViewSet & URLs
3. Frontend Types
4. Frontend Service Layer
5. Main Component Structure
6. State Management
7. Data Fetching
8. UI Layout (List Page)
9. Action Handlers (Add, Edit, Delete)
10. Modal Integration
11. Testing & Validation

### Transaction Form Wiring (14 Phases)
Use for: Leave Request, Attendance Adjustment, Lead, Opportunity, Campaign, etc.

1. Backend Model & Serializer
2. Backend ViewSet with Workflow
3. Frontend Types
4. Frontend Service Layer
5. Form Page Component Structure
6. **TransactionToolbar Integration** ⚠️ IMPORTANT
7. Header Section
8. Line Items Grid (if applicable)
9. Lookup Modals
10. Workflow Actions
11. Status State Machine
12. Real-time Calculations
13. Validation & Error Handling
14. Testing

### Workflow Wiring (10 Phases)
Use for: Leave approval, Attendance workflow, Lead qualification, Opportunity stages, etc.

1. Status State Machine Definition
2. Backend Workflow Actions
3. Frontend Workflow Service
4. Status-based UI States
5. Action Buttons & Toolbar
6. Validation Rules
7. Authorization & Permissions
8. Audit Trail
9. Notifications
10. Testing

---

## 8. HRM FEATURE TEMPLATES

### Master Data Templates
- **Employee Master** → Use `MST-M` (Medium Master Template)
- **Department** → Use `MST-S` (Simple Master Template)
- **Position** → Use `MST-S` (Simple Master Template)
- **Organizational Unit** → Use `MST-M` (Medium Master Template)

### Transaction Templates
- **Leave Request** → Use `TXN-M` (Medium Transaction Template)
- **Attendance Adjustment** → Use `TXN-S` (Simple Transaction Template)
- **Expense Claim** → Use `TXN-M` (Medium Transaction Template)
- **Performance Review** → Use `TXN-C` (Complex Transaction Template)

---

## 9. REFERENCE IMPLEMENTATIONS

### For Master Data Pages
**Reference**: `frontend/src/pages/CustomerSetup.tsx`

**Copy for**: Employee, Department, Position, Contact, Account, etc.

**Pattern**:
- List view with search and filters
- "Add New" button (primary orange)
- Table with hover states
- Edit/Delete actions
- Modal for add/edit

### For Transaction Forms
**Reference**: `retail/frontend/procurement/pages/PurchaseOrderFormPage.tsx`

**Copy for**: Leave Request, Attendance Adjustment, Lead, Opportunity, etc.

**Pattern**:
- TransactionToolbar at top
- Header section with fields
- Line items grid (if applicable)
- Workflow actions (Save, Submit, Approve, etc.)
- Status state machine

---

## 10. TESTING TOOLS

### Interactive Toolbar Inspector
**File**: `HRM/bootstrap-hrm-only/99_toolbar_explorer_hrm.html`

**Purpose**: Test toolbar configurations before implementation

**Usage**: Open in browser to inspect toolbar behavior

---

**END OF QUICK REFERENCE PATTERNS**

**Next**: Read `02_governance_rules_summary.md` for governance rules
