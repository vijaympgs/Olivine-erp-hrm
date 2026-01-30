# Task 01: Procurement API Readiness
Status: In Progress
Created: 2025-12-23

## Objective
Upgrade the frontend procurement service and types to support real CRUD operations with the backend.

## Sub-tasks
- [x] Analyze Backend Models & Serializers for PO.
- [x] Add workflow actions (submit/approve/cancel) to PurchaseOrderViewSet.
- [x] Enhance PurchaseOrderSerializer to support nested line create/update.
- [x] Add automatic total recalculation logic.
- [x] Define comprehensive PO Types in `procurement.types.ts`.
- [x] Implement CRUD & Workflow actions in `procurement.service.ts`.
- [x] Wire PurchaseOrderFormPage to real API.
- [x] Add loading states and error handling.
- [x] Implement form validation.
- [x] Add error banner display.
- [ ] Test create/edit/submit flows end-to-end.

## Execution Log
- *2025-12-23 20:23*: ✅ Added `submit`, `approve`, `cancel` actions to `PurchaseOrderViewSet`.
- *2025-12-23 20:24*: ✅ Enhanced `PurchaseOrderSerializer` with nested line support and auto-totaling.
- *2025-12-23 20:24*: Backend Phase 1 complete. Moving to frontend types definition.
- *2025-12-23 20:35*: ✅ Wired PurchaseOrderFormPage to real API with loading/error states.
- *2025-12-23 20:36*: ✅ Fixed all TypeScript lint errors (POStatus import, field names).
- *2025-12-23 20:37*: ✅ Added error banner and form validation.
- *2025-12-23 20:37*: Phase 3 complete. Ready for end-to-end testing.
