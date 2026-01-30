# Procurement Functional Test Scripts

This document contains detailed manual test scripts for the Procurement module, corresponding to the Test Case IDs defined in `01_Procurement_BBP_4x_Test_Mapping.md`.

**Version**: 1.0 (Stabilization Phase)
**Date**: 2025-12-27

---

## 4.1 Purchase Requisition (PR)

### PR-TS-01: Create PR with Multiple Items
**Objective**: Verify that a user can successfully create a PR with multiple line items.
**Preconditions**: User logged in, at least one Supplier and Item exist.

| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Navigate to Procurement > Requisitions. | Requisition list page loads. |
| 2 | Click "New" (or press F2). | New Requisition form opens. Status is "NEW". |
| 3 | Verify "Requested By" and "Location" fields. | Fields populate with current user and location. |
| 4 | Select a "Required Date" (future date). | Date is selected/typed. |
| 5 | (Optional) Select a "Suggested Supplier". | Supplier is selected. |
| 6 | Click "Add Item" in lines section. | A new line row appears. |
| 7 | Click "Item Code" field or press F1. | Product Lookup Modal opens. |
| 8 | Search for an item and select it. | Modal closes. Item Code, Name, and UOM are populated in the line. |
| 9 | Enter Quantity (e.g., 5). | Quantity field accepts the value. |
| 10 | Repeat steps 6-9 for 2 more items. | Multiple lines are added correctly. |
| 11 | Click "Save" (or press F8). | Page title updates to PR ID (e.g., PR-2025-0015). Status remains DRAFT. Form remains editable. |
| 12 | Click "Exit" (or Ctrl+Q). | Navigates back to the list. The new PR is visible. |

### PR-TS-02: Validate Context (Location/Company)
**Objective**: Ensure PR is created for the correct Location and Company.
**Preconditions**: User has access to multiple locations (if applicable).

| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Create a new PR. | Form loads. |
| 2 | Observe the "Location" field. | It shows the location selected in the global header/context. |
| 3 | Attempt to save with 0 items. | Validation error: "Invalid lines" or visual cue. |
| 4 | Add valid item and Save. | Saved successfully. |
| 5 | Check Database/Admin. | Record has correct `company_id` and `requesting_location_id`. |

### PR-TS-03: Submit PR for Approval
**Objective**: Verify the workflow transition from DRAFT to SUBMITTED.

| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Open an existing DRAFT PR. | Form loads with data. |
| 2 | Click "Submit" (or press F9). | Status changes to **SUBMITTED** (or APPROVED if no rules). Toolbar buttons update (Save disabled). |
| 3 | Attempt to edit fields. | Fields are Read-Only (except maybe special approver fields). |

---

## 4.2 Request for Quotation (RFQ)

### RFQ-TS-02: Standalone RFQ Creation
**Objective**: Verify creation of an RFQ directly (without PR link).

| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Navigate to Procurement > RFQs. | RFQ list page loads. |
| 2 | Click "New". | New RFQ form opens. |
| 3 | Select "Location". | Location is selected. |
| 4 | Enter "Title" (e.g., "Q1 Stationery Restock"). | Title accepts text. |
| 5 | Select "Deadline Date". | Date is valid. |
| 6 | Add Items using Lookup. | Items are added with canonical IDs resolved. |
| 7 | Click "Save". | RFQ saved. ID generated. Status: **DRAFT**. |

### RFQ-TS-04: Publish RFQ
**Objective**: Verify transition to PUBLISHED state (open for bidding).

| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Open a DRAFT RFQ. | Form loads. |
| 2 | (Future) Select Invited Vendors. | Vendors added. |
| 3 | Click "Publish" (or equivalent workflow action). | Status changes to **PUBLISHED**. |
| 4 | Verify Editability. | Main details (Items) should be locked. |

---

## 4.3 Purchase Order (PO)

### PO-TS-03: Standalone PO Creation
**Objective**: Verify direct creation of a Purchase Order to a supplier.

| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Navigate to Procurement > Purchase Orders. | PO List loads. |
| 2 | Click "New". | New PO form opens. |
| 3 | Select "Supplier" using Lookup (Input is Read-only). | Supplier selected. Payment terms may auto-populate. |
| 4 | Add Items (include Price). | Items added. Line totals calculated. |
| 5 | Verify Grand Total. | Sum of line totals is correct. |
| 6 | Click "Save". | PO Saved. Status: **DRAFT**. |

### PO-TS-05: PO Approval Workflow
**Objective**: Verify DRAFT -> SUBMITTED -> APPROVED flow.

| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Open DRAFT PO. | Form loads. |
| 2 | Click "Submit". | Status -> **SUBMITTED**. Fields locked. |
| 3 | (As Approver) Click "Approve". | Status -> **APPROVED**. |
| 4 | Verify Actions. | "Send" or "Receive" actions become available. "Edit" is disabled (or strictly controlled). |

---

## 4.10 Workflow & Integrations

### INT-TS-01: Global Exit/Cancel
**Objective**: Verify the 'Exit' functionality works consistently.

| Step | Action | Expected Result |
| :--- | :--- | :--- |
| 1 | Open any document (PR, RFQ, PO) in any status. | Form loads. |
| 2 | Click the "Exit" (X) icon in the toolbar. | Immediate navigation to the respective list page. |
