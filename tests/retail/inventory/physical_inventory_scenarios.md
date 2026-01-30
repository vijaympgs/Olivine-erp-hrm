# Physical Inventory Scenarios

**Screens Covered**:
- Cycle Counting Schedule
- Stock Take List
- Stock Take Execution
- Variance Analysis
- Count Approval
- Reconciliation

---

## Scenarios

### SC-PHYS-001: Create Cycle Counting Schedule
- **Action**: Define "Monthly Warehouse Count" for specific racks.
- **Verify**: Schedule created and appears in calendar.

### SC-PHYS-002: Start Stock Take (Creation)
- **Path**: Inventory > Physical > Stock Take
- **Action**: Click New, Select Location, Add Items (Snapshot).
- **Verify**: System locks item quantities as of the snapshot time.

### SC-PHYS-003: Stock Take Execution (Entry)
- **Path**: Inventory > Physical > Execution
- **Action**: Staff enters counted quantities for SKU-001, SKU-002.
- **Verify**: Data saved against the stock take reference.

### SC-PHYS-004: Variance Analysis
- **Path**: Inventory > Physical > Variance
- **Action**: Click "Compare" after count entry.
- **Verify**: Grid shows Expected vs Actual with Variance amount and value.

### SC-PHYS-005: Approve Count Variance
- **Path**: Inventory > Physical > Approval
- **Action**: Manager reviews variance and clicks Approve.
- **Verify**: Status changes to "Approved", ready for reconciliation.

### SC-PHYS-006: Post Reconciliation (Final Step)
- **Path**: Inventory > Physical > Reconciliation
- **Action**: Click "Post Adjustments".
- **Verify**: System creates stock adjustment entries to sync system qty with actual count.

---
**Scenario Count**: 6
