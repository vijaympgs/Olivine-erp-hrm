# Gold Standard Master Record Pattern

This guide documents the standard architecture for Master Record implementations in the Olivine Platform. All new master setups should follow this pattern to ensure consistency in UI/UX and behavior.

## 1. Architecture: Container & Form

Split logic into two files:
1.  **`[Name]Setup.tsx`** (Container) - Handles list view, toolbar, dialogs, and state.
2.  **`[Name]Form.tsx`** (Component) - Handles data entry, validation, and internal state.

## 2. The Setup Container (`[Name]Setup.tsx`)

### Responsibilities
- **List View**: Displays the grid/table of records.
- **Content Swapping**: Toggles between List and Form using `showForm`.
- **Toolbar**: Integrates `<MasterToolbar>` for actions (New, Edit, Save, etc.).
- **Dialogs**: Manages all confirmation dialogs (Exit, Discard, Delete, Clear, Success).

### Standard State
```typescript
// Data
const [items, setItems] = useState<Item[]>([]);
const [loading, setLoading] = useState(true);

// UI Mode
const [showForm, setShowForm] = useState(false);
const [editingId, setEditingId] = useState<string | null>(null);
const [viewMode, setViewMode] = useState(false); // Read-only mode

// Dialogs
const [isExitDialogOpen, setIsExitDialogOpen] = useState(false);
const [isDiscardDialogOpen, setIsDiscardDialogOpen] = useState(false);
const [saveSuccessConfig, setSaveSuccessConfig] = useState<{ isOpen: boolean, mode: 'NEW' | 'EDIT' } | null>(null);
```

### Standard Dialog Pattern
**Success Dialog**:
- **Confirm**: "Back to List" -> Closes form, reloads list.
- **Cancel**: "Create Another" (if NEW) or "Stay Here" (if EDIT). -> Resets form or keeps current state.

```typescript
<ConfirmationDialog
    isOpen={true}
    onClose={() => handlePostSaveRedirect('STAY')}
    onConfirm={() => handlePostSaveRedirect('LIST')}
    title={saveSuccessConfig.mode === 'NEW' ? "Item Created" : "Item Updated"}
    message={saveSuccessConfig.mode === 'NEW' 
        ? "Item created successfully. Return to list?" 
        : "Item changes saved. Return to list?"
    }
    confirmLabel="Back to List"
    cancelLabel={saveSuccessConfig.mode === 'NEW' ? "Create Another" : "Stay Here"}
    intent="success"
/>
```

## 3. The Form Component (`[Name]Form.tsx`)

### Interface
Must expose `submit` and `reset` via `forwardRef / useImperativeHandle`.

```typescript
export interface FormRef {
  submit: () => void;
  reset: () => void;
}

export const ItemForm = forwardRef<FormRef, Props>(({ id, readOnly, onSuccess, onCancel }, ref) => {
  useImperativeHandle(ref, () => ({
    submit: () => handleSubmit(),
    reset: () => resetForm()
  }));
```

### Styling Rules
- **Flat Design**: Use `rounded-none` for main containers.
- **Inputs**: Use standard tailwind `border-gray-300 focus:ring-orange-500`.
- **Validation**: Inline error messages below fields.

## 4. Checklist
- [ ] **Content Swap**: Form replaces list (no modals for main masters).
- [ ] **Toolbar**: Actions (Save, Cancel, New) mapped correctly.
- [ ] **View Mode**: Clicking "Eye" or double-clicking row opens form in Read-Only mode.
- [ ] **Clear Action**: "Clear" button resets filters (List mode) or resets form (Form mode).
- [ ] **Exit Guard**: Clicking "Exit" or switching views warns about unsaved changes.
