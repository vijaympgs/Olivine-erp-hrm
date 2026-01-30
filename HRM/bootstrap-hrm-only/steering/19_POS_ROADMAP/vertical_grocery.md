# POS Vertical: Grocery / Supermarket / Kirana

**Reference**: GoFrugal, LS Retail
**Parent**: [roadmap_pos.md](./roadmap_pos.md)

## 🛒 Feature Checklist (Functional Specification)

### 1. High-Speed Checkout Operations
- [ ] **Scan Ergonomics**:
  - Constant-Scan Mode (No "Enter" key needed).
  - Handle "Item Not Found" without blocking queue (Supervisor approval flow).
- [ ] **Weighing Scale Integration**:
  - **Direct Scale**: Real-time weight reading from COM/USB scale.
  - **Tare Logic**: Manual Tare (enter crate weight) or Pre-set Tare.
  - **Price Embedded Barcodes**: Logic to parse `20AAAAABBBBC` (Item AAAAA, Price/Weight BBBB).
- [ ] **Queue Busting**:
  - "Line Buster" App support (Scan items in queue, print token, cashier recalls token).
  - **Hold/Resume**: Park transaction for customer who forgot wallet.

### 2. Inventory Efficiency & Shrinkage
- [ ] **Dump / Wastage Management (Critical)**:
  - One-touch "Dump" button for Perishables (Rotten Veg/Fruit).
  - Reason Codes: "Expired", "Damaged", "Rat Bite", "Admin Consumption".
  - Auto-write off from Inventory.
- [ ] **Repacking / Conversion**:
  - Workflow: Convert "Sugar 50kg Sack" -> "50 x 1kg Packets".
  - Auto-generate barcodes for new packets.
  - Track Yield/Loss during repacking (e.g., 50kg -> 49.5kg packed + 0.5kg dust).
- [ ] **Stock Audit**:
  - Support for PDT (Portable Data Terminal) stock counting while store is live.

### 3. Dual Unit & Loose Quantities
- [ ] **Dual UOM**:
  - Buy in Crate (24 Pcs), Sell in Pc.
  - Buy in Kg, Sell in Grams (0.250 Kg).
- [ ] **Loose Item Lookup**:
  - "PLU Matrix" touch screen for non-barcoded items (Onion, Potato).

### 4. Schemes & Customer Loyalty
- [ ] **Grocery-Specific Promos**:
  - "Manufacture Bill Buster": Buy P&G products > 500 get 50 off.
  - "Happy Hours": Vegetables 20% off after 9 PM.
- [ ] **Wallet/Points**:
  - Earn/Burn points.
  - Store Credit for Returns (Keep cash in ecosystem).

### 5. Home Delivery & Omni
- [ ] **Phone Order / WhatsApp Integration**:
  - Convert WhatsApp/Call list to Bill.
  - Assign "Picker" and "Delivery Boy".
- [ ] **Billing for Delivery**:
  - "Cash on Delivery" tracking (Driver reconciliation).
