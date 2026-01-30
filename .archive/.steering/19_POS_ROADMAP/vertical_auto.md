# POS Vertical: Automobile (Parts / Service / EV)

**Reference**: Epicor (Eagle/Propello)
**Parent**: [roadmap_pos.md](./roadmap_pos.md)

## 🔧 Feature Checklist (Functional Specification)

### 1. Vehicle Intelligence & Catalog
- [ ] **Fitment Logic (ACES/PIES Standard)**:
  - Granular selection: **Year -> Make -> Model -> Trim -> Engine** (e.g., 2023 -> Hyundai -> Creta -> SX(O) -> 1.5L Diesel).
  - "My Garage": Save customer's vehicle details for quick recall.
- [ ] **VIN Decoding**:
  - Input VIN (Manual/Scan) -> Auto-resolve vehicle specs.
  - Integration with VIN data providers.
- [ ] **Interactive Diagrams (Schematics)**:
  - Exploded View navigation (Click on "Alternator" in engine diagram -> Add to Cart).
- [ ] **Part Interchangability**:
  - **Cross-Reference**: Link OEM P/N to Aftermarket (Bosch, Denso, NGK).
  - **Supersession**: Manage chain of replaced part numbers (Part A -> Part B -> Part C).
  - **Compatible Models**: "This Oil Filter fits i20, Verna, and Creta".

### 2. Service & Workshop Operations
- [ ] **Job Card Integration**:
  - Create/Lookup Open Job Card.
  - Issue Parts to Job (Material Issue Slip).
  - Return unused Parts from Job.
- [ ] **Service Packages**:
  - "General Service" Bundle: 4L Oil + 1 Oil Filter + 1 Air Filter + 2hr Labor.
  - "Brake Pad Replacement" Bundle.
- [ ] **Bay Management**:
  - Schedule appointments by Bay/Lift.
  - Track "Vehicle In" / "Vehicle Out" times.
- [ ] **Technician Management**:
  - Assign Mechanic to Line Item (for Labor sales).
  - Track Efficiency (Standard Repair Time vs Actual).

### 3. Special Inventory Handling
- [ ] **Core Charge / Exchange Management**:
  - Sell "Battery (New)" -> Charge "Core Deposit".
  - Return "Battery (Old)" -> Refund "Core Deposit".
  - Track "Core" inventory separately (for recycling).
- [ ] **Serialized Inventory**:
  - Mandatory Serial Scan for Batteries and Tyres.
  - Track **Warranty Period** (e.g., 36 months pro-rated).
  - Print Warranty Card (with Serial No, Date, KM Reading).
- [ ] **Kit / BOM Assembly**:
  - "Engine Overhaul Kit" (Contains 50 child parts).
  - Explode Kit on Bill or Sell as Unit.

### 4. Fleet & B2B Sales
- [ ] **Fleet Management**:
  - Bill to "Head Office" (e.g., Taxi Company), Ship to "Driver".
  - Validate "PO Number" or "Driver ID".
- [ ] **Wholesale Price Tiers**:
  - Price A (Retail), Price B (Garage/Mechanic), Price C (Distributor).
  - Auto-apply based on Customer Type.

### 5. Compliance & Reporting
- [ ] **Hazardous Material Handling**:
  - Compliance flags for Oils/Chemicals.
- [ ] **Scrap Management**:
  - Process for disposing of old cores/scrap metal.
