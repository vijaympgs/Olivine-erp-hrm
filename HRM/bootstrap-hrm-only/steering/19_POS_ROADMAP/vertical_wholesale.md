# POS Vertical: Wholesale / B2B / Cash & Carry

**Reference**: Epicor, Netsuite
**Parent**: [roadmap_pos.md](./roadmap_pos.md)

## 📦 Feature Checklist (Functional Specification)

### 1. Customer Intelligence & Pricing
- [ ] **Contract Pricing**:
  - **Price Lists**: Assign specific Price List to Customer Group.
  - **Fixed Price Contracts**: "Item X is always $10 for this customer".
  - **Last Sold Price**: Pop-up "Last sold at $9.50 on 10-Jan".
- [ ] **Tiered / Volume Discounts**:
  - Quantity Breaks: "1-10 @ $10, 11-50 @ $9, 50+ @ $8".
  - Mix & Match Volume: "Buy 10 cases of ANY soap get 5% off".

### 2. Credit Control & Financials
- [ ] **Credit Limit Enforcement**:
  - Checks: (Current Balance + New Bill Value) > Credit Limit.
  - **Aging Check**: Block bill if any invoice is > 45 days overdue.
  - **Override Workflow**: Cashier requests -> Manager approves on mobile.
- [ ] **Invoicing**:
  - **Tax Invoice**: Mandatory GSTIN printing.
  - **E-Invoice**: Real-time IRN generation/printing.
  - **E-Way Bill**: Auto-generation if value > 50k (India).

### 3. Inventory Handling (Bulk)
- [ ] **Multi-UOM Scanning**:
  - Barcode A = 1 Pc.
  - Barcode B = 1 Case (24 Pcs).
  - System auto-deducts 24 units inventory.
- [ ] **Break-Bulk**:
  - "Do not sell loose units" flag for certain wholesale items.

### 4. Operations
- [ ] **Quotation to Invoice**:
  - Create Quote -> Customer Approves -> Convert to Invoice.
  - Partial fulfillment of Orders (Backorder handling).
- [ ] **Gate Pass**:
  - Print "Gate Pass" for security check upon exit.

### 5. Sales Rep & Commissions
- [ ] **Route Sales**:
  - Tag Salesman to Invoice.
  - Track Collections against Invoices.
