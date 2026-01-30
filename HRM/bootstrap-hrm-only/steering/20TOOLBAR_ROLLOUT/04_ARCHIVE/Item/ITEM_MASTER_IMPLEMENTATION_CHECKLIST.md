# 📘 **ITEM MASTER - TOOLBAR IMPLEMENTATION & VERIFICATION CHECKLIST**

**Screen**: Item Master Setup  
**Path**: `/retail/inventory/item-master-setup`  
**Menu ID**: `ITEM_MASTER`  
**Toolbar Config**: `NESCKVDXRQF`  
**Screen Type**: MASTER (List + Form)  
**Reference**: UOM Setup (Gold Standard)  
**Created**: 2026-01-10 14:45 IST

---

## 🎯 **IMPLEMENTATION OVERVIEW**

This checklist provides a **step-by-step guide** to apply the UOM Gold Standard pattern to the Item Master screen. Follow each phase sequentially to ensure complete compliance with the canonical architecture.

---

## 📋 **PHASE 1: PRE-IMPLEMENTATION AUDIT**

### **1.1 Current State Assessment**

- [ ] **Locate Current File**: `retail/frontend/inventory/pages/ItemMasterSetup.tsx`
- [ ] **Review Existing Structure**: Document current toolbar implementation (if any)
- [ ] **Identify Form Component**: Locate `ItemForm.tsx` or equivalent
- [ ] **Check Service Layer**: Verify `itemService.ts` exists with CRUD methods
- [ ] **Backend API Verification**: Confirm `/api/items/` endpoint exists with pagination
- [ ] **Menu Registry Check**: Verify `ITEM_MASTER` menu ID in `ERP Menu Items` table

### **1.2 Dependencies Verification**

- [ ] **MasterToolbar Import**: Verify `@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven` is accessible
- [ ] **Service Methods**: Confirm itemService has:
  - `getItems(filters)` - Returns paginated list
  - `getItemById(id)` - Returns single item
  - `createItem(data)` - Creates new item
  - `updateItem(id, data)` - Updates existing item
  - `deleteItem(id)` - Soft deletes item (sets is_active=false)
  - `checkItemUsage(id)` - Checks if item is used in transactions (optional)

### **1.3 Backup Current Implementation**

- [ ] **Create Backup**: Copy current `ItemMasterSetup.tsx` to `.backups/ItemMasterSetup_BEFORE_TOOLBAR_ROLLOUT.tsx`
- [ ] **Document Custom Logic**: Note any custom business logic that must be preserved
- [ ] **Screenshot Current UI**: Capture current state for comparison

---

## 📋 **PHASE 2: COMPONENT STRUCTURE IMPLEMENTATION**

### **2.1 State Management Setup**

Implement the following state variables in `ItemMasterSetup.tsx`:

```typescript
// Core UI State
const [showForm, setShowForm] = useState<boolean>(false);
const [editingId, setEditingId] = useState<string | null>(null);
const [selectedItemId, setSelectedItemId] = useState<string | null>(null);
const [viewMode, setViewMode] = useState<boolean>(false);

// Data State
const [items, setItems] = useState<ItemListItem[]>([]);
const [loading, setLoading] = useState<boolean>(false);
const [error, setError] = useState<string | null>(null);

// Filter State
const [showFilterPanel, setShowFilterPanel] = useState<boolean>(false);
const [searchTerm, setSearchTerm] = useState<string>('');
const [filters, setFilters] = useState<ItemFilters>({
  company_id: null,
  category: null,
  status: 'active',
  item_type: null,
});

// Form Reference
const formRef = useRef<any>(null);
```

**Checklist**:
- [ ] All state variables declared
- [ ] TypeScript types properly imported
- [ ] Form ref created with `useRef`

### **2.2 Mode Helper Function**

Implement the `getToolbarMode()` helper:

```typescript
const getToolbarMode = (): MasterMode => {
  if (!showForm) return 'VIEW';           // List view
  if (viewMode) return 'VIEW_FORM';       // Read-only populated form
  return editingId ? 'EDIT' : 'CREATE';  // Editable form (Edit existing vs New)
};
```

