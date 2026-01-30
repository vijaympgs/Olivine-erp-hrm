# In-Place Master-Detail UI Pattern

**Status**: ✅ Approved Standard
**Applicability**: All Masters, Transactions, Workflow Settings.
**Exclusions**: Settings, POS Billing.

---

## 1. Overview
This pattern mandates an "In-Place" form experience for Master Data and Transactional pages. Instead of using Modals or separate routes, the Form component replaces the List component within the same page container, controlled by a unified **Master Toolbar**.

## 2. Page Structure
The Page Component (e.g., `UOMSetup.tsx`, `UserManagement.tsx`) is the orchestrator.
- **Header**: Persistent Page Header (Title, Subtitle).
- **Toolbar**: Persistent `MasterToolbar` at the top (below Header or above, as per layout).
- **Content Area**: Dynamic area that swaps between `ListView` and `FormView` based on state.

```tsx
<div className="page-container">
  <MasterToolbar ... />
  <PageHeader ... />
  
  {showForm ? (
    <FormComponent ref={formRef} ... />
  ) : (
    <ListComponent ... />
  )}
</div>
```

## 3. Toolbar Logic (Strict Rules)

### A. List Mode (View)
- **Enabled Actions**: `New`, `Refresh`, `Exit`. (Plus `Delete` if selection exists).
- **Disabled Actions**: `Save`, `Clear`.
- **Exit Action**: Navigates to the Module Home (e.g., `/retail`) or Parent Page.

### B. Form Mode (Create/Edit)
- **Enabled Actions**: `Save`, `Clear`, `Exit` **ONLY**.
- **Disabled Actions**: `New`, `Refresh`, `Delete`, `Export`, `Import`, `Search`.
- **Action Behaviors**:
  - **Save (F8)**: Triggers form submission (via `ref.current.submit()`).
  - **Clear (F5)**: Resets the form to a "New/Create" state (Clear all fields). **Crucial**: Even in Edit mode, Clear switches context to "Add New".
  - **Exit (ESC)**: Cancels the form and returns to **List Mode**.

## 4. Component Requirements

### Page Component
- Manages `showForm` and `editingId` state.
- Implements `handleToolbarAction` with a `switch` statement enforcing the above rules.
- Uses `getDisabledActions()` based on mode.

### Form Component (`MyForm.tsx`)
- Must accept a `ref` exposing `submit()` and `reset()`.
- **In-Place Design**: No Modal wrappers (`BaseModal`, fixed overlays). Should fill the available content container.
- **State**: Should default to "Create" mode data. `reset()` should restore this state.
- **Inputs**: Standard form fields with validation.

## 5. Visual Guide
- **Toolbar**: Light gray background, sticky top.
- **Icons**:
  - Delete: `Trash2` (Rose-600)
  - Exit: `X` (Gray-600)
  - Save: `Save` (Emerald-600)
  - Clear: `RotateCcw` (Amber-500)

---
**Adhere to this pattern for all future refactoring.**
