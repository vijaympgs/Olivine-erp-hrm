# 📘 **UOM SETUP - TOOLBAR ACTION REFERENCE MANUAL**

**Screen**: Units of Measure (UOM) Setup  
**Path**: `/retail/inventory/uom-setup`  
**Menu ID**: `INVENTORY_UOM_SETUP`  
**Toolbar Config**: `NESCKVDXRQF`  
**Screen Type**: MASTER (List + Form)  
**Last Updated**: 2026-01-10 10:10 IST

---

## 🎯 **OVERVIEW**

This manual documents the behavior of every toolbar action in the UOM Setup screen across all three modes: **VIEW**, **NEW**, and **EDIT**.

---

## 📊 **MODE SUMMARY**

| Mode | Description | Form Visible | List Visible | Toolbar Buttons |
|------|-------------|--------------|--------------|-----------------|
| **VIEW** | Browse and manage UOM list | ❌ No | ✅ Yes | N, E, V, D, R, Q, F, Import, Export, X |
| **NEW** | Create new UOM | ✅ Yes | ❌ No | S, C, K, X |
| **EDIT** | Modify existing UOM | ✅ Yes | ❌ No | S, C, K, X |

---

## 🎯 **SELECTION BEHAVIOR (VIEW MODE)**

### **When NO Record is Selected**:

| Button | Status | Reason |
|--------|--------|--------|
| **New** | ✅ **Enabled** | Can create new UOM anytime |
| **Edit** | ❌ **Disabled** | No UOM selected to edit |
| **View** | ❌ **Disabled** | No UOM selected to view |
| **Delete** | ❌ **Disabled** | No UOM selected to delete |
| **Refresh** | ✅ **Enabled** | Can refresh list anytime |
| **Search** | ✅ **Enabled** | Can search anytime |
| **Filter** | ✅ **Enabled** | Can toggle filters anytime |
| **Import** | ✅ **Enabled** | Can import anytime |
| **Export** | ✅ **Enabled** | Can export current list |
| **Exit** | ✅ **Enabled** | Can exit anytime |

**Visual State**: Buttons requiring selection appear **grayed out** (disabled state).

---

### **When a Record IS Selected** (Row Clicked):

| Button | Status | Change |
|--------|--------|--------|
| **New** | ✅ **Enabled** | No change |
| **Edit** | ✅ **Enabled** | ✅ **Now clickable** |
| **View** | ✅ **Enabled** | ✅ **Now clickable** |
| **Delete** | ✅ **Enabled** | ✅ **Now clickable** |
| **Refresh** | ✅ **Enabled** | No change |
| **Search** | ✅ **Enabled** | No change |
| **Filter** | ✅ **Enabled** | No change |
| **Import** | ✅ **Enabled** | No change |
| **Export** | ✅ **Enabled** | No change |
| **Exit** | ✅ **Enabled** | No change |

**Visual State**:
- Selected row is **highlighted in blue** (`bg-blue-100`)
- Edit, View, and Delete buttons become **fully visible** (no longer grayed out)

---

### **How to Select a Record**:

1. **Click anywhere on the row** in the UOM list
2. The row background changes to **blue**
3. `selectedUOMId` state is updated with the clicked UOM's ID
4. Edit, View, and Delete buttons become enabled

**To Deselect**:
- Click the **Clear** button (in VIEW mode, clears selection)
- Click **Refresh** (reloads list and clears selection)
- Navigate away and return

---

### **Code Implementation**:

```typescript
// Selection state
const [selectedUOMId, setSelectedUOMId] = useState<string | null>(null);

// Row click handler
<tr
  onClick={() => setSelectedUOMId(uom.id)}
  className={`cursor-pointer ${
    selectedUOMId === uom.id ? 'bg-blue-100' : 'hover:bg-blue-50'
  }`}
>

// Button enabled check
const isActionEnabled = (action: ActionButton): boolean => {
  if (action.id === 'edit' && !hasSelection) return false;
  if (action.id === 'delete' && !hasSelection) return false;
  if (action.id === 'view' && !hasSelection) return false;
  return true;
};
```

---

