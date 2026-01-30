# 7. Inventory – Functional Specification (FS)

---

## 7.1 Stock on Hand – Overview (Read Model)

### 7.1.1 Purpose
Provide a consolidated, real-time view of inventory availability derived from stock movements.

---

### 7.1.2 Data Source
- Derived from: `stock_movement`
- No direct write operations
- Read-only projection

---

### 7.1.3 Data Fields (Inventory Balance View)

| Field Name | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| item_id | UUID | Y | Reference to Item Master |
| sku | String | Y | Item SKU |
| item_name | String | Y | Item name |
| location_id | UUID | Y | Store / Warehouse |
| on_hand_qty | Decimal(12,3) | Y | Total physical stock |
| reserved_qty | Decimal(12,3) | Y | Reserved stock |
| available_qty | Decimal(12,3) | Y | Derived: on_hand − reserved |
| last_movement_ref | String | N | Last stock movement reference |
| last_updated_at | Timestamp | Y | Last recalculation time |

---

### 7.1.4 UI Behavior
- Grid view
- Sorting & filtering
- Drill-down enabled (to By Location, Stock Flow)

---

### 7.1.5 Validation Rules
- available_qty ≥ 0
- No negative on_hand_qty
- No inline edit allowed

---

## 7.2 Stock on Hand – By Location

### 7.2.1 Purpose
Provide item-wise stock visibility at each location / sub-location.

---

### 7.2.2 Data Fields

| Field Name | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| item_id | UUID | Y | Item reference |
| location_id | UUID | Y | Warehouse / Store |
| bin_id | UUID | N | Bin / Shelf |
| on_hand_qty | Decimal(12,3) | Y | Quantity at location |
| reserved_qty | Decimal(12,3) | Y | Reserved at location |
| available_qty | Decimal(12,3) | Y | Derived |

---

### 7.2.3 Validation Rules
- Location must be active
- Bin must belong to location

---

## 7.3 Low Stock

### 7.3.1 Purpose
Identify replenishment needs and feed Procurement (PR).

---

### 7.3.2 Data Model – Reorder Policy

| Field Name | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| policy_id | UUID | Y | Primary key |
| item_id | UUID | Y | Item |
| location_id | UUID | Y | Location |
| min_qty | Decimal(12,3) | Y | Minimum threshold |
| reorder_qty | Decimal(12,3) | Y | Suggested reorder qty |
| active | Boolean | Y | Policy active flag |

---

### 7.3.3 System Behavior
- Evaluated periodically or on stock update
- Generates PR suggestion only

---

### 7.3.4 Validation Rules
- min_qty ≥ 0
- reorder_qty > 0

---

## 7.4 Stock Flow (Inventory Ledger)

### 7.4.1 Purpose
Maintain a complete, immutable audit trail of inventory movements.

---

### 7.4.2 Data Model – Stock Movement

| Field Name | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| movement_id | UUID | Y | Primary key |
| item_id | UUID | Y | Item |
| qty | Decimal(12,3) | Y | +ve or −ve quantity |
| from_location_id | UUID | N | Source location |
| to_location_id | UUID | N | Destination location |
| movement_type | Enum | Y | GRN, SALE, TRANSFER, ADJUSTMENT |
| reference_type | Enum | Y | GRN, Fulfillment, Transfer |
| reference_id | UUID | Y | Business document |
| posted_at | Timestamp | Y | Posting time |
| created_by | UUID | Y | System / User |

---

### 7.4.3 Validation Rules
- reference_id must exist
- movement_type must match reference_type
- No update/delete after posting

---

## 7.5 Internal Transfers

### 7.5.1 Purpose
Move stock between internal locations within the same legal entity.

---

### 7.5.2 Data Model – Transfer Header

| Field Name | Type | Mandatory |
|-----------|------|-----------|
| transfer_id | UUID | Y |
| source_location_id | UUID | Y |
| destination_location_id | UUID | Y |
| status | Enum (Draft, Approved, Posted) | Y |
| created_at | Timestamp | Y |

---

### 7.5.3 Data Model – Transfer Line

| Field Name | Type | Mandatory |
|-----------|------|-----------|
| transfer_line_id | UUID | Y |
| transfer_id | UUID | Y |
| item_id | UUID | Y |
| qty | Decimal(12,3) | Y |

