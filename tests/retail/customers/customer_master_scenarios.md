# Screen: Customer Master

**Sidebar Path**: Retail > Customers > Customer Management > Customer Master  
**URL**: `/partners/customers`  
**Component**: `CustomerMasterSetup.tsx`  
**Status**: GOLD STANDARD Reference Implementation

---

## Purpose

The Customer Master maintains all customer records for sales and POS transactions. It supports:
- Customer identification and contact information
- Credit limits and payment terms
- Loyalty program enrollment
- Intercompany (IC) relationships for ICT
- Address management (Billing/Shipping)

Per BBP evidence: Follows Unified Container Pattern with IC fields for intercompany trade.

---

## Preconditions

| Prerequisite | Dependency Chain | Required |
|--------------|------------------|----------|
| Company Setup | Level 0 | Yes |
| Location Setup (for IC) | Level 0 | For IC only |
| User Permission | `partners.customer.create`, `partners.customer.edit` | Yes |

---

## Scenarios

### SC-CUST-001: Create Customer (Happy Path)

**Type**: Happy Path  
**Priority**: Critical  
**Preconditions**: Company configured

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to Customer Master | `/partners/customers` | List view loads |
| 2 | Click New | `[data-testid="btn-new"]` | Form in CREATE mode |
| 3 | Enter Customer Code | `[data-testid="customer-code"]` = "CUST-001" | Alphanumeric accepted |
| 4 | Enter Customer Name | `[data-testid="customer-name"]` = "John Smith" | Text field |
| 5 | Select Customer Type | Dropdown = "Retail" | Selection applied |
| 6 | Enter Email | `[data-testid="email"]` = "john@email.com" | Valid email format |
| 7 | Enter Phone | `[data-testid="phone"]` = "+91-9876543210" | Phone format |
| 8 | Click Save | `[data-testid="btn-save"]` | Success, status Active |

**Postconditions**: Customer "CUST-001" created and available for POS

---

### SC-CUST-002: Create Intercompany Customer

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: Related company exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | `[data-testid="btn-new"]` | CREATE mode |
| 2 | Fill basic info | Code, Name | Fields populated |
| 3 | Click Intercompany tab | `[data-tab="intercompany"]` | IC fields visible |
| 4 | Toggle "Is Intercompany" | ON | IC fields enabled |
| 5 | Select Related Company | Dropdown | Related company selected |
| 6 | Select Related Location | Dropdown | Location populated |
| 7 | Save | Save button | IC customer created |

**Postconditions**: Customer linked to internal company for ICT

---

### SC-CUST-003: Edit Customer

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: Customer "CUST-001" exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Search customer | "CUST-001" | Found in list |
| 2 | Click row | Select | Row highlighted |
| 3 | Click Edit | `[data-testid="btn-edit"]` | EDIT mode |
| 4 | Modify name | "John Smith Jr" | Editable |
| 5 | Save | Save button | Changes persisted |

**Postconditions**: Customer name updated

---

### SC-CUST-004: Set Credit Limit

**Type**: Feature  
**Priority**: High  
**Preconditions**: Customer exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Edit customer | EDIT mode | Form loaded |
| 2 | Click Credit tab | `[data-tab="credit"]` | Credit fields visible |
| 3 | Enable Credit | Toggle ON | Credit fields active |
| 4 | Set Credit Limit | ₹50,000 | Numeric field |
| 5 | Set Payment Terms | "Net 30" | Dropdown |
| 6 | Save | Save button | Credit settings saved |

**Postconditions**: Customer can purchase on credit up to limit

---

### SC-CUST-005: Loyalty Enrollment

**Type**: Feature  
**Priority**: Medium  
**Preconditions**: Loyalty program configured, Customer exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Edit customer | EDIT mode | Form loaded |
| 2 | Click Loyalty tab | `[data-tab="loyalty"]` | Loyalty fields |
| 3 | Enroll in program | Select program | Program assigned |
| 4 | Verify tier | Default tier | "Bronze" or entry tier |
| 5 | Save | Save button | Loyalty linked |

**Postconditions**: Customer earns points on purchases

---

### SC-CUST-006: Address Management

**Type**: Feature  
**Priority**: Medium  
**Preconditions**: Customer exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Edit customer | EDIT mode | Form loaded |
| 2 | Click Addresses tab | `[data-tab="addresses"]` | Address grid |
| 3 | Add Billing Address | Add button | Address form |
| 4 | Fill address | Street, City, State, PIN | Fields populated |
| 5 | Mark as Default | Checkbox | Default billing set |
| 6 | Add Shipping Address | Another address | Second address |
| 7 | Save | Save button | Both addresses saved |

**Postconditions**: Customer has billing and shipping addresses

---

### SC-CUST-007: Duplicate Code Validation

**Type**: Validation  
**Priority**: High  
**Preconditions**: Customer "CUST-001" exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | New button | CREATE mode |
| 2 | Enter existing code | "CUST-001" | Field accepts |
| 3 | Fill other fields | Minimum data | - |
| 4 | Save | Save button | Error: Duplicate code |

**Postconditions**: No duplicate created

---

### SC-CUST-008: Customer Groups

**Type**: Feature  
**Priority**: Medium  
**Preconditions**: Customer Groups defined

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Edit customer | EDIT mode | Form loaded |
| 2 | Select Group | Dropdown | "VIP", "Corporate" |
| 3 | Save | Save button | Group assigned |

**Postconditions**: Customer inherits group-level pricing/discounts

---

## Data Cleanup

After test execution:
- Delete test customers (prefix "TEST-")
- Reset loyalty points
- Unlink test IC relationships

---

**Scenario Count**: 8  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
