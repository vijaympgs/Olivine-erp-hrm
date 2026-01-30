# ONBOARDING FOR AGENTS: STEP 4 - Frontend & UI Canon

## SPA STRUCTURE (Mandatory)

This structure is optimized for:
- Vite + React + TypeScript
- Tailwind CSS
- Enterprise-scale modular growth

### src/ (Application Source Root)
All runtime SPA code **must live inside `src/`**.

```
src/
├── app/          # Global providers (Auth, Layout). NO business logic.
├── modules/      # Domain-Driven Modules (One folder per domain).
├── components/   # Shared UI (Buttons, Inputs, Tables). Props only.
├── services/     # API Infrastructure (Auth, HTTP).
├── store/        # Global State (Zustand/Redux).
├── styles/       # Tailwind + Global CSS.
├── hooks/        # Shared Hooks.
├── utils/        # Formatters, Validators.
```

### Module Design (src/modules/)
Each business domain mirrors backend domains.
```
src/modules/procurement/
├── pages/        # Route screens
├── components/   # Module-specific UI
├── services/     # Module-specific API calls
├── hooks/        # Module-specific logic
├── types.ts      # Domain interfaces
└── index.ts      # Public API
```

---

## 🎨 UI CANON: LOOKUPS & MODALS (Strict)

**RULE**: Lookups are an extension of Sidebar + App Header, NOT independent island components.

**IMPLEMENTATION**: All lookups **MUST use `LookupContainer.tsx`**.

### Compliance Checklist:
1.  **Theme Identity**: Header uses EXACT SAME background gradient (`#14162A` → `#101223`) and Brand Color (`#22D3EE`) as the App Header.
2.  **Typography**: Use `Inter`. No custom fonts.
3.  **Interaction**: Keyboard-first (Escape closes, Auto-focus search).
4.  **Reusability**: Use generic `LookupContainer`. Do not build custom modal shells.

### Usage Example:
```typescript
import { LookupContainer } from '../../ui/components/LookupContainer';

export const ProductLookupModal = ({ isOpen, onClose, onSelect }) => (
  <LookupContainer
    isOpen={isOpen}
    onClose={onClose}
    title="Product Lookup"
    icon={<Package size={20} />} // Lucide icon
    searchBar={/* ... */}
  >
    {/* Results Table */}
  </LookupContainer>
);
```

### ❌ PROHIBITIONS:
- ❌ Use `bg-[#0078d4]` or hardcoded blues.
- ❌ Create custom modal headers that ignore the theme.
- ❌ Mix light headers with dark sidebar themes.

---

## VB.NET STYLE TOOLBAR
All "Document" pages (PO, Invoice, etc.) must use the `TransactionToolbar`.
- **Location**: Fixed at the top (Sticky).
- **Style**: High contrast, functional buttons.
- **Shortcuts**: Map F-keys (F1-F12) to actions where possible.

## TYPOGRAPHY
- **Primary Font**: `Inter`.
- **Weights**: 400 (Regular), 500 (Medium), 600 (SemiBold).
- **Numbers**: Use `tnum` (Tabular Numerals) for all data grids.

## NON-NEGOTIABLE RULES
1. One module = one domain.
2. No circular imports.
3. No cross-module component access (use shared `components/` if needed).
4. Pages never talk directly to HTTP (use `services/`).
