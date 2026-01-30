# 📋 UNIVERSAL IMPLEMENTATION CHECKLIST (GOVERNANCE CANON)

**Status**: ✅ ACTIVE AUTHORITY  
**Scope**: All Modules (Retail, FMS, HRM, CRM)  
**Applies To**: Masters, Transactions, Reports, Dashboards  

> **PROTOCOL (NON-NEGOTIABLE)**  
> This checklist must be executed **BEFORE**, **DURING**, and **AFTER** every screen implementation.  
> Failure to follow this checklist constitutes an **incomplete and invalid delivery**.

---

## 1. 🛑 PRE-FLIGHT VALIDATION (MANDATORY BEFORE CODING)

> You are **not permitted to write or refactor code** until this section is completed.

- [ ] **Legacy Functionality Audit**
  - [ ] Enumerate every visible element: buttons, fields, tabs, grids, badges.
  - [ ] Identify hidden logic flows (auto-calculation, conditional behavior, disabled states).
  - [ ] Capture screenshots OR produce a precise mental model of existing behavior.
  - [ ] Confirm: _“I fully understand the current screen before touching it.”_

- [ ] **Service Layer Verification**
  - [ ] Open the corresponding `*Service.ts` file.
  - [ ] **CRITICAL RULE**: Identify **all fields** defined in service contracts (even if not shown in UI today).
  - [ ] Confirm that the new UI will include:
    - Old UI fields  
    - + Service contract fields  
    - − **No silent drops allowed**

- [ ] **Routing Awareness**
  - [ ] Locate existing route in `router.tsx`.
  - [ ] Identify whether implementation is:
    - In-place upgrade, OR  
    - Path migration  
  - [ ] Explicitly plan transition:  
    - `Existing Route` → `New Route`  
    - With no broken navigation.

---

## 2. 🏗️ ARCHITECTURE & CONFIG DISCIPLINE

> If this layer is wrong, everything above it becomes fragile.

- [ ] **Toolbar Configuration Integrity**
  - [ ] Define toolbar config string (e.g., `NESCKVDXRQF`).
  - [ ] Confirm corresponding entry exists in backend:
    - `ERPMenuItem`
    - `seed_toolbar_controls.py` or CSV seed
  - [ ] Explicitly validate mode behavior:
    - VIEW  
    - EDIT  
    - CREATE  
    are all correctly respected.

- [ ] **Container Pattern Compliance**
  - [ ] **Masters** must use:
    - `MasterToolbar`
    - Setup layout (Tabbed / Dense Form)
  - [ ] **Transactions** must use:
    - Toolbar + Workflow layout
    - List ↔ Detail behavior correctly wired

- [ ] **Permission Enforcement**
  - [ ] **Admin Law**: Built-in admin must always resolve to full permission mask (`111111...`).
  - [ ] Toolbar must receive resolved permissions dynamically.

- [ ] **Navigation Logic**
  - [ ] **Smart Exit**: 'Exit' action from Form mode must return to List mode (not Dashboard).
  - [ ] **Cancel**: 'Cancel' in Form mode returns to List mode.

---

## 3. 🧩 MASTERS (Item, Customer, Supplier, etc.)

> These are not CRUD demos. These are enterprise data control panels.

- [ ] **Screen Structure (STRICT)**
  - [ ] **Unified Container Only**:
    - List and Form Logic MUST be in the same component (State-based swap).
    - Router points to ONE file (the Setup component).
    - NO separate `ListPage.tsx`.
  - [ ] **Persistent Context**:
    - Master Title/Header must remain visible in both List and Form views.

- [ ] **Data Density Discipline**
  - [ ] Tabs present where required:
    - General  
    - Details  
    - Domain-specific (UOM, Addresses, Variants, etc.)
  - [ ] **No Skeleton Rule**:
    - Do NOT ship “basic now, we’ll add later”
    - Full richness first, refinement later.

- [ ] **Parity Guarantee**
  - [ ] Does the new UI support every capability the old UI supported?
  - [ ] Are metadata fields respected (Created By, Updated By, timestamps)?
  - [ ] Nothing removed silently.

---

## 4. 📝 TRANSACTIONS (PO, SO, Invoice, etc.)

> Transaction screens are governed by workflow correctness, not visual completion.

- [ ] **Navigation Controls**
  - [ ] First  
  - [ ] Previous  
  - [ ] Next  
  - [ ] Last  
  must be wired and functional.

- [ ] **Workflow Correctness**
  - [ ] Buttons (`Submit`, `Authorize`, `Reject`, etc.) appear **only** when allowed.
  - [ ] Status badge clearly visible and accurate (DRAFT, POSTED, etc.).

- [ ] **Operational Inputs**
  - [ ] Date range filters where applicable.
  - [ ] Line entry grids functional (not placeholders).
  - [ ] No broken add/remove/edit row flows.

---

## 5. 📊 REPORTS & DASHBOARDS

> Visual correctness is meaningless without data correctness.

- [ ] **Filter Panel**
  - [ ] F4 (or equivalent) filter panel present.
  - [ ] Supports core filters:
    - Date range  
    - Company  
    - Location  

- [ ] **Export Integrity**
  - [ ] Export works (CSV / PDF where applicable).
  - [ ] Exported data matches UI data.

- [ ] **Performance Discipline**
  - [ ] Server-side pagination enforced.
  - [ ] No full dataset loading for large reports.

---

## 6. ✅ FINAL VERIFICATION GATE (MERGE BLOCKER)

> You are **not allowed to declare completion** unless every item below passes.

- [ ] **Zero Regression Test**
  - [ ] Can I do everything the previous screen allowed?
  - [ ] No capability lost.

- [ ] **Build Integrity**
  - [ ] Vite build passes.
  - [ ] No unresolved imports.
  - [ ] No runtime crashes.

- [ ] **Console Hygiene**
  - [ ] No React warnings (keys, effects, hooks).
  - [ ] No red errors in console during normal flow.

- [ ] **Structural Discipline**
  - [ ] Folder boundaries respected (`apps/`, `core/`, `common`).
  - [ ] No cross-module leakage.
  - [ ] No architectural drift.

---

## 7. 🧨 ABSOLUTE FAILURE CONDITIONS

Any of the following immediately invalidates the delivery:

- Skeleton UI shipped for a complex master  
- Data exists in backend but list shows “No records”  
- Create form does not open or does not save  
- Fields removed without approval  
- Refactor treated as rewrite  
- Toolbar correct but screen functionally broken  

> Toolbar correctness **without functional correctness = FAILED DELIVERY**

---

**Last Updated**: 2026-01-10  
**Authority**: Viji (Final)  
**Classification**: Platform Governance Canon  

