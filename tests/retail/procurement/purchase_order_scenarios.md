# Screen: Purchase Order

**Sidebar Path**: Retail > Procurement > Purchasing > Purchase Orders  
**URL**: `/procurement/orders`  
**Component**: `PurchaseOrderListPage.tsx` → `PurchaseOrderFormPage.tsx`  
**Status**: Core Procurement Transaction

---

## Purpose

Purchase Orders (PO) represent the commitment to purchase goods from suppliers. The PO is central to the Procure-to-Pay flow:
- PR → **PO** → GRN → Invoice Match → Payment

Per BBP evidence: PO can be created directly or from approved PR.

---

## Preconditions

| Prerequisite | Dependency Chain | Required |
|--------------|------------------|----------|
| Active Supplier | `/partners/suppliers` | Yes |
| Purchasable Items | `/inventory/item-master` | Yes |
| Delivery Location | Company setup | Yes |
| Tax Profiles (optional) | Finance setup | No |
| User Permission | `procurement.po.create`, `procurement.po.approve` | Yes |

---

## Scenarios

### SC-PO-001: Create PO (Direct - Happy Path)

**Type**: Happy Path  
**Priority**: Critical  
**Preconditions**: Supplier "SUP-001" exists, Item "SKU-001" exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to PO list | `/procurement/orders` | List view loads |
| 2 | Click New | `[data-testid="btn-new"]` | Form in CREATE mode |
| 3 | Verify PO Number | Auto-generated | Format: PO-YYYY-NNNNN |
| 4 | Select Supplier | `[data-testid="supplier-lookup"]` → SUP-001 | Supplier info loads |
| 5 | Set Delivery Date | Date picker | Future date acceptable |
| 6 | Select Ship To | Location dropdown | Warehouse selected |
| 7 | Click Add Line | `[data-testid="btn-add-line"]` | Empty line row |
| 8 | Select Item | Item lookup → SKU-001 | Item details populate |
| 9 | Enter Quantity | Qty = 100 | Quantity set |
| 10 | Verify Rate | Price from master or enter | Rate: ₹50.00 |
| 11 | Verify Line Total | Auto-calculated | ₹5,000.00 |
| 12 | Click Save | `[data-testid="btn-save"]` | Status: Draft |
| 13 | Click Submit | `[data-testid="btn-submit"]` | Status: Pending Approval |

**Postconditions**: PO in Pending Approval status, no inventory impact yet

---

### SC-PO-002: Create PO from Approved PR

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: PR in Approved status exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to approved PR | `/procurement/requisitions` | Find approved PR |
| 2 | Open PR | Click row | PR detail view |
| 3 | Click "Convert to PO" | Action button | PO form opens |
| 4 | Verify lines | Auto-populated from PR | Items, quantities match |
| 5 | Select Supplier | Required field | Supplier assigned |
| 6 | Save and Submit | Standard flow | PO created, linked to PR |

**Postconditions**: PO linked to source PR, PR status updated

---

### SC-PO-003: Approve PO

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: PO in Pending Approval, user has approve permission

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Find Pending PO | Filter by status | PO visible |
| 2 | Open PO | Click row | Detail view |
| 3 | Click Approve | `[data-testid="btn-approve"]` | Confirmation dialog |
| 4 | Confirm | Yes | Status: Approved |
| 5 | Verify status | Header | "Approved" badge |

**Postconditions**: PO ready for receiving (GRN)

---

### SC-PO-004: Reject PO

**Type**: Edge Case  
**Priority**: Medium  
**Preconditions**: PO in Pending Approval

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Open Pending PO | Click row | Detail view |
| 2 | Click Reject | `[data-testid="btn-reject"]` | Rejection dialog |
| 3 | Enter reason | Required text field | Reason captured |
| 4 | Confirm | Submit | Status: Rejected |

**Postconditions**: PO rejected, cannot receive against it

---

### SC-PO-005: Edit Draft PO

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: PO in Draft status

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Open Draft PO | Click row | EDIT mode |
| 2 | Add line | Add new item | Line added |
| 3 | Modify quantity | Change existing line | Updated |
| 4 | Save | Save button | Changes persisted |

**Postconditions**: Draft updated, can still submit

---

### SC-PO-006: Cannot Edit Approved PO

**Type**: Edge Case  
**Priority**: Medium  
**Preconditions**: PO in Approved status

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Open Approved PO | Click row | VIEW mode |
| 2 | Verify Edit disabled | Toolbar | Edit button disabled or hidden |
| 3 | Attempt direct edit | Try field interaction | Fields read-only |

**Postconditions**: Approved PO immutable

---

### SC-PO-007: Cancel PO

**Type**: Edge Case  
**Priority**: Medium  
**Preconditions**: PO in Draft or Pending status

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Open PO | Click row | Detail view |
| 2 | Click Cancel | `[data-testid="btn-cancel"]` | Confirmation |
| 3 | Enter reason | Optional | - |
| 4 | Confirm | Yes | Status: Cancelled |

**Postconditions**: PO cancelled, no receiving possible

---

### SC-PO-008: Validation - No Lines

**Type**: Validation  
**Priority**: High  
**Preconditions**: None

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Create PO | Fill header only | Supplier, dates |
| 2 | Click Save | Without adding lines | Validation error |
| 3 | Verify message | Error display | "At least one line item required" |

**Postconditions**: Cannot save PO without lines

---

### SC-PO-009: Print/PDF PO

**Type**: Feature  
**Priority**: Low  
**Preconditions**: PO exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Open PO | Any status | Detail view |
| 2 | Click Print | `[data-testid="btn-print"]` | Print preview |
| 3 | Verify format | Preview | Company header, lines, totals |
| 4 | Download PDF | PDF option | File downloaded |

**Postconditions**: PO document generated

---

### SC-PO-010: Close PO (Fully Received)

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: PO fully received via GRN

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Open received PO | All lines received | Detail view |
| 2 | Verify status | Header | Status: Received or Closed |
| 3 | Check open qty | Lines | All Open Qty = 0 |

**Postconditions**: PO lifecycle complete

---

## Data Cleanup

After test execution:
- Cancel test POs
- Delete draft POs
- Reverse any GRNs against test POs

---

**Scenario Count**: 10  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
