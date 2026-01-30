# Screen: Company Settings

**Sidebar Path**: System Configuration > Company Settings  
**URL**: `/config/company`  
**Component**: `CompanySettingsPage.tsx`

---

## Purpose

Company Settings manages the core organizational entity:
- Company profile and legal information
- Statutory registrations (GST, PAN, TAN, etc.)
- Contact and address details
- Logo and branding
- Business preferences
- Default settings for transactions

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `config.company.edit` permission | Yes |
| Initial setup complete | For edit |

---

## Scenarios

### SC-COMP-001: View Company Settings

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/config/company` | Page loads |
| 2 | Verify sections | Profile, Statutory, Address, Defaults |
| 3 | Verify current data | Company info displayed |

---

### SC-COMP-002: Edit Company Profile

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Edit | EDIT mode |
| 2 | Modify Company Name | "Olivine Retail Pvt Ltd" |
| 3 | Modify Legal Name | Full legal name |
| 4 | Save | Changes saved |

---

### SC-COMP-003: Update Statutory Information

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Statutory section | Expand |
| 2 | Enter GST Number | Valid GSTIN format |
| 3 | Enter PAN | 10-char alphanumeric |
| 4 | Enter TAN | If applicable |
| 5 | Enter CIN | Company Identification |
| 6 | Save | Validated and saved |

---

### SC-COMP-004: GST Number Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter invalid GSTIN | Wrong format |
| 2 | Save | Validation error |
| 3 | Verify message | "Invalid GSTIN format" |
| 4 | Enter valid GSTIN | 15-char pattern |
| 5 | Save | Success |

---

### SC-COMP-005: Upload Company Logo

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Logo section | Image uploader |
| 2 | Select file | PNG/JPG |
| 3 | Verify preview | Logo shown |
| 4 | Save | Logo persisted |
| 5 | Check reports | Logo appears |

---

### SC-COMP-006: Remove Company Logo

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Remove Logo | Remove icon |
| 2 | Confirm | Logo cleared |
| 3 | Save | Default placeholder |

---

### SC-COMP-007: Update Address

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Address section | Expand |
| 2 | Enter Address Line 1 | Street address |
| 3 | Enter City | City name |
| 4 | Enter State | State/Province |
| 5 | Enter PIN/Zip | Postal code |
| 6 | Select Country | Dropdown |
| 7 | Save | Address saved |

---

### SC-COMP-008: Configure Business Defaults

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Defaults section | Expand |
| 2 | Select Default Currency | INR |
| 3 | Select Default UOM | PCS |
| 4 | Set Fiscal Year Start | April |
| 5 | Save | Defaults applied |

---

### SC-COMP-009: Configure Contact Information

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Contact section | Expand |
| 2 | Enter Phone | Primary phone |
| 3 | Enter Email | Company email |
| 4 | Enter Website | Company URL |
| 5 | Save | Contact info saved |

---

### SC-COMP-010: Email Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter invalid email | "notanemail" |
| 2 | Save | Validation error |
| 3 | Enter valid email | "info@company.com" |
| 4 | Save | Success |

---

### SC-COMP-011: Multi-Company View (Enterprise)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | If multi-company enabled | Company selector |
| 2 | Switch company | Dropdown |
| 3 | View different company | Settings change |

---

### SC-COMP-012: Required Field Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Clear Company Name | Empty |
| 2 | Save | Validation error |
| 3 | Verify | "Company name required" |

---

**Scenario Count**: 12  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