---

### 7.5.4 Posting Logic
- Creates OUT movement (source)
- Creates IN movement (destination)

---

## 7.6 Intercompany Transfers

### 7.6.1 Purpose
Move stock across legal entities with audit and valuation integrity.

---

### 7.6.2 Data Model

| Field Name | Type | Mandatory |
|-----------|------|-----------|
| ic_transfer_id | UUID | Y |
| source_entity_id | UUID | Y |
| target_entity_id | UUID | Y |
| status | Enum | Y |
| in_transit_flag | Boolean | Y |

---

### 7.6.3 Workflow
Initiated → In Transit → Received → Posted

---

## 7.7 Stock Take (Including Cycle Count)

### 7.7.1 Purpose
Reconcile **system-recorded inventory** with **physical inventory counts** to ensure accuracy, audit compliance, and financial integrity.

This section covers:
- **Full Stock Take** (periodic, complete)
- **Cycle Count** (continuous, selective)

Cycle Count is implemented as a **type of Stock Take**, not a separate module.

---

### 7.7.2 Stock Take Types

| Type Code | Description |
|---------|-------------|
| FULL | Complete physical count for a location |
| CYCLE | Partial, rule-based periodic count |

Both types follow the **same workflow, validation, and posting logic**.

---

### 7.7.3 Data Model – Stock Take Header

| Field Name | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| stock_take_id | UUID | Y | Primary key |
| location_id | UUID | Y | Store / Warehouse |
| stock_take_type | Enum (FULL, CYCLE) | Y | Type of stock take |
| snapshot_datetime | Timestamp | Y | System quantity snapshot time |
| status | Enum (Planned, Counted, Reviewed, Posted) | Y | Workflow status |
| auto_generated | Boolean | Y | TRUE for cycle counts |
| cycle_code | String | N | ABC / Fast-Moving / High-Value |
| count_window_start | Date | N | Allowed count start |
| count_window_end | Date | N | Allowed count end |
| created_by | UUID | Y | User / system |
| created_at | Timestamp | Y | Creation time |

---

### 7.7.4 Data Model – Stock Take Line

| Field Name | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| stock_take_line_id | UUID | Y | Primary key |
| stock_take_id | UUID | Y | Header reference |
| item_id | UUID | Y | Item |
| system_qty | Decimal(12,3) | Y | Quantity at snapshot |
| physical_qty | Decimal(12,3) | Y | Counted quantity |
| variance_qty | Decimal(12,3) | Y | physical − system |
| variance_reason | Enum | N | Optional explanation |

---

### 7.7.5 Item Selection Logic

#### FULL Stock Take
- All active items for the selected location
- Item list frozen at snapshot time

#### CYCLE Count
- Item list generated automatically based on rules:
  - ABC classification
  - High-value items
  - Fast-moving items
  - Exception-based triggers
- auto_generated = TRUE

---

### 7.7.6 UI / UX Requirements

#### Header
- Location selector
- Stock Take Type selector (FULL / CYCLE)
- Snapshot date/time (read-only after creation)
- Status indicator

#### Count Entry
- Grid with:
  - Item
  - System Qty (read-only)
  - Physical Qty (editable)
  - Variance (auto-calculated)
- Highlight significant variances

#### Review & Approval
- Read-only variance view
- Approver comments
- Post action

---

### 7.7.7 Validation Rules

- Snapshot quantities must not change after creation
- physical_qty ≥ 0
- Variance calculation is system-controlled
- No edits allowed after status = Posted
- Cycle Count cannot bypass approval

---

### 7.7.8 Workflow



## 7.8 Adjustments

### 7.8.1 Purpose
Handle inventory exceptions (damage, loss, correction).

---

### 7.8.2 Data Model – Stock Adjustment

| Field Name | Type | Mandatory |
|-----------|------|-----------|
| adjustment_id | UUID | Y |
| item_id | UUID | Y |
| location_id | UUID | Y |
| qty_delta | Decimal(12,3) | Y |
| reason_code | Enum | Y |
| approved_by | UUID | Y |
| status | Enum | Y |

---

### 7.8.3 Posting Logic
- Requires approval
- Creates stock movement entry
