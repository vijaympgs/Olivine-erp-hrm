# Screen: Fiscal Periods

**Sidebar Path**: System Configuration > Fiscal Periods  
**URL**: `/config/fiscal-periods`  
**Component**: `FiscalPeriodsPage.tsx`

---

## Purpose

Fiscal Periods manages financial calendar and periods:
- Fiscal year definition
- Period (month) management
- Period opening and closing
- Year-end processes
- Period status control

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `config.fiscal.manage` permission | Yes |
| Company exists | Parent entity |

---

## Scenarios

### SC-FISCAL-001: View Fiscal Years

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/config/fiscal-periods` | Page loads |
| 2 | Verify fiscal years | List of years |
| 3 | Verify columns | Year, Start, End, Status |

---

### SC-FISCAL-002: Create Fiscal Year

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "New Fiscal Year" | Create dialog |
| 2 | Enter Year Name | "FY 2026-27" |
| 3 | Set Start Date | April 1, 2026 |
| 4 | Set End Date | March 31, 2027 |
| 5 | Click Generate Periods | 12 months created |
| 6 | Save | Fiscal year created |

---

### SC-FISCAL-003: Auto-Generate Periods

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create fiscal year | Start/End dates |
| 2 | Click Generate | Auto-generate |
| 3 | Verify | 12 monthly periods |
| 4 | Each period | Correct date range |

---

### SC-FISCAL-004: View Periods in Year

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click fiscal year | Expand |
| 2 | View periods | 12 month rows |
| 3 | Verify columns | Period, Start, End, Status |

---

### SC-FISCAL-005: Open Period

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select period | Status: Closed |
| 2 | Click "Open" | Confirmation |
| 3 | Confirm | Status: Open |
| 4 | Verify | Transactions allowed |

---

### SC-FISCAL-006: Close Period

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select period | Status: Open |
| 2 | Click "Close" | Confirmation |
| 3 | Confirm | Status: Closed |
| 4 | Verify | No new transactions |

---

### SC-FISCAL-007: Cannot Post to Closed Period

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Close period | March 2026 |
| 2 | Try posting invoice | Date in March |
| 3 | Verify | Error: Period closed |

---

### SC-FISCAL-008: Reopen Closed Period

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select closed period | Status: Closed |
| 2 | Click "Reopen" | Admin action |
| 3 | Enter reason | Required |
| 4 | Confirm | Status: Open |
| 5 | Audit | Logged |

---

### SC-FISCAL-009: Year-End Close

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select fiscal year | All periods closed |
| 2 | Click "Year-End Close" | Year-end wizard |
| 3 | Run reconciliations | Verify totals |
| 4 | Confirm | Year closed |
| 5 | Create opening balances | For next year |

---

### SC-FISCAL-010: Lock Period

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select period | Any period |
| 2 | Click "Lock" | Stronger than close |
| 3 | Verify | Cannot reopen without admin |

---

### SC-FISCAL-011: Adjustment Period

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create adjustment period | Period 13 |
| 2 | Set as adjustment | Flag |
| 3 | Use | For year-end adjustments |

---

### SC-FISCAL-012: Overlapping Year Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create fiscal year | Overlapping dates |
| 2 | Save | Error: Overlap |

---

### SC-FISCAL-013: Delete Unused Fiscal Year

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select fiscal year | No transactions |
| 2 | Click Delete | Confirmation |
| 3 | Confirm | Year deleted |

---

### SC-FISCAL-014: Cannot Delete Used Fiscal Year

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select fiscal year | Has transactions |
| 2 | Click Delete | Error |
| 3 | Verify | "Year has transactions" |

---

**Scenario Count**: 14  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
