# Procurement Implementation Plan
**Objective**: Implement the full Procurement module (PR, PO, GRN, Bill, Return) in the "Sales Module Style" (Dynamics 365 UI, React/Django).

## 1. Requirement Analysis (from BBP 4.1 - 4.10)

### 4.1 Purchase Requisition (PR)
*   **Purpose**: Internal demand capture.
*   **Key Fields**: `pr_number`, `requesting_location`, `requested_by`, `status`, `approval_required`.
*   **Lines**: `item`, `qty`, `required_date`.
*   **Workflow**: `DRAFT -> SUBMITTED -> APPROVED -> ORDERED`.

### 4.2 Request for Quotation (RFQ)
*   **Scope**: Out of Scope for Phase 1 MVP (Focus on Core Flow: PR -> PO). *Unless strictly requested now*. (User said 4.1 to 4.10 complete... implying all? I will prioritize core flow first).

### 4.3 Purchase Order (PO)
*   **Purpose**: Commitment to Supplier.
*   **Key Fields**: `po_number`, `supplier`, `ordering_location`, `date`, `status`, `total_amount`.
*   **Lines**: `item`, `ordered_qty`, `price`, `tax`, `discount`.
*   **Workflow**: `DRAFT -> APPROVED -> SENT -> RECEIVED -> CLOSED`.

### 4.4 ASN (Advance Shipment Notice)
*   **Purpose**: Supplier notifies shipment.
*   **Notes**: Often skipped in simple execution. I will implement as optional foundation or Phase 2.

### 4.5 Goods Receipt Note (GRN)
*   **Purpose**: Receiving stock.
*   **Key Fields**: `grn_number`, `po_ref`, `received_date`.
*   **Lines**: `item`, `received_qty`, `rejected_qty`.
*   **Impact**: Increases Inventory (Stock Moves).

### 4.6 Invoice Matching (Bill)
*   **Purpose**: 3-Way match (PO - GRN - Invoice).
*   **Key Fields**: `invoice_number`, `supplier`, `amount`.
*   **Workflow**: Match `qty` and `price`. `POSTED` status.

### 4.7 Supplier Returns
*   **Purpose**: Returning goods to supplier.
*   **Ref**: Linked to GRN or PO.

### 4.10 Configuration
*   **Purpose**: Global rules (Enable PRs?, Approval limits).

## 2. Implementation Strategy (Sales Style)

### Architecture
*   **Location**: `backend/domain/procurement/` and `frontend/src/pages/procurement/`.
*   **Style**: 
    *   **UI**: Dynamics 365 Layout (AppHeader, Sidebar, PageTitle, CommandBar, Grid).
    *   **Router**: `/procurement/*`.
    *   **Models**: Django Models with Audit/Status Enums.

### Phasing
**Phase 1: Core Purchasing (The "Happy Path")**
1.  **Models**: PR, PO, GRN, Bill, Return, Config.
2.  **UI - Purchase Orders**: The central document. List & Detail.
3.  **UI - Requisitions**: Internal demand.
4.  **UI - Configuration**: To enable/disable workflow steps.

**Phase 2: Execution**
1.  **UI - Receipts (GRN)**: Handling stock.
2.  **UI - Bills**: Financials.
3.  **UI - Returns**.

## 3. Detailed Data Models (Planned)

### `PurchaseRequisition`
```python
class PRStatus(models.TextChoices):
    DRAFT = 'DRAFT'
    SUBMITTED = 'SUBMITTED'
    APPROVED = 'APPROVED'
    ORDERED = 'ORDERED'
```

### `PurchaseOrder`
```python
class POStatus(models.TextChoices):
    DRAFT = 'DRAFT'
    APPROVED = 'APPROVED'
    SENT = 'SENT'
    PARTIAL = 'PARTIALLY_RECEIVED'
    FULL = 'FULLY_RECEIVED'
```

### `GoodsReceipt`
```python
# Links to PO. Updates Inventory.
```

## 4. UI Structure (Menu)
*   **Procurement**
    *   **Purchase Orders** (`/procurement/orders`)
    *   **Requisitions** (`/procurement/requisitions`)
    *   **Receipts** (`/procurement/receipts`)
    *   **Bills** (`/procurement/bills`)
    *   **Returns** (`/procurement/returns`)
    *   **Configuration** (`/procurement/config`)

## 5. Next Steps
1.  Create Backend Models (`backend/domain/procurement/models.py`).
2.  Create Frontend Pages (List/Detail).
3.  Wiring Router & Menu.