## 🔵 **VIEW MODE** (List View)

**When Active**: When user is viewing the UOM list (default state)  
**Form State**: Hidden  
**List State**: Visible  
**Selection**: Optional (click on row to select)

### **Visible Toolbar Buttons**:

| Button | Icon | Shortcut | Action | Requires Selection |
|--------|------|----------|--------|-------------------|
| **New** | ➕ Plus | F2 | Create new UOM | ❌ No |
| **Edit** | ✏️ Edit | F3 | Edit selected UOM | ✅ Yes |
| **View** | 👁️ Eye | F7 | View selected UOM | ✅ Yes |
| **Delete** | 🗑️ Trash | - | Deactivate selected UOM | ✅ Yes |
| **Refresh** | 🔄 Refresh | - | Reload UOM list from server | ❌ No |
| **Search** | 🔍 Search | - | Focus on search input | ❌ No |
| **Filter** | 🎛️ Filter | - | Toggle filter panel visibility | ❌ No |
| **Import** | 📥 Upload | - | Import UOMs from Excel/CSV | ❌ No |
| **Export** | 📤 Download | - | Export UOMs to Excel/CSV | ❌ No |
| **Exit** | 🚪 Logout | ESC | Navigate to Dashboard | ❌ No |

---

### **📋 DETAILED ACTION BEHAVIORS - VIEW MODE**

#### **1. New (F2)** ➕
**What happens**:
1. ✅ Hides the UOM list
2. ✅ Shows the UOM form (empty)
3. ✅ Switches toolbar to **NEW mode**
4. ✅ Clears any previous selection
5. ✅ Form fields are empty and ready for input

**Code Flow**:
```typescript
case 'new':
  handleCreate();
  // Sets: editingId = null, showForm = true
```

**Result**: User can now create a new UOM record.

---

#### **2. Edit (F3)** ✏️
**Requires**: A UOM must be selected (row clicked)

**What happens**:
1. ✅ Checks if a UOM is selected
2. ✅ Hides the UOM list
3. ✅ Shows the UOM form (populated with selected UOM data)
4. ✅ Switches toolbar to **EDIT mode**
5. ✅ Loads selected UOM data into form fields

**Code Flow**:
```typescript
case 'edit':
  if (selectedUOMId && !showForm) handleEdit(selectedUOMId);
  // Sets: editingId = selectedUOMId, showForm = true
```

**Result**: User can now modify the selected UOM record.

**If no selection**: Button is **disabled** (grayed out).

---

#### **3. View (F7)** 👁️
**Requires**: A UOM must be selected (row clicked)

**What happens**:
1. ✅ Checks if a UOM is selected
2. ✅ Hides the UOM list
3. ✅ Shows the UOM form (populated with selected UOM data)
4. ✅ Switches toolbar to **EDIT mode**
5. ✅ Form is editable (same as Edit button)

**Code Flow**:
```typescript
case 'view':
  if (selectedUOMId && !showForm) handleEdit(selectedUOMId);
  // Currently same as Edit - TODO: Add read-only mode
```

**Current Behavior**: Opens in **EDIT mode** (same as Edit button).  
**Future Enhancement**: Should open in **read-only mode** with disabled fields.

**If no selection**: Button is **disabled** (grayed out).

---

#### **4. Delete** 🗑️
**Requires**: A UOM must be selected (row clicked)

**What happens**:
1. ✅ Checks if a UOM is selected
2. ✅ Finds the selected UOM in the list
3. ✅ Calls `handleDeactivate(uom)` to deactivate the UOM
4. ✅ Sends DELETE request to backend: `/api/uoms/{id}/`
5. ✅ Reloads the UOM list after successful deletion
6. ✅ Shows error message if deletion fails

**Code Flow**:
```typescript
case 'delete':
  if (selectedUOMId && !showForm) {
    const uom = uoms.find(u => u.id === selectedUOMId);
    if (uom) handleDeactivate(uom);
    // Calls: uomService.deleteUOM(uom.id)
    // Then: loadUOMs() to refresh list
  }
```

**Result**: Selected UOM is marked as inactive (soft delete).