**Checklist**:
- [ ] Function implemented
- [ ] Returns correct mode based on state
- [ ] Handles all four modes: VIEW, VIEW_FORM, EDIT, CREATE

### **2.3 Toolbar Integration**

Place the toolbar at the top of the component:

```typescript
return (
  <>
    {/* Toolbar - Fixed at top, outside page-container */}
    <MasterToolbar
      viewId="ITEM_MASTER"
      mode={getToolbarMode()}
      onAction={handleToolbarAction}
      hasSelection={!!selectedItemId}
    />

    {/* Rest of the page content */}
    <div className="flex flex-col h-[calc(100vh-var(--toolbar-height))]">
      {/* Fixed Header Section */}
      <div className="max-w-[80rem] mx-auto w-full px-6 pt-6 pb-0">
        {/* Page Title, Breadcrumbs, Filters */}
      </div>

      {/* Scrollable Content Section */}
      <div className="flex-1 overflow-y-auto hairline-scrollbar">
        <div className="max-w-[80rem] mx-auto w-full px-6 pt-0">
          {showForm ? (
            <ItemForm
              itemId={editingId}
              readOnly={viewMode}
              ref={formRef}
              onSuccess={handleFormSuccess}
              onCancel={handleFormCancel}
            />
          ) : (
            <ItemListTable />
          )}
        </div>
      </div>
    </div>
  </>
);
```

**Checklist**:
- [ ] Toolbar placed outside page-container
- [ ] Toolbar has `sticky top-0 z-[100]` positioning
- [ ] Toolbar has solid background (no transparency)
- [ ] Decoupled scrolling implemented (fixed header, scrollable content)
- [ ] `.hairline-scrollbar` class applied to scrollable container
- [ ] Surgical spacing achieved (one-line gap between sections)

---

## 📋 **PHASE 3: ACTION HANDLERS IMPLEMENTATION**

### **3.1 CRUD Handlers**

Implement the core CRUD handlers:

```typescript
// CREATE
const handleCreate = () => {
  setEditingId(null);
  setViewMode(false);
  setShowForm(true);
  setSelectedItemId(null);
};

// EDIT
const handleEdit = (id: string) => {
  setEditingId(id);
  setViewMode(false);
  setShowForm(true);
};

// VIEW (Read-only)
const handleView = (id: string) => {
  setEditingId(id);
  setViewMode(true);
  setShowForm(true);
};

// DELETE (Soft delete with pre-check)
const handleDelete = async (id: string) => {
  try {
    // Optional: Check if item is used in transactions
    // const usage = await itemService.checkItemUsage(id);
    // if (usage.isUsed) {
    //   alert(`Cannot delete: Item is used in ${usage.count} transactions`);
    //   return;
    // }

    if (window.confirm('Are you sure you want to deactivate this item?')) {
      await itemService.deleteItem(id);
      await loadItems();
      setSelectedItemId(null);
    }
  } catch (err: any) {
    setError(err.message || 'Failed to delete item');
  }
};
```

**Checklist**:
- [ ] `handleCreate` implemented
- [ ] `handleEdit` implemented
- [ ] `handleView` implemented (with viewMode=true)
- [ ] `handleDelete` implemented with confirmation
- [ ] Optional: Pre-delete usage check implemented
- [ ] Error handling in place

### **3.2 Form Lifecycle Handlers**

```typescript
const handleFormSuccess = async () => {
  setShowForm(false);
  setEditingId(null);
  setViewMode(false);
  await loadItems();
  // Optional: Show success message
};

const handleFormCancel = () => {
  setShowForm(false);
  setEditingId(null);
  setViewMode(false);
};
```

**Checklist**:
- [ ] `handleFormSuccess` implemented
- [ ] `handleFormCancel` implemented
- [ ] Form state properly reset on success/cancel
- [ ] List reloaded after successful save

### **3.3 Centralized Toolbar Action Handler**

Implement the master switch-case handler:

