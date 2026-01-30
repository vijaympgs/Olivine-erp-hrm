# 🛠️ **ITEM MASTER - IMPLEMENTATION GUIDE**

**Quick Start Guide for Applying UOM Gold Standard to Item Master**  
**Estimated Time**: 2-3 hours  
**Difficulty**: Medium  
**Last Updated**: 2026-01-10 14:50 IST

---

## 🎯 **OBJECTIVE**

Transform the existing Item Master screen to match the UOM Gold Standard:
- ✅ Dynamic toolbar with mode-based button visibility
- ✅ Decoupled scrolling (fixed header, scrollable content)
- ✅ Surgical spacing (one-line gaps)
- ✅ Selection-first architecture
- ✅ Read-only view mode
- ✅ Keyboard shortcuts (F2, F3, F5, F7, F8, ESC)

---

## 📂 **FILES TO MODIFY**

1. **Primary**: `retail/frontend/inventory/pages/ItemMasterSetup.tsx`
2. **Form**: `retail/frontend/master/item/ItemForm.tsx` (if exists)
3. **Service**: `frontend/src/services/itemService.ts`
4. **Styles**: `frontend/src/index.css` (ensure `.hairline-scrollbar` exists)

---

## 🚀 **STEP-BY-STEP IMPLEMENTATION**

### **STEP 1: Backup Current Implementation** (5 minutes)

```bash
# Create backup
cp retail/frontend/inventory/pages/ItemMasterSetup.tsx .backups/ItemMasterSetup_BEFORE_TOOLBAR_$(date +%Y%m%d).tsx

# Take screenshot of current UI for comparison
# (Manual step - open browser and screenshot)
```

---

### **STEP 2: Update Imports** (2 minutes)

Replace the imports section in `ItemMasterSetup.tsx`:

```typescript
import React, { useEffect, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { Box, Search, AlertCircle, X } from "lucide-react";
import { itemService, ItemFilters, ItemListItem } from "@services/itemService";
import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";
import { ItemForm } from "../master/item/ItemForm";
```

---

### **STEP 3: Add State Variables** (5 minutes)

Add these state declarations at the top of the component:

```typescript
export const ItemMasterSetup: React.FC = () => {
  // Navigation
  const navigate = useNavigate();

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

  // ... rest of component
```

---

### **STEP 4: Add Helper Functions** (10 minutes)

```typescript
// Mode Helper - Determines which toolbar buttons to show
const getToolbarMode = (): MasterMode => {
  if (!showForm) return 'VIEW';           // List view
  if (viewMode) return 'VIEW_FORM';       // Read-only populated form
  return editingId ? 'EDIT' : 'CREATE';  // Editable form
};

// Data Loading
const loadItems = async () => {
  setLoading(true);
  setError(null);
  try {
    const response = await itemService.getItems(filters);
    setItems(response.results || []);
  } catch (err: any) {
    setError(err.message || 'Failed to load items');
  } finally {
    setLoading(false);
  }
};

// Load items on mount and filter changes
useEffect(() => {
  loadItems();
}, [filters]);

// Filter Handler
const handleFilterChange = (key: keyof ItemFilters, value: any) => {
  setFilters(prev => ({ ...prev, [key]: value }));
};

// Search Handler
const handleSearch = () => {
  setFilters(prev => ({ ...prev, search: searchTerm }));
};
```

---

### **STEP 5: Add CRUD Handlers** (15 minutes)

```typescript
// CREATE - Open empty form
const handleCreate = () => {
  setEditingId(null);
  setViewMode(false);
  setShowForm(true);
  setSelectedItemId(null);
};

// EDIT - Open form with data
const handleEdit = (id: string) => {
  setEditingId(id);
  setViewMode(false);
  setShowForm(true);
};

// VIEW - Open read-only form
const handleView = (id: string) => {
  setEditingId(id);
  setViewMode(true);
  setShowForm(true);
};

// DELETE - Soft delete with confirmation
const handleDelete = async (id: string) => {
  try {
    // Optional: Check usage before delete
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

// Form Success - Save completed
const handleFormSuccess = async () => {
  setShowForm(false);
  setEditingId(null);
  setViewMode(false);
  await loadItems();
};

// Form Cancel - Discard changes
const handleFormCancel = () => {
  setShowForm(false);
  setEditingId(null);
  setViewMode(false);
};
```