**If no selection**: Button is **disabled** (grayed out).

**Error Handling**: Shows error message if UOM cannot be deleted (e.g., in use).

---

#### **5. Refresh** 🔄
**What happens**:
1. ✅ Calls `loadUOMs()` function
2. ✅ Fetches fresh UOM data from server
3. ✅ Updates the list with latest data
4. ✅ Applies current filters and search term
5. ✅ Shows loading spinner during fetch

**Code Flow**:
```typescript
case 'refresh':
  loadUOMs();
  // Calls: uomService.getUOMs(filters)
  // Updates: setUOMs(response.results)
```

**Result**: UOM list is refreshed with latest data from database.

**Use Case**: After another user makes changes, or to verify data sync.

---

#### **6. Search** 🔍
**What happens**:
1. ✅ Finds the search input field on the page
2. ✅ Sets focus to the search input
3. ✅ User can immediately start typing

**Code Flow**:
```typescript
case 'search':
  document.querySelector<HTMLInputElement>('input[type="text"]')?.focus();
```

**Result**: Cursor is placed in the search box for quick filtering.

**Note**: Actual search is triggered by pressing **Enter** in the search box.

---

#### **7. Filter** 🎛️
**What happens**:
1. ✅ Toggles the filter panel visibility
2. ✅ If hidden, shows the filter panel
3. ✅ If visible, hides the filter panel
4. ✅ Filter panel contains: Company, Type, Active/Inactive dropdowns

**Code Flow**:
```typescript
case 'filter':
  setShowFilterPanel(!showFilterPanel);
  // Toggles between true/false
```

**Result**: Filter panel is shown/hidden, allowing user to filter UOMs by:
- Company
- UOM Type (Stock, Purchase, Sales, Generic)
- Active Status (Active Only, Include Inactive)

---

#### **8. Import** 📥
**What happens**:
1. ⏳ Shows alert: "Import functionality coming soon"
2. ⏳ TODO: Will open file picker for Excel/CSV
3. ⏳ TODO: Will parse and validate file
4. ⏳ TODO: Will bulk insert UOMs into database

**Code Flow**:
```typescript
case 'import':
  alert('Import functionality coming soon');
  // TODO: Implement import functionality
```

**Result**: Currently shows placeholder message.

**Future**: Will allow bulk import of UOMs from Excel/CSV files.

---

#### **9. Export** 📤
**What happens**:
1. ⏳ Shows alert: "Export functionality coming soon"
2. ⏳ TODO: Will generate Excel/CSV file
3. ⏳ TODO: Will download file with current UOM list
4. ⏳ TODO: Will respect current filters

**Code Flow**:
```typescript
case 'export':
  alert('Export functionality coming soon');
  // TODO: Implement export to Excel/CSV
```

**Result**: Currently shows placeholder message.

**Future**: Will export current UOM list to Excel/CSV file.

---

#### **10. Exit** 🚪
**What happens**:
1. ✅ Navigates away from UOM Setup screen
2. ✅ Redirects to Dashboard (`/dashboard`)
3. ✅ Discards any unsaved changes
4. ✅ Clears selection and filters

**Code Flow**:
```typescript
case 'exit':
  navigate('/dashboard');
```

**Result**: User is taken to the main Dashboard screen.

**Warning**: Any unsaved changes in the form will be lost.

---

## 🟢 **NEW MODE** (Create Form)

**When Active**: After clicking "New" button in VIEW mode  
**Form State**: Visible (empty)  
**List State**: Hidden  
**Selection**: N/A (creating new record)

### **Visible Toolbar Buttons**:

| Button | Icon | Shortcut | Action | Description |
|--------|------|----------|--------|-------------|
| **Save** | 💾 Save | F8 | Save new UOM | Creates new UOM record |
| **Cancel** | ❌ X | ESC | Cancel creation | Returns to VIEW mode |
| **Clear** | 🔄 RotateCcw | F5 | Clear form | Resets all form fields |
| **Exit** | 🚪 Logout | ESC | Exit screen | Navigate to Dashboard |

---

### **📋 DETAILED ACTION BEHAVIORS - NEW MODE**

