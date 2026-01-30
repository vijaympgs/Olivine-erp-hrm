# Screen: Session Open (Shift Start)

**Sidebar Path**: Retail > Store Ops > Daily Operations > Shift Start  
**URL**: `/operations/pos/session-open`  
**Component**: `SessionOpenPage.tsx`

---

## Purpose

Session Open starts a cashier's shift within an open day. It:
- Assigns a terminal to the user
- Records opening cash count
- Enables POS Checkout access
- Tracks transactions per session

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Day is open | Yes |
| Terminal available | Yes |
| User has `pos.session.open` permission | Yes |

---

## Scenarios

### SC-SESSION-001: Start Shift (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Session Open | Form loads |
| 2 | Select Terminal | Dropdown shows available |
| 3 | Enter Opening Cash | ₹1,000.00 |
| 4 | Click "Start Shift" | Session started |
| 5 | Redirect to POS | `/pos/ui` accessible |

**Postconditions**: Session active, cashier can transact

---

### SC-SESSION-002: Cannot Start Without Day Open

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Day not open | Pre-condition |
| 2 | Navigate to Session Open | Blocked |
| 3 | Message | "Open day first" |

---

### SC-SESSION-003: Terminal Already In Use

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Terminal has active session | Other user |
| 2 | Select same terminal | Error |
| 3 | Message | "Terminal in use by [User]" |

---

### SC-SESSION-004: Multiple Sessions Same User

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | User has active session | On another terminal |
| 2 | Attempt new session | Error or warning |
| 3 | Behavior | Per business rules |

---

### SC-SESSION-005: Opening Cash Zero Allowed

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter ₹0 opening | Zero is valid |
| 2 | Start Shift | Success |

---

**Scenario Count**: 5
