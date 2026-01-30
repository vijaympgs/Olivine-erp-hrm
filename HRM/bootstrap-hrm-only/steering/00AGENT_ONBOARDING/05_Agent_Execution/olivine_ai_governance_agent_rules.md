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