---

### **STEP 6: Add Centralized Action Handler** (20 minutes)

```typescript
const handleToolbarAction = (action: string) => {
  switch (action) {
    // ============ VIEW MODE ACTIONS ============
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
        handleDelete(selectedItemId);
      }
      break;

    case 'refresh':
      loadItems();
      setSelectedItemId(null);
      break;

    case 'search':
      document.querySelector<HTMLInputElement>('input[type="text"]')?.focus();
      break;

    case 'filter':
      setShowFilterPanel(!showFilterPanel);
      break;

    case 'import':
      alert('Import functionality coming soon');
      // TODO: Implement Excel/CSV import
      break;

    case 'export':
      alert('Export functionality coming soon');
      // TODO: Implement Excel/CSV export
      break;

    // ============ FORM MODE ACTIONS ============
    case 'save':
      if (showForm) formRef.current?.submit();
      break;

    case 'cancel':
      handleFormCancel();
      break;

    case 'clear':
      if (showForm) {
        // In form mode: reset form
        formRef.current?.reset();
      } else {
        // In list mode: clear selection and search
        setSelectedItemId(null);
        setSearchTerm('');
      }
      break;

    // ============ UNIVERSAL ACTIONS ============
    case 'exit':
      if (showForm) {
        // If form is open, close it
        handleFormCancel();
      } else {
        // If in list view, exit to dashboard
        navigate('/dashboard');
      }
      break;

    default:
      console.warn(`Unhandled toolbar action: ${action}`);
  }
};
```

---

### **STEP 7: Add Keyboard Shortcuts** (10 minutes)

```typescript
// Keyboard Shortcuts
useEffect(() => {
  const handleKeyDown = (e: KeyboardEvent) => {
    // Prevent shortcuts when typing in input fields
    const target = e.target as HTMLElement;
    if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.tagName === 'SELECT') {
      // Allow ESC even in inputs
      if (e.key !== 'Escape') return;
    }

    switch (e.key) {
      case 'F2':
        e.preventDefault();
        if (!showForm) handleCreate();
        break;

      case 'F3':
        e.preventDefault();
        if (selectedItemId && !showForm) handleEdit(selectedItemId);
        break;

      case 'F5':
        e.preventDefault();
        if (showForm) formRef.current?.reset();
        break;

      case 'F7':
        e.preventDefault();
        if (selectedItemId && !showForm) handleView(selectedItemId);
        break;

      case 'F8':
        e.preventDefault();
        if (showForm) formRef.current?.submit();
        break;

      case 'Escape':
        e.preventDefault();
        handleToolbarAction('exit');
        break;
    }
  };

  window.addEventListener('keydown', handleKeyDown);
  return () => window.removeEventListener('keydown', handleKeyDown);
}, [showForm, selectedItemId, editingId]);
```

---

### **STEP 8: Build the JSX Structure** (30 minutes)

Replace the entire return statement:

