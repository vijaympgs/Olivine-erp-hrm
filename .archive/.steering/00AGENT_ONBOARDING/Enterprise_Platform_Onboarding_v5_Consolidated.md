
# Enterprise ERP Platform – Onboarding & Governance Guide (v5)

> **Status:** AUTHORITATIVE  
> **Audience:** Architects, Senior Engineers, Agents  
> **Scope:** Retail, HRM, CRM, FMS  
> **Rule:** This document CONSOLIDATES v3 and v4 in full, without omission.  
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

#### Backend
- Python 3.x
- Django (modular app architecture)
- Django REST Framework (API-first)
- PostgreSQL

#### Frontend
- Vite
- React (SPA)
- TypeScript (strict)
- Tailwind CSS (UI canon)

---

## PAGE 2 — ENTERPRISE SHELL & SPA ARCHITECTURE

### 4. Enterprise Shell Concept

The platform operates as an **Enterprise Shell**:

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

If this fails, architecture is invalid.

### 5. App Separation Rule (LOCKED)

- No app may assume the presence of another app
- No cross-app imports are allowed
- No shared database tables across apps
- Shared logic is consumed, never owned

Retail is **not special** despite being actively developed.

### 6. SPA Approach

The platform is a **Single Page Application (SPA)** with multiple isolated apps:
- Retail
- HRM
- CRM
- FMS

Each app behaves like a **mini-application**.

### 7. Phase-1 Scope Rule
- Only core operational features
- No enterprise-heavy modules
- Phase-2 features are explicitly parked

---

## PAGE 3 — DETAILED EXECUTION FOLDER STRUCTURE (AUTHORITATIVE)

### 8. Execution Folder Tree

```
retail-erp-platform/
├── retail/
│   ├── backend/
│   └── frontend/
│
├── hrm/
│   ├── backend/
│   │   ├── models/
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── urls.py
│   │   └── migrations/
│   ├── frontend/
│   │   ├── pages/
│   │   ├── modules/
│   │   ├── services/
│   │   ├── routes/
│   │   └── templates/
│
├── crm/
│   ├── backend/
│   │   ├── models/
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── urls.py
│   │   └── migrations/
│   ├── frontend/
│   │   ├── pages/
│   │   ├── modules/
│   │   ├── services/
│   │   ├── routes/
│   │   └── templates/
│
├── fms/
│   ├── backend/
│   └── frontend/
│
├── common/
│   ├── auth/
│   ├── permissions/
│   ├── ui-canon/
│   └── shared-services/
│
└── README.md
```

### 9. Folder Structure Principles
- Every app has **its own backend + frontend**
- No cross-app imports
- Shared logic only via `common` or `domain`
- Folder layout is **non-negotiable**

---

## PAGE 4 — MERGEABILITY CONTRACT (NON-NEGOTIABLE)

### 10. App Mergeability Contract

Target structure:
```
retail-erp-platform/
├── retail/
├── hrm/
├── crm/
├── fms/
```

### 11. Copy–Paste Rule (Golden Rule)

It must be possible to:
```
COPY   retail-erp-platform/hrm
PASTE  into another platform
```

and have it work after reconnecting:
- Auth
- DB
- Routing

❌ If refactoring is required → architecture is WRONG  
✅ If copy-paste works → architecture is CORRECT

### 12. Strict Boundaries

- No app imports another app’s models
- No shared DB tables without domain abstraction
- Retail is NOT special

---

## PAGE 5 — LICENSING vs COMPANY vs LOCATION (CRITICAL)

### 13. Licensing (Commercial / SaaS Layer)

Licensing answers: **“Who bought what?”**

Licensing controls:
- Which apps are enabled (Retail / HRM / CRM / FMS)
- How many companies may be created
- How many Retail locations are allowed per company

Licensing:
- Is system-level
- Is commercial
- Does **not** own business data
- Does **not** participate in transactions

Licensing enforces **limits and entitlements only**.

### 14. Company (Business / Legal Layer)

Company answers: **“Which legal business exists?”**

Rules:
- Company is a PLATFORM-LEVEL domain
- Lives under System Administration / `common`
- Consumed by ALL apps (Retail, HRM, CRM, FMS)
- Owned by NO individual app

Licensing may limit how many Companies can be created,
but does NOT own Company data.

### 15. Location (Operational / Retail Layer)

Location answers: **“Where does Retail operate?”**

Rules:
- Location is a RETAIL-OWNED operational concept
- Used ONLY by Retail transactions
- HRM, CRM, FMS MUST NOT reference Location
- Location MUST NOT exist in `common`

> Location Setup may appear under System Administration UI for centralized administration;
> however, Locations are owned by the Retail domain and are Retail-exclusive.

UI placement does NOT define domain ownership.

---

## PAGE 6 — HRM / CRM PLATFORM MODEL REFERENCES (READ-ONLY)

### 16. Platform Core Models (Reference Only)

The following models are **platform-level contracts**.  
HRM and CRM may **consume** them but must NOT modify, extend, or duplicate them.

- `Company`
- `User`
- `UserPermission`
- `Role`
- `OrganizationRole`
- `AuthPolicy`

Rules:
- No Retail-owned concepts allowed (e.g., `Location`)
- HRM / CRM operate strictly at **Company level**
- Must remain **independently copy–paste mergeable**

---

## PAGE 7 — DOMAIN OWNERSHIP MATRIX

### 17. Domain Model Ownership (LOCKED)

#### Platform / common
- Company
- User
- Permission
- ItemMaster (base)
- Supplier (base)
- UnitOfMeasure

Rules:
- Models must be minimal
- No Location reference allowed
- No domain-specific behavior

#### Retail Domain
- Location
- Retail extensions of:
  - Customer
  - ItemMaster
  - Supplier

#### HRM Domain
- Employee
- Department
- Position

#### CRM Domain
- Lead
- Opportunity
- Account

#### FMS Domain
- Accounting (GL, AP, AR)
- Vendor usage via Supplier (base)

---

## PAGE 8 — EXECUTION & AGENT RULES

### 18. What Agents MAY Do
- Validate mergeability
- Report violations
- Propose migration plans
- Execute changes ONLY when approved

### 19. What Agents MUST NOT Do
- Move governance into apps
- Duplicate common models
- Introduce cross-app dependencies
- Assume all apps coexist locally

---

## FINAL LOCK

> **Licensing controls entitlements.  
> Company represents the business.  
> Location is a Retail-owned operational unit.**

Any violation of these principles is a **governance breach**.

---

**END OF DOCUMENT**