```typescript
const handleToolbarAction = (action: string) => {
  switch (action) {
    // VIEW MODE ACTIONS
    case 'new':
      if (!showForm) handleCreate();
      break;

    case 'edit':
      if (selectedItemId && !showForm) handleEdit(selectedItemId);
      break;

    case 'view':
      if (selectedItemId && !showForm) handleView(selectedItemId);
      break;

    case 'delete':
      if (selectedItemId && !showForm) {
        const item = items.find(i => i.id === selectedItemId);
        if (item) handleDelete(item.id);
      }
      break;

    case 'refresh':
      loadItems();
      break;

    case 'search':
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

    // FORM MODE ACTIONS
    case 'save':
      if (showForm) formRef.current?.submit();
      break;

    case 'cancel':
      handleFormCancel();
      break;

    case 'clear':
      if (showForm) {
        formRef.current?.reset();
      } else {
        // In VIEW mode, clear selection
        setSelectedItemId(null);
        setSearchTerm('');
      }
      break;

    case 'exit':
      if (showForm) {
        handleFormCancel();
      } else {
        navigate('/dashboard');
      }
      break;

    default:
      console.warn(`Unhandled toolbar action: ${action}`);
  }
};
```

**Checklist**:
- [ ] All VIEW mode actions implemented (N, E, V, D, R, Q, F, Import, Export, X)
- [ ] All FORM mode actions implemented (S, C, K, X)
- [ ] Selection checks in place for Edit/View/Delete
- [ ] Form ref methods called correctly (submit, reset)
- [ ] Smart Exit logic (cancel form if open, else navigate to dashboard)
- [ ] Default case for unhandled actions

---

## 📋 **PHASE 4: LIST VIEW IMPLEMENTATION**

### **4.1 Row Selection Logic**

```typescript
<tr
  onClick={() => setSelectedItemId(item.id)}
  className={`cursor-pointer transition-colors ${
    selectedItemId === item.id 
      ? 'bg-blue-100 border-l-4 border-blue-500' 
      : 'hover:bg-blue-50'
  }`}
>
  {/* Table cells */}
</tr>
```

**Checklist**:
- [ ] Row click handler sets `selectedItemId`
- [ ] Selected row has distinct background color (`bg-blue-100`)
- [ ] Hover state for non-selected rows (`hover:bg-blue-50`)
- [ ] Visual indicator (e.g., left border) for selected row
- [ ] Cursor changes to pointer on hover

### **4.2 Table Structure**

Implement a clean, high-density table:

```typescript
<table className="w-full border-collapse">
  <thead className="bg-slate-100 sticky top-0 z-10">
    <tr>
      <th className="px-3 py-2 text-left text-xs font-semibold text-slate-700">SKU</th>
      <th className="px-3 py-2 text-left text-xs font-semibold text-slate-700">Item Name</th>
      <th className="px-3 py-2 text-left text-xs font-semibold text-slate-700">Category</th>
      <th className="px-3 py-2 text-left text-xs font-semibold text-slate-700">Type</th>
      <th className="px-3 py-2 text-right text-xs font-semibold text-slate-700">Price</th>
      <th className="px-3 py-2 text-center text-xs font-semibold text-slate-700">Stock</th>
      <th className="px-3 py-2 text-center text-xs font-semibold text-slate-700">Status</th>
    </tr>
  </thead>
  <tbody>
    {items.map(item => (
      <tr key={item.id} onClick={() => setSelectedItemId(item.id)} className={...}>
        <td className="px-3 py-2 text-sm border-t border-slate-200">{item.sku}</td>
        <td className="px-3 py-2 text-sm border-t border-slate-200">{item.name}</td>
        <td className="px-3 py-2 text-sm border-t border-slate-200">{item.category}</td>
        <td className="px-3 py-2 text-sm border-t border-slate-200">{item.item_type}</td>
        <td className="px-3 py-2 text-sm border-t border-slate-200 text-right font-feature-settings-tnum">
          {item.price?.toFixed(2)}
        </td>
        <td className="px-3 py-2 text-sm border-t border-slate-200 text-center">{item.stock_qty}</td>
        <td className="px-3 py-2 text-sm border-t border-slate-200 text-center">
          {getStatusBadge(item.status)}
        </td>
      </tr>
    ))}
  </tbody>
</table>
```

**Checklist**:
- [ ] Table uses `border-collapse` for clean borders
- [ ] Header row is sticky (`sticky top-0`)
- [ ] Typography follows standards (12-13px for table text)
- [ ] Numeric columns use tabular numerals (`font-feature-settings: "tnum"`)
- [ ] Proper alignment (left for text, right for numbers, center for status)
- [ ] Consistent padding (px-3 py-2)
- [ ] Border styling matches UOM standard

