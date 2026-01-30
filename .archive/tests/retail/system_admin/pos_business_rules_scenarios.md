# Screen: POS Business Rules

**Sidebar Path**: System Administration > POS Business Rules  
**URL**: `/pos/business-rules`  
**Component**: `POSBusinessRulesPage.tsx`

---

## Purpose

Configures vertical-specific behaviors and feature flags for POS operations.
Supports 8 verticals with category-based rule organization.

---

## Verticals Supported

| Vertical | Key | Description |
|----------|-----|-------------|
| General | `general` | Common retail settings |
| Grocery | `grocery` | Supermarket/Grocery features |
| Fashion | `fashion` | Apparel/Fashion retail |
| Restaurant | `restaurant` | F&B / QSR |
| Pharmacy | `pharmacy` | Medical/Pharmacy |
| Electronics | `electronics` | Electronics/Gadgets |
| Services | `services` | Salon/SPA/Professional |
| Fuel | `fuel` | Petrol Pump/Fuel Station |

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `pos.settings.admin` permission | Yes |

---

## Scenarios

### SC-RULES-001: View Business Rules Page

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/pos/business-rules` | Page loads |
| 2 | Verify vertical tabs | 8 tabs visible |
| 3 | Verify TOC | Table of contents with categories |

---

### SC-RULES-002: Navigate Between Verticals

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "General" tab | General rules shown |
| 2 | Click "Grocery" tab | Grocery rules shown |
| 3 | Click "Pharmacy" tab | Pharmacy rules shown |
| 4 | Each tab | Different rule set |

---

### SC-RULES-003: Toggle Boolean Rule

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select "Grocery" vertical | Tab active |
| 2 | Find `WEIGHTED_ITEMS` rule | Boolean toggle |
| 3 | Toggle from OFF to ON | Visual change |
| 4 | Click Save (F8) | Changes saved |
| 5 | Refresh (F5) | Value persists |

---

### SC-RULES-004: Set Numeric Value

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select "Grocery" vertical | Tab active |
| 2 | Find "Weight Precision" | Numeric input |
| 3 | Enter value: 3 | Accepts 1-4 range |
| 4 | Save | Value persisted |

---

### SC-RULES-005: Set Choice/Dropdown Value

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Find choice-type rule | Dropdown |
| 2 | Select option | e.g., "FIFO" |
| 3 | Save | Selection saved |

---

### SC-RULES-006: Master Toggle Behavior

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click vertical master toggle | e.g., "Pharmacy" |
| 2 | Toggle OFF | Vertical disabled |
| 3 | Child rules | All greyed out, non-editable |
| 4 | Toggle ON | Children editable again |

---

### SC-RULES-007: Search/Filter Rules

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter in search box | "batch" |
| 2 | Results | Only batch-related rules |
| 3 | Clear search | Full list restored |

---

### SC-RULES-008: Expand/Collapse All

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Collapse All" | All sections collapsed |
| 2 | Click "Expand All" | All sections expanded |
| 3 | TOC click | Scrolls to section |

---

### SC-RULES-009: Keyboard Shortcuts

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Press F5 | Refresh rules |
| 2 | Press F8 | Save changes |
| 3 | Press Esc | Exit (with confirm if dirty) |

---

### SC-RULES-010: Validation on Numeric

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Find numeric rule | With min/max |
| 2 | Enter out-of-range | e.g., -1 |
| 3 | Save | Validation error |
| 4 | Enter valid | Saves successfully |

---

### SC-RULES-011: Help Text Display

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Hover info icon | ℹ️ on any rule |
| 2 | Tooltip appears | Description of rule |

---

### SC-RULES-012: Rule Dependencies

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enable `BATCH_REQUIRED` | Pharmacy |
| 2 | Check dependent rule | e.g., `FEFO_ENABLED` |
| 3 | Verify | Dependent auto-enabled or required |

---

### SC-RULES-013: Unsaved Changes Warning

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Make changes | Toggle some rules |
| 2 | Navigate away | Click another menu |
| 3 | Confirm dialog | "Unsaved changes" warning |
| 4 | Cancel | Stay on page |
| 5 | Discard | Navigate without save |

---

### SC-RULES-014: Reset to Defaults

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Reset to Defaults" | If available |
| 2 | Confirmation | Confirm action |
| 3 | All rules | Reset to system defaults |

---

## Rule Categories (General Vertical)

| Category | Examples |
|----------|----------|
| 1.1 Stock Management | Allow negative stock, Reserve on hold |
| 1.2 Pricing & Quantity | Allow price override, Max qty per line |
| 1.3 Discounts & Loyalty | Allow discount, Max discount % |
| 1.4 Rounding & Amounts | Round total, Rounding precision |
| 1.5 Customer & Sales | Customer mandatory, Walk-in allowed |
| 1.6 Billing & Documents | Auto-print receipt, Email receipt |
| 1.7 Advanced Settings | Multi-UOM, Batch tracking |

---

**Scenario Count**: 14  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
