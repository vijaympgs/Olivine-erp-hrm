# Screen: Tax Configuration

**Sidebar Path**: System Configuration > Tax Configuration  
**URL**: `/config/taxes`  
**Component**: `TaxConfigurationPage.tsx`

---

## Purpose

Tax Configuration manages tax setup for transactions:
- Tax codes and rates
- Tax groups
- GST configuration (CGST, SGST, IGST)
- HSN/SAC codes
- Tax exemptions
- Tax applicability rules

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `config.tax.manage` permission | Yes |
| Company with tax registration | GST enabled |

---

## Scenarios

### SC-TAX-001: View Tax Configuration

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/config/taxes` | Page loads |
| 2 | Verify tabs | Tax Codes, Tax Groups, HSN, Rules |
| 3 | Verify list | Existing tax codes |

---

### SC-TAX-002: Create Tax Code (GST)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Add Tax Code" | Create form |
| 2 | Enter Code | "GST18" |
| 3 | Enter Name | "GST 18%" |
| 4 | Enter Rate | 18 |
| 5 | Select Type | "GST" |
| 6 | Save | Tax code created |

---

### SC-TAX-003: Create CGST/SGST Components

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create parent | "GST18" at 18% |
| 2 | Add component | "CGST" at 9% |
| 3 | Add component | "SGST" at 9% |
| 4 | Verify total | Components = Parent |

---

### SC-TAX-004: Create IGST Tax

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create tax code | "IGST18" |
| 2 | Set rate | 18% |
| 3 | Set type | "IGST" |
| 4 | Link to GST | Alternative for interstate |
| 5 | Save | IGST configured |

---

### SC-TAX-005: Create Tax Group

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Go to Tax Groups tab | Group list |
| 2 | Click "Add Group" | Create form |
| 3 | Enter Name | "Standard GST 18%" |
| 4 | Add tax codes | CGST9, SGST9 |
| 5 | Save | Group created |

---

### SC-TAX-006: Assign HSN Code

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Go to HSN tab | HSN list |
| 2 | Click "Add HSN" | Create form |
| 3 | Enter HSN Code | "6204" |
| 4 | Enter Description | "Women's suits" |
| 5 | Assign Tax Rate | 12% |
| 6 | Save | HSN configured |

---

### SC-TAX-007: SAC Code for Services

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Add SAC Code | Service code |
| 2 | Enter Code | "998311" |
| 3 | Enter Description | "Management consulting" |
| 4 | Assign Rate | 18% |
| 5 | Save | SAC configured |

---

### SC-TAX-008: Tax Exemption

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create exempt tax | "EXEMPT" |
| 2 | Set rate | 0% |
| 3 | Set type | "Exempt" |
| 4 | Save | Used for exempted items |

---

### SC-TAX-009: Zero-rated Tax

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create zero-rated | "ZERO-RATED" |
| 2 | Set rate | 0% |
| 3 | Set type | "Zero-rated" |
| 4 | Save | For exports, etc. |

---

### SC-TAX-010: Edit Tax Rate

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select tax code | Existing |
| 2 | Click Edit | Edit mode |
| 3 | Change rate | 12% to 18% |
| 4 | Set effective date | Future date |
| 5 | Save | Rate scheduled |

---

### SC-TAX-011: Tax Rate History

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select tax code | With history |
| 2 | Click History | Rate history |
| 3 | Verify | Date, Old rate, New rate |

---

### SC-TAX-012: Tax Applicability Rule

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Go to Rules tab | Rule list |
| 2 | Create rule | Tax logic |
| 3 | Set conditions | State, Category, etc. |
| 4 | Set tax group | Apply when matches |
| 5 | Save | Rule active |

---

### SC-TAX-013: Interstate vs Intrastate

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Configure rule | Same state = CGST+SGST |
| 2 | Configure rule | Different state = IGST |
| 3 | Test | Transaction switches |

---

### SC-TAX-014: Deactivate Tax Code

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select tax code | Not actively used |
| 2 | Click Deactivate | Confirmation |
| 3 | Confirm | Status: Inactive |

---

### SC-TAX-015: Tax Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter negative rate | -5% |
| 2 | Save | Error: Invalid rate |
| 3 | Enter rate > 100 | 150% |
| 4 | Save | Warning or error |

---

### SC-TAX-016: Default Tax Assignment

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Set default tax | For new items |
| 2 | Create new item | Item Master |
| 3 | Verify | Default tax applied |

---

### SC-TAX-017: Compound Tax

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create compound | Tax on tax |
| 2 | Set base tax | First tax |
| 3 | Set compound | Calculated on base+first |
| 4 | Save | Compound configured |

---

### SC-TAX-018: Inclusive vs Exclusive

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Configure tax | Inclusive mode |
| 2 | Enter price | 118 |
| 3 | Verify | Base = 100, Tax = 18 |
| 4 | Switch to exclusive | |
| 5 | Enter price | 100 |
| 6 | Verify | Total = 118 |

---

**Scenario Count**: 18  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
