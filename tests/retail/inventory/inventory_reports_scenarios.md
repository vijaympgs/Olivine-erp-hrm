# Inventory Reports & Analytics Scenarios

**Screens Covered**: 
- Inventory Overview
- Stock by Location
- Stock Valuation
- Movement Trends
- Low Stock / Overstock Alerts
- Stock Aging Analysis
- All Inventory Reports (Stock Summary, Movement, ABC, Velocity, etc.)

---

## Scenarios

### SC-INV-RPT-001: View Inventory Dashboard (Overview)
- **Path**: Inventory > Dashboard > Overview
- **Action**: Load dashboard
- **Verify**: Stock level charts, Top moving items, Low stock alerts visible.

### SC-INV-RPT-002: Filter Stock by Location
- **Path**: Inventory > Stock Management > By Location
- **Action**: Select "Warehouse A" from dropdown
- **Verify**: Grid filters to items only in Warehouse A.

### SC-INV-RPT-003: Stock Valuation Report (FIFO)
- **Path**: Inventory > Dashboard > Stock Valuation
- **Action**: Select "FIFO" method and "Export PDF"
- **Verify**: PDF generates with correct valuation based on FIFO logic.

### SC-INV-RPT-004: Stock Aging Analysis
- **Path**: Inventory > Stock Management > Aging
- **Action**: View aging buckets (0-30, 31-60, 60+ days)
- **Verify**: Items allocated correctly to age buckets based on GRN date.

### SC-INV-RPT-005: ABC Analysis Report
- **Path**: Inventory > Reports > ABC Analysis
- **Action**: Run report for last 6 months
- **Verify**: Items classified into A (high value), B, or C categories.

### SC-INV-RPT-006: Movement Trends Chart
- **Path**: Inventory > Dashboard > Movement Trends
- **Action**: Toggle between Inward and Outward trends
- **Verify**: Line chart updates correctly.

### SC-INV-RPT-007: Low Stock Alerts List
- **Path**: Inventory > Stock Management > Low Stock
- **Action**: View list
- **Verify**: All items where `qty < reorder_level` are displayed.

### SC-INV-RPT-008: Dead Stock Report
- **Path**: Inventory > Reports > Dead Stock
- **Action**: Set threshold to "No movement for 180 days"
- **Verify**: List shows items with zero transactions in that period.

---
**Scenario Count**: 8
