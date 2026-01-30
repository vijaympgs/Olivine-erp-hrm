# Toolbar Configuration & Behavior Checklist

## 1. Toolbar String Applicability (ERPMenuItem.applicable_toolbar_config)
Revisit all menu items and assign default strings based on page nature:

| UI Category | Recommended Toolbar String | Actions Included | Note |
| :--- | :--- | :--- | :--- |
| **Masters** | `NESCKVDXR` | New, Edit, Save, Cancel, Clear, View, Delete, Exit, Refresh | Standard for Item/Customer Master |
| **Transactions** | `NESCKPVDXRTJZ` | All Master + Print, Submit, Reject, Auth | For Sales Orders, GRNs, etc. |
| **Config/Setup** | `NESCX` or `VRX` | Depends on if it's a simple list or a form | e.g., Valuation Methods |
| **Workflow/Approval** | `TZJH` | Submit, Reject, Hold, View | For Approval Queues |
| **Business Rules** | `NESCX` | New, Edit, Save, Cancel, Exit | e.g., Approval Rules |
| **Dashboards** | `RFQ` | Refresh, Filter, Search | No CRUD |
| **Reports** | `RFYXP` | Refresh, Filter, Export, Exit, Print | Focus on data output |

- [ ] **Action Items**:
    - [ ] Update `MOVEMENT_TYPES` to `NRQFX` (List) / `NESCKVDXR` (Form).
    - [ ] Update `VALUATION_METHODS` to `VRX`.
    - [ ] Update `INV_PARAMETERS` to `ESCKXR` (Edit focus).
    - [ ] Update `APPROVAL_RULES` to `NRQFX` (List).

---

## 2. Dynamic Behavior (Mode-based Button States)
Verify tool button states based on UI mode:

### Mode: VIEW (Default List/Record View)
- [ ] **Enabled**: New (`N`), Edit (`E`), View (`V`), Print (`P`), Email (`M`), Refresh (`R`), Export (`Y`), Import (`I`), Search (`Q`), Filter (`F`), Nav Buttons (`1234`), Tools (`BGW`), Help (`?`), Exit (`X`).
- [ ] **Disabled**: Save (`S`), Cancel (`C`), Clear (`K`), Submit (`T`), Reject (`J`), Hold (`H`), Void (`O`).
- [ ] **Conditional**: Delete (`D`) & Clone (`L`) enabled only if a record is selected.

### Mode: CREATE / NEW (After pressing `+`)
- [ ] **Enabled**: Save (`S`), Cancel (`C`), Clear (`K`), Help (`?`), Tools (`BGW`).
- [ ] **Disabled**: New (`N`), Edit (`E`), Delete (`D`), View (`V`), Print (`P`), Email (`M`), Refresh (`R`), Export (`Y`), Import (`I`), Search (`Q`), Filter (`F`), Nav Buttons (`1234`), Exit (`X`).
- [ ] **Transitions**: Pressing `Save` or `Cancel` returns to `VIEW` mode.

### Mode: EDIT (After pressing `Edit`)
- [ ] **Enabled**: Save (`S`), Cancel (`C`), Clear (`K`), Help (`?`), Tools (`BGW`).
- [ ] **Disabled**: Same as CREATE mode.
- [ ] **Transitions**: Pressing `Save` or `Cancel` returns to `VIEW` mode.

---

## 3. UI/UX Refinements
- [ ] Ensure all buttons are visible in a single line (No scrolling).
- [ ] Tooltip display for all 29 buttons.
- [ ] Consistency of icons across all modules.

---
**Please confirm the categorization and state transitions before I apply these defaults to the database and frontend logic.**