#### **1. Save (F8)** 💾
**What happens**:
1. ✅ Triggers form validation
2. ✅ Checks all required fields are filled
3. ✅ Validates data format (e.g., UOM code is unique)
4. ✅ Sends POST request to backend: `/api/uoms/`
5. ✅ If successful:
   - ✅ Hides the form
   - ✅ Returns to VIEW mode
   - ✅ Reloads UOM list (new UOM appears)
   - ✅ Shows success message
6. ❌ If validation fails:
   - ❌ Shows error messages on form fields
   - ❌ Form remains open for correction

**Code Flow**:
```typescript
case 'save':
  if (showForm) formRef.current?.submit();
  // Calls: uomService.createUOM(formData)
  // On success: setShowForm(false), loadUOMs()
```

**Result**: New UOM is created and added to the list.

**Validation Rules**:
- ✅ Company: Required
- ✅ UOM Code: Required, unique, max 10 characters
- ✅ UOM Name: Required, max 50 characters
- ✅ UOM Type: Required (Stock/Purchase/Sales/Generic)
- ✅ Decimal Allowed: Boolean
- ✅ Rounding Precision: Optional, numeric
- ✅ Is Core UOM: Boolean
- ✅ Is Active: Boolean

---

#### **2. Cancel (ESC)** ❌
**What happens**:
1. ✅ Discards all form data (no save)
2. ✅ Hides the form
3. ✅ Returns to VIEW mode
4. ✅ Shows the UOM list again
5. ✅ No changes are made to database

**Code Flow**:
```typescript
case 'cancel':
  handleFormCancel();
  // Sets: showForm = false, editingId = null
```

**Result**: Form is closed, user returns to UOM list.

**Warning**: All entered data is lost (no confirmation dialog).

---

#### **3. Clear (F5)** 🔄
**What happens**:
1. ✅ Resets all form fields to empty/default values
2. ✅ Clears any validation errors
3. ✅ Form remains open (still in NEW mode)
4. ✅ User can start entering data again

**Code Flow**:
```typescript
case 'clear':
  if (showForm) {
    setEditingId(null);
    formRef.current?.reset();
  }
```

**Result**: Form is cleared, ready for fresh input.

**Use Case**: User wants to start over without closing the form.

---

#### **4. Exit (ESC)** 🚪
**What happens**:
1. ✅ Navigates away from UOM Setup screen
2. ✅ Redirects to Dashboard (`/dashboard`)
3. ✅ Discards any unsaved form data
4. ✅ No confirmation dialog

**Code Flow**:
```typescript
case 'exit':
  navigate('/dashboard');
```

**Result**: User is taken to Dashboard, form data is lost.

**Warning**: Any unsaved changes will be lost.

---

## 🟡 **EDIT MODE** (Modify Form)

**When Active**: After clicking "Edit" or "View" button in VIEW mode  
**Form State**: Visible (populated with existing data)  
**List State**: Hidden  
**Selection**: The UOM being edited

### **Visible Toolbar Buttons**:

| Button | Icon | Shortcut | Action | Description |
|--------|------|----------|--------|-------------|
| **Save** | 💾 Save | F8 | Save changes | Updates existing UOM record |
| **Cancel** | ❌ X | ESC | Cancel editing | Returns to VIEW mode |
| **Clear** | 🔄 RotateCcw | F5 | Reset form | Reloads original UOM data |
| **Exit** | 🚪 Logout | ESC | Exit screen | Navigate to Dashboard |

---

### **📋 DETAILED ACTION BEHAVIORS - EDIT MODE**

#### **1. Save (F8)** 💾
**What happens**:
1. ✅ Triggers form validation
2. ✅ Checks all required fields are filled
3. ✅ Validates data format
4. ✅ Sends PUT request to backend: `/api/uoms/{id}/`
5. ✅ If successful:
   - ✅ Hides the form
   - ✅ Returns to VIEW mode
   - ✅ Reloads UOM list (updated UOM appears)
   - ✅ Shows success message
6. ❌ If validation fails:
   - ❌ Shows error messages on form fields
   - ❌ Form remains open for correction

