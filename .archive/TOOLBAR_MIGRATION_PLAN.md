# MasterToolbar Migration Plan (Jan 2026)

**Objective**: Standardize all List pages to use the "Gold Standard" `MasterToolbar` pattern (Ribbon-style breadcrumbs + command buttons) for consistent UX and centralized action management.

## 🚀 Status Summary
- **Target Pages**: ~15 Inventory/Procurement pages.
- **Completed**: 0 (in recent sprint)
- **Pattern**: `MasterToolbar` (from `@core/ui-canon`)

---

## 🛠️ Migration List

### **Phase 1: Inventory Transactional Lists** (High Priority)
Goal: Standardize movement and counting screens.
| Page | File | Current Status | Milestone |
| :--- | :--- | :--- | :--- |
| **Internal Transfers** | `TransferListPage.tsx` | Custom Command Bar | [ ] Replace with `MasterToolbar` |
| **Intercompany Transfers** | `IntercompanyTransferListPage.tsx` | Custom Command Bar | [ ] Replace with `MasterToolbar` |
| **Stock Adjustments** | `AdjustmentListPage.tsx` | Custom Command Bar | [ ] Replace with `MasterToolbar` |
| **Stock Takes** | `StockTakeListPage.tsx` | Custom Command Bar | [ ] Replace with `MasterToolbar` |
| **Adjustment Approvals**| `AdjustmentApprovalListPage.tsx` | Custom Command Bar | [ ] Replace with `MasterToolbar` |

### **Phase 2: Master Intelligence & Analytics** (Medium Priority)
Goal: Standardize high-volume data screens.
| Page | File | Current Status | Milestone |
| :--- | :--- | :--- | :--- |
| **Stock Levels** | `StockLevelListPage.tsx` | Custom Header/Filters | [ ] Replace with `MasterToolbar` |
| **Stock Movements** | `StockMovementListPage.tsx` | Custom Header/Filters | [ ] Replace with `MasterToolbar` |
| **Batch Management** | `BatchListPage.tsx` | Custom Header/Filters | [ ] Replace with `MasterToolbar` |
| **Serial Numbers** | `SerialListPage.tsx` | Custom Header/Filters | [ ] Replace with `MasterToolbar` |

### **Phase 3: Tactical Reports & Tools** (Low Priority)
Goal: Consistency across secondary screens.
| Page | File | Current Status | Milestone |
| :--- | :--- | :--- | :--- |
| **Reorder Rules** | `ReorderRulesPage.tsx` | Simple Header | [ ] Replace with `MasterToolbar` |
| **Cycle Counting Schedule** | `CycleCountingSchedulePage.tsx` | Simple Header | [ ] Replace with `MasterToolbar` |
| **Expiry Management** | `ExpiryManagementPage.tsx` | Simple Header | [ ] Replace with `MasterToolbar` |

---

## 📋 Standard Implementation Checklist
1. [ ] Remove local `Page Header` and `Command Bar` divs.
2. [ ] Inject `MasterToolbar` at top of main flex container.
3. [ ] Define `viewId` for the screen (e.g., `INVENTORY_TRANSFERS`).
4. [ ] Wire `onAction` handler to existing functions (`handleNew`, `handleRefresh`, etc.).
5. [ ] (Optional) Integrate search from MasterToolbar into list filtering logic.
6. [ ] Apply **Zero Border Radius** to any remaining elements.

---

## 🔗 Reference Implementations
- `AttributeSetup.tsx` (Model for Setup Screens)
- `PurchaseOrderListPage.tsx` (Model for Transactional Lists)