```typescript
return (
  <>
    {/* ========== TOOLBAR - Fixed at Top ========== */}
    <MasterToolbar
      viewId="ITEM_MASTER"
      mode={getToolbarMode()}
      onAction={handleToolbarAction}
      hasSelection={!!selectedItemId}
    />

    {/* ========== MAIN CONTENT AREA ========== */}
    <div className="flex flex-col h-[calc(100vh-var(--toolbar-height))]">
      
      {/* ========== FIXED HEADER SECTION ========== */}
      <div className="max-w-[80rem] mx-auto w-full px-6 pt-6 pb-0">
        
        {/* Page Title & Breadcrumbs */}
        <div className="mb-4">
          <h1 className="text-xl font-semibold text-slate-800">Item Master</h1>
          <p className="text-sm text-slate-500 mt-1">
            Retail &gt; Master Data &gt; Items
          </p>
        </div>

        {/* Error Message */}
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

        {/* Read-Only Banner (when in VIEW_FORM mode) */}
        {viewMode && showForm && (
          <div className="bg-blue-50 border border-blue-200 rounded-md p-3 mb-4">
            <p className="text-sm text-blue-800">
              📖 Viewing record (Read-only mode)
            </p>
          </div>
        )}

        {/* Search Bar (only in VIEW mode) */}
        {!showForm && (
          <div className="flex items-center gap-3 mb-4">
            <div className="flex-1 relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400" />
              <input
                type="text"
                placeholder="Search by SKU, name, or description..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
                className="w-full h-9 pl-10 pr-4 rounded-md border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
          </div>
        )}

        {/* Filter Panel (only in VIEW mode) */}
        {!showForm && showFilterPanel && (
          <div className="bg-slate-50 border border-slate-200 rounded-md p-4 mb-4">
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              
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
                  <option value="FINISHED_GOODS">Finished Goods</option>
                  <option value="RAW_MATERIALS">Raw Materials</option>
                  <option value="CONSUMABLES">Consumables</option>
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

      </div>

      {/* ========== SCROLLABLE CONTENT SECTION ========== */}
      <div className="flex-1 overflow-y-auto hairline-scrollbar">
        <div className="max-w-[80rem] mx-auto w-full px-6 pt-0">

          {/* FORM VIEW */}
          {showForm ? (
            <ItemForm
              itemId={editingId}
              readOnly={viewMode}
              ref={formRef}
              onSuccess={handleFormSuccess}
              onCancel={handleFormCancel}
            />
          ) : (
            /* LIST VIEW */
            <>
              {/* Loading State */}
              {loading ? (
                <div className="flex items-center justify-center py-12">
                  <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
                  <span className="ml-3 text-sm text-slate-600">Loading items...</span>
                </div>
              ) : (
                /* Table */
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
                    {items.length === 0 ? (
                      <tr>
                        <td colSpan={7} className="px-6 py-12 text-center text-slate-500">
                          <Box className="mx-auto h-12 w-12 text-slate-300 mb-3" />
                          <p className="text-sm">No items found</p>
                          <p className="text-xs mt-1">Click "New" to create your first item</p>
                        </td>
                      </tr>
                    ) : (
                      items.map(item => (
                        <tr
                          key={item.id}
                          onClick={() => setSelectedItemId(item.id)}
                          className={`cursor-pointer transition-colors border-t border-slate-200 ${
                            selectedItemId === item.id 
                              ? 'bg-blue-100 border-l-4 border-l-blue-500' 
                              : 'hover:bg-blue-50'
                          }`}
                        >
                          <td className="px-3 py-2 text-sm">{item.sku}</td>
                          <td className="px-3 py-2 text-sm font-medium">{item.name}</td>
                          <td className="px-3 py-2 text-sm">{item.category}</td>
                          <td className="px-3 py-2 text-sm">{item.item_type}</td>
                          <td className="px-3 py-2 text-sm text-right font-feature-settings-tnum">
                            ${item.price?.toFixed(2) || '0.00'}
                          </td>
                          <td className="px-3 py-2 text-sm text-center">{item.stock_qty || 0}</td>
                          <td className="px-3 py-2 text-sm text-center">
                            <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                              item.is_active 
                                ? 'bg-green-100 text-green-800' 
                                : 'bg-red-100 text-red-800'
                            }`}>
                              {item.is_active ? 'Active' : 'Inactive'}
                            </span>
                          </td>
                        </tr>
                      ))
                    )}
                  </tbody>
                </table>
              )}
            </>
          )}

        </div>
      </div>

    </div>
  </>
);
```

---

### **STEP 9: Update ItemForm Component** (15 minutes)

In `retail/frontend/master/item/ItemForm.tsx`, ensure it supports:

```typescript
import React, { forwardRef, useImperativeHandle } from 'react';

interface ItemFormProps {
  itemId?: string | null;
  readOnly?: boolean;
  onSuccess?: () => void;
  onCancel?: () => void;
}

export const ItemForm = forwardRef<any, ItemFormProps>(
  ({ itemId, readOnly = false, onSuccess, onCancel }, ref) => {
    
    // Expose submit and reset methods to parent via ref
    useImperativeHandle(ref, () => ({
      submit: () => {
        // Trigger form submission
        handleSubmit();
      },
      reset: () => {
        // Reset form to initial state
        setFormData(initialFormData);
      }
    }));

    // Rest of form implementation
    // Make sure all inputs respect the readOnly prop:
    
    return (
      <form onSubmit={handleSubmit}>
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
        {/* More fields... */}
      </form>
    );
  }
);
```

---

### **STEP 10: Verify Hairline Scrollbar** (2 minutes)

Ensure this CSS exists in `frontend/src/index.css`:

```css
/* Hairline Scrollbar - Premium thin scrollbar */
.hairline-scrollbar::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

