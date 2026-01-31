
SCCB — TOOLBAR-GOVERNANCE-V2 (LOCKED)
Authority: Viji (Product Owner) + Mindra (Chief Architect)
Status: IMMUTABLE — No deviation without explicit approval
Applies to: Retail, HRM, FMS, CRM, all current and future modules

============================================================
CORE PRINCIPLE
============================================================

The toolbar is the SINGLE authoritative command surface for all UI actions.

- No row-based actions
- No hidden actions
- No implicit actions
- No per-component custom buttons
- No bypassing toolbar contract
- No "modern UX exceptions"

If an action exists, it must:
- Appear in the toolbar
- Be governed by mode
- Be permission-controlled
- Be traceable via ERPMenuItem.toolbar_* columns

Toolbar is LAW.

============================================================
MODES (CANONICAL)
============================================================

Every UI must operate strictly in one of these modes:

- LIST
- VIEW
- EDIT
- CREATE

No hybrid modes.
No implicit mutation outside EDIT/CREATE.

============================================================
MODE → ALLOWED ACTIONS CONTRACT
============================================================

LIST MODE (Multiple records visible)

Toolbar may contain ONLY:
- N → New
- R → Refresh
- Q → Quick Search
- F → First (optional navigation)
- V → View (requires exactly one record selected)
- E → Edit (requires exactly one record selected)
- D → Delete (requires ≥1 record selected)
- I → Import (stub allowed)
- O → Export (stub allowed)
- X → Exit

Rules:
- All user actions originate from toolbar
- No row-based buttons allowed
- No context menus allowed
- No double-click behavior allowed
- Selection is used only to validate toolbar actions
- LIST itself must never mutate data

------------------------------------------------------------

VIEW MODE (Single record, read-only)

Toolbar may contain ONLY:
- X → Exit
- E → Edit (if permission allows)
- D → Delete (if permission allows)

Rules:
- VIEW is strictly read-only
- No Save
- No mutation allowed
- No hidden changes
- VIEW exists purely for inspection + decision

------------------------------------------------------------

EDIT MODE (Entered explicitly via toolbar E)

Toolbar may contain ONLY:
- S → Save
- C → Clear
- X → Exit

Rules:
- This is the ONLY mode where mutation is allowed
- Save must validate against API contracts
- Exit must discard unsaved changes (unless confirmed)
- No Delete here

------------------------------------------------------------

CREATE MODE (Entered via toolbar N)

Toolbar may contain ONLY:
- S → Save
- C → Clear
- X → Exit

Rules:
- New object lifecycle only
- No Delete allowed here
- Save creates entity

============================================================
PERMISSION INTEGRATION
============================================================

All toolbar actions must be controlled via:

ERPMenuItem.toolbar_list
ERPMenuItem.toolbar_view
ERPMenuItem.toolbar_edit
ERPMenuItem.toolbar_create

Permissions system must:
- Enable/disable actions per user per menu_id
- Never hide logic inside component
- Never allow component to override contract

If user does not have permission:
- Action must be disabled or not rendered
- No workaround logic allowed

============================================================
STRICT PROHIBITIONS (NON-NEGOTIABLE)
============================================================

You must NOT:
- Add row-based edit/delete buttons
- Add per-component action buttons
- Trigger actions outside toolbar
- Use local component state to control allowed actions
- Hardcode toolbar behavior inside screens
- Invent new actions without updating contract
- Create alternative command surfaces
- Bypass ERPMenuItem.toolbar_* contract

Violation = architectural breach.

============================================================
DATA FLOW (CANONICAL PIPELINE)
============================================================

ERPMenuItem (database)
        ↓
menuConfig / registry sync (seeded or mirrored)
        ↓
useToolbarConfig resolves actions by:
    (menu_id + mode + permissions)
        ↓
MasterToolbar renders allowed actions
        ↓
UI dispatches commands strictly via toolbar

No direct component control.
No ad-hoc buttons.
No exceptions.

============================================================
RATIONALE (DO NOT DESIGN AROUND THIS)
============================================================

This governance ensures:
- Deterministic automation (Test Console, Playwright)
- Predictable permission enforcement
- Zero drift across modules
- Long-term maintainability
- Enterprise-grade auditability
- Platform-level consistency

This is intentional rigidity.

============================================================
FINAL STATUS
============================================================

This document is LOCKED as:
toolbar-governance-v2

All agents must comply.
Any deviation requires explicit approval from Viji.

END OF SCCB


┌──────────────────────────────────────────────────────────┐
│                    GOVERNANCE LAYER                       │
│  (Locked contracts: modes, actions, behavior, SCCB rules) │
│  - LIST / VIEW / EDIT / CREATE                            │
│  - Mode → Action law                                       │
│  - No row actions, no component overrides                  │
└──────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│                  POLICY BASELINE (STATIC)                 │
│                  ERPMenuItem Table (DB)                   │
│----------------------------------------------------------│
│ menu_id                                                   │
│ toolbar_list                                              │
│ toolbar_view                                              │
│ toolbar_edit                                              │
│ toolbar_create                                            │
│----------------------------------------------------------│
│ Purpose: Defines MAXIMUM allowed actions per screen       │
│ Stable, deterministic, environment-agnostic               │
└──────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│           FUTURE OVERLAY: PERMISSION RESOLUTION           │
│              (Not required today, supported)              │
│----------------------------------------------------------│
│ User → Role → Permission Matrix                            │
│ License restrictions                                      │
│ Company / Context overrides                                │
│----------------------------------------------------------│
│ Result: May only REDUCE actions from ERPMenuItem           │
│ Never expands beyond baseline                              │
└──────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│              BACKEND POLICY RESOLVER (API)                │
│----------------------------------------------------------│
│ Input: viewId, mode, user, context                         │
│ Logic:                                                     │
│   - Read ERPMenuItem baseline                              │
│   - Apply permission overrides (future)                    │
│   - Return final allowed actions                           │
│ Output: ['N','R','Q','V','X'] etc                           │
└──────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│            CENTRAL TOOLBAR ENGINE (Frontend)              │
│----------------------------------------------------------│
│ Receives allowedActions[]                                  │
│ Renders toolbar buttons                                    │
│ Enforces mode purity                                       │
│ No business logic inside screens                           │
│ One implementation for entire platform                     │
└──────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│                 ALL SCREENS (DUMB CONSUMERS)              │
│----------------------------------------------------------│
│ Employee Records                                          │
│ Item Master                                               │
│ Purchase Orders                                           │
│ Invoices                                                  │
│ 200+ screens...                                           │
│----------------------------------------------------------│
│ Screens do ONLY:                                           │
│   - Provide viewId                                         │
│   - Track mode (LIST/VIEW/EDIT/CREATE)                     │
│   - Never decide buttons                                  │
│   - Never hardcode actions                                │
└──────────────────────────────────────────────────────────┘