# 📦 INVENTORY BBP - MODEL REFERENCE GUIDE

**Purpose**: Django model creation reference for all Inventory BBP files  
**Last Updated**: 2025-12-28 10:32 IST  
**Total Files**: 56 BBP files  
**Total Models**: 32 unique models

---

## 📋 **BBP FILE METADATA - COMPLETE LIST**

### **5.1 INVENTORY DASHBOARD**

#### **5.1.1_Inventory_Overview_bbp.md**
- **Type**: DASHBOARD
- **Models Required**: Inventory, ItemMaster, Location
- **Reference Masters**: Company, UOM, Category, Brand
- **Comments**: Main dashboard showing stock summary, KPIs, alerts. Aggregates data from Inventory table.

#### **5.1.2_Stock_by_Location_bbp.md**
- **Type**: DASHBOARD
- **Models Required**: Inventory, Location
- **Reference Masters**: Company
- **Comments**: Location-wise stock visualization. Groups Inventory by Location.

#### **5.1.3_Stock_Valuation_bbp.md**
- **Type**: DASHBOARD
- **Models Required**: Inventory, ItemMaster, ValuationMethod
- **Reference Masters**: Company, UOM
- **Comments**: Stock value dashboard using FIFO/LIFO/Weighted Average methods.

#### **5.1.4_Movement_Trends_bbp.md**
- **Type**: DASHBOARD
- **Models Required**: StockMovement, Inventory
- **Reference Masters**: MovementType, Location, ItemMaster
- **Comments**: Movement analytics with trend charts. Aggregates StockMovement data.

#### **5.1.5_Alerts_Notifications_bbp.md**
- **Type**: DASHBOARD
- **Models Required**: Inventory, ReorderPolicy, ItemMaster
- **Reference Masters**: Location, UOM
- **Comments**: Low stock, overstock, expiry alerts. Uses ReorderPolicy thresholds.

---

### **5.2 STOCK MANAGEMENT**

#### **5.2.1_Stock_on_Hand_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Inventory, ItemMaster, Location
- **Reference Masters**: Company, UOM, Category, Brand
- **Comments**: Main stock inquiry view. Shows all items with current stock levels.

#### **5.2.2_Stock_by_Location_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Inventory, Location
- **Reference Masters**: Company, ItemMaster
- **Comments**: Stock filtered by location. Same as 5.2.1 with location filter.

#### **5.2.3_Stock_by_Category_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Inventory, ItemMaster, Category
- **Reference Masters**: Company, Location, UOM
- **Comments**: Stock grouped by category. Joins Inventory → ItemMaster → Category.

#### **5.2.4_Stock_by_Batch_Serial_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Inventory, Batch, SerialNumber
- **Reference Masters**: ItemMaster, Location
- **Comments**: Batch/serial tracking view. Shows stock with batch/serial details.

#### **5.2.5_Low_Stock_Alerts_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Inventory, ReorderPolicy, ItemMaster
- **Reference Masters**: Location, UOM
- **Comments**: Items below reorder point. Compares Inventory.quantity with ReorderPolicy.reorder_point.

#### **5.2.6_Overstock_Alerts_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Inventory, ReorderPolicy, ItemMaster
- **Reference Masters**: Location, UOM
- **Comments**: Items above max stock. Compares Inventory.quantity with ReorderPolicy.max_quantity.

#### **5.2.7_Stock_Aging_Analysis_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Inventory, StockMovement, ItemMaster
- **Reference Masters**: Location, UOM
- **Comments**: Stock age calculation. Uses StockMovement.created_at to calculate age.

---

### **5.3 STOCK MOVEMENTS**

#### **5.3.1_Movement_History_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: StockMovement, ItemMaster, Location
- **Reference Masters**: MovementType, User, Company
- **Comments**: All stock movements log. Main movement history view.

