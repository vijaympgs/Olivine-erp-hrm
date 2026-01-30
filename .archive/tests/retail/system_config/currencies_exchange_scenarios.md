# Screen: Currencies & Exchange

**Sidebar Path**: System Configuration > Currencies & Exchange  
**URL**: `/config/currencies`  
**Component**: `CurrenciesExchangePage.tsx`

---

## Purpose

Currencies & Exchange manages multi-currency support:
- Currency definitions
- Exchange rate management
- Rate history
- Default currency settings
- Currency formatting

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `config.currency.manage` permission | Yes |
| Company exists | For base currency |

---

## Scenarios

### SC-CURR-001: View Currency List

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/config/currencies` | Page loads |
| 2 | Verify tabs | Currencies, Exchange Rates |
| 3 | Verify list | Code, Name, Symbol, Is Base |

---

### SC-CURR-002: Add Currency

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Add Currency" | Create form |
| 2 | Enter Code | "USD" |
| 3 | Enter Name | "US Dollar" |
| 4 | Enter Symbol | "$" |
| 5 | Set Decimal Places | 2 |
| 6 | Save | Currency added |

---

### SC-CURR-003: Set Base Currency

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select currency | INR |
| 2 | Click "Set as Base" | Confirmation |
| 3 | Confirm | INR is base |
| 4 | Verify | All rates relative to INR |

---

### SC-CURR-004: Cannot Change Base with Transactions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Transactions exist | In base currency |
| 2 | Try change base | Attempt |
| 3 | Verify | Warning/Blocked |

---

### SC-CURR-005: Add Exchange Rate

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Go to Exchange Rates tab | Rate list |
| 2 | Click "Add Rate" | Rate form |
| 3 | Select From | USD |
| 4 | Select To | INR (base) |
| 5 | Enter Rate | 83.50 |
| 6 | Set Effective Date | Today |
| 7 | Save | Rate added |

---

### SC-CURR-006: View Exchange Rate History

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select currency pair | USD/INR |
| 2 | Click History | Rate history |
| 3 | Verify | Date, Rate, Source |
| 4 | Chart | Rate trend |

---

### SC-CURR-007: Update Exchange Rate

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select rate | Existing rate |
| 2 | Click Edit | Edit mode |
| 3 | Change rate | 83.75 |
| 4 | Save | Rate updated |
| 5 | History | Old rate preserved |

---

### SC-CURR-008: Import Exchange Rates

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Import | Import dialog |
| 2 | Select source | CSV/API |
| 3 | Upload/Fetch | Rates imported |
| 4 | Verify | New rates listed |

---

### SC-CURR-009: Auto-Fetch Rates

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enable auto-fetch | Toggle ON |
| 2 | Select source | Central bank/Provider |
| 3 | Set schedule | Daily |
| 4 | Save | Auto-update configured |

---

### SC-CURR-010: Rate Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter invalid rate | 0 or negative |
| 2 | Save | Validation error |
| 3 | Enter valid rate | Positive number |
| 4 | Save | Success |

---

### SC-CURR-011: Currency Formatting

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Edit currency | Currency form |
| 2 | Set decimal places | 2 |
| 3 | Set thousand separator | "," |
| 4 | Set decimal separator | "." |
| 5 | Save | Format applied |
| 6 | Verify in app | 1,234.56 |

---

### SC-CURR-012: Deactivate Currency

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select currency | Not used |
| 2 | Click Deactivate | Confirmation |
| 3 | Confirm | Status: Inactive |
| 4 | Verify | Not in dropdowns |

---

### SC-CURR-013: Cannot Deactivate Used Currency

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select currency | Used in transactions |
| 2 | Click Deactivate | Error |
| 3 | Verify | "Currency has transactions" |

---

### SC-CURR-014: Triangulation Rate

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | No direct rate | USD to EUR |
| 2 | System calculates | Via INR |
| 3 | Verify | Triangulated rate |

---

### SC-CURR-015: Rate Date Lookup

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Transaction date | Historical |
| 2 | System lookup | Rate on that date |
| 3 | Verify | Correct rate applied |

---

**Scenario Count**: 15  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
