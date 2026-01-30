# Screen: Day Open

**Sidebar Path**: Retail > Store Ops > Daily Operations > Day Open  
**URL**: `/operations/pos/day-open`  
**Component**: `DayOpenPage.tsx`

---

## Purpose

Day Open is the first step in the POS daily operations chain. Opening the day:
- Sets the business date for all transactions
- Records opening float for cash reconciliation
- Enables session operations
- Gates access to POS Checkout

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Terminal configured | Yes |
| Previous day closed (if not first day) | Yes |
| User has `pos.day.open` permission | Yes |

---

## Scenarios

### SC-DAYOPEN-001: Open Day (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/operations/pos/day-open` | Day Open form loads |
| 2 | Verify date | Today's date pre-selected |
| 3 | Enter Opening Float | Amount: ₹5,000.00 |
| 4 | Click "Open Day" | Day status: Open |
| 5 | Verify navigation | Session Open now available |

**Postconditions**: Day is open, sessions can start

---

### SC-DAYOPEN-002: Cannot Open Already Open Day

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Day already open | Pre-condition |
| 2 | Navigate to Day Open | Redirect or message |
| 3 | Verify message | "Day already open" |

---

### SC-DAYOPEN-003: Cannot Open Without Closing Previous

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Previous day not closed | Outstanding sessions |
| 2 | Attempt Day Open | Error message |
| 3 | Verify | "Close previous day first" |

---

### SC-DAYOPEN-004: Opening Float Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter negative float | -₹100 |
| 2 | Click Open Day | Validation error |
| 3 | Verify | "Amount must be positive" |

---

### SC-DAYOPEN-005: Audit Trail

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open day successfully | Day opened |
| 2 | Check audit log | Entry recorded with user, time |

---

**Scenario Count**: 5