#### **5.3.2_Goods_Receipt_bbp.md**
- **Type**: REFERENCE VIEW (Read-only from Procurement)
- **Models Required**: StockMovement (filter: movement_type='GRN')
- **Reference Masters**: GoodsReceipt (Procurement 4.6), PurchaseOrder, Vendor, Location, ItemMaster
- **Scope**: View-only - Shows GRN impact on inventory. No creation/editing allowed.
- **Source Module**: Procurement (4.6 GRN)
- **Comments**: Displays how Procurement GRNs affect inventory levels. Click GRN number to navigate to Procurement module for full details.

#### **5.3.3_Goods_Issue_bbp.md**
- **Type**: REFERENCE VIEW (Read-only from Sales)
- **Models Required**: StockMovement (filter: movement_type='SALE' or 'ISSUE')
- **Reference Masters**: SalesOrder (Sales module), Invoice (Sales module), Customer, Location, ItemMaster
- **Scope**: View-only - Shows sales/delivery impact on inventory. No creation/editing allowed.
- **Source Module**: Sales (Invoice/Delivery)
- **Comments**: Displays how Sales invoices and deliveries affect inventory levels. Click invoice/delivery number to navigate to Sales module for full details.

#### **5.3.4_Internal_Transfers_bbp.md**
- **Type**: TRANSACTION
- **Models Required**: StockTransfer, StockMovement, Location
- **Reference Masters**: ItemMaster, User, Company
- **Comments**: Inter-location transfers. Creates StockTransfer + 2 StockMovements (OUT/IN).

#### **5.3.5_Intercompany_Transfers_bbp.md**
- **Type**: TRANSACTION
- **Models Required**: IntercompanyTransfer, StockMovement, Company
- **Reference Masters**: Location, ItemMaster, User
- **Comments**: Inter-company transfers. Creates IntercompanyTransfer + StockMovements for both companies.

#### **5.3.6_Movement_Reports_bbp.md**
- **Type**: REPORT
- **Models Required**: StockMovement, ItemMaster, Location
- **Reference Masters**: MovementType, User, Company
- **Comments**: Movement history export. Same data as 5.3.1 with export capability.

---

### **5.4 STOCK ADJUSTMENTS**

#### **5.4.1_Adjustment_Entry_bbp.md**
- **Type**: TRANSACTION
- **Models Required**: StockAdjustment, StockMovement, AdjustmentReason
- **Reference Masters**: ItemMaster, Location, User, Company
- **Comments**: Create stock adjustments. Creates StockAdjustment + StockMovement. Requires approval if > threshold.

#### **5.4.2_Adjustment_History_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: StockAdjustment, ItemMaster, User
- **Reference Masters**: AdjustmentReason, Location, Company
- **Comments**: All adjustments log. Shows status (pending/approved/rejected).

#### **5.4.3_Reason_Code_Management_bbp.md**
- **Type**: MASTER
- **Models Required**: AdjustmentReason
- **Reference Masters**: Company
- **Comments**: Master data for adjustment reasons (e.g., Damage, Theft, Expiry, Correction).

#### **5.4.4_Approval_Workflow_bbp.md**
- **Type**: RULE DEFINITION
- **Models Required**: StockAdjustment, ApprovalRule, User
- **Reference Masters**: Role, Company
- **Comments**: Approval rules for adjustments. Threshold-based approval (e.g., >$1000 needs approval).

#### **5.4.5_Adjustment_Reports_bbp.md**
- **Type**: REPORT
- **Models Required**: StockAdjustment, ItemMaster, AdjustmentReason
- **Reference Masters**: Location, User, Company
- **Comments**: Adjustment history export. Same as 5.4.2 with export.

---

### **5.5 PHYSICAL INVENTORY**

#### **5.5.1_Cycle_Counting_Schedule_bbp.md**
- **Type**: CONFIGURATION
- **Models Required**: CycleCountSchedule, Location, ItemMaster
- **Reference Masters**: Company, User
- **Comments**: Schedule cycle counts. Defines frequency (daily/weekly/monthly) and items to count.

