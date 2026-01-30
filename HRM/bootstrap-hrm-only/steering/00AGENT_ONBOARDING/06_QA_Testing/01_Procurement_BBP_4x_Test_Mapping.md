# Procurement BBP 4.x — Detailed Test Script Mapping

This document provides a **detailed, canonical mapping** of Procurement test scripts to BBP sections **4.1 → 4.10**.
It is intended for architects, QA leads, auditors, and implementation teams.

---

## 4.1 Purchase Requisition (PR)

**Objective:** Validate internal demand creation, approvals, and integrity.

### Test Cases
- PR-TS-01: Create PR with ≥10 items
- PR-TS-02: Validate company & location context
- PR-TS-03: Submit PR for approval
- PR-TS-04: Approve PR (single / multi-level)
- PR-TS-05: Reject & resubmit PR
- PR-TS-06: Amend PR before approval
- PR-TS-07: Lock PR after approval
- PR-TS-08: Permission checks
- PR-TS-09: Invalid quantity/date validation
- PR-TS-10: Audit trail verification

---

## 4.2 Request for Quotation (RFQ)

**Objective:** Ensure competitive vendor evaluation with full auditability.

### Test Cases
- RFQ-TS-01: Create RFQ from approved PR (≥10 items)
- RFQ-TS-02: Standalone RFQ creation
- RFQ-TS-03: Add minimum vendors
- RFQ-TS-04: Publish RFQ
- RFQ-TS-05: Vendor response submission
- RFQ-TS-06: Partial quote handling
- RFQ-TS-07: Multi-round negotiation
- RFQ-TS-08: Blocked vendor rule
- RFQ-TS-09: Evaluation & scoring
- RFQ-TS-10: Award approval
- RFQ-TS-11: Cancel / close RFQ
- RFQ-TS-12: RFQ → PO eligibility

---

## 4.3 Purchase Order (PO)

**Objective:** Validate legally binding purchase commitments.

### Test Cases
- PO-TS-01: Create PO from RFQ award
- PO-TS-02: Create PO from PR
- PO-TS-03: Standalone PO
- PO-TS-04: PO with ≥10 items
- PO-TS-05: PO approval workflow
- PO-TS-06: Amend PO before issue
- PO-TS-07: Controlled amendment after issue
- PO-TS-08: Cancel PO
- PO-TS-09: PO → GRN readiness
- PO-TS-10: Commercial lock enforcement

---

## 4.4 Advance Shipment Notice (ASN)

**Objective:** Validate shipment visibility before receipt.

### Test Cases
- ASN-TS-01: Create ASN against PO
- ASN-TS-02: Partial shipment ASN
- ASN-TS-03: Over-shipment prevention
- ASN-TS-04: ASN → GRN linkage
- ASN-TS-05: ASN cancellation

---

## 4.5 Goods Receipt Note (GRN) & QC

**Objective:** Validate physical receipt and inventory impact.

### Test Cases
- GRN-TS-01: Full GRN (≥10 items)
- GRN-TS-02: Partial GRN (multiple receipts)
- GRN-TS-03: Over / under receipt rules
- GRN-TS-04: QC accept / reject
- GRN-TS-05: Inventory update validation
- GRN-TS-06: GRN reversal
- GRN-TS-07: GRN audit trail

---

## 4.6 Supplier Invoice

**Objective:** Ensure financial matching and tolerances.

### Test Cases
- INV-TS-01: Invoice against GRN
- INV-TS-02: Invoice against PO
- INV-TS-03: 2-way / 3-way matching
- INV-TS-04: Price mismatch within tolerance
- INV-TS-05: Price mismatch beyond tolerance
- INV-TS-06: Tax mismatch handling
- INV-TS-07: Invoice approval
- INV-TS-08: Invoice posting
- INV-TS-09: Duplicate invoice prevention

---

## 4.7 Returns & Adjustments

### Test Cases
- RET-TS-01: Return against GRN
- RET-TS-02: Return after invoice
- RET-TS-03: Debit note generation
- RET-TS-04: Stock & financial adjustment

---

## 4.8 Procurement Configuration

### Test Cases
- CFG-TS-01: RFQ threshold enforcement
- CFG-TS-02: Approval matrix impact
- CFG-TS-03: Invoice tolerance impact
- CFG-TS-04: Category/location rules

---

## 4.9 Reports & Audit

### Test Cases
- AUD-TS-01: End-to-end traceability
- AUD-TS-02: Status timeline
- AUD-TS-03: Vendor performance
- AUD-TS-04: Compliance reporting

---

## 4.10 Integrations

### Test Cases
- INT-TS-01: Inventory integration
- INT-TS-02: Finance/AP integration
- INT-TS-03: Notifications
- INT-TS-04: Vendor portal touchpoints

---

**Status:** Locked reference for QA and audit.