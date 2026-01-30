# POS Vertical: Fashion / Lifestyle / Apparel

**Reference**: LS Retail, Square
**Parent**: [roadmap_pos.md](./roadmap_pos.md)

## 👔 Feature Checklist (Functional Specification)

### 1. Matrix & Variant Management
- [ ] **Matrix Grid UI**:
  - View Stock/Sales in a 2D Grid (Rows: Size, Cols: Color).
  - Quick Order Entry: Enter '2' in Red/M cell, '1' in Blue/L cell.
- [ ] **Variant Logic**:
  - **Style Master**: Parent Item (e.g., "Slim Fit Shirt").
  - **Child SKUs**: Auto-generated (Style + Color + Size).
  - **Barcode Management**: Unique UPC for each variant vs Common Style Code.

### 2. Alteration & Tailoring Workflow
- [ ] **Tailoring Request**:
  - Select Item -> Click "Alter".
  - Capture Measurements (Waist, Hem, Length).
  - Set **Promised Date**.
  - Assign **Tailor** (Internal/External).
- [ ] **Status Tracking**:
  - New -> In Progress -> Ready -> Delivered.
  - SMS Alert to customer when "Ready".

### 3. Salesperson & Commission
- [ ] **Commission Tagging**:
  - **Per Line**: Salesman A sold the Shirt, Salesman B sold the Belt.
  - **Per Bill**: Split commission equally.
- [ ] **Targets & Incentives**:
  - View "My Sales vs Target" on POS dashboard.

### 4. Seasonality & Pricing
- [ ] **Ageing Analysis**:
  - Report: Stock > 90 Days.
- [ ] **Markdown Management**:
  - Auto-apply discount based on Ageing (e.g., > 120 days = 30% off).
  - "End of Season Sale" (EOSS) bulk price updates.
- [ ] **Layaway / Deposits**:
  - Pay 20% now, hold item for 7 days.
  - Forfeit rules if not collected.

### 5. Returns & Exchange Policy
- [ ] **Strict Returns Validation**:
  - "Return within 14 days" check.
  - "Tag Intact" checkbox confirmation by Cashier.
  - No Cash Refund (Credit Note Only) configuration.
- [ ] **Gift Receipts**:
  - Print receipt without price for gifting.
  - Allow exchange using Gift Receipt reference.
