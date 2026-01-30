# SPA_STRUCTURE.md

## Purpose
This document defines the **standard Single Page Application (SPA) structure**
for the Olivine Retail ERP frontend.  
It is the **single source of truth** for frontend layout, module boundaries,
and design discipline.

This structure is optimized for:
- Vite + React + TypeScript
- Tailwind CSS
- Enterprise-scale modular growth
- AI-assisted development (predictable paths)

---

## Root Structure

frontend/
├── src/
├── docs/
├── public/
├── package.json
├── vite.config.mts
├── tailwind.config.cjs
├── tsconfig.json
├── index.html
└── README.md

---

## src/ (Application Source Root)

All runtime SPA code **must live inside `src/`**.

src/
├── app/
├── modules/
├── components/
├── routes/
├── services/
├── store/
├── styles/
├── hooks/
├── utils/
├── App.tsx
└── main.tsx

---

## app/ (Application Shell & Providers)

Global application wiring only.

src/app/
├── AppProviders.tsx
├── ErrorBoundary.tsx
├── AuthGuard.tsx
└── LayoutProvider.tsx

Rules:
- No business logic
- No API calls
- No domain logic

---

## modules/ (Domain-Driven SPA Modules)

Each business domain mirrors backend domains.

src/modules/
├── pos/
├── inventory/
├── procurement/
├── sales/
├── customers/
├── finance/
└── hr/

### Example: POS Module

src/modules/pos/
├── pages/
├── components/
├── services/
├── hooks/
├── types.ts
└── index.ts

Rules:
- Pages = route-level screens
- Components = POS-only UI
- Services = POS API calls only
- No cross-module imports

---

## components/ (Shared UI Components)

Reusable, domain-agnostic UI components.

src/components/
├── layout/
├── navigation/
├── forms/
├── tables/
├── feedback/
└── ui/

Rules:
- No business rules
- No API calls
- Props-driven only

---

## routes/ (Routing Configuration)

Centralized route definitions.

src/routes/
├── index.tsx
├── protected.routes.tsx
└── public.routes.tsx

Rules:
- Routes reference pages only
- No JSX business logic

---

## services/ (Shared Infrastructure Services)

Cross-cutting technical services.

src/services/
├── http.ts
├── auth.service.ts
├── storage.service.ts
└── feature-flags.ts

Rules:
- No UI imports
- No React components

---

## store/ (State Management)

Global and module-level state.

src/store/
├── index.ts
├── auth.store.ts
└── ui.store.ts

Rules:
- No API calls inside reducers
- Async logic via services

---

## styles/ (Design System & Tokens)

src/styles/
├── globals.css
├── tailwind.css
├── tokens.css
└── themes.css

Rules:
- No inline magic values
- Tokens first

---

## hooks/ & utils/

src/hooks/
├── useDebounce.ts
├── usePermission.ts
└── useTheme.ts

src/utils/
├── formatters.ts
├── validators.ts
└── constants.ts

---

## docs/ (Frontend Documentation)

All markdown documentation lives here.

docs/
├── DESIGN_SYSTEM.md
├── TYPOGRAPHY_SYSTEM.md
├── SIDEBAR_NAVIGATION_SPEC.md
├── SPA_STRUCTURE.md
└── UI_LAYOUT_TERMINOLOGY.md

Rules:
- No docs inside src/
- Docs do not import code

---

## Explicit Exclusions (Never Included)

The following must NEVER appear in SPA structure docs:

- node_modules/
- dist/
- .vite/
- *.map
- package internals

---

## Non-Negotiable Rules

1. One module = one domain
2. No circular imports
3. No cross-module component access
4. Shared UI only via `components/`
5. Services never import UI
6. Pages never talk directly to HTTP

---

## Final Note

Any new frontend work MUST:
- Respect this structure
- Place files in the correct boundary
- Update this document only if architecture evolves

This document is **authoritative**.
