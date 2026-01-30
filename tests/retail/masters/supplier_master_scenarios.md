# Screen: Supplier Master

**Sidebar Path**: Retail > Procurement > Vendor Management > Supplier Master  
**URL**: `/partners/suppliers`  
**Component**: `SupplierMasterSetup.tsx`  
**Status**: GOLD STANDARD Reference Implementation

---

## Purpose

The Supplier Master maintains all vendor/supplier records for procurement. It supports:
- Basic supplier information (code, name, contact)
- Payment terms and bank details
- Intercompany (IC) relationships for ICT
- Address management
- Compliance tracking

Per BBP evidence: Follows Unified Container Pattern with IC fields for intercompany trade.

---

## Preconditions

| Prerequisite | Dependency Chain | Required |
|--------------|------------------|----------|
| Company Setup | Level 0 | Yes |
| Location Setup (for IC) | Level 0 | For IC only |
| User Permission | `partners.supplier.create`, `partners.supplier.edit` | Yes |

---

## Scenarios

### SC-SUP-001: Create Supplier (Happy Path)

**Type**: Happy Path  
**Priority**: Critical  
**Preconditions**: Company configured

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Navigate to Supplier Master | `/partners/suppliers` | List view loads |
| 2 | Click New | `[data-testid="btn-new"]` | Form in CREATE mode |
| 3 | Enter Supplier Code | `[data-testid="supplier-code"]` = "SUP-001" | Alphanumeric accepted |
| 4 | Enter Supplier Name | `[data-testid="supplier-name"]` = "ABC Supplies Ltd" | Text field |
| 5 | Select Payment Terms | Dropdown = "Net 30" | Selection applied |
| 6 | Enter Contact Email | `[data-testid="email"]` = "abc@supplier.com" | Valid email format |
| 7 | Enter Phone | `[data-testid="phone"]` = "+91-9876543210" | Phone format |
| 8 | Click Save | `[data-testid="btn-save"]` | Success, status Active |

**Postconditions**: Supplier "SUP-001" created and available for PO

---

### SC-SUP-002: Create Intercompany Supplier

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: Related company exists (e.g., Sister Company)

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | `[data-testid="btn-new"]` | CREATE mode |
| 2 | Fill basic info | Code, Name | Fields populated |
| 3 | Click Intercompany tab | `[data-tab="intercompany"]` | IC fields visible |
| 4 | Toggle "Is Intercompany" | ON | IC fields enabled |
| 5 | Select Related Company | Dropdown | Sister company selected |
| 6 | Select Related Location | Dropdown | Location populated |
| 7 | Save | Save button | IC supplier created |

**Postconditions**: Supplier linked to internal company for ICT

---

### SC-SUP-003: Edit Supplier

**Type**: Happy Path  
**Priority**: High  
**Preconditions**: Supplier "SUP-001" exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Search supplier | "SUP-001" | Found in list |
| 2 | Click row | Select | Row highlighted |
| 3 | Click Edit | `[data-testid="btn-edit"]` | EDIT mode |
| 4 | Modify name | "ABC Supplies Updated" | Editable |
| 5 | Save | Save button | Changes persisted |

**Postconditions**: Supplier name updated

---

### SC-SUP-004: Duplicate Code Validation

**Type**: Validation  
**Priority**: High  
**Preconditions**: Supplier "SUP-001" exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | New button | CREATE mode |
| 2 | Enter existing code | "SUP-001" | Field accepts |
| 3 | Fill other fields | Minimum data | - |
| 4 | Save | Save button | Error: Duplicate code |

**Postconditions**: No duplicate created

---

### SC-SUP-005: Required Field Validation

**Type**: Validation  
**Priority**: High  
**Preconditions**: None

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Click New | New button | CREATE mode |
| 2 | Leave Code empty | Skip | - |
| 3 | Leave Name empty | Skip | - |
| 4 | Save | Save button | Validation errors |
| 5 | Verify errors | Field indicators | Red border on required |

**Postconditions**: Submission blocked

---

### SC-SUP-006: Bank Details Tab

**Type**: Feature  
**Priority**: Medium  
**Preconditions**: Supplier exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Edit supplier | EDIT mode | Form loaded |
| 2 | Click Bank Details tab | `[data-tab="bank"]` | Bank fields visible |
| 3 | Enter Bank Name | "State Bank" | Field populated |
| 4 | Enter Account Number | "12345678901234" | Numeric |
| 5 | Enter IFSC | "SBIN0001234" | Format validated |
| 6 | Save | Save button | Bank details persisted |

**Postconditions**: Bank details available for payments

---

### SC-SUP-007: Contact Person Management

**Type**: Feature  
**Priority**: Medium  
**Preconditions**: Supplier exists

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Edit supplier | EDIT mode | Form loaded |
| 2 | Click Contacts tab | `[data-tab="contacts"]` | Contact grid |
| 3 | Add Contact | Add button | New row |
| 4 | Enter Name | "John Doe" | Text field |
| 5 | Enter Role | "Sales Manager" | Text field |
| 6 | Enter Email | "john@supplier.com" | Email format |
| 7 | Save | Save button | Contact added |

**Postconditions**: Multiple contacts can be tracked per supplier

---

### SC-SUP-008: Delete Supplier (No Transactions)

**Type**: Happy Path  
**Priority**: Medium  
**Preconditions**: Supplier with no POs

| Step | Action | Input/Selector | Expected Result |
|------|--------|----------------|-----------------|
| 1 | Select supplier | No transaction history | Selected |
| 2 | Click Delete | Delete button | Confirmation |
| 3 | Confirm | Yes | Soft deleted |

**Postconditions**: Supplier marked inactive

---

## Data Cleanup

After test execution:
- Delete test suppliers (prefix "TEST-")
- Unlink test IC relationships

---

**Scenario Count**: 8  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