### **4.3 Empty State**

```typescript
{items.length === 0 && !loading && (
  <tr>
    <td colSpan={7} className="px-6 py-12 text-center text-slate-500">
      <Box className="mx-auto h-12 w-12 text-slate-300 mb-3" />
      <p className="text-sm">No items found</p>
      <p className="text-xs mt-1">Click "New" to create your first item</p>
    </td>
  </tr>
)}
```

**Checklist**:
- [ ] Empty state message displayed when no items
- [ ] Icon included for visual clarity
- [ ] Helpful guidance text provided
- [ ] Proper colspan to span all columns

---

## 📋 **PHASE 5: FILTER PANEL IMPLEMENTATION**

### **5.1 Filter Panel Structure**

```typescript
{showFilterPanel && (
  <div className="bg-slate-50 border border-slate-200 rounded-md p-4 mb-4">
    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
      {/* Company Filter */}
      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">
          Company
        </label>
        <select
          value={filters.company_id || ''}
          onChange={(e) => handleFilterChange('company_id', e.target.value)}
          className="w-full h-9 rounded-md border border-slate-300 px-3 text-sm"
        >
          <option value="">All Companies</option>
          {/* Company options */}
        </select>
      </div>

      {/* Category Filter */}
      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">
          Category
        </label>
        <select
          value={filters.category || ''}
          onChange={(e) => handleFilterChange('category', e.target.value)}
          className="w-full h-9 rounded-md border border-slate-300 px-3 text-sm"
        >
          <option value="">All Categories</option>
          {/* Category options */}
        </select>
      </div>

      {/* Item Type Filter */}
      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">
          Item Type
        </label>
        <select
          value={filters.item_type || ''}
          onChange={(e) => handleFilterChange('item_type', e.target.value)}
          className="w-full h-9 rounded-md border border-slate-300 px-3 text-sm"
        >
          <option value="">All Types</option>
          <option value="STOCK">Stock Item</option>
          <option value="SERVICE">Service</option>
          <option value="NON_STOCK">Non-Stock</option>
        </select>
      </div>

      {/* Status Filter */}
      <div>
        <label className="block text-xs font-medium text-slate-600 mb-1">
          Status
        </label>
        <select
          value={filters.status || ''}
          onChange={(e) => handleFilterChange('status', e.target.value)}
          className="w-full h-9 rounded-md border border-slate-300 px-3 text-sm"
        >
          <option value="active">Active Only</option>
          <option value="all">Include Inactive</option>
        </select>
      </div>
    </div>
  </div>
)}
```

**Checklist**:
- [ ] Filter panel toggles with Filter button
- [ ] All relevant filters included (Company, Category, Type, Status)
- [ ] Filter changes trigger list reload
- [ ] Consistent styling with UOM standard
- [ ] Responsive grid layout (1 col mobile, 4 cols desktop)

---

## 📋 **PHASE 6: FORM INTEGRATION**

### **6.1 Form Component Props**

Ensure `ItemForm` component accepts these props:

```typescript
interface ItemFormProps {
  itemId?: string | null;
  readOnly?: boolean;
  ref?: React.Ref<any>;
  onSuccess?: () => void;
  onCancel?: () => void;
}
```

**Checklist**:
- [ ] `itemId` prop for edit mode
- [ ] `readOnly` prop for view mode
- [ ] Form ref exposed for submit/reset methods
- [ ] `onSuccess` callback implemented
- [ ] `onCancel` callback implemented

### **6.2 Read-Only Mode Implementation**

In `ItemForm.tsx`, implement read-only mode:

```typescript
<input
  type="text"
  value={formData.name}
  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
  disabled={readOnly}
  className={`w-full h-9 rounded-md border px-3 text-sm ${
    readOnly 
      ? 'bg-slate-100 text-slate-600 cursor-not-allowed' 
      : 'border-slate-300'
  }`}
/>
```

