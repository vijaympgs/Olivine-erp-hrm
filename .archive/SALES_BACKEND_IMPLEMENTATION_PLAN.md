# Sales Backend Implementation Plan
**Created**: 2025-12-30 19:02 IST  
**Status**: Phase 1 - In Progress  
**Objective**: Implement comprehensive Sales module backend based on completed BBPs

---

## 📋 **Implementation Overview**

### **Scope**
Implement enterprise-grade Sales module backend with full BBP compliance:
- Sales Quotation (6.1)
- Sales Order (6.2)
- Sales Invoice (6.3)
- Sales Return/RMA (6.4)
- Sales Configuration (6.5)

### **Current State**
- ✅ Sales app registered in settings: `apps.retail.backend.sales.apps.SalesConfig`
- ✅ Basic models exist (Quote, SalesOrder, Invoice, SalesReturn, Config)
- ⚠️ Models are simplified - need BBP-compliant enhancement
- ⚠️ Missing: Serializers, ViewSets, Business Logic, Workflow Actions

---

## 🎯 **Phase 1: Models & Migrations** (Current)

### **Task 1.1: Enhance Sales Quotation Models**
**File**: `apps/retail/backend/sales/models.py`

**Changes Required**:
1. **Quote Header** (`Quote` → `SalesQuote`):
   - Add all BBP 6.1 fields (87 fields total)
   - Add revision tracking (parent_quote_id, revision_number, is_latest_revision)
   - Add margin tracking (cost_price_total, gross_margin_pct)
   - Add approval workflow fields (approval_rule_snapshot)
   - Add customer response tracking
   - Add PDF/email tracking fields

2. **Quote Line** (`QuoteLine` → `SalesQuoteLine`):
   - Add price source tracking (price_source, price_list_id, override_reason)
   - Add margin calculation (cost_price, gross_margin_pct)
   - Add line status enum

3. **Quote-Order Link** (`SalesQuoteOrderLink`):
   - Create new model for partial conversion tracking
   - Track ordered_qty_from_quote per line

### **Task 1.2: Enhance Sales Order Models**
**File**: `apps/retail/backend/sales/models.py`

**Changes Required**:
1. **Order Header** (`SalesOrder`):
   - Add all BBP 6.2 fields (100+ fields)
   - Add fulfillment tracking (allocated_at, picked_at, packed_at, shipped_at)
   - Add credit management (credit_hold, credit_hold_reason, credit_approved_by)
   - Add revision tracking
   - Add margin tracking
   - Add shipping tracking (tracking_number, carrier_name)

2. **Order Line** (`SalesOrderLine`):
   - Add fulfillment quantities (allocated_qty, picked_qty, shipped_qty, delivered_qty)
   - Add backorder tracking (backorder_qty, backorder_reason)
   - Add price source tracking
   - Add margin calculation
   - Add line status enum with fulfillment states

### **Task 1.3: Enhance Sales Invoice Models**
**File**: `apps/retail/backend/sales/models.py`

**Changes Required**:
1. **Invoice Header** (`Invoice` → `SalesInvoice`):
   - Add all BBP 6.3 fields
   - Add payment tracking (payment_status, paid_amount, outstanding_amount)
   - Add revenue recognition fields
   - Add dunning workflow fields
   - Add credit note linkage

2. **Invoice Line** (`InvoiceLine` → `SalesInvoiceLine`):
   - Link to order_line (not just order)
   - Add revenue recognition tracking
   - Add tax breakdown

3. **Invoice Match Detail** (NEW):
   - Create model for order-invoice matching
   - Track invoiced quantities per order line

### **Task 1.4: Enhance Sales Return Models**
**File**: `apps/retail/backend/sales/models.py`

**Changes Required**:
1. **Return Header** (`SalesReturn` → `SalesReturnNote`):
   - Add all BBP 6.4 fields
   - Add RMA workflow (authorization, inspection, disposition)
   - Add refund/exchange tracking
   - Add restocking fee calculation
   - Add quality inspection fields

2. **Return Line** (`SalesReturnLine`):
   - Add disposition tracking (restock, scrap, repair)
   - Add quality inspection results
   - Add refund calculation breakdown

### **Task 1.5: Enhance Sales Configuration Models**
**File**: `apps/retail/backend/sales/models.py`

**Changes Required**:
1. **Sales Process Settings** (`SalesProcessSetting` → `SalesConfig`):
   - Add all BBP 6.5 config flags (40+ settings)
   - Organize into sections: Process, Tolerance, Approval, Margin, Revenue

