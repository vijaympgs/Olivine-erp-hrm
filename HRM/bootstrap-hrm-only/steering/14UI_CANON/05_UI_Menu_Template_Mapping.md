# UI MENU → TEMPLATE TAGGING (TASK 1)
Status: COMPLETED
Scope: Retail, HRM, FMS, CRM
Source: menuConfig.ts (authoritative)

---

## RETAIL

| Menu Path | Screen | Template |
|---------|--------|----------|
| Merchandising → Catalog | Item Master | MST-M |
| Merchandising → Variants | Item Attributes | MST-M |
| Merchandising → UOM | UOM | MST-S |
| Inventory → Stock Take | Stock Take | TXN-M |
| Inventory → Adjustments | Inventory Adjustment | TXN-M |
| Procurement → Requisitions | Purchase Requisition | TXN-M |
| Procurement → RFQ | Request for Quotation | TXN-M |
| Procurement → Purchase Orders | Purchase Order | TXN-M |
| Store Ops → Checkout | POS | TXN-C |
| Sales → Invoices | Sales Invoice | TXN-M |
| Sales → Returns | Sales Return | TXN-M |
| Configuration → Procurement Config | Procurement Config | CFG-M |

---

## HRM

| Menu Path | Screen | Template |
|---------|--------|----------|
| Employee Management → Employee Directory | Employee Master | MST-C |
| Organization Setup → Departments | Department | MST-C |
| Organization Setup → Positions | Position | MST-M |
| Time & Attendance → Leave Requests | Leave Request | TXN-M |
| Time & Attendance → Attendance Adjustments | Attendance Adjustment | TXN-S |
| Compliance → Company Policies | HR Policies | CFG-M |
| Reports → Employee Reports | HR Reports | RPT |

---

## FMS

| Menu Path | Screen | Template |
|---------|--------|----------|
| General Ledger → Chart of Accounts | COA | MST-C |
| General Ledger → Journal Entries | Journal Entry | TXN-S |
| Accounts Payable → Vendor Bills | Vendor Bill | TXN-M |
| Accounts Receivable → Customer Invoices | AR Invoice | TXN-M |
| Cash & Bank → Bank Reconciliation | Bank Reco | TXN-M |
| Tax Management → Tax Configuration | Tax Config | CFG-M |
| Period Closing → Period Lock | Period Lock | CFG-M |
| Reports → Balance Sheet | Balance Sheet | RPT |

---

## CRM

| Menu Path | Screen | Template |
|---------|--------|----------|
| Lead Management → Lead Capture | Lead | TXN-M |
| Contact Management → Contact Directory | Contact | MST-M |
| Account Management → Account Directory | Account | MST-M |
| Opportunity Management → Pipeline | Opportunity | TXN-M |
| Campaign Management → Campaign Planning | Campaign | TXN-M |
| Configuration → Roles & Permissions | CRM Security | CFG-M |
| Analytics → Sales Analytics | Sales Analytics | RPT |

---

## GOVERNANCE NOTE
- Template derivation is mandatory
- Agents must resolve template before UI work
- No deviations allowed