**Checklist**:
- [ ] All input fields respect `readOnly` prop
- [ ] Disabled fields have distinct styling (grayed out)
- [ ] Read-only banner displayed at top of form
- [ ] Save/Cancel buttons hidden in read-only mode (handled by toolbar)

---

## 📋 **PHASE 7: VISUAL POLISH**

### **7.1 Decoupled Scrolling**

**Checklist**:
- [ ] Toolbar remains fixed at top during scroll
- [ ] Page title and breadcrumbs remain fixed
- [ ] Filter panel remains fixed (if in header section)
- [ ] Only table/form area scrolls
- [ ] No double scrollbars
- [ ] Scrollbar is thin and styled (`.hairline-scrollbar`)

### **7.2 Surgical Spacing**

**Checklist**:
- [ ] Exactly one line gap between filter panel and table
- [ ] No unexpected whitespace from `.page-container`
- [ ] Consistent padding throughout (px-6 for horizontal)
- [ ] Header section has `pb-0`
- [ ] Scrollable section has `pt-0`

### **7.3 Loading States**

```typescript
{loading && (
  <div className="flex items-center justify-center py-12">
    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
    <span className="ml-3 text-sm text-slate-600">Loading items...</span>
  </div>
)}
```

**Checklist**:
- [ ] Loading spinner displayed during data fetch
- [ ] Toolbar remains visible during loading
- [ ] Loading state doesn't break layout
- [ ] Smooth transition from loading to data display

### **7.4 Error Handling**

```typescript
{error && (
  <div className="bg-red-50 border border-red-200 rounded-md p-4 mb-4">
    <div className="flex items-center justify-between">
      <div className="flex items-center">
        <AlertCircle className="h-5 w-5 text-red-600 mr-2" />
        <span className="text-sm text-red-800">{error}</span>
      </div>
      <button
        onClick={() => setError(null)}
        className="text-red-600 hover:text-red-800"
      >
        <X className="h-4 w-4" />
      </button>
    </div>
  </div>
)}
```

**Checklist**:
- [ ] Error messages displayed prominently
- [ ] Error banner has close button
- [ ] Error state doesn't break layout
- [ ] Errors are dismissible

---

## 📋 **PHASE 8: KEYBOARD SHORTCUTS**

### **8.1 Shortcut Implementation**

```typescript
useEffect(() => {
  const handleKeyDown = (e: KeyboardEvent) => {
    // F2 - New
    if (e.key === 'F2' && !showForm) {
      e.preventDefault();
      handleCreate();
    }
    
    // F3 - Edit
    if (e.key === 'F3' && selectedItemId && !showForm) {
      e.preventDefault();
      handleEdit(selectedItemId);
    }
    
    // F5 - Clear
    if (e.key === 'F5' && showForm) {
      e.preventDefault();
      formRef.current?.reset();
    }
    
    // F7 - View
    if (e.key === 'F7' && selectedItemId && !showForm) {
      e.preventDefault();
      handleView(selectedItemId);
    }
    
    // F8 - Save
    if (e.key === 'F8' && showForm) {
      e.preventDefault();
      formRef.current?.submit();
    }
    
    // ESC - Cancel/Exit
    if (e.key === 'Escape') {
      e.preventDefault();
      handleToolbarAction('exit');
    }
  };

  window.addEventListener('keydown', handleKeyDown);
  return () => window.removeEventListener('keydown', handleKeyDown);
}, [showForm, selectedItemId, editingId]);
```

**Checklist**:
- [ ] F2 (New) shortcut works
- [ ] F3 (Edit) shortcut works (with selection check)
- [ ] F5 (Clear) shortcut works
- [ ] F7 (View) shortcut works (with selection check)
- [ ] F8 (Save) shortcut works
- [ ] ESC (Cancel/Exit) shortcut works
- [ ] Shortcuts don't interfere with browser defaults
- [ ] Event listener properly cleaned up

---

## 📋 **PHASE 9: POST-IMPLEMENTATION VERIFICATION**

### **9.1 Functional Testing**

**VIEW Mode Tests**:
- [ ] New button creates empty form
- [ ] Edit button opens form with selected item data (requires selection)
- [ ] View button opens read-only form (requires selection)
- [ ] Delete button deactivates item with confirmation (requires selection)
- [ ] Refresh button reloads list
- [ ] Search button focuses search input
- [ ] Filter button toggles filter panel
- [ ] Import button shows placeholder message
- [ ] Export button shows placeholder message
- [ ] Exit button navigates to dashboard