2. **Sales Approval Matrix** (`SalesApprovalMatrix`):
   - Enhance with threshold-based rules
   - Add role-based approval chains

---

## 🎯 **Phase 2: Serializers** (Next)

### **Task 2.1: Quote Serializers**
**File**: `apps/retail/backend/sales/serializers.py`

**Create**:
- `SalesQuoteLineSerializer` (nested)
- `SalesQuoteSerializer` (with nested lines)
- `SalesQuoteListSerializer` (optimized for list view)
- `SalesQuoteDetailSerializer` (full detail with relationships)

### **Task 2.2: Order Serializers**
**File**: `apps/retail/backend/sales/serializers.py`

**Create**:
- `SalesOrderLineSerializer` (nested)
- `SalesOrderSerializer` (with nested lines)
- `SalesOrderListSerializer`
- `SalesOrderDetailSerializer`
- `SalesOrderFulfillmentSerializer` (for fulfillment tracking)

### **Task 2.3: Invoice Serializers**
**File**: `apps/retail/backend/sales/serializers.py`

**Create**:
- `SalesInvoiceLineSerializer`
- `SalesInvoiceSerializer`
- `SalesInvoiceListSerializer`
- `SalesInvoiceDetailSerializer`

### **Task 2.4: Return Serializers**
**File**: `apps/retail/backend/sales/serializers.py`

**Create**:
- `SalesReturnLineSerializer`
- `SalesReturnNoteSerializer`
- `SalesReturnListSerializer`
- `SalesReturnDetailSerializer`

### **Task 2.5: Config Serializers**
**File**: `apps/retail/backend/sales/serializers.py`

**Create**:
- `SalesConfigSerializer`
- `SalesApprovalMatrixSerializer`

---

## 🎯 **Phase 3: ViewSets & Endpoints** (Next)

### **Task 3.1: Quote ViewSet**
**File**: `apps/retail/backend/sales/views.py`

**Create**: `SalesQuoteViewSet`
- CRUD operations
- Workflow actions:
  - `submit_quote` (DRAFT → SUBMITTED)
  - `approve_quote` (SUBMITTED → APPROVED)
  - `reject_quote` (SUBMITTED → REJECTED)
  - `send_to_customer` (APPROVED → SENT_TO_CUSTOMER)
  - `mark_accepted` (SENT_TO_CUSTOMER → ACCEPTED)
  - `mark_rejected` (SENT_TO_CUSTOMER → REJECTED)
  - `convert_to_order` (ACCEPTED → CONVERTED)
  - `create_revision` (create new revision)
  - `cancel_quote`
  - `duplicate_quote`

### **Task 3.2: Order ViewSet**
**File**: `apps/retail/backend/sales/views.py`

**Create**: `SalesOrderViewSet`
- CRUD operations
- Workflow actions:
  - `submit_order` (DRAFT → PENDING_APPROVAL)
  - `approve_order` (PENDING_APPROVAL → APPROVED)
  - `reject_order` (PENDING_APPROVAL → REJECTED)
  - `confirm_order` (APPROVED → CONFIRMED)
  - `allocate_inventory` (CONFIRMED → PROCESSING)
  - `process_picking` (update picked_qty)
  - `process_packing` (update packed status)
  - `create_shipment` (PROCESSING → PARTIALLY_SHIPPED/FULLY_SHIPPED)
  - `generate_invoice` (create invoice from order)
  - `cancel_order`
  - `create_revision`

### **Task 3.3: Invoice ViewSet**
**File**: `apps/retail/backend/sales/views.py`

**Create**: `SalesInvoiceViewSet`
- CRUD operations
- Workflow actions:
  - `post_invoice` (DRAFT → POSTED)
  - `record_payment` (update payment status)
  - `generate_credit_note`
  - `send_to_customer`
  - `cancel_invoice`

### **Task 3.4: Return ViewSet**
**File**: `apps/retail/backend/sales/views.py`

**Create**: `SalesReturnNoteViewSet`
- CRUD operations
- Workflow actions:
  - `submit_return` (DRAFT → SUBMITTED)
  - `approve_return` (SUBMITTED → APPROVED)
  - `reject_return` (SUBMITTED → REJECTED)
  - `receive_return` (APPROVED → RECEIVED)
  - `process_refund` (RECEIVED → REFUNDED)
  - `process_exchange` (RECEIVED → EXCHANGED)
  - `cancel_return`

