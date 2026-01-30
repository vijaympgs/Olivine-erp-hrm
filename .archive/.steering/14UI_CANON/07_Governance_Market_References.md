# CONSOLIDATED GOVERNANCE RULES
Generated consolidation of 4 files.



================================================================================
FILE START: agent.olivine_ruleset.md
================================================================================

# Olivine ERP Ruleset
### Version: 1.0.0
### Last Updated: 06-Dec-2025 , 16:51PM  
### Source Authority: BBP v0.4 + Project Naming/Architecture 

Purpose: To ensure all AI-assisted development follows the BBP, design language, architecture, templates, and execution workflow — with consistency, traceability, and zero assumptions.

1️⃣ System Rules (Behavior Layer)

These govern HOW the AI behaves.

- The BBP is the single source of truth.
- Never invent fields, statuses, relationships, processes, or logic.
- If information is missing or unclear → ask before generating.
- Follow the defined folder structure, naming conventions, and module patterns.
- All generated code must match the tech stack:
  React 18 + TypeScript + Vite + Tailwind.
- Always follow ELOBS execution flow when building modules.
- Use the correct template (mst01/mst02/mst03/txn01/txn02/txn03).
- Apply validation rules as defined in BBP.
- Generate readable, modular, maintainable code.
- Do not generate delete functionality where the BBP specifies soft-deactivation.

