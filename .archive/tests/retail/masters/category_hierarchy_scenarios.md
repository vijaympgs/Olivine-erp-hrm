# Screen: Category Hierarchy

**Sidebar Path**: Retail > Inventory > Stock Management > Category Hierarchy  
**URL**: `/inventory/categories`  
**Component**: Category tree with drag-and-drop

---

## Purpose

Manages product category hierarchy. Categories are used for:
- Item classification
- Reporting and filtering
- POS navigation (Quick Keys)
- Pricing rules by category

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Company configured | Yes |
| User has `inventory.category.create` permission | Yes |

---

## Scenarios

### SC-CAT-001: Create Root Category

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Categories | Tree loads |
| 2 | Click Add Root | Form opens |
| 3 | Enter Code | "ELEC" |
| 4 | Enter Name | "Electronics" |
| 5 | Save | Root category created |

---

### SC-CAT-002: Create Sub-Category

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select parent | "Electronics" |
| 2 | Click Add Child | Form opens |
| 3 | Enter "PHONES" | Sub-category |
| 4 | Save | Nested under Electronics |

---

### SC-CAT-003: Drag and Drop Reorder

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Drag category | From one position |
| 2 | Drop to new location | Position changes |
| 3 | Hierarchy updated | New parent/order saved |

---

### SC-CAT-004: Edit Category

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click category | Selected |
| 2 | Click Edit | Form opens |
| 3 | Modify name | Updated |
| 4 | Save | Changes persisted |

---

### SC-CAT-005: Delete Empty Category

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select category | No items assigned |
| 2 | Click Delete | Confirmation |
| 3 | Confirm | Category removed |

---

### SC-CAT-006: Cannot Delete Category With Items

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Category has items | References exist |
| 2 | Attempt delete | Error |
| 3 | Message | "Category has X items" |

---

**Scenario Count**: 6
