# Screen: Price List Master

**Sidebar Path**: Retail > Merchandising > Pricing > Price List Master  
**URL**: `/inventory/price-lists`  
**Component**: `PriceListSetup.tsx`

---

## Purpose

Manages pricing tiers for items. Price lists support:
- Date-range validity
- Customer group assignments
- Currency-specific prices
- Discount rules

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Items exist | Yes |
| Currency configured | Yes |
| User has `inventory.pricelist.create` permission | Yes |

---

## Scenarios

### SC-PRICE-001: Create Price List

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Price Lists | List loads |
| 2 | Click New | CREATE mode |
| 3 | Enter Code | "PL-RETAIL" |
| 4 | Enter Name | "Retail Price List" |
| 5 | Select Currency | INR |
| 6 | Set Valid From | Today |
| 7 | Set Valid To | End of year |
| 8 | Save | Price list created |

---

### SC-PRICE-002: Add Items to Price List

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit price list | Form loads |
| 2 | Click Items tab | Item grid |
| 3 | Add item | Item lookup |
| 4 | Enter price | ₹100.00 |
| 5 | Save | Item price added |

---

### SC-PRICE-003: Bulk Price Update

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select multiple items | Check boxes |
| 2 | Click Bulk Update | Dialog |
| 3 | Enter % increase | 10% |
| 4 | Apply | All prices +10% |

---

### SC-PRICE-004: Date Range Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Valid From | Future date |
| 2 | Valid To | Before From | 
| 3 | Save | Error: Invalid range |

---

### SC-PRICE-005: Assign to Customer Group

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit price list | Form open |
| 2 | Assignment tab | Customer groups |
| 3 | Select "VIP" | Assigned |
| 4 | Save | VIP customers use this list |

---

### SC-PRICE-006: Overlapping Price Lists

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Two lists same item | Overlapping dates |
| 2 | System behavior | Priority rules apply |

---

**Scenario Count**: 6
