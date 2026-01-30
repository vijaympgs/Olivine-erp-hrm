# POS Vertical: F&B (QSR / Dining / Cafe / Cloud Kitchen)

**Reference**: Toast, LS Hospitality, Petpooja
**Parent**: [roadmap_pos.md](./roadmap_pos.md)

## 🍔 Feature Checklist (Functional Specification)

### 1. Operations & Service Modes
- [ ] **Service Mode Switch**: Fast toggle between modes on main screen.
  - **Dine-In**: Table selection mandatory. Service Charge logic.
  - **Takeaway**: Quick name/mobile capture. No Service Charge.
  - **Delivery**: Address capture/lookup. Aggregator integration.
  - **Drive-Thru**: Queue/Timer logic.
- [ ] **Multi-Brand / Cloud Kitchen**:
  - Single POS managing multiple Brands (Burger King, Popeyes).
  - Brand-specific KOT printing.

### 2. Table Management (Fine Dining)
- [ ] **Interactive Floor Plan**:
  - Color-coded status: Vacant, Occupied (Timer running), Bill Printed, Settlement Pending, Dirty.
- [ ] **Guest Actions**:
  - **Split Bill**: By Seat (Seat 1 pays X, Seat 2 pays Y), By Item, or Equal Split.
  - **Move Table**: Transfer orders from Table 5 to Table 9.
  - **Merge**: Join Table 5 and 6.
- [ ] **Captain App**: Handheld ordering at table.

### 3. Advanced Menu & Modifiers
- [ ] **Nested Modifiers**:
  - Parent: Pizza.
  - Level 1: Crust (Thin/Thick - Forced 1).
  - Level 2: Sauce (Tomato/Pesto - Forced 1).
  - Level 3: Toppings (Pepperoni/Mushroom - Optional Max 3).
- [ ] **Combos / Set Meals**:
  - "Meal Deal": Burger + Choice of Side + Choice of Drink.
  - Inventory deduction for specific choices.
- [ ] **Menu Day Parts**:
  - "Breakfast Menu" active only 7AM - 11AM.

### 4. Kitchen Management (KOT & KDS)
- [ ] **Intelligent Routing**:
  - Drinks -> Bar Printer.
  - Cold Items -> Salad Station Printer.
  - Hot Items -> Main Kitchen.
- [ ] **Course Firing**:
  - "Fire Starters" (Now) -> "Fire Mains" (Later).
- [ ] **Kitchen Display System (KDS)**:
  - Digital screen instead of paper.
  - Timer alerts (Yellow after 10m, Red after 15m).
  - "Bump" order when ready.

### 5. Aggregator Integration
- [ ] **Zomato / Swiggy / UberEats**:
  - **Menu Sync**: Push price/stock status to aggregators.
  - **Order Injection**: Auto-accept orders directly into POS.
  - **Rider Tracking**: Capture Rider Name/Phone.

### 6. Settlements
- [ ] **Tip Management**: Record Tips per server.
- [ ] **No-Charge Bills**: Manager Meals, Wastage, Staff Food.
