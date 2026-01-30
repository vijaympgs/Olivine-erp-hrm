# Django Codebase Audit Report

## Module: HR
**App:** `hr` (Implicit)
**File:** `backend/hr/models.py`
**Models:**
*   `Employee` (models.Model)
    *   **Relationships:** `reporting_manager` (Self, ForeignKey)
    *   **Meta:** None (Defaults to `hr`)

## Module: User Management
**App:** `user_management`
**File:** `backend/domain/user_management/models.py`
**Models:**
*   `Employee` (models.Model)
    *   **Relationships:** `reporting_manager` (Self, ForeignKey)
    *   **Meta:** `app_label = "user_management"`

## Module: Business Entities
**App:** `business_entities`
**File:** `backend/domain/business_entities/models.py`
**Models:**
*   `Company` (models.Model)
    *   **Meta:** `app_label = "business_entities"`, `db_table = "be_company"`.
*   `Category` (models.Model)
    *   **Meta:** `db_table = 'be_category'`.
*   `Brand` (models.Model)
    *   **Meta:** `db_table = 'be_brand'`.
*   `Attribute` (models.Model)
    *   **Relationships:** `company` (FK).
    *   **Meta:** `unique_together = ('company', 'attribute_code')`.
*   `AttributeValue` (models.Model)
    *   **Relationships:** `company` (FK), `attribute` (FK).
*   `ProductAttributeTemplate` (models.Model)
    *   **Relationships:** `company` (FK), `category_scope` (FK).
*   `UnitOfMeasure` (models.Model)
    *   **Relationships:** `company` (FK).
*   `PriceList` (models.Model)
    *   **Relationships:** `company` (FK).
*   `TaxClass` (models.Model)
*   `ItemMaster` (models.Model)
    *   **Relationships:** `company`, `attribute_template`, `category`, `brand`, `stock_uom`, `price_list`, `tax_class` (All FKs).
*   `Customer` (models.Model)
    *   **Relationships:** `company` (FK).
*   `Supplier` (models.Model)
    *   **Relationships:** `company` (FK).

**File:** `backend/domain/business_entities/master_data_models.py`
**Models:**
*   `PaymentMethod` (models.Model)
*   `TaxClassEnhanced` (models.Model)
*   `CustomerGroup` (models.Model)
*   `Promotion` (models.Model)
*   `LoyaltyProgram` (models.Model)
*   `CustomerLoyalty` (models.Model)
    *   **Relationships:** `customer` (OneToOne), `program` (FK).

## Module: Company
**App:** `company` (Implicit/Likely)
**File:** `backend/domain/company/models.py`
**Models:**
*   `Company` (models.Model)
    *   **Meta:** `db_table = 'company'`.
*   `Location` (models.Model)
    *   **Relationships:** `company` (FK), `parent_location` (Self).
*   `Attribute` (models.Model)
    *   **Relationships:** `company` (FK).
*   `AttributeValue` (models.Model)
    *   **Relationships:** `company` (FK), `attribute` (FK).
*   `ProductAttributeTemplate` (models.Model)
    *   **Relationships:** `company` (FK).
*   `ProductAttributeTemplateLine` (models.Model)
    *   **Relationships:** `template` (FK), `attribute` (FK), `default_value` (FK).
*   `UnitOfMeasure` (models.Model)
    *   **Relationships:** `company` (FK).
*   `UOMConversion` (models.Model)
    *   **Relationships:** `company` (FK), `from_uom` (FK), `to_uom` (FK).
*   `Item` (models.Model)
    *   **Relationships:** `company` (FK), `attribute_template` (FK), `stock_uom` (FK).
    *   **Note:** `category_id`, `brand_id`, `tax_class_id` are `UUIDField` (Loose Coupling).
*   `ItemVariant` (models.Model)
    *   **Relationships:** `item` (FK), `sales_uom` (FK), `purchase_uom` (FK), `stock_uom` (FK).
*   `VariantAttribute` (models.Model)
    *   **Relationships:** `item_variant` (FK), `attribute` (FK), `attribute_value` (FK).
*   `VariantUOM` (models.Model)
    *   **Relationships:** `item_variant` (FK), `uom` (FK).
*   `PriceList` (models.Model)
    *   **Relationships:** `company` (FK).
*   `PriceListLine` (models.Model)
    *   **Relationships:** `price_list` (FK), `item` (FK), `item_variant` (FK), `uom` (FK), `location_scope` (FK).
