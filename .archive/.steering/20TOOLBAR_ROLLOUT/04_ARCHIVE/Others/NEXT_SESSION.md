# Next Session - Toolbar Rollout Phase 2 (2026-01-10)

## 🎯 Primary Focus
Systematic integration of the `MasterToolbar` into the remaining functional pages identified by the Registry Deep Scan, starting with the **Retail Core (Inventory & Sales)**.

## 🚀 Immediate Tasks

### 1. Operational Integration
*   **Inventory Masters**: Add `<MasterToolbar viewId="ITEM_MASTER" />` to the actual `ItemPage.tsx` and ensure `VIEW` / `EDIT` mode toggles work as expected.
*   **Purchasing Chain**: 
    *   Integrate toolbar into `PurchaseOrderListPage.tsx` and `PurchaseOrderFormPage.tsx`.
    *   Map "Submit/Authorize" actions to the appropriate backend service calls.

### 2. UI Refinement
*   **Header Alignment**: Ensure all pages follow the `OrderListPage` pattern (Toolbar on top, then Page Header with Title/Subtitle).
*   **Breadcrumb Placement**: Investigate moving breadcrumbs into the sticky toolbar rail to save vertical space.

### 3. Workflow Validation
*   **Action Mapping**: Verify that `Authorize (F10)` and `Submit (Alt+S)` buttons trigger the correct business logic in the `onAction` handlers.
*   **State Management**: Ensure `hasSelection={!!selectedId}` is correctly passed from the grid/table state to allow the "Edit/Delete/View" buttons to enable/disable dynamically.

## 📌 Critical References
*   `CORE Registry`: Managed via Django Admin (`ERPMenuItem`)
*   `Standard Configs`: 
    *   **MASTER**: `NESCKVDXRQFIO`
    *   **TRANSACTION**: `NESCKZTJAVPMRDX1234QF`
    *   **REPORT**: `VRXPYQFG`
    *   **DASHBOARD**: `VRXQFG`
