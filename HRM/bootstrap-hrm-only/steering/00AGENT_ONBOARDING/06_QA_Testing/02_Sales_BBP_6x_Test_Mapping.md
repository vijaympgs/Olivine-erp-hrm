# Sales BBP 6.x — Detailed Test Script Mapping

This document provides a **detailed, canonical mapping** of Sales test scripts to BBP sections **6.1 → 6.5**.
It is intended for architects, QA leads, auditors, and implementation teams.

---

## 6.1 Sales Quotation (Quote)

**Objective:** Validate customer demand capture, pricing, approvals, and quote-to-order conversion.

### Test Cases
- QT-TS-01: Create Quote with ≥10 items
- QT-TS-02: Validate company & location context
- QT-TS-03: Submit Quote for approval
- QT-TS-04: Approve Quote (single / multi-level)
- QT-TS-05: Reject & resubmit Quote
- QT-TS-06: Amend Quote before sending to customer
- QT-TS-07: Send Quote to customer (email/PDF)
- QT-TS-08: Customer acceptance/rejection
- QT-TS-09: Quote expiry handling
- QT-TS-10: Quote → Order conversion
- QT-TS-11: Partial conversion (multiple orders from one quote)
- QT-TS-12: Quote revision workflow
- QT-TS-13: Price override validation
- QT-TS-14: Margin check enforcement
- QT-TS-15: Discount approval workflow
- QT-TS-16: Quote win/loss tracking
- QT-TS-17: Permission checks
- QT-TS-18: Invalid quantity/date validation
- QT-TS-19: Audit trail verification
- QT-TS-20: Duplicate quote prevention

---

## 6.2 Sales Order (SO)

**Objective:** Validate order fulfillment, inventory allocation, and order-to-invoice flow.

### Test Cases
- SO-TS-01: Create Order from approved Quote (≥10 items)
- SO-TS-02: Standalone Order creation
- SO-TS-03: Order approval workflow
- SO-TS-04: Credit limit validation
- SO-TS-05: Credit hold & override
- SO-TS-06: Inventory allocation
- SO-TS-07: Backorder handling
- SO-TS-08: Picking workflow
- SO-TS-09: Packing workflow
- SO-TS-10: Partial shipment
- SO-TS-11: Multiple shipments per order
- SO-TS-12: Shipment tracking
- SO-TS-13: Delivery confirmation
- SO-TS-14: Order → Invoice conversion
- SO-TS-15: Partial invoicing
- SO-TS-16: Multiple invoices per order
- SO-TS-17: Order amendment before shipment
- SO-TS-18: Order cancellation
- SO-TS-19: Order revision workflow
- SO-TS-20: Margin visibility & protection
- SO-TS-21: Price source traceability
- SO-TS-22: Fulfillment timeline tracking
- SO-TS-23: Permission checks
- SO-TS-24: Audit trail verification
- SO-TS-25: Order closure workflow

---

## 6.3 Sales Invoice

**Objective:** Validate invoice generation, payment tracking, and revenue recognition.

### Test Cases
- INV-TS-01: Invoice against Order
- INV-TS-02: Invoice against Shipment
- INV-TS-03: Standalone Invoice
- INV-TS-04: Invoice with ≥10 items
- INV-TS-05: Order-based matching
- INV-TS-06: Delivery-based matching
- INV-TS-07: Price variance within tolerance
- INV-TS-08: Price variance beyond tolerance
- INV-TS-09: Tax calculation & compliance
- INV-TS-10: Invoice approval workflow
- INV-TS-11: Send Invoice to customer
- INV-TS-12: Payment recording (full)
- INV-TS-13: Payment recording (partial)
- INV-TS-14: Multiple payments per invoice
- INV-TS-15: Payment allocation
- INV-TS-16: Overpayment handling
- INV-TS-17: Unapplied cash
- INV-TS-18: Invoice overdue tracking
- INV-TS-19: Dunning process
- INV-TS-20: Credit note generation
- INV-TS-21: Debit note generation
- INV-TS-22: Invoice revision workflow
- INV-TS-23: Revenue recognition (on invoice)
- INV-TS-24: Revenue recognition (on payment)
- INV-TS-25: Revenue recognition (on delivery)
- INV-TS-26: Write-off processing
- INV-TS-27: Duplicate invoice prevention
- INV-TS-28: Invoice posting to AR
- INV-TS-29: Permission checks
- INV-TS-30: Audit trail verification

---

## 6.4 Sales Return (RMA)

**Objective:** Validate return authorization, inspection, refund/exchange processing.

