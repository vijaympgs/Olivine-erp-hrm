# Screen: Purchase Requisition

**Sidebar Path**: Retail > Procurement > Purchasing > Purchase Requisitions  
**URL**: `/procurement/requisitions`  
**Component**: `RequisitionListPage.tsx` → `RequisitionFormPage.tsx`

---

## Purpose

Internal request for goods before formal PO. PR captures demand which gets approved before committing to suppliers.

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Items exist | Yes |
| User has `procurement.pr.create` permission | Yes |

---

## Scenarios

### SC-PR-001: Create PR (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to PR list | List loads |
| 2 | Click New | CREATE mode |
| 3 | PR Number auto-generated | PR-YYYY-NNNNN |
| 4 | Select Requestor | Current user |
| 5 | Select Department | Operations |
| 6 | Set Priority | Normal |
| 7 | Set Required Date | Future |
| 8 | Add line item | Item lookup |
| 9 | Enter quantity | 100 |
| 10 | Save | Draft |
| 11 | Submit | Pending Approval |

---

### SC-PR-002: Approve PR

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Pending PR | Detail view |
| 2 | Review details | Lines visible |
| 3 | Click Approve | Confirmation |
| 4 | Confirm | Status: Approved |

---

### SC-PR-003: Reject PR

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Pending PR | Detail view |
| 2 | Click Reject | Reason dialog |
| 3 | Enter reason | Required |
| 4 | Confirm | Status: Rejected |

---

### SC-PR-004: Convert PR to PO

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Approved PR | Detail view |
| 2 | Click "Convert to PO" | PO form |
| 3 | Lines populated | From PR |
| 4 | Select Supplier | Required |
| 5 | Save | PO created, linked |

---

### SC-PR-005: Edit Draft PR

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Draft PR | EDIT mode |
| 2 | Add line | New item |
| 3 | Modify qty | Changed |
| 4 | Save | Updated |

---

### SC-PR-006: Cannot Edit Approved PR

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Approved PR | VIEW mode |
| 2 | Edit disabled | Read-only |

---

**Scenario Count**: 6
