# UnifiedPOS Roadmap & Feature Checklist (Master)

**Status**: Active / Elaboration Phase
**Context**: Master Index for POS Roadmap
**Reference**: UnifiedPOS Deep Dive

---

## 🏗️ 1. Common Core (Universal POS)
*The foundational layer required by ALL verticals. Must be robust, secure, and keyboard-friendly.*

### 1.1 Shift & Till Management
- [ ] **Opening Operations**: Float entry, Till assignment, Device health check.
- [ ] **Mid-Shift Operations**: Cash Drops (Safe Drops), Cash Pickups, X-Report (Blind spot check).
- [ ] **Closing Operations**: Z-Report (Day End), Blind Cash Count, Variance recording.
- [ ] **Denomination Logic**: UI for counting notes/coins (2000x2, 500x10...).

### 1.2 Authentication & Security
- [ ] **Login Methods**: User/Pass, PIN (4-6 digits), Magstripe Card, Biometric.
- [ ] **Rights Management**: Granular permissions for Void, Refund, Discount, Price Override, No-Sale drawer open.
- [ ] **Audit Logs**: Traceability of all 'Void Line' and 'Void Bill' actions with reason codes.
- [ ] **Manager Override**: Supervisor PIN requirement for high-risk actions.

### 1.3 Catalog & Cart Operations
- [ ] **Search capability**: Global search (Name, SKU, Barcode, Description).
- [ ] **Scan Modes**: Constant scan (Grocery), Quantity prompt (Fashion), Serial Entry (Electronics).
- [ ] **Line Attributes**: Salesperson tagging (Commission), Line Notes, Item attributes (Color/Size).
- [ ] **Cart Actions**: Park/Hold Bill (Queue busting), Retrieve Bill, Suspend Transaction.
- [ ] **Price Override**: Reason code based overrides (Damaged, Price Match).
- [ ] **Customer Association**: Lookup via Mobile/Name, View Loyalty Points, Last Purchase interactions.

### 1.4 Pricing & Promotion Engine
- [ ] **Standard Promos**: Discount %, Discount Amount, Fixed Price.
- [ ] **Advanced Promos**: Mix & Match ("Buy 2 distinct shampoos get 10% off"), BOGO, Threshold (Buy > 2000 get 100 off).
- [ ] **Coupon Management**: Validation, Single-use tracking, Coupon stacking rules.

### 1.5 Payments & settlement
- [ ] **Modes**: Cash, Credit/Debit Card, Integrated UPI (QR), Wallet, Gift Card, Loyalty Points.
- [ ] **Complex Settlement**: Split Payment (Part Cash, Part Card), Foreign Currency (Tourism).
- [ ] **Rounding**: Nearest 0.50/1.00, Round Down/Up strategies (Configurable).

---

## 🏢 2. Vertical Specific Roadmaps
*See detailed specifications for each vertical:*

- [**Grocery / Supermarket / Kirana**](./vertical_grocery.md)
  - Weighing, MRP, Expiry, Repacking, Dump.
- [**F&B (QSR / Dining / Cafe)**](./vertical_fnb.md)
  - KOT, Modifiers, Table Mgmt, Aggregators.
- [**Pharmacy**](./vertical_pharmacy.md)
  - Schedule H/H1, Salt Search, Substitutes, Rx.
- [**Automobile (Parts / Service)**](./vertical_auto.md)
  - VIN Logic, Compatibility, Job Cards, Cores.
- [**Fashion / Lifestyle**](./vertical_fashion.md)
  - Size/Color Matrix, Alterations, Seasonality.
- [**Wholesale / B2B**](./vertical_wholesale.md)
  - Contract Pricing, Credit Limits, Tax Invoicing.

---

## 🇮🇳 3. India Compliance & Localization
*Ref: GoFrugal, ClearTax*
- [ ] **GST Logic**: State-logic (IGST vs CGST/SGST), HSN/SAC validation, Tax Slabs.
- [ ] **E-Invoicing**: Real-time IRN generation (B2B).
- [ ] **Legal Metrology**: "Best Before" rules, MRP enforcement.
- [ ] **Payments**: Dynamic UPI QR display.

---

## 💾 4. Non-Functional Requirements (NFR)
- [ ] **Offline First**: SQLite/IndexedDB, Background Sync, Conflict Resolution.
- [ ] **Performance**: App Load < 3s, Scan-to-Cart < 200ms.
- [ ] **Scalability**: Local DB for 100k+ SKUs.
- [ ] **Telemetry**: Crash reporting, Performance monitoring.

---

## 🔌 5. Hardware Ecosystem
- [ ] **Input**: Barcode Scanners (HID/Serial), Programmable Keyboards.
- [ ] **Output**: Thermal Printers (ESC/POS), Customer Displays (CFD).
- [ ] **I/O Equipment**: Cash Drawers, Weighing Scales, Biometric Readers.
- [ ] **Payments**: Pinelabs / Paytm / PhonePe terminals.