#### **5.5.2_Stock_Take_Execution_bbp.md**
- **Type**: TRANSACTION
- **Models Required**: StockTake, StockTakeLine, Inventory
- **Reference Masters**: Location, ItemMaster, User, Company
- **Comments**: Execute physical count. Creates StockTake (header) + StockTakeLine (lines).

#### **5.5.3_Variance_Analysis_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: StockTake, Inventory, ItemMaster
- **Reference Masters**: Location, UOM
- **Comments**: Count vs system variance. Compares StockTakeLine.counted_qty with Inventory.quantity.

#### **5.5.4_Count_Approval_bbp.md**
- **Type**: RULE DEFINITION
- **Models Required**: StockTake, ApprovalRule, User
- **Reference Masters**: Role, Company
- **Comments**: Approve stock take. Variance > threshold needs approval.

#### **5.5.5_Reconciliation_bbp.md**
- **Type**: TRANSACTION
- **Models Required**: StockTake, StockAdjustment, StockMovement
- **Reference Masters**: ItemMaster, Location, User
- **Comments**: Post-approval reconciliation. Creates StockAdjustment for variances.

---

### **5.6 INVENTORY VALUATION**

#### **5.6.1_Valuation_Methods_bbp.md**
- **Type**: CONFIGURATION
- **Models Required**: ValuationMethod, Company
- **Reference Masters**: -
- **Comments**: Configure valuation method (FIFO/LIFO/Weighted Average) per company.

#### **5.6.2_Valuation_Reports_bbp.md**
- **Type**: REPORT
- **Models Required**: Inventory, ItemMaster, ValuationMethod
- **Reference Masters**: Location, UOM, Company
- **Comments**: Stock value report. Calculates value using configured method.

#### **5.6.3_Cost_Analysis_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Inventory, ItemMaster, StockMovement
- **Reference Masters**: Location, UOM, ValuationMethod
- **Comments**: Cost breakdown by item. Shows cost components (purchase, freight, etc.).

#### **5.6.4_Revaluation_Phase2_bbp.md** ⭐ PHASE 2
- **Type**: TRANSACTION
- **Models Required**: InventoryRevaluation, GLEntry
- **Reference Masters**: Inventory, ItemMaster, User, Company
- **Comments**: PHASE 2 - Stock revaluation. Requires Finance GL integration. Creates GL entries.

#### **5.6.5_Period_End_Valuation_bbp.md**
- **Type**: REPORT
- **Models Required**: Inventory, ItemMaster, FiscalPeriod
- **Reference Masters**: Location, ValuationMethod, Company
- **Comments**: Period-end stock value snapshot. Captures value at period close.

---

### **5.7 REPLENISHMENT & PLANNING**

#### **5.7.1_Reorder_Point_Management_bbp.md**
- **Type**: CONFIGURATION
- **Models Required**: ReorderPolicy, ItemMaster, Location
- **Reference Masters**: Company, UOM, Vendor
- **Comments**: Set reorder points per item-location. Defines when to reorder.

#### **5.7.2_Safety_Stock_Levels_bbp.md**
- **Type**: CONFIGURATION
- **Models Required**: ReorderPolicy, ItemMaster, Location
- **Reference Masters**: Company, UOM
- **Comments**: Configure safety stock. Buffer stock to prevent stockouts.

#### **5.7.3_Min_Max_Planning_bbp.md**
- **Type**: CONFIGURATION
- **Models Required**: ReorderPolicy, ItemMaster, Location
- **Reference Masters**: Company, UOM
- **Comments**: Min-max inventory planning. Sets min and max stock levels.

#### **5.7.4_Reorder_Policies_bbp.md**
- **Type**: RULE DEFINITION
- **Models Required**: ReorderPolicy, ItemMaster, Vendor
- **Reference Masters**: Location, UOM, Company
- **Comments**: Reorder policy rules. Defines reorder quantity, lead time, preferred vendor.

