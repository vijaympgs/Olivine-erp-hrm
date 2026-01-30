
# Enterprise ERP Platform – Onboarding & Governance Guide (v6)

> **Status:** AUTHORITATIVE  
> **Audience:** Architects, Senior Engineers, Agents  
> **Scope:** Retail, HRM, CRM, FMS  
> **Rule:** This document supersedes v5 and all earlier versions.  
> All rules herein are NON-NEGOTIABLE.

---

## PAGE 1 — PURPOSE, GOVERNANCE & TECH STACK

### 1. Purpose of This Document
This document defines the **non-negotiable architectural, governance, and data-ownership rules**
for the Enterprise ERP Platform.

It exists to ensure:
- Long-term scalability
- Multi-machine development
- Copy–paste mergeability of domain apps
- Zero architectural drift across agents

This is **not** a suggestion document.  
This is a **governance contract**.

### 2. Repository & Folder Governance

The platform follows a **strict separation between reference and execution folders**.

#### Base / Reference Folder (READ-ONLY)
- **01practice-v2**
- Canonical reference for:
  - Permissions
  - Menu structures
  - UI patterns
  - Architecture conventions
- ❌ No changes allowed

#### Current / Execution Folder (WRITE-ONLY)
- **retail-erp-platform / erp-platform**
- All active development happens here:
  - Retail
  - HRM
  - CRM
  - FMS

### 3. Technology Stack

**Backend**
- Python 3.x
- Django (modular app architecture)
- Django REST Framework (API-first)
- PostgreSQL

**Frontend**
- Vite
- React (SPA)
- TypeScript (strict)
- Tailwind CSS (UI canon)

---

## PAGE 2 — ENTERPRISE SHELL & SPA ARCHITECTURE

### 4. Enterprise Shell Concept

```
erp-platform/
├── Retail/
├── HRM/
├── CRM/
├── FMS/
└── common/
```

Each domain app:
- Is independently developed
- May live on a separate machine
- Must be mergeable later by folder copy–paste

> **COPY → PASTE → RUN** is the primary validation test.

### 5. App Separation Rule (LOCKED)
- No app may assume the presence of another app
- No cross-app imports are allowed
- No shared database tables across apps
- Shared logic is consumed, never owned

Retail is **not special** despite being actively developed.

---

## PAGE 3 — DETAILED EXECUTION FOLDER STRUCTURE

```
retail-erp-platform/
├── retail/
│   ├── backend/
│   └── frontend/
├── hrm/
│   ├── backend/
│   └── frontend/
├── crm/
│   ├── backend/
│   └── frontend/
├── fms/
│   ├── backend/
│   └── frontend/
├── common/
│   ├── domain/
│   ├── auth/
│   ├── permissions/
│   ├── ui-canon/
│   └── shared-services/
└── README.md
```

---

## PAGE 4 — MERGEABILITY CONTRACT

> **COPY → PASTE → RUN** is mandatory.

If refactoring is required after copy–paste, architecture is INVALID.

---

## PAGE 5 — LICENSING vs COMPANY vs LOCATION

### Licensing (Commercial Control Plane)
- Controls entitlements and limits
- Enables / disables apps
- Limits number of companies and retail locations
- **OWNS NO BUSINESS DATA**

### Company (Platform Domain)
- Legal / business entity
- Lives in `common/domain`
- Consumed by all apps

### Location (Retail Domain)
- Retail-owned operational concept
- Used only by Retail
- Never referenced by HRM / CRM / FMS

---

## PAGE 6 — DOMAIN OWNERSHIP MATRIX

**Platform / common**
- Company
- User
- Permission
- ItemMaster (base)
- Supplier (base)
- UnitOfMeasure

**Retail**
- Location
- Retail extensions of Item, Supplier

**HRM**
- Employee, Department, Position

**CRM**
- Lead, Opportunity, Account

**FMS**
- GL, AP, AR

---

## PAGE 7 — HRM / CRM PLATFORM MODEL REFERENCES (READ-ONLY)

HRM / CRM may CONSUME (read-only):
- Company
- User
- Permission
- Role
- OrganizationRole
- AuthPolicy

❌ Must NOT reference Location  
❌ Must NOT modify platform models

---

## PAGE 8 — AGENT EXECUTION RULES

Agents MAY:
- Validate mergeability
- Propose plans
- Execute only after approval

Agents MUST NOT:
- Move governance into apps
- Duplicate masters
- Introduce cross-app dependencies

---

## PAGE 11 — LICENSING OWNS NO MASTERS (LOCK)

> **LICENSING OWNS NO BUSINESS MASTERS.**

Licensing MUST NOT own or manage:
- Company
- ItemMaster
- Supplier
- UnitOfMeasure
- Customer
- Any operational or reference master

Licensing exists ONLY to:
- Enforce entitlements
- Enforce limits
- Control app access

Any appearance of masters under Licensing is a **governance violation**.

---

## PAGE 12 — POST-MORTEM: WHY LICENSING WAS CLEANED UP

### Historical Issue
Earlier versions mixed:
- Base Item Masters
- Reference data

inside **Licensing**.

### Problems Caused
- Commercial vs operational confusion
- Duplicate UI risk
- Wrong ownership assumptions
- Schema pollution

### Corrective Action Taken
- All business masters removed from Licensing
- Licensing reduced to control plane only
- Masters reassigned to Platform or Retail

### Rule Going Forward
> **Licensing never owns business data.**

---

## PAGE 13 — MENU & UI AUDIT GUIDELINES

Single-UI Rule:
- Exactly ONE UI per master

Correct placement:
- Company → System Administration
- Item / Supplier / UoM → Retail → Merchandising

❌ Forbidden:
- Admin UI for Item
- Finance UI for UoM
- Duplicate Supplier screens

---

## PAGE 14 — REGRESSION PREVENTION CHECKLIST

Before approving changes, verify:
- No masters under Licensing
- No duplicate UIs
- No Location in HRM / CRM / FMS
- common/domain contains only contracts
- Retail owns operational UI
- Apps are copy–paste mergeable

---

**END OF DOCUMENT**