### **Task 3.5: Config ViewSet**
**File**: `apps/retail/backend/sales/views.py`

**Create**: `SalesConfigViewSet`
- CRUD operations for company-level config
- Validation for config changes

---

## 🎯 **Phase 4: Business Logic & Services** (Next)

### **Task 4.1: Quote Service**
**File**: `apps/retail/backend/sales/services/quote_service.py`

**Create**:
- `QuoteNumberGenerator` (auto-generate quote numbers)
- `QuoteApprovalEngine` (check approval requirements)
- `QuoteExpiryHandler` (auto-expire quotes)
- `QuoteMarginCalculator` (calculate margins)
- `QuoteRevisionManager` (handle revisions)

### **Task 4.2: Order Service**
**File**: `apps/retail/backend/sales/services/order_service.py`

**Create**:
- `OrderNumberGenerator`
- `OrderApprovalEngine`
- `CreditLimitChecker` (validate credit limits)
- `InventoryAllocationService` (allocate stock)
- `OrderFulfillmentTracker` (track fulfillment progress)
- `OrderRevisionManager`

### **Task 4.3: Invoice Service**
**File**: `apps/retail/backend/sales/services/invoice_service.py`

**Create**:
- `InvoiceNumberGenerator`
- `InvoiceMatchingEngine` (match order to invoice)
- `RevenueRecognitionEngine`
- `PaymentAllocationService`
- `DunningWorkflowEngine`

### **Task 4.4: Return Service**
**File**: `apps/retail/backend/sales/services/return_service.py`

**Create**:
- `ReturnNumberGenerator`
- `ReturnApprovalEngine`
- `QualityInspectionHandler`
- `RefundCalculator`
- `RestockingFeeCalculator`

---

## 🎯 **Phase 5: URL Configuration** (Next)

### **Task 5.1: Register URLs**
**File**: `apps/retail/backend/sales/urls.py`

**Create**:
```python
router.register(r'quotes', SalesQuoteViewSet, basename='sales-quote')
router.register(r'orders', SalesOrderViewSet, basename='sales-order')
router.register(r'invoices', SalesInvoiceViewSet, basename='sales-invoice')
router.register(r'returns', SalesReturnNoteViewSet, basename='sales-return')
router.register(r'config', SalesConfigViewSet, basename='sales-config')
```

---

## 🎯 **Phase 6: Migrations** (Next)

### **Task 6.1: Create Migrations**
```bash
python manage.py makemigrations sales
python manage.py migrate sales
```

### **Task 6.2: Data Migration**
- Migrate existing simple data to new schema (if any)
- Create default config for existing companies

---

## 📊 **Success Criteria**

### **Phase 1 Complete When**:
- ✅ All models enhanced with BBP-compliant fields
- ✅ All enums defined for status tracking
- ✅ All relationships properly defined
- ✅ Migrations created and applied successfully

### **Phase 2 Complete When**:
- ✅ All serializers created with proper validation
- ✅ Nested serializers working correctly
- ✅ List/Detail serializers optimized

### **Phase 3 Complete When**:
- ✅ All ViewSets created with CRUD operations
- ✅ All workflow actions implemented
- ✅ Proper permissions and filtering applied

### **Phase 4 Complete When**:
- ✅ All business logic extracted to services
- ✅ Number generation working
- ✅ Approval engines functional
- ✅ Integration with inventory/payments working

### **Phase 5 Complete When**:
- ✅ All URLs registered
- ✅ API endpoints accessible
- ✅ Swagger documentation generated

### **Phase 6 Complete When**:
- ✅ Migrations applied without errors
- ✅ Database schema matches BBP specifications
- ✅ Existing data migrated (if applicable)

---

## 🚀 **Execution Strategy**

### **AUTO-EXECUTION MODE**
Following the user's directive, I will:
1. Execute all phases sequentially
2. Resolve dependencies automatically
3. Apply best practices from Procurement module
4. Only stop for genuine missing inputs or governance violations

### **Reference Pattern**
Using Procurement module as reference:
- Model structure and field naming
- Serializer patterns
- ViewSet action patterns
- Service layer organization
- Number generation logic

---

## 📝 **Next Steps**

**Immediate**: Start Phase 1 - Enhance Models
1. Backup existing models.py
2. Enhance Quote models
3. Enhance Order models
4. Enhance Invoice models
5. Enhance Return models
6. Enhance Config models
7. Create migrations

**After Phase 1**: Proceed to Phase 2 (Serializers)

---

**Ready to execute Phase 1!** 🚀