2️⃣ BBP Rules (Domain Layer)
- Located in: /docs/bbp/*
- Treated as the authoritative business rule definition.
- Every module must map:
  • Fields
  • Data Types
  • Relationships
  • Statuses
  • Business Rules
  • Lifecycle Behavior
- Modules must not diverge from BBP definitions.
- If a BBP file exists for a module, it must be referenced before generating code.
- If BBP is updated, code must be updated accordingly.

3️⃣ Template Rules (Module Structure Layer)

Templates define HOW modules are shaped.

Location: /docs/templates/*

Template Mappings:
- mst01 → Simple Master (flat fields, low logic)
- mst02 → Medium Master (relationships + rules)
- mst03 → Complex Master (variants, nested structures)
- txn01 → Simple Transaction
- txn02 → Medium Workflow Transaction
- txn03 → Complex ERP Workflow

Rules:
- All module generation must start by selecting the correct template.
- UI patterns, file names, folder structure, and component boundaries come from the template.
- Templates must NOT be modified without explicit approval.

4️⃣ Build Guide Rules (Execution Process – ELOBS)
E = Extract
    Read BBP fields, relationships, statuses, and rules.

L = Layout
    Apply template (mst or txn) to determine structure.

O = Organize
    Create the correct file/folder scaffolding.

B = Build
    Generate code in the following order:
      1. Types
      2. Validation Schema
      3. Service Layer (mock → live)
      4. Hooks
      5. UI Screens (list → form → filters)
      6. Routing + Sidebar registration

S = Sync
    Cross-check against BBP and template and correct inconsistencies.

5️⃣ Folder & Naming Rules
src/modules/<module>/
    <module>.types.ts
    <module>.schema.ts (Zod when needed)
    <module>.service.ts
    use<Module>.ts
    <Module>Page.tsx


Routing location: src/app/router.tsx
Sidebar entry: src/ui/components/Sidebar.tsx

Naming rules:

- PascalCase for components
- camelCase for variables and hooks
- kebab-case for folders
- Suffixes: .types.ts, .service.ts, .schema.ts, .tsx

6️⃣ Interaction Rules (How to Command Continue)
Future requests should be short execution commands, not full instructions.

Examples:

✔ Generate module "Company" using mst01 and BBP section 1.1. Follow ELOBS.
✔ Update Locations based on new BBP rules. Only modify affected files.
✔ Add validation changes for Company status rule.

Not allowed:

✘ "Create a Company module with random fields"
✘ Long conversational instructions.
✘ New rules unless explicitly approved.

7️⃣ Versioning & Governance Rules
- BBP updates must increment version numbers.
- Code should reflect the latest BBP version.
- Breaking rule changes must be confirmed before applying.
- Template changes must be explicitly approved.


📦 Updated Rule Block to Append to the Ruleset (copy-paste into Olivine_Ruleset.md)
### 🚧 Navigation + Routing Construction Rule (Applies to All Modules)

For every new module generated using mst01, mst02, mst03, txn01, txn02, or txn03:

1. **Routing Registration**
   - The route must be added automatically to the main router file:
     `src/app/router.tsx` (or the current router location).
   - The module page component must be imported.
   - The route must be nested under the protected `AppLayout` block.
   - Example expected format:

   ```tsx
   {
     path: "<module-name>",
     element: <ModuleNamePage />,
   }


2. **Sidebar Registration**

The module must appear in the sidebar automatically.
The sidebar group (section header) must match the BBP module classification:
Organization
Merchandising
Operations
Procurement
Finance
System

Each module must use the same NavLink styling pattern as existing items.
Example expected format:

<NavLink
  to="/<module-name>"
  className={({ isActive }) =>
    `block px-4 py-2 rounded-md transition-colors ${
      isActive ? "bg-emerald-700 text-white" : "text-white/80 hover:bg-emerald-800"
    }`
  }
>
  <ReadableLabel />
</NavLink>


No manual steps should be required.
If automatic placement is ambiguous, Continue must ask before inserting.
Validation Before Completion
Confirm route exists by simulated navigation path: /<module-name>

Confirm sidebar item appears after login.

🧪 Acceptance Test for Continue:

“A newly generated module must always be reachable by both typing the URL path and using the sidebar navigation link.”



================================================================================
FILE END: agent.olivine_ruleset.md
================================================================================



================================================================================
FILE START: olivine_ai_governance_agent_rules.md
================================================================================

# Olivine Engineering Governance Rules

> This document defines **non-negotiable engineering, layout, UX, and system
> governance rules** for the Olivine platform.
>
> These rules apply to **any human or AI coding assistant (including Astra)**
> connected via VS Code or any IDE.
>
> Tool choice is irrelevant. **Rules are permanent.**

---

## Rule 1 — Authority & Decision Ownership

**Intention:** Define who decides and who executes.

- Final authority: **Viji** (Founder, Architect)
- Humans and tools execute under defined rules
- No tool or contributor may reinterpret intent
- “Looks fine”, “industry standard”, or “AI suggested” is not justification

**Principle:**  
> Decisions come from architecture, not tools.

---

## Rule 2 — Platform Scope & Longevity

**Intention:** Ensure all changes scale with the full product vision.

Olivine is a unified enterprise platform comprising:
- Retail ERP
- POS
- FMS (Finance & Funds Management)
- HRM
- CRM (future)
- Code-extender / No-code layer (future)

This is a **long-lived enterprise system**, not a prototype.

---

## Rule 3 — Enterprise Reference Baselines

**Intention:** Establish the minimum quality bar.

All implementations must meet expectations set by mature systems:

**HRM:** SAP, PeopleSoft, greytHR  
**FMS:** Tally, NetSuite, Microsoft Dynamics Finance  
**Retail / POS:** Epicor, SAP Retail, NetSuite Retail, Toast, Square  
**CRM:** Salesforce, HubSpot, Microsoft Dynamics CRM  

These systems define:
- Data density
- Workflow depth
- Permissions & auditability
- UX seriousness

---

## Rule 4 — Folder Structure Is Law

**Intention:** Prevent structural drift.

### Frontend (SPA)
- `frontend/` or `spa/` is the only frontend root
- `src/app` → application shell, layout, routing
- `src/modules` → domain modules
- `src/pages` → page containers only
- `src/components` / `src/ui` → reusable UI
- `src/styles` → global styling system

### Backend
- `backend/` is authoritative
- `backend/domain` → business domains
- `backend/common` → shared utilities
- `backend/settings/base.py` → source of truth
- `backend/settings/dev.py` extends base.py

No duplication. No parallel structures.

---

## Rule 5 — Layout & Typography Ownership Model (CRITICAL)

**Intention:** Prevent layout, typography, and sidebar regressions.

Olivine follows a **config-driven, four-layer layout architecture**:

1. **TypeScript Configuration (Source of Truth)**  
   `frontend/src/config/layoutConfig.ts`

2. **Runtime Application Layer**  
   `LayoutManager` applies config as CSS variables

3. **CSS Execution Layer**  
   `frontend/src/styles/layout.css`

4. **Utility Layer (Consumer Only)**  
   `frontend/tailwind.config.cjs`

> TypeScript defines intent.  
> CSS executes intent.  
> Tailwind assists intent.

---

## Rule 6 — Sidebar Ownership & Navigation Discipline

**Intention:** Ensure navigation clarity without side effects.

- Sidebar width, collapse, visibility → `layoutConfig.ts`
- Sidebar typography MAY differ from content
- Sidebar fonts MUST:
  - Be defined in `layoutConfig.ts`
  - Be exposed via `LayoutManager`
  - Be applied ONLY in sidebar scope (`layout.css`)

**Approved sidebar fonts:**
- IBM Plex Sans (preferred)
- Source Sans 3
- Manrope (use cautiously)

Forbidden:
- Hardcoded sidebar CSS
- Tailwind-only sidebar changes
- Component-level overrides

---

## Rule 7 — Global Typography & Design Tokens

**Intention:** Maintain visual consistency.

- **Inter** is the global default font
- Typography, spacing, colors are token-driven
- Tokens are owned by:
  - `layoutConfig.ts`
  - `layout.css`
- Tailwind mirrors tokens only

No inline styles. No arbitrary values.

---

## Rule 8 — Backend Architecture Discipline

**Intention:** Preserve domain and data integrity.

- Search for existing models before creating new ones
- Never duplicate core entities
- Respect domain boundaries
- Prefer composition over duplication
- No manual DB changes

---

## Rule 9 — Development Behavior (Zero Patch Culture)

**Intention:** Prevent entropy.

Forbidden:
- TODO-driven development
- Temporary hacks
- Silent dependency upgrades
- Global refactors without approval

Every change must be:
- Scoped
- Intentional
- Reversible
- Stable across domains

---

## Rule 10 — Mandatory Pre-Change Review

Before any change, review:

**Frontend**
- `layoutConfig.ts`
- `layout.css`
- `index.css`
- `tailwind.config.cjs`
- App shell / layout

**Backend**
- `settings/base.py`
- Domain models
- Existing migrations

Skipping this review invalidates the change.

---

## Rule 11 — Completion & Validation Law

A change may be marked complete ONLY if:
- Matches architectural intent exactly
- No regression across Retail, POS, FMS, HRM, CRM
- LayoutManager flow intact
- No UX drift
- Build passes

If unsure → stop and ask Viji.

---

## Rule 12 — Security & Access Discipline

**Intention:** Protect enterprise data.

- No bypassing auth or permission layers
- No hardcoded secrets or tokens
- Role-based access must be enforced consistently
- Auditability is mandatory for finance, HR, and POS flows

Security bugs are correctness bugs.

---

## Rule 13 — Performance & Scalability Discipline

**Intention:** Ensure enterprise-scale readiness.

- Avoid N+1 patterns (API, DB, UI)
- No unnecessary re-renders or heavy client logic
- Respect pagination, lazy loading, and batching
- Performance regressions are treated as failures

---

## Rule 14 — Observability & Operability

**Intention:** Ensure the system can be understood and operated.

- Errors must be explicit, not silent
- Logs must be meaningful
- Failures must be diagnosable
- Enterprise systems must explain themselves

---

## Rule 15 — Permanence Clause

**Intention:** Make these rules timeless.

- These rules override task-level instructions
- Conflicts require explicit override from **Viji**

> Discipline preserves enterprise systems.  
> Velocity without rules destroys them.

---

## Rule 16 — Phase 2 Menu Management & Module Visibility

**Intention:** Ensure Phase 2 features are properly gated and modules can be selectively shown/hidden based on user needs.

### Phase 2 Menu System
- Phase 2 features are marked with `isPhase2: true` in `menuConfig.ts`
- Phase 2 visibility is controlled by `config.sidebar.showPhase2` in `layoutConfig.ts`
- Default state: **Phase 2 hidden** (`showPhase2: false`)
- Toggle location: **System Administration → Layout Settings**

### Module Visibility System
- Individual modules can be shown/hidden independently
- Module visibility controlled by:
  - `config.sidebar.showRetail` - Retail Operations module
  - `config.sidebar.showFinance` - Financial Management module
  - `config.sidebar.showCRM` - Customer Relationship Management module
  - `config.sidebar.showHRM` - Human Resources Management module
- Default state: **All modules visible** (all flags `true`)
- Toggle location: **System Administration → Layout Settings → Module Visibility**

### Configuration Reactivity Pattern
When layout configuration changes are saved:
1. `LayoutManager.saveConfig()` must dispatch `layout-config-update` event
2. `useLayoutConfig` hook must listen for both:
   - `storage` event (cross-tab updates)
   - `layout-config-update` event (same-tab updates)
3. Components using layout config must update **immediately** without page reload

### Implementation Rules
- **Never** bypass the event system for configuration updates
- **Always** use `layoutManager.saveConfig()` instead of direct localStorage writes
- **Never** require page reload for configuration changes (except where explicitly documented)
- Phase 2 filtering must be **recursive** (filter children, hide empty parents)
- Module filtering must be applied **after** Phase 2 filtering
- Module IDs to check: `'retail'`, `'finance'`, `'crm'`, `'hr'`

### Files Involved
- `frontend/src/config/layoutConfig.ts` - Configuration source of truth
- `frontend/src/hooks/useLayoutConfig.ts` - Reactive hook
- `frontend/src/ui/components/Sidebar.tsx` - Phase 2 and module filtering logic
- `frontend/src/pages/admin/LayoutSettingsPage.tsx` - UI controls

**Rationale:**  
> Enterprise users expect immediate feedback and flexible module visibility. Configuration changes that require manual page reloads create friction and appear broken. Event-driven reactivity ensures the UI stays synchronized with user intent. Module visibility allows users to focus on specific business areas without clutter from unused modules.

---

**End of Olivine Engineering Governance Rules**


================================================================================
FILE END: olivine_ai_governance_agent_rules.md
================================================================================



================================================================================
FILE START: system-rules.md
================================================================================

SYSTEM RULES FOR PROJECT: OLIVINE ERP

You must always read and follow the BBP documents located in:

/docs/bbp/*

The BBP is the single source of truth for:
- fields
- validations
- statuses
- relationships
- master data logic
- workflow sequences
- permissions
- naming and formatting rules

Never generate fields or logic that are not present in the BBP unless the user explicitly approves something new.

Module generation order:
1. Company
2. Locations
3. Attributes
4. Attribute Values
5. UOM
6. Product (SKU)
7. Supplier
8. Procurement Lifecycle
9. RBAC

Templates:
- _mst_01: Simple master
- _mst_02: Medium master (relations, rules)
- _mst_03: Complex master (variants, nested lines)

When generating code:
- Use React + TS + Vite + Tailwind
- Create types → services → hooks → UI → routing → sidebar
- Follow folder structure: src/modules/{name}/...

If unsure — ask before generating.


================================================================================
FILE END: system-rules.md
================================================================================



================================================================================
FILE START: 06prompt-ui-governance.md
================================================================================

# UI Governance Prompt

SPA & UI standards.


================================================================================
FILE END: 06prompt-ui-governance.md
================================================================================

