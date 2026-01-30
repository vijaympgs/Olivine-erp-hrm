# Inventory Menu Tree Structure

**Module:** Retail  
**Menu Group (L1):** Inventory

## Complete Hierarchy

```
📁 Inventory (L1)
│
├── 📂 Inventory Dashboard (L2)
│   ├── 📄 Inventory Overview (L3)
│   ├── 📄 Stock by Location (L3)
│   ├── 📄 Stock Valuation (L3)
│   ├── 📄 Movement Trends (L3)
│   └── 📄 Alerts & Notifications (L3)
│
├── 📂 Stock Management (L2)
│   ├── 📄 Stock on Hand (L3)
│   ├── 📄 Stock by Location (L3)
│   ├── 📄 Stock by Category (L3)
│   ├── 📄 Stock by Batch/Serial (L3)
│   ├── 📄 Low Stock Alerts (L3)
│   ├── 📄 Overstock Alerts (L3)
│   └── 📄 Stock Aging Analysis (L3)
│
├── 📂 Stock Movements (L2)
│   ├── 📄 Movement History (L3)
│   ├── 📄 Goods Receipt (from Procurement) (L3)
│   ├── 📄 Goods Issue (to Sales) (L3)
│   ├── 📄 Internal Transfers (L3)
│   ├── 📄 Intercompany Transfers (L3)
│   └── 📄 Movement Reports (L3)
│
├── 📂 Stock Adjustments (L2)
│   ├── 📄 Stock Adjustment Entry (L3)
│   ├── 📄 Adjustment History (L3)
│   ├── 📄 Reason Code Management (L3)
│   ├── 📄 Approval Workflow (L3)
│   └── 📄 Adjustment Reports (L3)
│
├── 📂 Physical Inventory (L2)
│   ├── 📄 Cycle Counting Schedule (L3)
│   ├── 📄 Stock Take Execution (L3)
│   ├── 📄 Variance Analysis (L3)
│   ├── 📄 Count Approval (L3)
│   └── 📄 Reconciliation (L3)
│
├── 📂 Inventory Valuation (L2)
│   ├── 📄 Valuation Methods (L3)
│   ├── 📄 Valuation Reports (L3)
│   ├── 📄 Cost Analysis (L3)
│   └── 📄 Period-end Valuation (L3)
│
├── 📂 Replenishment & Planning (L2)
│   ├── 📄 Reorder Point Management (L3)
│   ├── 📄 Safety Stock Levels (L3)
│   ├── 📄 Min-Max Planning (L3)
│   ├── 📄 Reorder Policies (L3)
│   └── 📄 Replenishment Suggestions (L3)
│
├── 📂 Batch & Serial Tracking (L2)
│   ├── 📄 Batch Management (L3)
│   ├── 📄 Serial Number Tracking (L3)
│   ├── 📄 Expiry Management (L3)
│   └── 📄 Batch Traceability (L3)
│
├── 📂 Inventory Reports (L2)
│   ├── 📄 Stock Summary Report (L3)
│   ├── 📄 Movement Report (L3)
│   ├── 📄 Valuation Report (L3)
│   ├── 📄 Aging Report (L3)
│   ├── 📄 ABC Analysis (L3)
│   ├── 📄 Fast/Slow Moving Analysis (L3)
│   └── 📄 Dead Stock Report (L3)
│
└── 📂 Configuration (L2)
    └── 📄 Inventory Setup (L3)
```

## Summary Statistics

- **L1 (Menu Group)**: 1 item (Inventory)
- **L2 (Subgroups)**: 10 items
- **L3 (Menu Items)**: 49 items
- **Total Inventory Items**: 60 items

## L2 Categories Breakdown

1. **Inventory Dashboard** - 5 L3 items
2. **Stock Management** - 7 L3 items
3. **Stock Movements** - 6 L3 items
4. **Stock Adjustments** - 5 L3 items
5. **Physical Inventory** - 5 L3 items
6. **Inventory Valuation** - 4 L3 items
7. **Replenishment & Planning** - 5 L3 items
8. **Batch & Serial Tracking** - 4 L3 items
9. **Inventory Reports** - 7 L3 items
10. **Configuration** - 1 L3 item

## Menu ID Reference

### L1
- `inventory`

### L2
- `inventory-dashboard`
- `stock-management`
- `stock-movements`
- `stock-adjustments`
- `physical-inventory`
- `inventory-valuation`
- `replenishment-planning`
- `batch-serial`
- `inventory-reports`
- `inventory-config`

### L3 (Selected Examples)
- `inventory-overview`
- `stock-all`
- `movement-history`
- `adjustment-entry`
- `cycle-schedule`
- `valuation-methods`
- `reorder-points`
- `batch-mgmt`
- `stock-summary-report`
- `inventory-setup`

## Django Admin View

In the Django admin, this structure appears as:

| App | Menu Group (L1) | Subgroup (L2) | Menu Item (L3) | Menu ID | Active | Order |
|-----|----------------|---------------|----------------|---------|--------|-------|
| Retail | 📁 Inventory | - | - | inventory | ✓ | 4 |
| Retail | 📁 Inventory | 📂 Inventory Dashboard | - | inventory-dashboard | ✓ | 1 |
| Retail | 📁 Inventory | 📂 Inventory Dashboard | 📄 Inventory Overview | inventory-overview | ✓ | 1 |
| Retail | 📁 Inventory | 📂 Inventory Dashboard | 📄 Stock by Location | stock-by-location | ✓ | 2 |
| ... | ... | ... | ... | ... | ... | ... |

## Filtering

You can filter this tree using:
- **App**: Select "retail"
- **Menu Group (L1)**: Select "RETAIL - Inventory"
- **Subgroup (L2)**: Select specific L2 like "Inventory > Inventory Dashboard"
- **Menu Item (L3)**: Select specific L3 like "Inventory > Inventory Dashboard > Inventory Overview"

## Status

✅ **All 60 inventory menu items are seeded and active**  
✅ **Structure matches frontend menuConfig.ts exactly**  
✅ **All 3 hierarchical levels (L1, L2, L3) are properly linked**
