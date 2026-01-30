# Retail Operations Model Audit Report

**Date**: 2025-12-21
**Scope**: `backend/domain`
**Mode**: Read-Only / Gap Analysis

## Store Ops
| Feature | Models Found | Coverage | Notes |
| :--- | :--- | :--- | :--- |
| **Checkout** | `domain.pos.transaction_models.POSTransaction` | ✅ Fully Covered | Includes Lines, Payments, Taxes. |
| **Daily Operations** | `domain.pos` (`DayOpen`, `PosSession`, `POSReconciliation`) | ✅ Fully Covered | Full operational workflow models exist. |
| **Registers** | `domain.pos.terminal.models.terminal.Terminal` | ✅ Fully Covered | |

## Sales
| Feature | Models Found | Coverage | Notes |
| :--- | :--- | :--- | :--- |
| **Quotes** | `domain.sales.models.Quote` | ✅ Fully Covered | |
| **Fulfillment** | `domain.sales.models.SalesOrder` | ✅ Fully Covered | |
| **Invoices** | `domain.sales.models.Invoice` | ✅ Fully Covered | Customer Invoice. |
| **Returns** | `domain.sales.models.SalesReturn` | ✅ Fully Covered | |
| **Configuration** | `domain.sales.models.SalesProcessSetting` | ✅ Fully Covered | |

## Merchandising
| Feature | Models Found | Coverage | Notes |
| :--- | :--- | :--- | :--- |
| **Catalog** | `domain.business_entities.models.ItemMaster` | ✅ Fully Covered | Canonical Product Model. |
| **Hierarchy** | `domain.business_entities.models.Category` | ✅ Fully Covered | |
| **Brands** | `domain.business_entities.models.Brand` | ✅ Fully Covered | |
| **Variants** | `domain.company.models.ItemVariant` | ✅ Fully Covered | Canonical Variant Model. |
| **Attributes** | `domain.business_entities.models.Attribute` | ✅ Fully Covered | Includes `AttributeValue`, `ProductAttributeTemplate`. |
| **Pricing** | `domain.business_entities.models.PriceList` | ✅ Fully Covered | **Warning**: Duplicate `domain.company.models.PriceList` exists. |
| **UOM** | `domain.business_entities.models.UnitOfMeasure` | ✅ Fully Covered | |

## Inventory
| Feature | Models Found | Coverage | Notes |
| :--- | :--- | :--- | :--- |
| **Stock on Hand** | `domain.inventory.models.StockLevel` | ✅ Fully Covered | Materialized view of stock. |
| **Logistics** | `domain.inventory.models.StockMovement`, `StockTransfer` | ✅ Fully Covered | Includes Intercompany Transfer. |
| **Physical Inventory** | `domain.inventory.models.StockTake` | ✅ Fully Covered | Includes Adjustments. |
| **Reorder Policies** | `domain.inventory.models.ReorderPolicy` | ✅ Fully Covered | |

## Procurement
| Feature | Models Found | Coverage | Notes |
| :--- | :--- | :--- | :--- |
| **Vendors** | `domain.business_entities.models.Supplier` | ✅ Fully Covered | |
| **Requisitions** | `domain.procurement.models.PurchaseRequisition` | ✅ Fully Covered | |
| **RFQ** | `domain.procurement.models.RequestForQuotation` | ✅ Fully Covered | |
| **Purchase Orders** | `domain.procurement.models.PurchaseOrder` | ✅ Fully Covered | |
| **ASNs** | None | ❌ Missing | Advance Shipment Notice model not found. |
| **Goods Receipts** | `domain.procurement.models.GoodsReceipt` | ✅ Fully Covered | |
| **Invoice Matching** | None | ❌ Missing | No `VendorBill` or 3-way matching model found. |
| **Purchase Returns** | None | ❌ Missing | No return workflow model found (only Sales Return exists). |
| **Payments** | None | ❌ Missing | No `VendorPayment` model found. |
| **Compliance** | `domain.procurement.models.VendorCompliance` | ✅ Fully Covered | |

## Customers
| Feature | Models Found | Coverage | Notes |
| :--- | :--- | :--- | :--- |
| **Directory** | `domain.business_entities.models.Customer` | ✅ Fully Covered | |
| **Groups** | `domain.business_entities.master_data_models.CustomerGroup` | ✅ Fully Covered | |
| **Loyalty** | `domain.business_entities.master_data_models.LoyaltyProgram` | ✅ Fully Covered | Includes `CustomerLoyalty`. |

## Summary

### Critical Gaps (Must-have for MVP)
1.  **Procurement Financials**: The "Pay" part of Procure-to-Pay is missing.
    *   Missing `VendorBill` (Invoice).
    *   Missing `PurchaseReturn` (Debit Note logic).
    *   Missing `VendorPayment` (Outbound payment).
2.  **ASN**: Missing `AdvanceShipmentNotice` means no inbound logistics visibility before GRN.

### Medium Gaps
1.  **PriceList Duplication**: `domain.company.PriceList` vs `domain.business_entities.PriceList`. Needs rationalization (Phase 4/5).

### Low Priority / Optional
1.  **Procurement Configuration**: Use `ProcurementConfig` (Found) to toggle missing features until implemented.


Procurement Data Model Documentation
1. Relationship Diagram (Procure-to-Pay)
text
[PurchaseOrder] (The central document)
  │
  ├── 1:N ── [AdvanceShipmentNotice] (Logistics: Pre-arrival tracking)
  │
  ├── 1:N ── [GoodsReceipt] (Inventory: Stock In)
  │            │
  │            └── 1:N ── [PurchaseReturn] (Debit Note: Stock Out / Credit Request)
  │
  └── 1:N ── [VendorBill] (Finance: Liability / AP)
               │
               ├── Linked via Lines ──> [GoodsReceiptLine] (For 3-way match verification)
               │
               └── N:M ── [PaymentAllocation] ── 1:1 ── [VendorPayment] (Settlement)
2. Model Reference
AdvanceShipmentNotice (ASN)
Purpose: Records details of a shipment dispatched by the vendor before it arrives at the warehouse.
Position: Between PO issuance and Goods Receipt.
Key Relationships: FK to 
PurchaseOrder
.
VendorBill (Supplier Invoice)
Purpose: Represents the financial claim (Invoice) from the supplier. It is the basis for Accounts Payable liability.
Position: After Goods Receipt (Standard 3-way match) or Concurrent.
Key Relationships:
Header: FK to 
PurchaseOrder
.
Lines: FK to 
GoodsReceiptLine
 (to verify Qty) and 
PurchaseOrderLine
 (to verify Price).
PurchaseReturn (Debit Note)
Purpose: Tracks handling of rejected or excess goods returned to the supplier, ensuring inventory adjustment and financial credit.
Position: Post-GRN.
Key Relationships: FK to 
GoodsReceipt
 (Origin) and 
VendorBill
 (if credit is applied against a specific bill).
VendorPayment
Purpose: Records the actual outflow of funds to settle vendor liabilities.
Position: Final step (Pay).
Key Relationships: Link to 
VendorBill
 via 
PaymentAllocation
 (allowing partial payments or one payment for multiple bills).
3. Validation Status
✅ Migration Ready: Models are fully defined with standard Django fields and constraints.
✅ No Admin Exposure: New models are NOT registered in 
admin.py
, strictly enforcing the "Backend Design Only" scope.
✅ Scope Respected: Process stopped immediately after model definitions; no side-effects or UI code created.
Procurement model layer complete at design level.