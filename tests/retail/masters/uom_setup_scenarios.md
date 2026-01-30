# Screen: UOM Setup

**Sidebar Path**: Retail > Merchandising > Setup > Units of Measure  
**URL**: `/inventory/uoms`  
**Component**: `UOMSetup.tsx`

---

## Purpose

Manages Units of Measure definitions. UOM is foundational - required before Item Master.
Supports base UOM and conversion factors.

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Company configured | Yes |
| User has `inventory.uom.create` permission | Yes |

---

## Scenarios

### SC-UOM-001: Create UOM (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to UOM Setup | List loads |
| 2 | Click New | CREATE mode |
| 3 | Enter Code | "PCS" |
| 4 | Enter Name | "Pieces" |
| 5 | Save | UOM created |

---

### SC-UOM-002: Create UOM with Base

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click New | CREATE mode |
| 2 | Enter Code | "BOX" |
| 3 | Enter Name | "Box" |
| 4 | Select Base UOM | "PCS" |
| 5 | Enter Factor | 12 |
| 6 | Save | 1 BOX = 12 PCS |

---

### SC-UOM-003: Duplicate Code Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create with existing code | "PCS" |
| 2 | Save | Error: Duplicate |

---

### SC-UOM-004: Edit UOM

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select UOM | Row selected |
| 2 | Click Edit | EDIT mode |
| 3 | Modify name | Change "Pieces" to "Units" |
| 4 | Save | Updated |

---

### SC-UOM-005: Cannot Delete UOM In Use

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | UOM used by items | Has references |
| 2 | Attempt delete | Error |
| 3 | Message | "UOM in use by X items" |

---

**Scenario Count**: 5