**CREATE Mode Tests**:
- [ ] Save button creates new item and returns to list
- [ ] Cancel button discards form and returns to list
- [ ] Clear button resets all form fields
- [ ] Exit button navigates to dashboard (discards form)
- [ ] Form validation works (required fields, unique constraints)
- [ ] Success message shown after save

**EDIT Mode Tests**:
- [ ] Save button updates item and returns to list
- [ ] Cancel button discards changes and returns to list
- [ ] Clear button resets form to original values
- [ ] Exit button navigates to dashboard (discards changes)
- [ ] Form pre-populated with correct item data

**VIEW_FORM Mode Tests**:
- [ ] All fields are disabled and grayed out
- [ ] Read-only banner displayed
- [ ] No Save/Cancel buttons visible (only Exit)
- [ ] Data displayed correctly

### **9.2 Selection Behavior Tests**

- [ ] Clicking a row selects it (blue highlight)
- [ ] Clicking another row changes selection
- [ ] Edit/View/Delete buttons disabled when no selection
- [ ] Edit/View/Delete buttons enabled when row selected
- [ ] Selection persists during filter changes
- [ ] Selection cleared after refresh
- [ ] Selection cleared after delete

### **9.3 Visual Verification**

- [ ] Toolbar is sticky at top
- [ ] Toolbar has solid background (no transparency)
- [ ] Decoupled scrolling works (header fixed, content scrolls)
- [ ] Hairline scrollbar visible and styled
- [ ] One-line gap between sections (surgical spacing)
- [ ] Selected row has distinct highlight
- [ ] Hover states work on non-selected rows
- [ ] Typography follows standards (Inter font, correct sizes)
- [ ] Numeric columns use tabular numerals
- [ ] Status badges have appropriate colors
- [ ] Loading spinner displays correctly
- [ ] Error messages display correctly with close button

### **9.4 Keyboard Shortcut Tests**

- [ ] F2 creates new item
- [ ] F3 edits selected item
- [ ] F5 clears form (in form mode)
- [ ] F7 views selected item (read-only)
- [ ] F8 saves form
- [ ] ESC cancels form or exits to dashboard

### **9.5 Responsive Design Tests**

- [ ] Layout works on desktop (1920px)
- [ ] Layout works on laptop (1366px)
- [ ] Layout works on tablet (768px)
- [ ] Filter panel stacks properly on mobile
- [ ] Table scrolls horizontally on small screens (if needed)
- [ ] No horizontal scrollbar on toolbar

### **9.6 Data Integrity Tests**

- [ ] New items appear in list after creation
- [ ] Updated items reflect changes in list
- [ ] Deleted items removed from list (or marked inactive)
- [ ] Pagination works correctly (if implemented)
- [ ] Filters work correctly (Company, Category, Type, Status)
- [ ] Search works correctly
- [ ] Data persists after page refresh

### **9.7 Error Handling Tests**

- [ ] Network error shows error message
- [ ] Validation errors display on form fields
- [ ] Duplicate SKU shows error
- [ ] Required field validation works
- [ ] Error messages are dismissible
- [ ] Errors don't break UI layout

### **9.8 Performance Tests**

- [ ] List loads in < 2 seconds
- [ ] Form opens instantly
- [ ] No lag when selecting rows
- [ ] Smooth scrolling performance
- [ ] No memory leaks (check DevTools)

---

## 📋 **PHASE 10: DOCUMENTATION & HANDOFF**

### **10.1 Code Documentation**

- [ ] Add JSDoc comments to all handler functions
- [ ] Document complex logic with inline comments
- [ ] Update component prop types with descriptions
- [ ] Add README in module folder if needed

### **10.2 User Documentation**

- [ ] Create user guide for Item Master screen
- [ ] Document all toolbar actions and shortcuts
- [ ] Add screenshots of key workflows
- [ ] Document validation rules and constraints

### **10.3 Technical Documentation**