*   `Customer` (models.Model)
    *   **Relationships:** `company` (FK).
*   `Supplier` (models.Model)
    *   **Relationships:** `company` (FK).

## Module: Finance
**App:** `finance` (Implicit)
**File:** `backend/domain/finance/models.py`
**Models:**
*   `AccountGroup` (models.Model)
    *   **Relationships:** `company` (FK), `parent` (Self).
*   `AccountLedger` (models.Model)
    *   **Relationships:** `company` (FK), `group` (FK).
*   `JournalEntry` (models.Model)
    *   **Relationships:** `company` (FK).
*   `JournalItem` (models.Model)
    *   **Relationships:** `entry` (FK), `ledger` (FK).

## Module: Inventory
**App:** `inventory`
**File:** `backend/domain/inventory/models.py`
**Models:**
*   `StockMovement` (models.Model)
    *   **Relationships:** `company` (FK to `business_entities.Company`), `item` (FK to `business_entities.ItemMaster`), `variant` (FK to `company.ItemVariant`), `from_location`/`to_location` (FK to `company.Location`).
    *   **Meta:** `app_label = 'inventory'`.
*   `StockLevel` (models.Model)
    *   **Relationships:** `company` (FK to `business_entities.Company`), `variant` (FK to `company.ItemVariant`), `location` (FK to `company.Location`).
*   `ReorderPolicy` (models.Model)
    *   **Relationships:** Same as above.
*   `StockTransfer` (models.Model)
    *   **Relationships:** `company` (FK to `business_entities.Company`), `source_location`/`destination_location` (FK to `company.Location`).
*   `StockTransferLine` (models.Model)
    *   **Relationships:** `transfer` (FK), `variant` (FK), `uom` (FK).
*   `StockTake` (models.Model)
    *   **Relationships:** `company`, `location` (FKs).
*   `StockTakeLine` (models.Model)
    *   **Relationships:** `stock_take` (FK), `variant` (FK).
*   `StockAdjustment` (models.Model)
    *   **Relationships:** `company`, `location`, `variant`, `uom` (FKs).

**File:** `backend/domain/inventory/intercompany_models.py`
**Models:**
*   `IntercompanyTransfer` (models.Model)
    *   **Relationships:** `source_company`/`destination_company` (FK to `business_entities.Company`), `source_location`/`destination_location` (FK to `company.Location`).
*   `IntercompanyTransferLine` (models.Model)
    *   **Relationships:** `transfer` (FK), `item` (FK to `business_entities.ItemMaster`), `item_variant` (FK to `company.ItemVariant`).

## Module: POS
**App:** `pos`
**File:** `backend/domain/pos/terminal/models/terminal.py`
**Models:**
*   `Terminal` (models.Model)
    *   **Relationships:** `company` (FK to `company.Company`), `location` (FK to `company.Location`).
    *   **Meta:** `db_table = 'pos_terminal'`.
*   `TerminalTransactionSettings` (models.Model)
    *   **Relationships:** `terminal` (OneToOne).
*   `TerminalTenderMapping` (models.Model)
    *   **Relationships:** `terminal` (FK).

**File:** `backend/domain/pos/session/models.py`
**Models:**
*   `PosSession` (models.Model)
    *   **Relationships:** `company` (FK to `company.Company`), `terminal` (FK), `location` (FK to `company.Location`), `user` (FK).

**File:** `backend/domain/pos/day_open/models.py`
**Models:**
*   `DayOpen` (models.Model)
    *   **Relationships:** `company` (FK to `company.Company`), `location` (FK), `opened_by`/`closed_by` (FK).

**File:** `backend/domain/pos/transaction_models.py`
**Models:**
*   `POSTransaction` (models.Model)
    *   **Relationships:** `company` (FK to `company.Company`), `terminal` (FK), `session` (FK), `day_open` (FK), `location` (FK), `customer` (FK to `business_entities.Customer`).
    *   **Meta:** `app_label = 'pos'`.
*   `POSTransactionLine` (models.Model)
    *   **Relationships:** `transaction` (FK), `item` (FK to `business_entities.ItemMaster`), `item_variant` (FK to `business_entities.ItemVariant` **[MISSING MODEL]**).