#### **5.7.5_Demand_Forecasting_Phase2_bbp.md** ⭐ PHASE 2
- **Type**: OPERATIONAL MODULE
- **Models Required**: DemandForecast, SalesHistory
- **Reference Masters**: ItemMaster, Location, Company
- **Comments**: PHASE 2 - Demand forecasting. Requires advanced analytics. Predicts future demand.

#### **5.7.6_Replenishment_Suggestions_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: ReorderPolicy, Inventory, PurchaseRequisition
- **Reference Masters**: ItemMaster, Location, Vendor
- **Comments**: Auto-suggest replenishment. Compares stock with reorder point, suggests PR creation.

---

### **5.8 BATCH & SERIAL TRACKING**

#### **5.8.1_Batch_Management_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Batch, Inventory, ItemMaster
- **Reference Masters**: Location, Company
- **Comments**: Batch tracking. Manages batch numbers, expiry dates, manufacturing dates.

#### **5.8.2_Serial_Number_Tracking_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: SerialNumber, Inventory, ItemMaster
- **Reference Masters**: Location, Company
- **Comments**: Serial number tracking. One-to-one tracking for high-value items.

#### **5.8.3_Expiry_Management_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Batch, Inventory, ItemMaster
- **Reference Masters**: Location, Company
- **Comments**: Expiry alerts. Shows batches nearing expiry. Uses Batch.expiry_date.

#### **5.8.4_Batch_Traceability_bbp.md**
- **Type**: OPERATIONAL MODULE
- **Models Required**: Batch, StockMovement, ItemMaster
- **Reference Masters**: Location, Company
- **Comments**: Batch movement history. Traces batch from receipt to sale.

#### **5.8.5_Recall_Management_Phase2_bbp.md** ⭐ PHASE 2
- **Type**: TRANSACTION
- **Models Required**: ProductRecall, Batch, Customer
- **Reference Masters**: ItemMaster, Location, SalesOrder
- **Comments**: PHASE 2 - Product recall workflow. Identifies affected batches and customers.

---

### **5.9 INVENTORY REPORTS**

#### **5.9.1_Stock_Summary_Report_bbp.md**
- **Type**: REPORT
- **Models Required**: Inventory, ItemMaster, Location
- **Reference Masters**: Company, UOM, Category
- **Comments**: Current stock export. Same as 5.2.1 with export.

#### **5.9.2_Movement_Report_bbp.md**
- **Type**: REPORT
- **Models Required**: StockMovement, ItemMaster, Location
- **Reference Masters**: MovementType, User, Company
- **Comments**: Movement history export. Same as 5.3.1 with export.

#### **5.9.3_Valuation_Report_bbp.md**
- **Type**: REPORT
- **Models Required**: Inventory, ItemMaster, ValuationMethod
- **Reference Masters**: Location, UOM, Company
- **Comments**: Stock value export. Same as 5.6.2 with export.

#### **5.9.4_Aging_Report_bbp.md**
- **Type**: REPORT
- **Models Required**: Inventory, StockMovement, ItemMaster
- **Reference Masters**: Location, UOM, Company
- **Comments**: Stock age export. Same as 5.2.7 with export.

#### **5.9.5_ABC_Analysis_bbp.md**
- **Type**: REPORT
- **Models Required**: Inventory, ItemMaster, SalesHistory
- **Reference Masters**: Location, Company
- **Comments**: ABC classification. A=high value, B=medium, C=low. Based on sales value.

#### **5.9.6_Velocity_Analysis_bbp.md**
- **Type**: REPORT
- **Models Required**: StockMovement, ItemMaster, SalesHistory
- **Reference Masters**: Location, Company
- **Comments**: Fast/slow moving analysis. Based on movement frequency.

#### **5.9.7_Dead_Stock_Report_bbp.md**
- **Type**: REPORT
- **Models Required**: Inventory, StockMovement, ItemMaster
- **Reference Masters**: Location, Company
- **Comments**: No movement items. Filter: no StockMovement in last X days.