- [ ] Update `.steering/20TOOLBAR_ROLLOUT/IMPLEMENTATION_COMPLETE.md`
- [ ] Add Item Master to completed modules list
- [ ] Document any deviations from UOM standard
- [ ] Note any custom business logic

### **10.4 Handoff Checklist**

- [ ] All tests passed
- [ ] Code reviewed and approved
- [ ] No console errors or warnings
- [ ] No TypeScript errors
- [ ] Git commit with clear message
- [ ] Pull request created (if applicable)
- [ ] Stakeholder demo completed
- [ ] User acceptance testing completed

---

## 🎯 **QUICK REFERENCE: TOOLBAR CONFIG**

### **Toolbar String**: `NESCKVDXRQF`

| Char | Action | VIEW Mode | CREATE Mode | EDIT Mode | VIEW_FORM Mode |
|------|--------|-----------|-------------|-----------|----------------|
| **N** | New | ✅ | ❌ | ❌ | ❌ |
| **E** | Edit | ✅ (selection) | ❌ | ❌ | ❌ |
| **S** | Save | ❌ | ✅ | ✅ | ❌ |
| **C** | Cancel | ❌ | ✅ | ✅ | ❌ |
| **K** | Clear | ❌ | ✅ | ✅ | ❌ |
| **V** | View | ✅ (selection) | ❌ | ❌ | ❌ |
| **D** | Delete | ✅ (selection) | ❌ | ❌ | ❌ |
| **X** | Exit | ✅ | ✅ | ✅ | ✅ |
| **R** | Refresh | ✅ | ❌ | ❌ | ❌ |
| **Q** | Search | ✅ | ❌ | ❌ | ❌ |
| **F** | Filter | ✅ | ❌ | ❌ | ❌ |

---

## 🚨 **COMMON PITFALLS TO AVOID**

1. **❌ Clicking a row does NOT open the form** - It only selects the row. User must then click Edit or View.
2. **❌ Don't use `.page-container` for surgical spacing** - Use raw Tailwind with max-width and centering.
3. **❌ Don't forget `hasSelection` prop** - Toolbar needs this to enable/disable selection-dependent buttons.
4. **❌ Don't hardcode button visibility** - Let `MasterToolbar` handle it based on mode and config.
5. **❌ Don't skip the form ref** - Toolbar needs it to trigger submit/reset.
6. **❌ Don't forget read-only mode** - View button must open form in read-only state.
7. **❌ Don't skip keyboard shortcuts** - They're essential for power users.
8. **❌ Don't forget error dismissal** - All error messages must have a close button.
9. **❌ Don't skip the hairline scrollbar** - It's part of the premium aesthetic.
10. **❌ Don't forget to clear selection after delete/refresh** - Prevents stale selection state.

---

## 📊 **PROGRESS TRACKER**

Use this to track your implementation progress:

- [ ] **Phase 1**: Pre-Implementation Audit (0/3 sections)
- [ ] **Phase 2**: Component Structure (0/3 sections)
- [ ] **Phase 3**: Action Handlers (0/3 sections)
- [ ] **Phase 4**: List View (0/3 sections)
- [ ] **Phase 5**: Filter Panel (0/1 section)
- [ ] **Phase 6**: Form Integration (0/2 sections)
- [ ] **Phase 7**: Visual Polish (0/4 sections)
- [ ] **Phase 8**: Keyboard Shortcuts (0/1 section)
- [ ] **Phase 9**: Post-Implementation Verification (0/8 sections)
- [ ] **Phase 10**: Documentation & Handoff (0/4 sections)

**Overall Progress**: 0/30 sections complete

---

## 📞 **SUPPORT & ESCALATION**

**Questions or Issues?**
- **Technical Lead**: Viji
- **Reference Implementation**: `retail/frontend/inventory/pages/UOMSetup.tsx`
- **Documentation**: `.steering/20TOOLBAR_ROLLOUT/UOM_TOOLBAR_ACTION_AND_CHECKLIST_MANUAL.md`
- **Architecture**: `.steering/01_ARCH_GOVERNANCE/CANONICAL_RULESET.md`

---

**Created**: 2026-01-10 14:45 IST  
**Version**: 1.0  
**Status**: ✅ Ready for Implementation  
**Approved By**: Astra (Antigravity Engineering Agent)