*   `POSTransactionPayment` (models.Model)
    *   **Relationships:** `transaction` (FK), `payment_method` (FK to `business_entities.PaymentMethod`).
*   `POSReconciliation` (models.Model)
    *   **Relationships:** `company` (FK to `company.Company`), `session` (FK), `terminal` (FK).

## Module: Procurement
**App:** `procurement` (Implicit)
**File:** `backend/domain/procurement/models.py`
**Models:**
*   `PurchaseRequisition` (models.Model)
    *   **Relationships:** `company` (FK to `business_entities.Company`), `requesting_location` (FK to `company.Location`).
*   `PurchaseRequisitionLine` (models.Model)
    *   **Relationships:** `item` (FK to `business_entities.ItemMaster`), `item_variant` (FK to `company.ItemVariant`).
*   `RequestForQuotation` (models.Model)
    *   **Relationships:** `company` (FK to `business_entities.Company`).
*   `RFQLine` (models.Model)
    *   **Relationships:** `item` (FK to `business_entities.ItemMaster`), `item_variant` (FK to `company.ItemVariant`).
*   `RFQVendor` (models.Model)
    *   **Relationships:** `supplier` (FK to `business_entities.Supplier`).
*   (`PurchaseOrder`, `GoodsReceipt`, `VendorBill` models are also present but commented out/in-progress in view).

## Module: Sales
**App:** `sales` (Implicit)
**File:** `backend/domain/sales/models.py`
**Models:**
*   `Quote`, `SalesOrder`, `SalesReturn`, `Invoice` (models.Model)
    *   **Relationships:** `company` (FK to `business_entities.Company`), `customer` (FK to `business_entities.Customer`).
*   `QuoteLine`, `SalesOrderLine`, `SalesReturnLine`, `InvoiceLine` (models.Model)
    *   **Relationships:** `item` (FK to `business_entities.ItemMaster`).
*   `SalesProcessSetting`, `SalesApprovalMatrix` (models.Model)
    *   **Relationships:** `company` (FK to `business_entities.Company`).

## Module: Master
**App:** `master` (Implicit)
**File:** `backend/domain/master/customer/models/models.py`
**Models:**
*   `Customer` (models.Model)
    *   **Meta:** `db_table = "customer"`.
    *   **Note:** No `Company` FK. Standalone.

---

## Ambiguities / Duplicates Detected

1.  **Duplicate `Company` Models (Major)**:
    *   `backend/domain/business_entities/models.py` defines `Company` (db_table: `be_company`).
    *   `backend/domain/company/models.py` defines `Company` (db_table: `company`).
    *   **Impact**: `POS` references `company.Company`. `Inventory`, `Sales`, `Procurement` refer to `business_entities.Company`. This creates a disjointed system where POS transactions live in a different "Company" universe than Inventory movements.

2.  **Duplicate `Customer` Models (Triplicate)**:
    *   `backend/domain/business_entities/models.py`: `Customer` (db_table: `be_customer`). Linked to `be_company`.
    *   `backend/domain/company/models.py`: `Customer` (db_table: `customer`). Linked to `company`.
    *   `backend/domain/master/customer/models/models.py`: `Customer` (db_table: `customer`). **Table Name Collision** with `company.Customer` if both installed.

3.  **Duplicate `Employee` Models**:
    *   `backend/hr/models.py`: `Employee`.
    *   `backend/domain/user_management/models.py`: `Employee`. Content is identical.

4.  **Inconsistent `Item` Architecture (Hybrid State)**:
    *   `business_entities` uses a flat `ItemMaster`.
    *   `company` uses `Item` (Parent) + `ItemVariant` (Child).
    *   `Inventory` hybridizes this by linking to `business_entities.ItemMaster` AND `company.ItemVariant`.
    *   `POS` (via `POSTransactionLine`) attempts to link to `business_entities.ItemVariant`, which **does not exist** (it only exists in `company`). This code is likely broken.

5.  **Duplicate Core Masters**:
    *   `UnitOfMeasure`, `PriceList`, `Supplier`, `Attribute`, `AttributeValue` are all defined in BOTH `business_entities` and `company` with different table names (`be_*` vs defaults).

6.  **Loose Coupling vs Strict FK**:
    *   `company.Item` uses UUIDFields (`category_id`, `brand_id`) without Foreign Keys.
    *   `business_entities.ItemMaster` uses explicit Foreign Keys (`category`, `brand`).