**Code Flow**:
```typescript
case 'save':
  if (showForm) formRef.current?.submit();
  // Calls: uomService.updateUOM(editingId, formData)
  // On success: setShowForm(false), loadUOMs()
```

**Result**: Existing UOM is updated with new data.

**Validation Rules**: Same as NEW mode.

---

#### **2. Cancel (ESC)** ❌
**What happens**:
1. ✅ Discards all form changes (no save)
2. ✅ Hides the form
3. ✅ Returns to VIEW mode
4. ✅ Shows the UOM list again
5. ✅ Original UOM data remains unchanged

**Code Flow**:
```typescript
case 'cancel':
  handleFormCancel();
  // Sets: showForm = false, editingId = null
```

**Result**: Form is closed, changes are discarded.

**Warning**: All changes are lost (no confirmation dialog).

---

#### **3. Clear (F5)** 🔄
**What happens**:
1. ✅ Resets form fields to original UOM data
2. ✅ Discards any unsaved changes
3. ✅ Reloads the UOM data from database
4. ✅ Form remains open (still in EDIT mode)
5. ✅ Clears any validation errors

**Code Flow**:
```typescript
case 'clear':
  if (showForm) {
    setEditingId(null);
    formRef.current?.reset();
  }
```

**Result**: Form is reset to original values.

**Use Case**: User made mistakes and wants to start over.

---

#### **4. Exit (ESC)** 🚪
**What happens**:
1. ✅ Navigates away from UOM Setup screen
2. ✅ Redirects to Dashboard (`/dashboard`)
3. ✅ Discards any unsaved form changes
4. ✅ No confirmation dialog

**Code Flow**:
```typescript
case 'exit':
  navigate('/dashboard');
```

**Result**: User is taken to Dashboard, changes are lost.

**Warning**: Any unsaved changes will be lost.

---

## 🎯 **MODE TRANSITION DIAGRAM**

```
┌─────────────────────────────────────────────────────────┐
│                      VIEW MODE                          │
│  (UOM List Visible, Form Hidden)                        │
│                                                          │
│  Toolbar: N E V D R Q F Import Export X                 │
└─────────────────────────────────────────────────────────┘
                    │                    │
                    │ New (F2)           │ Edit/View (F3/F7)
                    │                    │ (requires selection)
                    ▼                    ▼
        ┌──────────────────┐  ┌──────────────────┐
        │    NEW MODE      │  │   EDIT MODE      │
        │  (Empty Form)    │  │ (Populated Form) │
        │                  │  │                  │
        │  Toolbar: S C K X│  │  Toolbar: S C K X│
        └──────────────────┘  └──────────────────┘
                    │                    │
                    │ Save (F8)          │ Save (F8)
                    │ Cancel (ESC)       │ Cancel (ESC)
                    │                    │
                    ▼                    ▼
        ┌─────────────────────────────────────┐
        │         Back to VIEW MODE           │
        │      (List refreshed)               │
        └─────────────────────────────────────┘
```

---

## 📋 **QUICK REFERENCE TABLE**

| Action | VIEW Mode | NEW Mode | EDIT Mode | Requires Selection |
|--------|-----------|----------|-----------|-------------------|
| **New** | ✅ Create new UOM | ❌ Hidden | ❌ Hidden | ❌ No |
| **Edit** | ✅ Edit selected UOM | ❌ Hidden | ❌ Hidden | ✅ Yes |
| **View** | ✅ View selected UOM | ❌ Hidden | ❌ Hidden | ✅ Yes |
| **Save** | ❌ Hidden | ✅ Create record | ✅ Update record | ❌ No |
| **Cancel** | ❌ Hidden | ✅ Close form | ✅ Close form | ❌ No |
| **Clear** | ❌ Hidden | ✅ Reset form | ✅ Reset to original | ❌ No |
| **Delete** | ✅ Deactivate UOM | ❌ Hidden | ❌ Hidden | ✅ Yes |
| **Refresh** | ✅ Reload list | ❌ Hidden | ❌ Hidden | ❌ No |
| **Search** | ✅ Focus search box | ❌ Hidden | ❌ Hidden | ❌ No |
| **Filter** | ✅ Toggle filters | ❌ Hidden | ❌ Hidden | ❌ No |
| **Import** | ✅ Import UOMs | ❌ Hidden | ❌ Hidden | ❌ No |
| **Export** | ✅ Export UOMs | ❌ Hidden | ❌ Hidden | ❌ No |
| **Exit** | ✅ Go to Dashboard | ✅ Go to Dashboard | ✅ Go to Dashboard | ❌ No |

