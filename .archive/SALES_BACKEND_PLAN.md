# Sales Backend Implementation Plan
**Status**: Implemented
**Date**: 2025-12-29

## 1. API Endpoints
Base URL: `/api/sales/`

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/quotes/` | GET, POST | List and Create Quotes |
| `/quotes/{id}/` | GET, PUT, PATCH | Detail and Update Quote |
| `/orders/` | GET, POST | List and Create Orders |
| `/orders/{id}/` | GET, PUT | Detail and Update Order |
| `/returns/` | GET, POST | List and Create Returns |
| `/invoices/` | GET, POST | List and Create Invoices |
| `/configuration/my_settings/` | GET, PUT | Manage Sales Settings for current company |

## 2. Models & Serializers

### Quote
- **Model**: `Quote`
- **Fields**: `quote_number`, `customer`, `date`, `expiry_date`, `status`, `grand_total`, `lines`.
- **Auto-Generation**: `quote_number` (Format: QT-XXXXXXXX)

### Sales Order
- **Model**: `SalesOrder`
- **Fields**: `order_number`, `customer`, `quote`, `order_date`, `status`, `grand_total`, `lines`.
- **Auto-Generation**: `order_number` (Format: SO-XXXXXXXX)

### Invoice
- **Model**: `Invoice`
- **Fields**: `invoice_number`, `sales_order`, `customer`, `invoice_date`, `due_date`, `grand_total`, `lines`.

### Sales Return
- **Model**: `SalesReturn`
- **Fields**: `return_number`, `sales_order`, `customer`, `return_date`, `total_refund_amount`, `lines`.

## 3. Business Logic (Simple)
- **Company Isolation**: All ViewSets filter by the user's active company.
- **Auto-Creation**: `created_by` and `company` fields are populated automatically on `perform_create`.
- **Validation**: Basic model validation.

## 4. Next Steps (Frontend)
1.  **Service Layer**: Create `salesService.ts` to consume these endpoints.
2.  **Pages**:
    - `QuoteListPage`
    - `QuoteCreatePage`
    - `SalesOrderListPage`
    - `SalesOrderCreatePage`
3.  **Integration**: Link pages to the Sidebar.