### Test Cases
- RMA-TS-01: Create RMA against Order
- RMA-TS-02: Create RMA against Invoice
- RMA-TS-03: RMA approval workflow
- RMA-TS-04: Return within policy window
- RMA-TS-05: Return outside policy window
- RMA-TS-06: Return receipt
- RMA-TS-07: Quality inspection (accept)
- RMA-TS-08: Quality inspection (reject)
- RMA-TS-09: Quality inspection (partial)
- RMA-TS-10: Refund processing (full)
- RMA-TS-11: Refund processing (partial)
- RMA-TS-12: Refund to original payment method
- RMA-TS-13: Refund to store credit
- RMA-TS-14: Exchange order creation
- RMA-TS-15: Restocking fee calculation
- RMA-TS-16: Return shipping cost handling
- RMA-TS-17: Return-to-stock disposition
- RMA-TS-18: Quarantine disposition
- RMA-TS-19: Scrap disposition
- RMA-TS-20: Repair disposition
- RMA-TS-21: Vendor return disposition
- RMA-TS-22: Credit note generation
- RMA-TS-23: Inventory adjustment
- RMA-TS-24: Customer satisfaction tracking
- RMA-TS-25: RMA revision workflow
- RMA-TS-26: RMA cancellation
- RMA-TS-27: Permission checks
- RMA-TS-28: Audit trail verification
- RMA-TS-29: Return policy enforcement
- RMA-TS-30: Photo evidence for damage claims

---

## 6.5 Sales Configuration

**Objective:** Validate configuration-driven behavior across all sales modules.

### Test Cases
- CFG-TS-01: Quote enablement toggle
- CFG-TS-02: Quote-required-for-order enforcement
- CFG-TS-03: Credit check enforcement
- CFG-TS-04: Backorder allowance
- CFG-TS-05: Partial shipment/invoice allowance
- CFG-TS-06: Auto-allocation toggle
- CFG-TS-07: Auto-invoice-on-shipment toggle
- CFG-TS-08: Approval matrix (by amount)
- CFG-TS-09: Approval matrix (by discount %)
- CFG-TS-10: Approval matrix (by customer type)
- CFG-TS-11: Tolerance settings (price)
- CFG-TS-12: Tolerance settings (quantity)
- CFG-TS-13: Tolerance settings (credit limit)
- CFG-TS-14: Margin threshold enforcement
- CFG-TS-15: Return policy (by category)
- CFG-TS-16: Return policy (by customer type)
- CFG-TS-17: Restocking fee calculation
- CFG-TS-18: Revenue recognition method
- CFG-TS-19: Dunning schedule
- CFG-TS-20: Payment terms defaults
- CFG-TS-21: Category/location/customer type rules
- CFG-TS-22: Rule resolution hierarchy
- CFG-TS-23: Config change audit trail
- CFG-TS-24: Conflicting config prevention
- CFG-TS-25: Effective settings preview

---

## 6.6 Sales Reports & Analytics

**Objective:** Validate reporting, dashboards, and analytics.

### Test Cases
- RPT-TS-01: Sales pipeline report
- RPT-TS-02: Quote conversion rate
- RPT-TS-03: Order fulfillment metrics
- RPT-TS-04: Invoice aging report
- RPT-TS-05: Customer payment behavior
- RPT-TS-06: Return rate analysis
- RPT-TS-07: Margin analysis
- RPT-TS-08: Sales person performance
- RPT-TS-09: Customer satisfaction metrics
- RPT-TS-10: Revenue recognition report

---

## 6.7 Sales Audit & Compliance

**Objective:** Validate end-to-end traceability and compliance.

### Test Cases
- AUD-TS-01: End-to-end traceability (Quote → Order → Invoice → Payment)
- AUD-TS-02: Status timeline verification
- AUD-TS-03: Approval audit trail
- AUD-TS-04: Price change audit trail
- AUD-TS-05: Credit override audit trail
- AUD-TS-06: Return reason analysis
- AUD-TS-07: Tax compliance reporting
- AUD-TS-08: Revenue recognition audit
- AUD-TS-09: Customer credit limit compliance
- AUD-TS-10: Discount approval compliance

---

## 6.8 Sales Integrations

**Objective:** Validate integration touchpoints.

### Test Cases
- INT-TS-01: Inventory integration (allocation, reservation, return)
- INT-TS-02: Finance/AR integration (invoice posting, payment)
- INT-TS-03: CRM integration (customer data, opportunities)
- INT-TS-04: Payment gateway integration
- INT-TS-05: Shipping carrier integration
- INT-TS-06: Email notifications (quote, order, invoice)
- INT-TS-07: Customer portal touchpoints
- INT-TS-08: Mobile app integration
- INT-TS-09: eCommerce integration
- INT-TS-10: Tax calculation service integration

---

## Summary Statistics

**Total Test Cases:** 175+

**By Module:**
- 6.1 Sales Quotation: 20 test cases
- 6.2 Sales Order: 25 test cases
- 6.3 Sales Invoice: 30 test cases
- 6.4 Sales Return (RMA): 30 test cases
- 6.5 Sales Configuration: 25 test cases
- 6.6 Reports & Analytics: 10 test cases
- 6.7 Audit & Compliance: 10 test cases
- 6.8 Integrations: 10 test cases

**Coverage:**
- ✅ All BBP sections (6.1-6.5) covered
- ✅ Happy path scenarios
- ✅ Exception handling
- ✅ Approval workflows
- ✅ Integration points
- ✅ Audit & compliance
- ✅ Configuration-driven behavior

---

**Status:** Locked reference for QA and audit.
**Last Updated:** 2025-12-29
**Maintained By:** Product & QA Teams