---

### **5.10 CONFIGURATION**

#### **5.10.1_Movement_Types_bbp.md**
- **Type**: MASTER
- **Models Required**: MovementType
- **Reference Masters**: Company
- **Comments**: Master data for movement types (GRN, ISSUE, TRANSFER, ADJUSTMENT, etc.).

#### **5.10.2_Adjustment_Reason_Codes_bbp.md**
- **Type**: MASTER
- **Models Required**: AdjustmentReason
- **Reference Masters**: Company
- **Comments**: Master data for adjustment reasons. Same as 5.4.3.

#### **5.10.3_Valuation_Methods_bbp.md**
- **Type**: CONFIGURATION
- **Models Required**: ValuationMethod, Company
- **Reference Masters**: -
- **Comments**: Configure valuation method. Same as 5.6.1.

#### **5.10.4_Inventory_Parameters_bbp.md**
- **Type**: CONFIGURATION
- **Models Required**: InventoryParameter, Company
- **Reference Masters**: -
- **Comments**: Global inventory settings (e.g., negative stock allowed, auto-reorder enabled).

#### **5.10.5_Approval_Rules_bbp.md**
- **Type**: RULE DEFINITION
- **Models Required**: ApprovalRule, User, Role
- **Reference Masters**: Company
- **Comments**: Approval rules for adjustments, transfers, stock takes. Threshold-based.

---

## 📊 **MODEL SUMMARY - DJANGO MODEL CREATION GUIDE**

### **CORE MODELS (Must create first)**

1. **Inventory** - Stock on hand records
   - Fields: item, location, company, quantity, batch, serial_number, last_movement_date
   - Indexes: (item, location, company), (company, location)

2. **ItemMaster** - Product/SKU master (Already exists in domain.company)
   - Use existing model

3. **StockMovement** - Movement transactions
   - Fields: item, location, company, movement_type, quantity, reference_doc, batch, serial_number, user, created_at
   - Indexes: (company, created_at), (item, location)

4. **Location** - Warehouse/storage (Already exists in domain.company)
   - Use existing model

5. **Company** - Multi-tenant (Already exists in business_entities)
   - Use existing model

---

### **TRANSACTION MODELS**

6. **StockTransfer** - Internal transfers
   - Fields: company, from_location, to_location, transfer_date, status, user, notes
   - Lines: StockTransferLine (item, quantity, batch, serial_number)

7. **IntercompanyTransfer** - Inter-company transfers
   - Fields: from_company, to_company, from_location, to_location, transfer_date, status, user
   - Lines: IntercompanyTransferLine (item, quantity, batch, serial_number)

8. **StockAdjustment** - Stock adjustments
   - Fields: company, location, adjustment_date, reason, status, user, approval_status
   - Lines: StockAdjustmentLine (item, quantity, batch, serial_number)

9. **StockTake** - Physical inventory counts
   - Fields: company, location, count_date, status, user, approval_status
   - Lines: StockTakeLine (item, system_qty, counted_qty, variance, batch, serial_number)

---

### **MASTER DATA MODELS**

10. **AdjustmentReason** - Adjustment reason codes
    - Fields: company, code, name, is_active

11. **MovementType** - Movement type definitions
    - Fields: company, code, name, direction (IN/OUT), is_active

12. **Category** - Item categories (Already exists in domain.company)
    - Use existing model

13. **Batch** - Batch tracking
    - Fields: item, batch_number, manufacturing_date, expiry_date, company

14. **SerialNumber** - Serial number tracking
    - Fields: item, serial_number, status, location, company

---

### **CONFIGURATION MODELS**

15. **ReorderPolicy** - Reorder rules
    - Fields: item, location, company, reorder_point, safety_stock, min_quantity, max_quantity, reorder_quantity, lead_time_days, preferred_vendor

