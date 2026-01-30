# Procurement Module Stabilization Checklist

This document tracks the stabilization tasks required to bring the Procurement module to an "Enterprise-Ready" state.

## 🔴 CRITICAL: Architectural Correction (2025-12-23) ✅ COMPLETE

**Issue**: Operational models (Category, Brand, TaxClass, ItemMaster, Supplier, Customer) were incorrectly located in `domain.business_entities` instead of `domain.company`.

**Resolution**: All operational models moved to `domain.company` to enforce architectural lock:
- ✅ `business_entities` = LICENSING METADATA ONLY
- ✅ `domain.company` = OPERATIONAL MASTERS ONLY

**Changes Made**:
- [x] Added 6 operational models to `domain.company.models`
- [x] Updated `domain.company.views.py` imports
- [x] Updated `seed/seed_enterprise_masters.py` importsCtr
- [x] Verified all 302 ItemMaster records accessible
- [x] Verified all 145 Supplier records accessible
- [x] Verified all 170 Customer records accessible
- [x] Created `ARCHITECTURAL_CORRECTION_REPORT.md`
- [x] Created `ARCHITECTURAL_LOCK_REFERENCE.md`

**Impact**: Supplier and Item lookups now use correct canonical models from `domain.company`.

**Documentation**: See `.steering/01_ARCH_GOVERNANCE/ARCHITECTURAL_LOCK_REFERENCE.md`

---

## 🟢 Phase 1 & 2: Backend & Service Layer (Priority: High) ✅ COMPLETE
- [x] **API Wiring**: Implemented real API service with CRUD operations.
- [x] **Backend Workflow**: Added submit/approve/cancel actions to PurchaseOrderViewSet.
- [x] **Nested Serializer**: Enhanced PurchaseOrderSerializer to support line create/update.
- [x] **TypeScript Types**: Defined comprehensive types matching backend models.

## 🟢 Phase 3: Form Integration (Priority: High) ✅ COMPLETE
- [x] **Form Wiring**: Connected PurchaseOrderFormPage to procurementService.
- [x] **Loading States**: Added loading spinner and saving states.
- [x] **Error Handling**: Implemented error banner with dismissible UI.
- [x] **Form Validation**: Client-side validation before API calls.
- [x] **Save/Submit Logic**: Real API integration for create/update/submit.
- [x] **Data Fetching**: Load existing PO data in edit mode.
- [ ] **Header Population**: Dynamically fetch Supplier, Location, and Payment Term lists based on `currentCompanyId`.
- [ ] **Line Item Precision**: 
    - [ ] Auto-populate `unit_price` from `ItemMaster` last purchase cost.
    - [ ] Fetch default `UOM` and `TaxClass` from Item master.

## 🟠 Phase 2: Workflow & Business Rules
- [ ] **State Machine (Backend)**:
    - [ ] Implement `submit` action in `PurchaseOrderViewSet`.
    - [ ] Implement `approve` / `reject` actions (Manager role required).
    - [ ] Implement `cancel` logic for Draft/Submitted orders.
- [ ] **Authorization Scoping**: Ensure NO cross-company data visibility in Lookups or Forms.
- [ ] **Totaling Logic**: Backend re-calculation of Line Totals and Grand Totals during Serializer validation.

## 🟢 Phase 4: UX Polish (Priority: Medium) ✅ COMPLETE
- [x] **TransactionToolbar Sync**: Disable save/submit/clear during save operations.
- [x] **Supplier Lookup Integration**: Replace text input with lookup button and read-only display.
- [x] **Saving State Feedback**: Toolbar buttons disabled during save/submit.
- [x] **Location Lookup Handler**: Added placeholder handler (modal to be implemented later).
- [x] **Field Labels**: Added required field indicators (*).
- [ ] **Auto-focus in Lookups**: Already implemented in SupplierLookupModal.
- [ ] **Keyboard Shortcuts**: Already implemented in TransactionToolbar (F1-F12).
- [ ] **Print/Export**: Deferred to future phase.

---

## 📝 Remaining Enhancements (Future)
- [ ] **PO to GRN Transition**: Add "Create Receipt" action on Approved POs.
- [ ] **Print/Export**: Implement `Printer` icon action (PDF generation via backend).
- [ ] **Inventory Linkage**: Update stock "In-Transit" quantities when PO is Approved (Optional/Sanity).

## 🟡 Phase 4: UI/UX & Hotkeys
- [ ] **TransactionToolbar Synchronization**: 
    - [ ] Disable `Submit` if PO status is not `Draft`.
    - [ ] Map `F2` to `Save`, `F4` to `Submit` globally in the form.
- [ ] **Lookup Modal UX**:
    - [ ] Auto-focus on search bar when modal opens.
    - [ ] Column sorting in Product/Supplier selectors.

---
**Status Legend:**
- ⚪ Not Started
- 🟡 In Progress
- ✅ Completed
- ❌ Blocked
