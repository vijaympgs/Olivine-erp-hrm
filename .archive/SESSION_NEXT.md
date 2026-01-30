# Session 11 Roadmap - Toolbar Integration & Transactions
**Target Date**: Next Session
**Estimated Duration**: 6-8 hours
**Focus**: Toolbar Integration (Sales/Procurement) & Transactional Workflows

---

## 🎯 Session Objective
Enable full transactional capabilities by implementing the standard toolbar across Sales and Procurement modules, along with their respective state workflows (Draft -> Submitted -> Approved).

---

## 📋 Priority Breakdown

### **P0 - CRITICAL** (Must Complete)

#### **1. Sales Orders - Toolbar & Workflow**
**Priority**: HIGHEST
**Files**: `Retail/frontend/sales/pages/OrderListPage.tsx`, `OrderDetailPage.tsx`
**Tasks**:
- [ ] Implement `MasterToolbar` configuration for Sales Orders.
- [ ] Map backend statuses (`DRAFT`, `CONFIRMED`, `INVOICED`) to toolbar actions.
- [ ] Implement "Authorize/Confirm" action updates via API.
- [ ] Implement "Create Invoice" action from Order.

#### **2. Purchase Orders - Toolbar & Workflow**
**Priority**: HIGH
**Files**: `Retail/frontend/procurement/pages/PurchaseOrderListPage.tsx`, `PurchaseOrderFormPage.tsx`
**Tasks**:
- [ ] Implement `MasterToolbar` configuration for Purchase Orders.
- [ ] Map backend statuses (`DRAFT`, `SENT`, `RECEIVED`) to toolbar actions.
- [ ] Implement "Receive Goods" action (Navigate to GRN).

### **P1 - HIGH** (Important)

#### **3. Goods Receipts Locking**
**Priority**: HIGH
**Files**: `GoodsReceiptFormPage.tsx`
**Tasks**:
- [ ] Ensure `readOnly` prop is strictly enforced in View mode.
- [ ] Disable all inputs when status is `COMPLETED`.

### **P2 - MEDIUM** (Polish)

#### **4. Design System Audit (Compact Layout)**
**Tasks**:
- [ ] Reduce grid row padding (12px -> 8px) globally or in core grids.
- [ ] Verify standard shortcut keys (`Ctrl+S`, `Ctrl+P`).

---

## 📈 Progress Tracking
```
Gold Standard Masters:  ████████████████ 100% (4/4) ✅
Toolbar Integration:    █████████████████░░░ 85%
Overall Retail Module:  █████████████████░░░ 86%
```

## 🏁 Session 10 Summary (Completed)
- ✅ **Item Master**: Full CRUD, Template Inheritance, Auto-naming Variants, Strict Validation.
- ✅ **Category Hierarchy**: Recursive Tree, Drag-drop support, Standard Toolbar, Deletion Logic.
- ✅ **Customer Groups**: Gold standard (Dialogs, Reset, Clear).
- ✅ **Simple Masters**: Fixed payloads and edit modes.

**Status**: Ready for Session 11.
