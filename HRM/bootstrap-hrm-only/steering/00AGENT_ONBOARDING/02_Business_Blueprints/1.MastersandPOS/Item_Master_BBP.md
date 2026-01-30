# Item Master --- Business Blueprint (Enhanced Extract)

**Source:** RetailBBP --- Unified Business Blueprint\
**Section:** 2.5 Merchandise Setup → Item Master\
**Version:** Draft Enhancement\
**Authority:** Viji (Final)

> This document is a focused, execution-ready extraction of the Item
> Master BBP, enhanced for clarity, implementation fidelity, and future
> extensibility.\
> No fields have been invented. No scope has been altered. Structure is
> improved only for execution usefulness.

------------------------------------------------------------------------

## 1. Business Purpose

The Item Master defines all products and SKUs using a **parent
(style/product) + variant** architecture.\
It acts as the **single canonical source** for:

-   POS billing
-   Inventory
-   Procurement
-   Pricing
-   Reporting
-   Promotions
-   Analytics

It integrates tightly with: - Product Attribute Templates - Attributes
and Values - Units of Measure (UOM) - Variant-specific pricing and
barcodes

This is a **core complex master** and must never be implemented as a
partial or skeleton screen.

------------------------------------------------------------------------

## 2. Conceptual Structure

    Item (Parent)
       └── Variants (SKUs)
             ├── Variant Attributes (Color, Size, etc.)
             └── Variant UOMs (Barcode, Price, Sales unit)

-   Parent Item defines identity and classification.
-   Variants represent sellable SKUs.
-   Each SKU can have multiple UOM mappings.
-   Attribute Template controls what attributes and variants are
    allowed.

------------------------------------------------------------------------

## 3. Data Model

### 3.1 Item (Parent)

  Field                   Type          Required   Description
  ----------------------- ------------- ---------- ------------------------------
  id                      UUID          Yes        Primary key
  company_id              FK            Yes        Company scope
  item_code               String(50)    Yes        Unique style/product code
  item_name               String(200)   Yes        Full name
  short_name              String(100)   No         POS-friendly name
  item_type               Enum          Yes        STOCKED, SERVICE, KIT, GIFT
  attribute_template_id   FK            Yes        Product Attribute Template
  category_id             FK            No         Merchandise hierarchy
  brand_id                FK            No         Brand
  stock_uom_id            FK            Yes        Base stock UOM
  tax_class_id            FK            No         Tax logic (future)
  is_serialized           Boolean       No         Serial tracking
  is_lot_tracked          Boolean       No         Batch/lot tracking
  status                  Enum          Yes        DRAFT, ACTIVE, BLOCKED, etc.

------------------------------------------------------------------------

### 3.2 Item Variant (SKU)

  Field                Type          Required   Description
  -------------------- ------------- ---------- ------------------------
  id                   UUID          Yes        Primary key
  item_id              FK            Yes        Parent link
  sku_code             String(80)    Yes        Unique SKU
  variant_name         String(200)   Yes        e.g. Red / M
  is_default_variant   Boolean       No         Default for simple use
  sales_uom_id         FK            Yes        Default sales UOM
  purchase_uom_id      FK            No         Default PO UOM
  stock_uom_id         FK            Yes        Usually same as parent
  is_active            Boolean       Yes        Active flag

------------------------------------------------------------------------

### 3.3 Variant Attributes

  Field                Type   Required   Description
  -------------------- ------ ---------- -------------------------------
  id                   UUID   Yes        Primary key
  item_variant_id      FK     Yes        SKU
  attribute_id         FK     Yes        Attribute (Color, Size, etc.)
  attribute_value_id   FK     Yes        Selected value

------------------------------------------------------------------------

### 3.4 Variant UOM / Barcode / Price

  Field              Type      Required   Description
  ------------------ --------- ---------- -------------------
  id                 UUID      Yes        Primary key
  item_variant_id    FK        Yes        SKU
  uom_id             FK        Yes        Unit of measure
  is_default_sales   Boolean   No         Default POS UOM
  barcode            String    No         Barcode
  retail_price       Decimal   No         Seed/base price
  status             Enum      Yes        Active / Inactive

------------------------------------------------------------------------

## 4. UI / UX Specification

### Screen Layout

-   **List Screen:** Parent Item listing only
-   **Detail Screen:** Tabbed layout
    -   General
    -   Variants
    -   UOM / Barcodes

### General Tab

Captures parent-level fields: - Identity: item_code, item_name,
short_name - Classification: category, brand, item_type - Structure:
attribute_template - Logistics: stock_uom, serialization, lot tracking -
Status

### Variants Tab

-   Grid of all SKUs generated or manually added
-   Ability to:
    -   Auto-generate variants from template dimensions
    -   Edit SKU code
    -   Set default variant
    -   Activate/deactivate SKUs

### UOM / Barcode Tab

-   SKU-specific UOM mappings
-   Each SKU must have at least one Stock UOM mapping
-   Optional barcodes and base retail price per UOM

------------------------------------------------------------------------

## 5. Validation Rules

-   item_code must be unique per company
-   sku_code must be unique per company
-   Attribute template rules must be enforced (required attributes
    present)
-   Each active SKU must:
    -   Have at least one UOM mapping
    -   Have valid attribute assignments
-   Cannot activate an item if:
    -   No valid SKU exists
    -   Or SKU violates template rules

------------------------------------------------------------------------

## 6. Lifecycle & Status Model

Item lifecycle:

    DRAFT → ACTIVE → BLOCKED → DISCONTINUED → ARCHIVED

-   DRAFT: Editable, not usable in transactions
-   ACTIVE: Fully usable across modules
-   BLOCKED: Temporarily prevented from usage
-   DISCONTINUED: No new usage, history retained
-   ARCHIVED: Hidden from operations, retained for audit

Variants inherit operational usability from parent.

------------------------------------------------------------------------

## 7. Module Metadata

``` yaml
module_type: master
complexity: complex
template_ref: _mst_03

depends_on:
  - Company
  - Product Attribute Template
  - Attributes
  - Attribute Values
  - Units of Measure

used_by:
  - POS
  - Pricing
  - Inventory
  - Procurement
  - Reporting
```

------------------------------------------------------------------------

## 8. Implementation Guidance (Non-Functional)

These are execution expectations derived from complexity, not new
requirements:

-   Must use complex master template (\_mst_03)
-   Must support tabbed UI layout
-   Must handle high data density
-   Must not be implemented as modal-only UI
-   Must preserve full parity if refactoring existing UI
-   Must never ship as skeleton or partial form

------------------------------------------------------------------------

**Status:** Draft Enhanced Extract\
**Scope:** Item Master only\
**Authority:** Viji (Final)
