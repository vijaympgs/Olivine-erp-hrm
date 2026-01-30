# Sales Module Gap Analysis
**Date**: 2025-12-29
**Status**: DRAFT

## 1. Overview
The Sales module is critical for the "Retail Operations" pillar. While the database models have been defined, the API layer and Frontend implementation are currently missing or incomplete. This document identifies the gaps to be addressed to stabilize the Sales module.

## 2. Backend Gaps (Django)

### 2.1. Domain: `backend/domain/sales`
- **Models** (`models.py`): ✅ Exists
  - `Quote`, `QuoteLine`
  - `SalesOrder`, `SalesOrderLine`
  - `SalesReturn`, `SalesReturnLine`
  - `Invoice`, `InvoiceLine`
  - `SalesProcessSetting`, `SalesApprovalMatrix`
- **Serializers** (`serializers.py`): ❌ Missing
  - Need serializers for all above models.
  - Nested serializers for Lines (QuoteLine, OrderLine, etc.).
  - Read/Write separation (e.g., `QuoteListSerializer` vs `QuoteDetailSerializer`).
- **Views** (`views.py`): ❌ Missing
  - `QuoteViewSet`
  - `SalesOrderViewSet`
  - `SalesReturnViewSet`
  - `InvoiceViewSet`
  - `SalesConfigurationViewSet`
  - Business logic for "Converting Quote to Order" and "Order to Invoice".
- **URLs** (`urls.py`): ❌ Missing
  - Router registration for ViewSets.
- **Admin** (`admin.py`): ❌ Missing
  - Admin interfaces for debugging and management.
- **Signals/Services**: ❌ Missing
  - Logic to update Inventory on Order confirmation/fulfillment? (This might be in `SalesOrder.save()` or a service).
  - Logic to update Financials? (Planned for Phase 2, but placeholders needed).

### 2.2. Configuration
- **App Registration**: Check `backend/erp_core/settings/base.py` to ensure `domain.sales` is in `LOCAL_APPS`.

## 3. Frontend Gaps (React)

### 3.1. Routing & Structure
- **Module Directory**: ❌ Missing (`frontend/src/modules/sales`)
- **Routes**: ❌ Missing in `AppRouter.tsx` or `routes.tsx`.
- **Navigation**: ✅ Defined in `menuConfig.ts` (Paths: `/sales/quotes`, `/sales/orders`, etc.).

### 3.2. Components & Pages
- **Quotes**:
  - `QuoteListPage.tsx`
  - `QuoteDetailPage.tsx` / `QuoteForm.tsx`
- **Orders**:
  - `OrderListPage.tsx`
  - `OrderDetailPage.tsx`
- **Invoices**:
  - `InvoiceListPage.tsx`
- **Returns**:
  - `ReturnListPage.tsx`
- **Configuration**:
  - `SalesConfigPage.tsx`

### 3.3. API Integration
- **Types**: ❌ Missing (`types.ts` in module).
- **Service**: ❌ Missing (`salesService.ts` to consume backend API).

## 4. Workflows & Business Logic Gaps
- **Quote -> Order Conversion**: Logic to copy items and prices.
- **Order -> Invoice Conversion**: Logic to generate invoice.
- **Inventory Integration**:
  - Does `SalesOrder` reserve stock?
  - Does `Invoice` or `Shipment` deduct stock? (Currently `SalesOrder` has `fulfilled_quantity`).
- **Status Transitions**: State machine enforcement (e.g., Draft -> Submitted -> Approved).

## 5. Action Plan (Stabilization)
1.  **Backend Implementation**:
    - Create `serializers.py`.
    - Create `views.py`.
    - Create `urls.py`.
    - Register app in Settings.
2.  **API Validation**:
    - Verify endpoints with Swagger/Postman (or programmatic tests).
3.  **Frontend Skeleton**:
    - Create module structure.
    - Set up routes.
    - Create basic List/Empty states.
4.  **Frontend Integration**:
    - Connect List Pages to API.
