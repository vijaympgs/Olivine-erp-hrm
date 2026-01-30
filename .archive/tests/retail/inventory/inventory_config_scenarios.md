# Inventory Configuration & Stock Management Scenarios

**Screens Covered**:
- Stock on Hand (Levels)
- Category Hierarchy (Tree)
- Stock by Batch/Serial
- Valuation Methods Config
- General Parameters
- Movement Types
- Approval Rules

---

## Scenarios

### SC-INV-CFG-001: View Stock Levels (Global Search)
- **Path**: Inventory > Stock Management > Stock on Hand
- **Action**: Type part of SKU in global filter
- **Verify**: Real-time filtering of stock grid.

### SC-INV-CFG-002: Manage Category Tree
- **Path**: Inventory > Stock Management > Category Hierarchy
- **Action**: Add "Sub-category" under "Electronics".
- **Verify**: Tree UI updates and persists hierarchy.

### SC-INV-CFG-003: Stock Search by Batch
- **Path**: Inventory > Stock Management > By Batch
- **Action**: Search for Batch "B-12345"
- **Verify**: Displays all locations where this specific batch is stored.

### SC-INV-CFG-004: Configure Movement Types
- **Path**: Inventory > Config > Movement Types
- **Action**: Create new type "Sample Issue" with specific GL account mapping.
- **Verify**: Appears in Adjustment reason codes.

### SC-INV-CFG-005: Setup Inventory Approval Rules
- **Path**: Inventory > Config > Approval Rules
- **Action**: Set rule: "Adjustments > ₹10,000 require Manager Approval".
- **Verify**: Enforcement during adjustment entry.

---
**Scenario Count**: 5