---

## 🔑 **KEYBOARD SHORTCUTS**

| Shortcut | Action | Available In |
|----------|--------|--------------|
| **F2** | New | VIEW mode |
| **F3** | Edit | VIEW mode (with selection) |
| **F5** | Clear | NEW/EDIT mode |
| **F7** | View | VIEW mode (with selection) |
| **F8** | Save | NEW/EDIT mode |
| **ESC** | Cancel/Exit | All modes |

---

## ⚠️ **IMPORTANT NOTES**

### **Data Loss Warnings**:
1. ⚠️ **Cancel** button discards changes without confirmation
2. ⚠️ **Exit** button navigates away without saving
3. ⚠️ **Clear** button in EDIT mode resets to original data

### **Selection Requirements**:
- **Edit**, **View**, and **Delete** buttons are **disabled** unless a UOM is selected
- Click on any row in the list to select a UOM
- Selected row is highlighted in blue

### **Validation**:
- All required fields must be filled before saving
- UOM Code must be unique across the company
- Form shows inline error messages for validation failures

### **Future Enhancements**:
- ⏳ **View** button should open in read-only mode (currently same as Edit)
- ⏳ **Import** functionality to be implemented
- ⏳ **Export** functionality to be implemented
- ⏳ **Confirmation dialogs** for Cancel and Exit actions

---

## 📞 **SUPPORT**

For questions or issues with UOM Setup, contact:
- **Technical Lead**: Viji
- **Module**: Retail > Inventory > Setup
- **Documentation**: `.steering/20TOOLBAR_ROLLOUT/`

---

**Last Updated**: 2026-01-10 10:05 IST  
**Version**: 1.0  
**Status**: ✅ Production Ready

---

#  **PURCHASE ORDER - TRANSACTION SCREEN EXAMPLE**

**Screen**: Purchase Order Form  
**Path**: `/procurement/orders/{id}` or `/procurement/orders/new`  
**Menu ID**: `PURCHASE_ORDERS`  
**Toolbar Config**: `NESCKZTJAVPMRDX1234QF`  
**Screen Type**: TRANSACTION (Header + Lines)  

##  **KEY DIFFERENCES FROM UOM (MASTER)**

| Aspect | UOM (MASTER) | Purchase Order (TRANSACTION) |
|--------|--------------|------------------------------|
| **Workflow** |  No workflow |  DRAFT  SUBMITTED  APPROVED |
| **Approval Actions** |  None |  Submit, Authorize, Reject |
| **Navigation** |  No navigation |  First, Previous, Next, Last |
| **Document Actions** |  None |  Print, Email |
| **Toolbar Config** | `NESCKVDXRQF` (11 chars) | `NESCKZTJAVPMRDX1234QF` (22 chars) |

##  **TRANSACTION-SPECIFIC TOOLBAR ACTIONS**

### **Submit (T)** 
- **When**: EDIT mode (DRAFT PO only)
- **Action**: Submit PO for approval
- **Result**: Status  SUBMITTED, Mode  VIEW (read-only)

### **Authorize (Z)** 
- **When**: APPROVAL mode (SUBMITTED PO, approver only)
- **Action**: Approve the PO
- **Result**: Status  APPROVED

### **Reject (J)** 
- **When**: APPROVAL mode (SUBMITTED PO, approver only)
- **Action**: Reject PO with reason
- **Result**: Status  REJECTED, returns to DRAFT

### **Print (P)** 
- **When**: Any mode
- **Action**: Generate PDF and print PO document

### **Email (M)** 
- **When**: Any mode
- **Action**: Send PO to supplier via email

