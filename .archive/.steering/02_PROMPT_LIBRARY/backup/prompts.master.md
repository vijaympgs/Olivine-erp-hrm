# Master Prompt Template for Module Build

**Reference Documents**:
- `docs/steering/COMPONENT_LIBRARY.md` - UI components, design tokens, layout patterns
- `docs/steering/STATE_PATTERNS.md` - List, form, modal, API hook patterns
- `docs/templates/mst01.md` - Simple Master Template
- `docs/templates/mst02.md` - Medium Master Template  
- `docs/templates/mst03.md` - Complex Master Template
- `docs/templates/txn01.md` - Simple Transaction Template
- `docs/templates/txn02.md` - Medium Transaction Template
- `docs/templates/txn03.md` - Complex Transaction Template

---

## Prompt Template

```
Build [MODULE_NAME] as per BBP [SECTION_REF].

────────────────────────────────────────
BACKEND
────────────────────────────────────────
Models:
- [Model1] (fields as per BBP X.X.X)
- [Model2] (related/embedded)

API Endpoints:
- CRUD: /api/[module]/
- Special: /api/[module]/:id/[action]/

Permissions:
- Admin: [actions]
- Manager: [actions]
- User: [actions]

Validations:
- [Validation rule 1]
- [Validation rule 2]

────────────────────────────────────────
FRONTEND
────────────────────────────────────────
Template: [MST_TEMPLATE_01 | MST_TEMPLATE_02 | MST_TEMPLATE_03 | TXN_TEMPLATE_01 | TXN_TEMPLATE_02 | TXN_TEMPLATE_03]

Component Structure:
- [Module].jsx (main)
- [Module]Form.jsx (create/edit)
- [Module]Table.jsx (list view)
- [Module]Filters.jsx (if needed)

Pages/Views:
- List: [table | card | tree]
- Create/Edit: [form | modal | drawer | tabbed]

UI Behavior:
- View modes: [table | card | tree | graph]
- Tabs: [tab names if tabbed form]
- Filters: [filter fields]
- Actions: [create, edit, delete, bulk, export, etc.]

────────────────────────────────────────
COMPONENT & STATE REFERENCE
────────────────────────────────────────
Components Used:
- [Table, Tabs, Modal, Select, Toggle, Badge, etc.]

State Pattern:
- List: [standard | with selection | with tree]
- Form: [standard | tabbed | wizard]
- Modal: [standard | confirmation | drawer]

Status State Machine:
- States: [STATE1, STATE2, STATE3]
- Transitions: [allowed changes]
- Display: Badge with color mapping

API Hook:
- useCrud for /api/[module]/

────────────────────────────────────────
CONSTRAINTS / BUSINESS RULES
────────────────────────────────────────
- [Rule 1]
- [Rule 2]
- [Validation blocks]

────────────────────────────────────────
DELIVERABLES
────────────────────────────────────────
☐ Django Models
☐ DRF Serializers (nested if needed)
☐ DRF ViewSets + URLs
☐ React Components (per template structure)
☐ API Service/Hooks
☐ Validation Schema (Yup)
☐ Mock Data (for dev)
```

---

## Example: Terminal Management (BBP 6.1)

```
Build Terminal Management as per BBP 6.1.

────────────────────────────────────────
BACKEND
────────────────────────────────────────
Models:
- Terminal (as per BBP 6.1.2)
- TerminalTransactionSettings (embedded or related)
- TerminalTenderMapping (M2M with TenderType)

API Endpoints:
- CRUD: /api/pos/terminals/
- Special: /api/pos/terminals/:id/clone/

Permissions:
- Admin: full CRUD
- Manager: read, update
- Cashier: read-only

Validations:
- terminal_code unique per location
- At least one tender enabled
- Cannot delete if active sessions exist

────────────────────────────────────────
FRONTEND
────────────────────────────────────────
Template: MST_TEMPLATE_02 (Medium Complexity Master)

Component Structure:
- Terminal.jsx
- TerminalForm.jsx (tabbed)
- TerminalTable.jsx
- TerminalFilters.jsx

Pages/Views:
- List: Table with location/status filters
- Create/Edit: Tabbed form (General, Transactions, Tenders, Hardware)

UI Behavior:
- View modes: table only
- Tabs: General | Transactions | Tenders | Departments | Hardware
- Filters: location, status, terminal_type
- Actions: create, edit, clone, deactivate

────────────────────────────────────────
COMPONENT & STATE REFERENCE
────────────────────────────────────────
Components Used:
- Table (with sorting, pagination)
- Tabs (for form sections)
- Modal (for create/edit)
- Select (for dropdowns - location, type)
- Toggle (for boolean fields - is_active, allow_discount)
- Badge (for status display)

State Pattern:
- List: standard list state (data, loading, filters, pagination)
- Form: tabbed form state (formData, errors, activeTab, isSubmitting)
- Modal: standard modal state (isOpen, mode, selectedItem)

Status State Machine:
- States: ACTIVE, INACTIVE, MAINTENANCE
- Transitions: ACTIVE ↔ INACTIVE, ACTIVE → MAINTENANCE → ACTIVE
- Display: Badge with color mapping (success/surface/warning)

API Hook:
- useCrud for /api/pos/terminals/

────────────────────────────────────────
CONSTRAINTS / BUSINESS RULES
────────────────────────────────────────
- Terminal must belong to one location
- Disabled terminal cannot be used for billing
- Terminal policies override global defaults
- At least one tender must be enabled

────────────────────────────────────────
DELIVERABLES
────────────────────────────────────────
☐ Django Models (Terminal, TerminalTransactionSettings, TerminalTenderMapping)
☐ DRF Serializers (nested for settings/tenders)
☐ DRF ViewSets + URLs
☐ React Components (Terminal, TerminalForm, TerminalTable, TerminalFilters)
☐ API Service (useTerminal hook)
☐ Validation Schema (Yup)
☐ Mock Data