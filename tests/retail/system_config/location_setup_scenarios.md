# Screen: Location Setup

**Sidebar Path**: System Configuration > Location Setup  
**URL**: `/config/locations`  
**Component**: `LocationSetupPage.tsx`

---

## Purpose

Location Setup manages physical and logical business locations:
- Warehouses and stores
- Branch offices
- Location hierarchy
- Address and contact per location
- Location-specific settings
- Intercompany location mapping

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `config.location.manage` permission | Yes |
| Company exists | Parent entity |

---

## Scenarios

### SC-LOC-001: View Location List

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/config/locations` | List/tree loads |
| 2 | Verify columns | Code, Name, Type, Status |
| 3 | Verify hierarchy | Parent-child visible |

---

### SC-LOC-002: Create Location (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click New | CREATE mode |
| 2 | Enter Location Code | "LOC-MAIN" |
| 3 | Enter Location Name | "Main Warehouse" |
| 4 | Select Type | Warehouse/Store/Office |
| 5 | Select Parent | If hierarchy |
| 6 | Save | Location created |

---

### SC-LOC-003: Create Store Location

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click New | CREATE mode |
| 2 | Enter Code | "STORE-001" |
| 3 | Enter Name | "Downtown Store" |
| 4 | Select Type | "Store" |
| 5 | Enable POS | Toggle ON |
| 6 | Save | Store created |

---

### SC-LOC-004: Create Warehouse Location

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click New | CREATE mode |
| 2 | Enter Code | "WH-CENTRAL" |
| 3 | Enter Name | "Central Warehouse" |
| 4 | Select Type | "Warehouse" |
| 5 | Set as receiving | Toggle |
| 6 | Save | Warehouse created |

---

### SC-LOC-005: Edit Location

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select location | Row selected |
| 2 | Click Edit | EDIT mode |
| 3 | Modify name | Change name |
| 4 | Save | Updated |

---

### SC-LOC-006: Configure Location Address

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit location | EDIT mode |
| 2 | Open Address tab | Address fields |
| 3 | Enter full address | All fields |
| 4 | Save | Address saved |

---

### SC-LOC-007: Configure Location Contact

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit location | EDIT mode |
| 2 | Open Contact tab | Contact fields |
| 3 | Enter manager | Name |
| 4 | Enter phone | Number |
| 5 | Enter email | Email |
| 6 | Save | Contact saved |

---

### SC-LOC-008: Set Default Location

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select location | Any location |
| 2 | Click "Set Default" | Action |
| 3 | Confirm | Location is default |
| 4 | Verify | Star/badge indicator |

---

### SC-LOC-009: Deactivate Location

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select active location | No stock |
| 2 | Click Deactivate | Confirmation |
| 3 | Confirm | Status: Inactive |
| 4 | Verify | Not in dropdowns |

---

### SC-LOC-010: Cannot Deactivate Location with Stock

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select location | Has stock on hand |
| 2 | Click Deactivate | Error |
| 3 | Verify | "Location has stock" |

---

### SC-LOC-011: Duplicate Code Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create new location | Existing code |
| 2 | Save | Error: Duplicate |

---

### SC-LOC-012: Location Hierarchy

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create parent | "Region North" |
| 2 | Create child | Parent = "Region North" |
| 3 | View tree | Hierarchy visible |
| 4 | Expand parent | Children shown |

---

### SC-LOC-013: Intercompany Location Link

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit location | EDIT mode |
| 2 | Open IC tab | Intercompany settings |
| 3 | Link to related company | Select company |
| 4 | Select related location | Location in other company |
| 5 | Save | IC link established |

---

### SC-LOC-014: Location-Specific Tax

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit location | EDIT mode |
| 2 | Open Tax tab | Tax settings |
| 3 | Select tax profile | State-specific |
| 4 | Save | Tax applied to location |

---

### SC-LOC-015: Search Locations

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter search | Location name |
| 2 | Results | Filtered list |
| 3 | Clear | Full list |

---

### SC-LOC-016: Filter by Type

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Type filter | Dropdown |
| 2 | Select "Store" | Only stores |
| 3 | Select "Warehouse" | Only warehouses |

---

**Scenario Count**: 16  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
