# Screen: Session Close (Shift End)

**Sidebar Path**: Retail > Store Ops > Daily Operations > Shift End  
**URL**: `/operations/pos/session-close`  
**Component**: `SessionClosePage.tsx`

---

## Purpose

Session Close ends a cashier's shift. It:
- Records closing cash count
- Calculates variance (expected vs actual)
- Generates session summary
- Releases terminal for others

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Active session | Yes |
| No pending transactions | Yes |
| User owns the session | Yes |

---

## Scenarios

### SC-SESSCLOSE-001: Close Shift (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Session Close | Form loads with session summary |
| 2 | View expected cash | Calculated from transactions |
| 3 | Enter counted cash | ₹15,000.00 |
| 4 | Variance calculated | Expected - Counted |
| 5 | Click "Close Shift" | Session closed |
| 6 | Print summary | Session report available |

**Postconditions**: Session closed, terminal released

---

### SC-SESSCLOSE-002: Variance Over Threshold

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Expected: ₹15,000 | From sales |
| 2 | Counted: ₹14,500 | Short ₹500 |
| 3 | If threshold exceeded | Manager approval required |
| 4 | Approve/Reject | Per business rules |

---

### SC-SESSCLOSE-003: Cannot Close With Held Transactions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Held transactions exist | On this session |
| 2 | Attempt close | Warning |
| 3 | Action required | Complete or void held |

---

### SC-SESSCLOSE-004: Zero Sales Session

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | No sales in session | ₹0 expected |
| 2 | Close shift | Allowed |
| 3 | Opening cash = Counted | No variance |

---

### SC-SESSCLOSE-005: Print Session Report

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Close session | Success |
| 2 | Click Print | Report generates |
| 3 | Content | All transactions, totals |

---

**Scenario Count**: 5
