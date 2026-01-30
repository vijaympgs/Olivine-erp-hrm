# Sales & Customer Operations Scenarios

**Screens Covered**:
- Quotes & Estimates
- Sales Orders
- Invoices
- Returns & Refunds
- Sales Configuration
- Customer Groups
- Loyalty Programs

---

## Scenarios

### SC-SALES-001: Create Quotation
- **Path**: Sales > Order Management > Quotes
- **Action**: Select customer, add items, set expiry date.
- **Verify**: Quote generated in "Draft" status.

### SC-SALES-002: Convert Quote to Sales Order
- **Action**: Open Approved Quote, click "Convert to SO".
- **Verify**: Sales Order created with all quote data linked.

### SC-SALES-003: Generate Invoice from SO
- **Path**: Sales > Billing > Invoices
- **Action**: Select Sales Order, click "Generate Invoice".
- **Verify**: Invoice created, SO status updated to "Billed".

### SC-SALES-004: Process Sales Return (Credit Note)
- **Path**: Sales > Billing > Returns
- **Action**: Select Invoice, click "Return Items", enter reason.
- **Verify**: Credit Note generated, stock restored (if applicable).

### SC-SALES-005: Manage Customer Groups
- **Path**: Customers > Management > Groups
- **Action**: Create "Gold Member" group with 5% default discount.
- **Verify**: Discount applies automatically to customers in this group.

### SC-SALES-006: Loyalty Program Setup
- **Path**: Customers > Loyalty > Programs
- **Action**: Define "1 Point per ₹100 spent".
- **Verify**: Points accumulate on customer profile after invoice posting.

---
**Scenario Count**: 6