16. **ValuationMethod** - Costing methods
    - Fields: company, method (FIFO/LIFO/WEIGHTED_AVG), is_active

17. **InventoryParameter** - Global settings
    - Fields: company, allow_negative_stock, auto_reorder_enabled, default_valuation_method

18. **ApprovalRule** - Approval thresholds
    - Fields: company, rule_type (ADJUSTMENT/TRANSFER/STOCK_TAKE), threshold_amount, approver_role

19. **CycleCountSchedule** - Count scheduling
    - Fields: company, location, frequency (DAILY/WEEKLY/MONTHLY), items_to_count, last_count_date

---

### **INTEGRATION MODELS (External - READ-ONLY)**

20. **GoodsReceipt** - From Procurement (domain.procurement)
21. **PurchaseOrder** - From Procurement (domain.procurement)
22. **SalesOrder** - From Sales (domain.sales)
23. **Invoice** - From Sales (domain.sales)
24. **PurchaseRequisition** - To Procurement (domain.procurement)
25. **Vendor** - From Procurement (domain.company)

---

### **PHASE 2 MODELS (Future)**

26. **InventoryRevaluation** - Stock revaluation
    - Fields: company, revaluation_date, old_value, new_value, gl_entry, user

27. **GLEntry** - Finance integration (domain.finance)

28. **DemandForecast** - Forecasting
    - Fields: item, location, company, forecast_date, forecasted_quantity, confidence_level

29. **SalesHistory** - Historical data
    - Fields: item, location, company, sale_date, quantity, value

30. **ProductRecall** - Recall management
    - Fields: company, recall_date, reason, affected_batches, status

31. **Customer** - Customer data (domain.sales)

---

### **SUPPORTING MODELS**

32. **User** - User tracking (Already exists in auth)
33. **Role** - Access control (Already exists in auth)
34. **FiscalPeriod** - Period tracking (domain.finance)
35. **UOM** - Unit of measure (Already exists in domain.company)
36. **Brand** - Brand master (Already exists in domain.company)

---

## 🎯 **MODEL CREATION PRIORITY**

### **Phase 1A - Core Foundation (Create First)**
1. Inventory
2. StockMovement
3. MovementType (Master)

### **Phase 1B - Transactions**
4. StockTransfer + StockTransferLine
5. StockAdjustment + StockAdjustmentLine
6. AdjustmentReason (Master)

### **Phase 1C - Physical Inventory**
7. StockTake + StockTakeLine
8. CycleCountSchedule

### **Phase 1D - Batch/Serial**
9. Batch
10. SerialNumber

### **Phase 1E - Replenishment**
11. ReorderPolicy

### **Phase 1F - Configuration**
12. ValuationMethod
13. InventoryParameter
14. ApprovalRule

### **Phase 1G - Intercompany**
15. IntercompanyTransfer + IntercompanyTransferLine

### **Phase 2 - Advanced Features**
16. InventoryRevaluation
17. DemandForecast
18. ProductRecall
19. SalesHistory

---

## 📝 **DJANGO MODEL CREATION NOTES**

### **Model Location**
- Create in: `backend/domain/inventory/models.py`
- App: `domain.inventory`

### **Common Fields (All Models)**
- `company` - ForeignKey to Company (multi-tenant)
- `created_at` - Auto timestamp
- `updated_at` - Auto timestamp
- `created_by` - ForeignKey to User
- `updated_by` - ForeignKey to User

### **Naming Conventions**
- Model names: PascalCase (e.g., StockMovement)
- Field names: snake_case (e.g., movement_type)
- Table names: inventory_stockmovement

### **Indexes Required**
- All company + date fields
- All item + location combinations
- All status fields for transactions

### **Constraints**
- Unique: (company, code) for master data
- Check: quantity >= 0 (unless negative stock allowed)
- Foreign keys: ON DELETE PROTECT for masters, CASCADE for lines

---

**This guide provides all metadata needed for Django model creation!** ✅
