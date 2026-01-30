# Screen: POS Business Rules

**Sidebar Path**: Retail > Store Ops > Settings > Business Rules  
**URL**: `/pos/business-rules`  
**Component**: `POSBusinessRulesPage.tsx`

---

## Purpose

Configures vertical-specific behaviors and feature flags for POS. Supports 8 verticals:
- General, Grocery, Fashion, Restaurant, Pharmacy, Electronics, Services, Fuel

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `pos.settings.admin` permission | Yes |

---

## Scenarios

### SC-RULES-001: View Rules List

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Business Rules | Page loads |
| 2 | Verify vertical tabs | All 8 verticals shown |
| 3 | Verify categories | TOC visible |

---

### SC-RULES-002: Toggle Boolean Rule

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select vertical | e.g., Grocery |
| 2 | Find toggle rule | e.g., WEIGHTED_ITEMS |
| 3 | Toggle ON | Switch moves |
| 4 | Save | Changes persisted |

---

### SC-RULES-003: Set Numeric Value

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Find numeric rule | e.g., Weight Precision |
| 2 | Enter value | 3 decimal places |
| 3 | Save | Value saved |

---

### SC-RULES-004: Master Toggle Behavior

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Disable vertical | e.g., Pharmacy OFF |
| 2 | Child rules | All greyed out |
| 3 | Cannot edit | Children locked |
| 4 | Enable vertical | Children editable again |

---

### SC-RULES-005: Search Rules

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter search term | "batch" |
| 2 | Results filtered | Only batch-related rules |
| 3 | Clear search | Full list restored |

---

### SC-RULES-006: Expand/Collapse All

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Expand All | All sections open |
| 2 | Click Collapse All | All sections closed |

---

### SC-RULES-007: Keyboard Shortcuts

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Press F5 | Refresh rules |
| 2 | Press F8 | Save changes |
| 3 | Press Esc | Exit |

---

### SC-RULES-008: Validation on Numeric

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter negative | -5 where not allowed |
| 2 | Validation | Error shown |

---

**Scenario Count**: 8
