# Screen: Terminal Configuration (Registers)

**Sidebar Path**: Retail > Store Ops > Settings > Registers  
**URL**: `/pos/terminal`  
**Component**: `TerminalPage.tsx`

---

## Purpose

Manages POS terminal/register configuration. Each terminal:
- Has unique identifier
- Is assigned to a location
- Can have hardware assignments (printer, scanner)
- Is used in session operations

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Location configured | Yes |
| User has `pos.terminal.admin` permission | Yes |

---

## Scenarios

### SC-TERM-001: Create Terminal (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Registers | List loads |
| 2 | Click New | CREATE mode |
| 3 | Enter Terminal Code | "TERM-001" |
| 4 | Enter Terminal Name | "Register 1" |
| 5 | Select Location | Main Store |
| 6 | Save | Terminal created |

---

### SC-TERM-002: Edit Terminal

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select terminal | Row selected |
| 2 | Click Edit | EDIT mode |
| 3 | Modify name | Updated |
| 4 | Save | Changes persisted |

---

### SC-TERM-003: Hardware Assignment

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit terminal | Form open |
| 2 | Hardware tab | Hardware fields visible |
| 3 | Assign printer | Select printer |
| 4 | Assign scanner | Select scanner |
| 5 | Save | Assignments saved |

---

### SC-TERM-004: Deactivate Terminal

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select terminal | No active session |
| 2 | Click Deactivate | Confirmation |
| 3 | Confirm | Status: Inactive |
| 4 | Cannot use for session | Blocked |

---

### SC-TERM-005: Cannot Delete Terminal With History

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Terminal has sessions | Past usage |
| 2 | Attempt delete | Error |
| 3 | Message | "Has transaction history" |

---

### SC-TERM-006: Duplicate Code Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create new terminal | Same code as existing |
| 2 | Save | Error: Duplicate |

---

**Scenario Count**: 6
