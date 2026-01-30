# Unified Application Shell & Launcher Guide (Canonical)

**Status**: Authoritative (Aligned with Governance & Repo Reality)  
**Date**: 2026-01-18  
**Version**: 2.0  
**Scope**: Unified Platform Startup (Retail, HRM, CRM, FMS)  

> This document defines the **correct, governance-aligned architecture** of the Olivine Platform.  
> It explicitly avoids structural assumptions that contradict the real repository layout or agent governance contracts.

---

## 1. Architecture Overview

The Olivine Platform uses a **Unified Shell Gateway Architecture**.

This means:
- There is a **single unified frontend shell** (React) for the whole platform.
- There is a **single unified backend gateway** (Django project) that aggregates all modules.
- Each business module (Retail, HRM, CRM, FMS) remains a **separate ownership boundary at the root level** of the repository.

The unified shell **orchestrates and routes**, but it does **not own module code**.

### Core Modules (The Big Four)
- **Retail** – Store Ops, Inventory, POS, Procurement, Sales
- **HRM** – Employee Management, Org Structure, Payroll, Attendance
- **CRM** – Leads, Accounts, Opportunities, Pipeline
- **FMS** – GL, AR, AP, Tax, Finance

---

## 2. QA Launcher Console (Orchestration Layer)

The **QA Launcher Console** is the operational control plane used for development and QA.

**Location**:  
`Common/qa-launcher-console/`

**Responsibilities**:
- Starts unified backend (Django) process
- Starts unified frontend (React) process
- Streams logs (backend + frontend)
- Manages ports and detects conflicts
- Provides execution status

**Ports**:
- Launcher UI (Dev): `5174`
- Launcher API: `3100`
- Unified Backend: `8000`
- Unified Frontend: `3001`

> The Launcher does **not** define architecture.  
> It only **executes what architecture already defines**.

---

## 3. Canonical Repository Structure

This is the **structural truth**. Any documentation that deviates from this must be rejected.

```
olivine-platform/
├── backend/              ← Unified Django gateway project (Port 8000)
├── frontend/             ← Unified React shell (Port 3001)
│
├── Retail/               ← Retail ownership boundary
│   ├── backend/
│   └── frontend/
│
├── HRM/                  ← HRM ownership boundary
│   ├── backend/
│   └── frontend/
│
├── CRM/                  ← CRM ownership boundary
│   ├── backend/
│   └── frontend/
│
├── FMS/                  ← FMS ownership boundary
│   ├── backend/
│   └── frontend/
│
├── Core/                 ← Shared canonical services (auth, org, licensing, ui-canon)
├── Common/               ← Shared infrastructure (qa launcher, shared services, utilities)
├── .steering/            ← Governance canon (single source of truth)
└── BBPs/                 ← Business process blueprints
```

### Critical Principle

> The folders `Retail/`, `HRM/`, `CRM/`, `FMS/` are **jurisdictional ownership zones**, not implementation details.

This is essential for:
- Agent boundaries (E, Astra, etc.)
- Governance enforcement
- Preventing architectural drift
- Preventing accidental cross-module contamination

---

## 4. Unified Backend (Port 8000)

**Path**:  
`backend/`

**Role**:  
This is a **Django project acting as an API gateway and aggregator**.

It does:
- Hosts the main Django project (`erp_core`)
- Defines `INSTALLED_APPS`
- Includes module routes
- Centralizes authentication, permissions, and tenancy

It does **not**:
- Own HRM business logic
- Own Retail domain code
- Contain module implementations

### Example (Conceptual)

```python
# backend/erp_core/settings/base.py
INSTALLED_APPS = [
    # Core services
    "core.org_structure.backend.company",
    "core.auth_access.backend.user_management",
    "core.licensing.backend.business_entities",

    # Aggregated modules
    "HRM.backend.hrm",
    "Retail.backend.sales",
    "Retail.backend.inventory",
    "CRM.backend",
    "FMS.backend.finance",
]
```

```python
# backend/erp_core/urls.py
urlpatterns = [
    path('api/hrm/', include('HRM.backend.hrm.urls')),
    path('api/retail/', include('Retail.backend.sales.urls')),
    path('api/crm/', include('CRM.backend.urls')),
    path('api/fms/', include('FMS.backend.finance.urls')),
]
```

---

## 5. Unified Frontend Shell (Port 3001)

**Path**:  
`frontend/`

**Role**:  
A single React application that provides:
- Unified routing across modules
- Shared layout (sidebar, toolbar, workspace)
- Shared UI canon components
- Module isolation via routes and imports

The frontend shell:
- Routes `/hrm/*` → HRM UI
- Routes `/retail/*` → Retail UI
- Routes `/crm/*` → CRM UI
- Routes `/fms/*` → FMS UI

It does **not** mean:
- That HRM frontend code lives inside `frontend/`
- That module teams lose ownership

Modules still own their UI under:
- `HRM/frontend/`
- `Retail/frontend/`
- `CRM/frontend/`
- `FMS/frontend/`

The unified shell **composes** them — it does not absorb them.

---

## 6. Startup Workflow (Canonical)

### Step 1 – Start Launcher
```bash
cd Common/qa-launcher-console/backend
npm start

cd Common/qa-launcher-console/frontend
npm run dev
```

### Step 2 – Use Launcher UI
Open:
```
http://localhost:5174
```

Select:
- ERP Core (Unified Backend + Unified Frontend)
- Or controlled execution modes (backend only / frontend only)

Launcher then executes:
- `backend/` → Django on 8000
- `frontend/` → React on 3001

---

## 7. Adding a New Module (Governance-Compliant Process)

Example: Adding `SCM/`

1. Create new top-level folder:
```
SCM/
  ├── backend/
  └── frontend/
```

2. Register SCM backend into unified backend:
- Update `backend/erp_core/settings/base.py`
- Add SCM app into `INSTALLED_APPS`

3. Add API routes:
- Update `backend/erp_core/urls.py`

4. Integrate UI into shell:
- Add routing into unified frontend shell
- Respect menu system (`ERPMenuItem` / menuConfig.ts)
- Respect mst/txn UI canon
- Respect toolbar contracts

5. Register SCM into Launcher:
- Update Launcher config (e.g. `application_registry.json`) if applicable

> No module is considered valid unless it respects:
> - Governance rules
> - UI canon
> - Ownership boundaries
> - Folder jurisdiction

---

## 8. Architectural Invariants (Non-Negotiable)

These principles are enforced across all documentation and execution:

- Modules live at top-level (`HRM/`, `Retail/`, etc.)
- `backend/` is a gateway, not a module container
- `frontend/` is a shell, not a module owner
- `.steering/` is the single source of governance truth
- Folder ownership boundaries must always be respected
- Agents (E, Astra, etc.) must never cross their jurisdiction

Any document that contradicts these is considered:
> **Architectural Drift — Must be corrected before acceptance**

---

## 9. Final Statement

This architecture intentionally balances:
- Unified user experience
- Strong module ownership boundaries
- Governance discipline
- Multi-agent collaboration safety

It is designed specifically to prevent:
- Repo entropy
- Accidental cross-module modification
- Agent hallucinated structure
- Drift between documentation and reality

This document is now aligned with:
- Governance canon
- Repo reality
- Agent boundary contracts
- Operational behavior