### **Navigation (1,2,3,4)** 
- **When**: VIEW mode
- **Action**: Navigate between POs without returning to list
- **1**: First PO, **2**: Previous, **3**: Next, **4**: Last

##  **WORKFLOW STATE DIAGRAM**

```
CREATE (New PO)
   Save
  
EDIT (DRAFT PO)
   Submit
  
APPROVAL (SUBMITTED PO)
                
   Authorize     Reject
                
VIEW (APPROVED)  EDIT (DRAFT - for revision)
```

---

**Last Updated**: 2026-01-10 10:15 IST  
**Version**: 1.1 (Added PO Transaction Example)

---

##  **IMPORTANT CLARIFICATION: CLICKING A ROW vs EDITING**

### **Common Confusion**:
 "When I click a UOM record, does it go to EDIT mode?"

### **Answer**:
 **NO!** Clicking a row only **selects** it. You stay in VIEW mode.

### **Correct Flow**:

**Step 1: Click a UOM Row**
-  Row is selected (blue highlight)
-  **STAYS in VIEW mode**
-  List remains visible
-  Form is NOT shown
-  Edit, View, Delete buttons become enabled
-  Save button is NOT visible yet

**Step 2: Click Edit Button (F3)**
-  **NOW switches to EDIT mode**
-  List is hidden
-  Form is shown (populated with UOM data)
-  Save, Cancel, Clear buttons appear
-  Edit, View, Delete buttons are hidden

**Step 3: Click Save (F8)**
-  UOM is updated in database
-  Returns to VIEW mode
-  List is shown again

### **Key Takeaway**:
**Selecting a row  Editing a row**

You need **TWO actions**:
1. **Click row**  Select
2. **Click Edit**  Open form for editing

---

**Last Updated**: 2026-01-10 10:20 IST  
**Clarification Added**: Row selection vs editing behavior

---

## ✅ **IMPLEMENTED: TRUE READ-ONLY VIEW MODE**

### **Status**: ✅ **LIVE & FUNCTIONAL**

The read-only VIEW mode is now fully implemented and integrated with the permission system.

### **How it Works**:
1.  **View Button (F7)**: When clicked, it calls `handleView()`.
2.  **State**: `viewMode` is set to `true`.
3.  **Toolbar**: Automatically switches to `VIEW` mode (non-modifying actions only).
4.  **Form**: The `UOMForm` receives `readOnly={true}`.
5.  **Visuals**: 
    - A blue "Viewing record (Read-only)" banner appears.
    - All input fields, selects, and checkboxes are **disabled** and grayed out.

### **Validation**:
- ✅ Clicking **View** shows the data but prevents typing/changes.
- ✅ Toolbar only shows: **Exit**, **Refresh**, **Search**, **Filter**.
- ✅ Clicking **Edit** (from list) correctly allows changes.
- ✅ Transition between View and Edit modes is handled seamlessly.

---

## 🛠️ **TECHNICAL IMPLEMENTATION: TOOLBAR & FORM LOGIC**

### **1. Toolbar Mode Handling**
The toolbar state is dynamically computed based on the current UI state using the `getToolbarMode()` helper. This ensures the correct buttons (Save vs. Edit, etc.) are shown automatically.

```typescript
const getToolbarMode = (): MasterMode => {
  if (!showForm) return 'VIEW';           // List view
  if (viewMode) return 'VIEW_FORM';       // Read-only populated form
  return editingId ? 'EDIT' : 'CREATE';  // Editable form (Edit existing vs New)
};
```

### **2. The "New" (+) Action Flow**
When the user clicks the **Plus (+)** button, the UI performs a "Swap" rather than a popup. This maximizes screen real estate for data entry.

1.  **Handler**: `handleCreate()` is called.
2.  **State Change**: `setEditingId(null)` and `setShowForm(true)`.
3.  **UI Render**: The ternary operator in JSX swaps the `<Table>` for the `<UOMForm>`.
4.  **Focus**: The form component automatically focuses the first input field.

### **3. Centralized Action Handlers**
All toolbar clicks flow through a single `handleToolbarAction(action: string)` switch-case. This maintains a "single source of truth" for logic and prevents duplicate code.

