# Screen: User Management

**Sidebar Path**: System Administration > User Management  
**URL**: `/admin/users`  
**Component**: `UserManagementPage.tsx`

---

## Purpose

User Management is the central hub for managing all system users including:
- User creation and profile management
- Role and permission assignment
- Status control (Active/Inactive/Locked)
- Password management and policies
- Company/Location/Terminal assignment

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `admin.users.manage` permission | Yes |
| At least 1 role exists | For assignment |

---

## Scenarios

### SC-USRMGT-001: View User List

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/admin/users` | List loads |
| 2 | Verify columns | Username, Name, Email, Role, Status, Last Login |
| 3 | Verify pagination | Page controls visible |
| 4 | Verify search | Search box available |

---

### SC-USRMGT-002: Create User (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click New | CREATE mode |
| 2 | Enter Username | `testuser001` |
| 3 | Enter First Name | `Test` |
| 4 | Enter Last Name | `User` |
| 5 | Enter Email | `test@olivine.com` |
| 6 | Select Role | `Cashier` |
| 7 | Set Password | `SecurePass123!` |
| 8 | Confirm Password | Match |
| 9 | Select Company | Primary company |
| 10 | Select Location | Store location |
| 11 | Click Save | User created, status Active |

**Postconditions**: User can login with credentials

---

### SC-USRMGT-003: Edit User Profile

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select user in list | Row highlighted |
| 2 | Click Edit | EDIT mode |
| 3 | Modify email | New email address |
| 4 | Modify phone | New phone number |
| 5 | Save | Changes persisted |

---

### SC-USRMGT-004: Assign Role to User

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit user | EDIT mode |
| 2 | Click Roles tab | Role assignment panel |
| 3 | Add role | Select additional role |
| 4 | Save | User has multiple roles |
| 5 | Verify permissions | Combined permission set |

---

### SC-USRMGT-005: Deactivate User

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select active user | Status: Active |
| 2 | Click "Deactivate" | Confirmation dialog |
| 3 | Enter reason | Required field |
| 4 | Confirm | Status: Inactive |
| 5 | User login attempt | Login blocked |

---

### SC-USRMGT-006: Reactivate User

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Filter to Inactive | Show inactive users |
| 2 | Select inactive user | Status: Inactive |
| 3 | Click "Activate" | Confirmation |
| 4 | Confirm | Status: Active |
| 5 | User login | Access restored |

---

### SC-USRMGT-007: Lock User Account

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select user | Normal user |
| 2 | Click "Lock Account" | Security action |
| 3 | Confirm | Status: Locked |
| 4 | User login | "Account locked" message |

---

### SC-USRMGT-008: Unlock User Account

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Filter to Locked | Show locked users |
| 2 | Select locked user | Status: Locked |
| 3 | Click "Unlock" | Confirmation |
| 4 | Confirm | Status: Active |

---

### SC-USRMGT-009: Reset Password

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select user | Any user |
| 2 | Click "Reset Password" | Password dialog |
| 3 | Enter new password | Meets complexity |
| 4 | Confirm password | Match |
| 5 | Save | Password changed |
| 6 | User login | Uses new password |

---

### SC-USRMGT-010: Force Password Change

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit user | EDIT mode |
| 2 | Check "Force password change" | Flag set |
| 3 | Save | Setting persisted |
| 4 | User next login | Prompted to change password |

---

### SC-USRMGT-011: Duplicate Username Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create new user | Enter existing username |
| 2 | Save | Error: Username exists |

---

### SC-USRMGT-012: Duplicate Email Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create new user | Enter existing email |
| 2 | Save | Error: Email exists |

---

### SC-USRMGT-013: Password Complexity

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create user | Enter weak password `123` |
| 2 | Save | Error: Password requirements |
| 3 | Verify message | Min 8 chars, uppercase, number, special |

---

### SC-USRMGT-014: Search Users

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter search term | Username or name |
| 2 | Results filtered | Matching users shown |
| 3 | Clear | Full list restored |

---

### SC-USRMGT-015: Filter by Status

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Status filter | Dropdown |
| 2 | Select "Active" | Only active users |
| 3 | Select "Inactive" | Only inactive users |
| 4 | Select "Locked" | Only locked users |

---

### SC-USRMGT-016: Filter by Role

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Role filter | Dropdown |
| 2 | Select "Cashier" | Only cashiers shown |
| 3 | Select "Admin" | Only admins shown |

---

### SC-USRMGT-017: Cannot Delete Own Account

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select own user | Current logged-in user |
| 2 | Delete button | Disabled or hidden |

---

### SC-USRMGT-018: View User Activity

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select user | Any user |
| 2 | Click "Activity" tab | Activity log visible |
| 3 | Verify content | Login history, actions performed |

---

### SC-USRMGT-019: Export User List

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Export | Export dialog |
| 2 | Select CSV | Format choice |
| 3 | Download | File with user data |

---

**Scenario Count**: 19  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
