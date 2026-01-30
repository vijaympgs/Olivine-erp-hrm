# Screen: Internal Transfers

**Sidebar Path**: Retail > Inventory > Stock Movements > Internal Transfers  
**URL**: `/inventory/transfers`  
**Component**: `TransferListPage.tsx`

---

## Purpose

Manages stock transfers between locations within the same company.
Different from ICT which is between companies.

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Multiple locations | Yes |
| Stock at source location | Yes |
| User has `inventory.transfer.create` permission | Yes |

---

## Scenarios

### SC-TRANS-001: Create Transfer (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Transfers | List loads |
| 2 | Click New | CREATE mode |
| 3 | Select From Location | "Warehouse A" |
| 4 | Select To Location | "Store B" |
| 5 | Add item | Item lookup |
| 6 | Enter quantity | 50 |
| 7 | Save | Transfer draft |
| 8 | Submit | Status: In Transit |

---

### SC-TRANS-002: Receive Transfer

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Transfer in transit | At destination |
| 2 | Open transfer | Receiving view |
| 3 | Enter received qty | 50 |
| 4 | Click Receive | Stock updates |
| 5 | Source reduces | -50 |
| 6 | Destination increases | +50 |

---

### SC-TRANS-003: Partial Receive

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Transfer qty | 50 |
| 2 | Receive only 40 | Partial |
| 3 | Status | Partially Received |
| 4 | Remaining | 10 outstanding |

---

### SC-TRANS-004: Cannot Transfer More Than Available

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Source has 30 | Stock check |
| 2 | Enter 50 | Exceeds |
| 3 | Submit | Error: Insufficient stock |

---

### SC-TRANS-005: Cancel Transfer

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Draft transfer | Not yet submitted |
| 2 | Click Cancel | Confirmation |
| 3 | Confirm | Transfer cancelled |

---

### SC-TRANS-006: Transfer with Batch

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Batch-tracked item | Transfer |
| 2 | Select batch | Specific batch |
| 3 | Transfer | Batch moves with stock |

---

**Scenario Count**: 6
