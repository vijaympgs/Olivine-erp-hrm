# Screen: Day Close

**Sidebar Path**: Retail > Store Ops > Daily Operations > Day Close  
**URL**: `/operations/pos/day-close`  
**Component**: `DayClosePage.tsx`

---

## Purpose

Day Close ends the business day. It:
- Requires all sessions to be closed
- Generates daily summary report
- Locks day from further transactions
- Enables next day open

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| Day is open | Yes |
| All sessions closed | Yes |
| User has `pos.day.close` permission | Yes |

---

## Scenarios

### SC-DAYCLOSE-001: Close Day (Happy Path)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | All sessions closed | Pre-condition |
| 2 | Navigate to Day Close | Form loads |
| 3 | Review daily summary | Totals displayed |
| 4 | Click "Close Day" | Day closed |
| 5 | Status | Day status: Closed |

**Postconditions**: Day locked, can open next day

---

### SC-DAYCLOSE-002: Cannot Close With Open Sessions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Session still active | On some terminal |
| 2 | Attempt Day Close | Blocked |
| 3 | Message | "X sessions still open" |
| 4 | List sessions | Show active users |

---

### SC-DAYCLOSE-003: Daily Summary Report

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Day Close | Summary visible |
| 2 | Contents | Total sales, tenders, variance |
| 3 | Breakdown | By session, by terminal |

---

### SC-DAYCLOSE-004: Re-open Closed Day (Exceptional)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Day closed | Status: Closed |
| 2 | Admin attempts re-open | If allowed by config |
| 3 | Audit trail | Logged with reason |

---

### SC-DAYCLOSE-005: End of Day Report Print

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Close day | Success |
| 2 | Click Print EOD | Report generates |
| 3 | Content | Complete day summary |

---

**Scenario Count**: 5
