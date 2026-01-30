# Session 11: Transactional Workflow Integration & Toolbar Logic

**Date**: 2026-01-23
**Focus**: Sales Orders, Purchase Orders, Goods Receipt Locking
**Goal**: Enforce strict state management (Draft -> Confirmed -> Invoiced) via Universal Toolbar.

## 🎯 Priorities

### P0 - Sales Orders (Critical)
- [x] **Toolbar Configuration**: Implement `MasterToolbar` in `OrderListPage` and `OrderDetailPage`.
- [ ] **Workflow Actions**: Map `DRAFT`, `CONFIRMED`, `INVOICED` states to toolbar actions.
    - [x] Authorize (`DRAFT` -> `CONFIRMED`)
    - [x] Next Stage (`CONFIRMED` -> `INVOICED`) - **Implemented create_invoice**
    - [x] Cancel (`CONFIRMED` -> `CANCELLED`) - **Implemented status update**
- [x] **State Masking**: Disable Edit/Delete for Confirmed orders.
- [x] **Navigation**: Wire `First/Prev/Next/Last` buttons.

### P0 - Purchase Orders (Critical)
- [x] **Toolbar Configuration**: Implement `MasterToolbar` in `PurchaseOrderListPage`.
- [x] **Receive Action**: Implement transition from `SENT` -> `RECEIVED` (Navigate to GRN).
- [x] **State Masking**: Lock `SENT` orders from editing.
    - [x] Toolbar Actions locked.
    - [x] **Form Inputs locked** - **Completed**

### P1 - Goods Receipt Locking (High)
- [x] **Read-Only Enforcement**: Ensure `GoodsReceiptForm` is strictly read-only when status is `COMPLETED`.

## 📝 Activity Log
- **[Start]**: Initialized Session 11.
- **[Update]**: Completed Toolbar & Locking for POs and GRNs. Fixed PurchaseOrderFormPage structure. Sales Orders Authorize action implemented. Be aware of missing form locking on POs.