- **`save`**: Calls `formRef.current?.submit()` to trigger internal form logic.
- **`delete`**: Performs a **pre-check** (`uomService.checkUsage`) before showing the deactivation modal.
- **`exit`**: Smarter logic—if in form, it cancels back to list; if in list, it exits to dashboard.

- **Bulk Potential**: This architecture allows for future "Select All" and bulk actions without UI redesign.

### **5. Advanced Layout: Decoupled Scrolling**
To maximize information density and keep core tools accessible, the page uses a **split-scroll** architecture:
- **Locked Area**: The Toolbar, Page Header, and Search/Filters are fixed at the top. This ensures the user never loses context or search capability while scrolling through data.
- **Scrollable Area**: Only the listing (table) or input form scrolls. This is achieved using a flex-container with `flex-col h-full` and `overflow-y-auto` on the content region.

### **6. Surgical Spacing Control**
To achieve a "One-Line Gap" look (listing starting immediately after search), we bypass global `page-container` padding:
- **Raw Tailwind**: Use `max-w-[80rem] mx-auto w-full px-4/6/8` directly on fixed/scrollable wrappers to eliminate hidden gaps from `.page-container`.
- **Zero-Sum Padding**: Header bottom padding is `pb-0`, Scrollable top padding is `pt-0`.
- **Hairline Scrollbar**: Always apply the `.hairline-scrollbar` utility for a minimal, premium feel.

---

## 🏆 **GOLD STANDARD: IMPLEMENTATION & VERIFICATION CHECKLIST**

Use this checklist before and after implementing the toolbar on any new UI module.

### **Phase 1: Component Structure**
- [ ] **State Setup**: Implement `showForm`, `editingId`, `selectedId`, and `viewMode` states.
- [ ] **Mode Helper**: Create a `getToolbarMode()` function to drive the toolbar component.
- [ ] **Toolbar Integration**: Place `<MasterToolbar>` at the top of the fragment (outside `page-container`).
- [ ] **Opaque Anchor**: Ensure toolbar has `sticky top-0 z-[100]` and a solid background (no transparency).
- [ ] **Form Ref**: Use `useRef` to connect the Toolbar to the Form's `submit()` and `reset()` methods.

### **Phase 2: Action Handlers**
- [ ] **CRUD Sync**: Implement `handleCreate`, `handleEdit`, `handleView`, and `handleDelete`.
- [ ] **Pre-Delete Check**: Implement a backend `check_usage` endpoint to prevent invalid deactivations *before* showing the modal.
- [ ] **Confirmation Dialog**: Use the flat-design `ConfirmationDialog` for all risky actions.
- [ ] **Error Dismissal**: All error banners must have an **"X"** close button and be non-persistent.

### **Phase 3: Visual Polish**
- [ ] **Decoupled Scrolling**: Toolbar and Filters must remain fixed; only the list/form area scrolls (`flex-1 overflow-y-auto`).
- [ ] **Hairline Scrollbar**: Apply `.hairline-scrollbar` to the scrollable container for a sleek, thin look.
- [ ] **Surgical Spacing**: Use raw Tailwind (max-width + centering) instead of `.page-container` on the inner wrappers to eliminate unwanted gaps.
- [ ] **Selection Highlight**: Selected rows must have a clear background color (e.g., `bg-blue-100`).
- [ ] **Loading States**: Global `loading` state should not hide the toolbar; use skeleton or inline spinners.

### **Phase 4: Final Verification**
- [ ] **Shortcut Keys**: Test F2 (New), F3 (Edit), F8 (Save), and ESC (Cancel) functionality.
- [ ] **Soft Delete**: Verify "Delete" deactivates the record (`is_active=False`) instead of a hard purge.
- [ ] **Cross-Page**: Navigate away and back to ensure selection state is handled correctly.
- [ ] **Browser Test**: Verify no horizontal scrollbars appear on the toolbar at various resolutions.

---

**Last Updated**: 2026-01-10 12:05 IST  
**Version**: 1.8 (Advanced Layout & Surgical Spacing)
**Approved By**: Mindra Retail Platform Team
