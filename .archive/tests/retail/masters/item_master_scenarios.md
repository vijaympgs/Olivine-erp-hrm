# Screen: Item Master

**Sidebar Path**: Retail > Merchandising > Product Catalog > Item Master  
**URL**: `/inventory/item-master`  
**Component**: `ItemMasterSetup.tsx`  
**Status**: GOLD STANDARD Reference Implementation

---

## Purpose

The Item Master is the central repository for all product/SKU definitions in Olivine Retail. It serves as the source of truth for:
- Product identification (code, name, barcode)
- Categorization and classification
- Pricing (cost, selling price, MRP)
- Inventory tracking attributes (batch, serial, weighted)
- Attribute assignments via templates

Per BBP evidence: This follows the Unified Container Pattern with List + Form in same component.

---

## Preconditions

| Prerequisite | Dependency Chain | Required |
|--------------|------------------|----------|
| Company Setup | Level 0 | Yes |
| At least 1 UOM | Level 1 - `/inventory/uoms` | Yes |
| At least 1 Category | Level 1 - `/inventory/categories` | Yes |
| Attribute Template (optional) | Level 2 - `/inventory/attribute-templates` | No |
| User Permission | `inventory.item.create`, `inventory.item.edit`, `inventory.item.delete` | Yes |

---

## Scenarios

### SC-ITEM-001: Create Simple Item (Happy Path)

**Type**: Happy Path  
**Priority**: Critical  
**Preconditions**: UOM "PCS" exists, Category "General" exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to Item Master | URL: `/inventory/item-master` | List view loads with existing items |
| 2 | Click New button | `[data-testid="btn-new"]` | Form switches to CREATE mode, fields empty |
| 3 | Enter Item Code | `[data-testid="item-code"]` = "TEST-001" | Field accepts alphanumeric, max 50 chars |
| 4 | Enter Item Name | `[data-testid="item-name"]` = "Test Item One" | Field accepts text, max 200 chars |
| 5 | Select Category | `[data-testid="category-lookup"]` → "General" | Category lookup opens, selection persists |
| 6 | Select Base UOM | `[data-testid="uom-lookup"]` → "PCS" | UOM dropdown shows available options |
| 7 | Enter Selling Price | `[data-testid="selling-price"]` = "100.00" | Numeric field, 2 decimal places |
| 8 | Click Save | `[data-testid="btn-save"]` | API POST `/api/inventory/items/` returns 201 |
| 9 | Verify success dialog | `.success-dialog` visible | "Item saved successfully" with Stay/List options |
| 10 | Click "Go to List" | `[data-testid="btn-go-list"]` | Returns to list view, new item visible |

**Postconditions**: Item "TEST-001" exists in database with status Active

---

### SC-ITEM-002: Create Item with All Tabs (Complex Flow)

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: UOM, Category, Attribute Template exist

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | `[data-testid="btn-new"]` | CREATE mode |
| 2 | Fill General tab | Code, Name, Category, UOM | Fields populated |
| 3 | Click Pricing tab | `[data-tab="pricing"]` | Tab switches, pricing fields visible |
| 4 | Enter Cost Price | `[data-testid="cost-price"]` = "80.00" | Value accepted |
| 5 | Enter MRP | `[data-testid="mrp"]` = "120.00" | Value >= Selling Price |
| 6 | Click Inventory tab | `[data-tab="inventory"]` | Inventory settings visible |
| 7 | Set Reorder Level | `[data-testid="reorder-level"]` = "10" | Numeric field |
| 8 | Set Reorder Qty | `[data-testid="reorder-qty"]` = "50" | Numeric field |
| 9 | Click Tracking tab | `[data-tab="tracking"]` | Tracking options visible |
| 10 | Enable Batch Tracking | Toggle `is_batch_tracked` = ON | Toggle switches |
| 11 | Click Attributes tab | `[data-tab="attributes"]` | Attribute template selector visible |
| 12 | Select Template | Choose template → assign values | Attributes linked |
| 13 | Click Save | `[data-testid="btn-save"]` | All tabs data persisted |

**Postconditions**: Item with complete pricing, inventory, tracking, and attributes saved

---

### SC-ITEM-003: Edit Existing Item

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: Item "TEST-001" exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to list | `/inventory/item-master` | List loads |
| 2 | Search for item | Search box = "TEST-001" | Filtered results show item |
| 3 | Click row to select | Click on "TEST-001" row | Row highlighted, toolbar shows Edit |
| 4 | Click Edit | `[data-testid="btn-edit"]` | Form loads in EDIT mode with data |
| 5 | Modify Name | Change to "Test Item Updated" | Field editable |
| 6 | Click Save | `[data-testid="btn-save"]` | API PUT returns 200 |
| 7 | Verify in list | Check list | Updated name visible |