.hairline-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}

.hairline-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(148, 163, 184, 0.4);
  border-radius: 3px;
}

.hairline-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(148, 163, 184, 0.6);
}
```

---

## ✅ **POST-IMPLEMENTATION TESTING**

### **Quick Smoke Test** (10 minutes)

1. **Start the app**: `npm run dev`
2. **Navigate to Item Master**: `/retail/inventory/item-master-setup`
3. **Test each action**:
   - [ ] Click "New" → Form appears
   - [ ] Click "Cancel" → Back to list
   - [ ] Click a row → Row highlights in blue
   - [ ] Click "Edit" → Form opens with data
   - [ ] Click "Save" → Item updates, back to list
   - [ ] Click "View" → Read-only form opens
   - [ ] Click "Delete" → Confirmation, then item deactivated
   - [ ] Click "Refresh" → List reloads
   - [ ] Click "Filter" → Filter panel toggles
   - [ ] Press F2 → New form opens
   - [ ] Press F3 (with selection) → Edit form opens
   - [ ] Press F7 (with selection) → View form opens
   - [ ] Press F8 (in form) → Saves
   - [ ] Press ESC → Cancels/Exits

4. **Visual checks**:
   - [ ] Toolbar is sticky at top
   - [ ] Header section is fixed
   - [ ] Only table scrolls
   - [ ] Scrollbar is thin and styled
   - [ ] One-line gap between sections
   - [ ] Selected row has blue highlight
   - [ ] Typography looks correct (Inter font)

---

## 🐛 **COMMON ISSUES & FIXES**

### **Issue 1: Toolbar buttons not showing**
**Fix**: Check that `viewId="ITEM_MASTER"` matches the menu ID in the database.

### **Issue 2: Form ref not working**
**Fix**: Ensure `ItemForm` uses `forwardRef` and `useImperativeHandle`.

### **Issue 3: Selection not highlighting**
**Fix**: Check that `selectedItemId === item.id` condition is correct.

### **Issue 4: Scrollbar not styled**
**Fix**: Verify `.hairline-scrollbar` class exists in `index.css`.

### **Issue 5: Keyboard shortcuts not working**
**Fix**: Check that event listener is attached to `window` and dependencies are correct.

### **Issue 6: Double scrollbars**
**Fix**: Remove `overflow-y-auto` from parent containers, only apply to content section.

---

## 📊 **COMPLETION CHECKLIST**

- [ ] All imports updated
- [ ] State variables added
- [ ] Helper functions implemented
- [ ] CRUD handlers implemented
- [ ] Centralized action handler implemented
- [ ] Keyboard shortcuts implemented
- [ ] JSX structure updated
- [ ] ItemForm component updated
- [ ] Hairline scrollbar CSS verified
- [ ] Smoke test passed
- [ ] Visual verification passed
- [ ] No console errors
- [ ] No TypeScript errors

---

## 🎉 **SUCCESS CRITERIA**

Your implementation is complete when:

1. ✅ All toolbar buttons work correctly in all modes
2. ✅ Selection-first architecture works (Edit/View/Delete require selection)
3. ✅ Decoupled scrolling works (header fixed, content scrolls)
4. ✅ Keyboard shortcuts work (F2, F3, F5, F7, F8, ESC)
5. ✅ Read-only view mode works (all fields disabled)
6. ✅ Visual polish matches UOM standard (spacing, scrollbar, typography)
7. ✅ No console errors or warnings
8. ✅ No TypeScript errors

---

## 📞 **NEED HELP?**

**Reference Implementation**: `retail/frontend/inventory/pages/UOMSetup.tsx`  
**Documentation**: `.steering/20TOOLBAR_ROLLOUT/UOM_TOOLBAR_ACTION_AND_CHECKLIST_MANUAL.md`  
**Technical Lead**: Viji

---

**Created**: 2026-01-10 14:50 IST  
**Version**: 1.0  
**Estimated Time**: 2-3 hours  
**Status**: ✅ Ready to Use
