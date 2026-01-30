# Screen: Goods Receipt

**Sidebar Path**: Retail > Procurement > Receiving > Goods Receipts  
**URL**: `/procurement/receipts`  
**Component**: `GoodsReceiptListPage.tsx` → `GoodsReceiptFormPage.tsx`  
**Status**: Core Procurement Transaction

---

## Purpose

Goods Receipt Note (GRN) records the physical receipt of goods against a Purchase Order. It:
- Updates inventory levels
- Enables invoice matching (3-way match)
- Supports partial and full receipts
- Captures batch/serial numbers if required
- Triggers QC workflows

Per BBP evidence: PO → **GRN** → Invoice flow completes P2P.

---

## Preconditions

| Prerequisite | Dependency Chain | Required |
|--------------|------------------|----------|
| Approved PO | `/procurement/orders` | Yes |
| Receiving Location | Company setup | Yes |
| User Permission | `procurement.grn.create`, `procurement.grn.post` | Yes |

---

## Scenarios

### SC-GRN-001: Full Receipt (Happy Path)

**Type**: Happy Path  
**Priority**: Critical  
**Preconditions**: PO-001 approved, 100 units ordered

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to GRN list | `/procurement/receipts` | List loads |
| 2 | Click New | `[data-testid="btn-new"]` | CREATE mode |
| 3 | Select Source PO | `[data-testid="po-lookup"]` → PO-001 | PO lines populated |
| 4 | Verify lines | Grid shows ordered items | Open Qty = 100 |
| 5 | Enter Received Qty | All lines = 100 | Full receipt |
| 6 | Select Location | Dropdown = "Main Warehouse" | Location set |
| 7 | Click Save | `[data-testid="btn-save"]` | GRN saved (Draft) |
| 8 | Click Post | `[data-testid="btn-post"]` | Status: Posted |
| 9 | Verify inventory | Check stock levels | +100 units |

**Postconditions**: Stock increased, PO status updated to Received

---

### SC-GRN-002: Partial Receipt

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: PO with 100 units ordered

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Create GRN from PO | Select PO | Lines loaded |
| 2 | Enter partial qty | Received = 60 | 60 out of 100 |
| 3 | Post GRN | Post button | Success |
| 4 | Verify PO status | Check source PO | Open Qty = 40 |
| 5 | Verify stock | Check levels | +60 units |

**Postconditions**: PO remains open for remaining 40 units

---

### SC-GRN-003: Multiple Partial Receipts

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: PO with 100 units, 60 already received

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Create second GRN | Select same PO | Open Qty = 40 |
| 2 | Enter remaining | Received = 40 | All received |
| 3 | Post GRN | Post button | Success |
| 4 | Verify PO status | Check source PO | Status: Closed |
| 5 | Verify total stock | Check levels | +100 total |

**Postconditions**: PO fully received and closed

---

### SC-GRN-004: Over-Receipt Blocked

**Type**: Edge Case  
**Priority**: High  
**Preconditions**: PO with 100 units, 80 already received (open = 20)

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Create GRN | Select PO | Open Qty = 20 |
| 2 | Enter over qty | Received = 30 | Exceeds open |
| 3 | Post GRN | Post button | Error: Over-receipt |
| 4 | Verify message | Error display | "Cannot exceed PO quantity" |

**Postconditions**: GRN not posted, stock unchanged

---

### SC-GRN-005: Batch Capture at Receipt

**Type**: Feature  
**Priority**: High  
**Preconditions**: Item is batch-tracked, PO approved

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Create GRN | Select PO | Lines loaded |
| 2 | Click batch item line | Batch icon visible | Batch modal opens |
| 3 | Enter batch number | "BATCH-001" | Field populated |
| 4 | Enter expiry date | Future date | Date picker |
| 5 | Enter qty in batch | 100 | Batch qty |
| 6 | Save batch | Save | Batch assigned to line |
| 7 | Post GRN | Post button | Stock with batch |

**Postconditions**: Inventory has batch tracking enabled, FEFO applies

---

### SC-GRN-006: QC Reject Partial

**Type**: Feature  
**Priority**: Medium  
**Preconditions**: QC workflow enabled

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Create GRN | 100 received | Lines filled |
| 2 | Open QC section | QC tab or panel | QC fields visible |
| 3 | Mark QC pass qty | 90 passed | 10 rejected |
| 4 | Enter rejection reason | "Damaged" | Reason captured |
| 5 | Post GRN | Post button | Partial receipt |
| 6 | Check stock | Levels | +90 (not 100) |

**Postconditions**: Only QC-passed items added to stock

---

### SC-GRN-007: GRN without PO (Direct)

**Type**: Edge Case  
**Priority**: Low  
**Preconditions**: Direct receipt allowed in config

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Create GRN | No PO selected | Direct mode |
| 2 | Select Supplier | Manual entry | Supplier assigned |
| 3 | Add items manually | Item lookup | Items added |
| 4 | Enter quantities | Qty for each | Lines populated |
| 5 | Post GRN | Post button | Stock updated |

**Postconditions**: Stock received without formal PO (exceptional case)

---

### SC-GRN-008: Print GRN

**Type**: Feature  
**Priority**: Low  
**Preconditions**: GRN posted

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Open GRN | Posted GRN | Detail view |
| 2 | Click Print | Print button | Print preview |
| 3 | Download PDF | PDF option | File downloaded |

**Postconditions**: GRN document available for filing

---

## Data Cleanup

After test execution:
- Reverse posted GRNs
- Restore inventory levels
- Reset PO open quantities

---

**Scenario Count**: 8  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