**Postconditions**: Item name changed to "Test Item Updated"

---

### SC-ITEM-004: Duplicate Code Validation (Edge Case)

**Type**: Validation  
**Priority**: High  
**Preconditions**: Item "TEST-001" exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | `[data-testid="btn-new"]` | CREATE mode |
| 2 | Enter existing code | `[data-testid="item-code"]` = "TEST-001" | Field accepts input |
| 3 | Fill required fields | Name, Category, UOM | Minimum data |
| 4 | Click Save | `[data-testid="btn-save"]` | API returns 400 |
| 5 | Verify error | Error toast visible | "Item code already exists" |
| 6 | Verify form state | Form remains in CREATE mode | Data not lost, can correct |

**Postconditions**: No duplicate item created, form allows correction

---

### SC-ITEM-005: Required Field Validation

**Type**: Validation  
**Priority**: High  
**Preconditions**: None

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | `[data-testid="btn-new"]` | CREATE mode |
| 2 | Leave Code empty | Skip item code | - |
| 3 | Leave Name empty | Skip item name | - |
| 4 | Click Save | `[data-testid="btn-save"]` | Validation prevents submit |
| 5 | Verify field errors | Required fields show red border | "This field is required" |

**Postconditions**: Form submission blocked, user guided to fix errors

---

### SC-ITEM-006: Delete Item (Soft Delete)

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: Item "TEST-DELETE" exists, not used in transactions

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Search for item | "TEST-DELETE" | Item found |
| 2 | Select row | Click row | Selected |
| 3 | Click Delete | `[data-testid="btn-delete"]` | Confirmation dialog |
| 4 | Confirm deletion | Click "Yes, Delete" | API DELETE returns 200 |
| 5 | Verify removal | Check list | Item not in active list |

**Postconditions**: Item soft-deleted (is_active = false)

---

### SC-ITEM-007: Delete Item with Transactions (Blocked)

**Type**: Edge Case  
**Priority**: Medium  
**Preconditions**: Item used in at least 1 POS transaction or PO

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Select item with transactions | - | Selected |
| 2 | Click Delete | `[data-testid="btn-delete"]` | Confirmation dialog |
| 3 | Confirm | Click "Yes" | API returns 400 |
| 4 | Verify error | Error toast | "Cannot delete: Item has transactions" |

**Postconditions**: Item not deleted, referential integrity preserved

---

### SC-ITEM-008: Search and Filter

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: Multiple items exist

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Enter search term | Search = "Test" | Filtered to matching items |
| 2 | Clear search | Clear button | Full list restored |
| 3 | Open filter panel | Click filter icon | Filter sidebar opens |
| 4 | Filter by Category | Select "Electronics" | Only electronics items shown |
| 5 | Filter by Status | Select "Active" | Only active items shown |
| 6 | Reset filters | Click "Reset" | All filters cleared |

**Postconditions**: Filtering does not modify data, only view

---

### SC-ITEM-009: Cancel Create (Discard Changes)

**Type**: Edge Case  
**Priority**: Low  
**Preconditions**: None

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | `[data-testid="btn-new"]` | CREATE mode |
| 2 | Enter some data | Fill code and name | Form dirty |
| 3 | Click Cancel | `[data-testid="btn-cancel"]` | Confirmation if dirty |
| 4 | Confirm discard | "Yes, discard" | Returns to list mode |
| 5 | Verify no save | Check list | No new item added |

**Postconditions**: Uncommitted data discarded

---

### SC-ITEM-010: UOM Conversion Setup

**Type**: Feature  
**Priority**: Medium  
**Preconditions**: Item exists with base UOM "PCS"

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Edit item | Load item form | EDIT mode |
| 2 | Click UOM Conversions tab | `[data-tab="uom-conversions"]` | Conversion grid visible |
| 3 | Add conversion | Click "Add" | New row appears |
| 4 | Select alternate UOM | Dropdown → "BOX" | UOM selected |
| 5 | Enter conversion factor | Factor = "12" | 1 BOX = 12 PCS |
| 6 | Save | Save button | Conversion persisted |

**Postconditions**: Item can be sold/purchased in PCS or BOX

---

## Data Cleanup

After test execution:
- Delete items with code prefix "TEST-"
- Restore any modified items to original state

---

**Scenario Count**: 10  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
