# Screen: Stock Adjustment

**Sidebar Path**: Retail > Inventory > Stock Adjustments > Stock Adjustment Entry  
**URL**: `/inventory/adjustments/new`  
**Component**: `AdjustmentFormPage.tsx`

---

## Purpose

Records inventory corrections for:
- Damage/spoilage
- Theft/shrinkage
- Found stock
- Count corrections
- Sample/promotional use

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Items exist with stock | Yes |
| Reason codes configured | Yes |
| User has `inventory.adjustment.create` permission | Yes |

---

## Scenarios

### SC-ADJ-001: Positive Adjustment (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Adjustment | Form loads |
| 2 | Select Location | Warehouse |
| 3 | Select Reason | "Found Stock" |
| 4 | Add item | Item lookup |
| 5 | Enter positive qty | +10 |
| 6 | Save | Draft |
| 7 | Post | Stock increased |

---

### SC-ADJ-002: Negative Adjustment

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create adjustment | Form |
| 2 | Select Reason | "Damage" |
| 3 | Enter negative qty | -5 |
| 4 | Post | Stock reduced |

---

### SC-ADJ-003: Approval Required

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Large adjustment | Exceeds threshold |
| 2 | Submit | Status: Pending Approval |
| 3 | Manager approves | Then posts |

---

### SC-ADJ-004: Cannot Exceed Stock

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Stock on hand | 20 |
| 2 | Adjust by | -25 |
| 3 | Post | Error: Would go negative |

---

### SC-ADJ-005: Reason Code Required

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create adjustment | No reason |
| 2 | Save | Validation error |
| 3 | Message | "Reason required" |

---

### SC-ADJ-006: Batch Adjustment

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Batch-tracked item | Adjust |
| 2 | Select specific batch | Batch lookup |
| 3 | Adjust qty | Per batch |
| 4 | Post | Batch stock updated |

---

**Scenario Count**: 6
