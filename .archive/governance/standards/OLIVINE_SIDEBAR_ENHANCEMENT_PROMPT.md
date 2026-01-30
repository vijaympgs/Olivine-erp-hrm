# Olivine Console — Sidebar Enhancement Master Prompt

## Context

We are building an enterprise-grade SaaS platform called **Olivine Console**.
A premium, dark-themed login screen is already implemented.

The sidebar must be visually elevated to the **same design maturity** and feel like a
**command / control console**, not a generic ERP navigation tree.

This task is **UI / UX enhancement only**.
No business logic, routing, or menuConfig structure changes are allowed.

Retail, HRM, CRM, and other modules must remain functionally unchanged.

---

## Objective

Enhance the **sidebar UI only** using:
- Typography
- Font system
- Color tokens
- Icons
- Dividers
- Spacing
- Interaction states

The result must be:
- Rich but restrained
- Enterprise-grade
- Visually unique to Olivine
- Consistent with the login screen

---

## Design Principles (Non-Negotiable)

1. Sidebar must feel like a **secure control console**
2. Reduce visual noise despite deep menu hierarchy
3. Phase-2 features must feel **advanced & gated**
4. Typography-first hierarchy (not icon-heavy)
5. Dark, calm, premium tone

---

## Font System (Mandatory)

### Font
**Inter**

```css
font-family: 'Inter', system-ui, -apple-system, sans-serif;
```

### Font Weights & Sizes

| Usage | Weight | Size |
|-------|--------|------|
| Module titles (L1) | 600 | 13–14px |
| Menu items (L2) | 500 | 13px |
| Sub-items (L3) | 400 | 12.5px |
| Section labels | 500 | 11px |
| Phase / badges | 500 | 10.5px |

**Rules:**
- ❌ Do NOT use 700+
- ❌ Do NOT use light fonts
- ❌ Avoid ALL CAPS except section labels

---

## Exact Tailwind Tokens (ADD AS-IS)

### `tailwind.config.js`

```javascript
theme: {
  extend: {
    colors: {
      sidebar: {
        bg: '#0E0F1A',
        surface: '#14162A',
        divider: 'rgba(255,255,255,0.08)',
      },
      text: {
        primary: '#E7E9F1',
        secondary: '#A4A7C1',
        muted: '#6F7396',
      },
      accent: {
        primary: '#7C6AF2',
        soft: 'rgba(124,106,242,0.15)',
        subtle: 'rgba(124,106,242,0.08)',
      },
    },
    fontFamily: {
      sans: ['Inter', 'system-ui', 'sans-serif'],
    },
    fontSize: {
      xs2: '10.5px',
      xs3: '11px',
    },
    transitionDuration: {
      fast: '120ms',
      normal: '180ms',
    },
  },
}
```

---

## Icon Strategy

**Icon library:** Lucide

**Rules:**
- ✅ Icons only for Level-1 modules
- ❌ No icons for L2 / L3 items
- `stroke-width: 1.5;`
- `opacity: 0.85;`

**Active icon color:**
```css
text-accent-primary
```

**Inactive icon color:**
```css
text-text-muted
```

---

## Divider Style (Optical Only)

No solid borders.

```jsx
<div className="my-3 h-px bg-gradient-to-r from-transparent via-sidebar-divider to-transparent" />
```

**Use dividers only:**
- Between modules
- Before Phase-2
- Before Admin / System

---

## Hover & Active States

### Hover
```css
hover:bg-white/5
```

### Active (Olivine Signature)
```css
bg-accent-soft
border-l-[3px] border-accent-primary
shadow-[inset_0_0_0_1px_rgba(124,106,242,0.2)]
```

---

## Phase-2 Visual Language

### Label
```
⚡ ADVANCED
```

### Style
```css
text-xs3
tracking-widest
uppercase
text-[#B5AFFF]
```

### Container
```css
bg-accent-subtle
rounded-lg
p-2
```

**Phase-2 may be:**
- Collapsible
- Role-gated
- Visually separated

---

## React Sidebar JSX Skeleton (STRUCTURE ONLY)

```jsx
<aside className="w-64 bg-sidebar-bg text-text-primary font-sans h-screen flex flex-col">

  {/* Header */}
  <div className="px-4 py-3 text-sm font-semibold tracking-wide">
    Olivine
  </div>

  <div className="my-2 h-px bg-gradient-to-r from-transparent via-sidebar-divider to-transparent" />

  {/* Navigation */}
  <nav className="flex-1 overflow-y-auto px-2 space-y-4">

    {/* Module */}
    <div>
      <div className="flex items-center gap-2 px-2 py-2 text-sm font-semibold text-text-secondary">
        <Icon className="w-4 h-4 text-text-muted" />
        Financial Management
      </div>

      <div className="ml-6 space-y-1">
        <NavItem label="Overview" active />
        <NavItem label="General Ledger" />
        <NavItem label="Receivables" />
        <NavItem label="Payables" />
        <NavItem label="Cash & Bank" />
        <NavItem label="Tax" />
        <NavItem label="Reports" />
        <NavItem label="Period Close" />
      </div>
    </div>

    <div className="my-3 h-px bg-gradient-to-r from-transparent via-sidebar-divider to-transparent" />

    {/* Phase 2 */}
    <div className="rounded-lg bg-accent-subtle p-2">
      <div className="mb-2 text-xs3 tracking-widest uppercase text-[#B5AFFF]">
        ⚡ Advanced
      </div>

      <div className="ml-2 space-y-1">
        <NavItem label="Multi-Currency & FX" />
        <NavItem label="Consolidation" />
        <NavItem label="Treasury" />
        <NavItem label="Revenue Recognition" />
      </div>
    </div>

  </nav>

</aside>
```

### NavItem Reference (Styling Intent)

```jsx
function NavItem({ label, active }) {
  return (
    <div
      className={clsx(
        'px-3 py-2 rounded-md text-sm cursor-pointer transition-colors duration-normal',
        active
          ? 'bg-accent-soft border-l-[3px] border-accent-primary'
          : 'hover:bg-white/5 text-text-secondary'
      )}
    >
      {label}
    </div>
  )
}
```

---

## DO NOT

- ❌ Do not change menuConfig logic
- ❌ Do not flatten hierarchy
- ❌ Do not add icons everywhere
- ❌ Do not use generic admin panel styles
- ❌ Do not mix fonts

---

## Success Criteria

When done:

✅ Sidebar visually matches login maturity  
✅ Finance feels authoritative and calm  
✅ Phase-2 feels advanced, not noisy  
✅ Sidebar feels engineered, not templated

---

## Implementation Files

### Files to Update

1. **Sidebar Component**
   - `frontend/src/ui/components/Sidebar.tsx`
   - Update layout structure, spacing, active/hover states

2. **Tailwind Config**
   - `frontend/tailwind.config.cjs`
   - Add color tokens, font family, spacing tokens

3. **Global Styles**
   - `frontend/src/styles/index.css` or `globals.css`
   - Add Inter font import
   - Add CSS custom properties if needed

4. **Menu Renderer**
   - Update icon rendering rules (L1 only)
   - Update Phase-2 grouping visuals
   - Update divider placement logic

### Font Loader

Add to `index.html` or main layout:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap">
```

---

## Color Tokens Reference

```css
/* Sidebar */
--sidebar-bg: #0E0F1A;
--sidebar-surface: #14162A;
--sidebar-divider: rgba(255,255,255,0.08);

/* Text */
--text-primary: #E7E9F1;
--text-secondary: #A4A7C1;
--text-muted: #6F7396;

/* Accent */
--accent-primary: #7C6AF2;
--accent-soft: rgba(124,106,242,0.15);
--accent-subtle: rgba(124,106,242,0.08);
```

---

## Spacing System

```css
/* Sidebar padding */
padding: 12px 10px;

/* Menu item padding */
padding: 8px 10px;

/* Menu border-radius */
border-radius: 8px;

/* Group spacing */
margin-top: 14px;
```

**Whitespace is intentional — do not compact.**

---

## Micro-Interactions

- **Expand / collapse:** 180ms ease
- **Active indicator slide:** 120ms
- **Hover delay:** 40ms
- ❌ No bounce, no flashy animations

---

## Phase Implementation

### Phase 1: Foundation
1. Add Tailwind tokens
2. Import Inter font
3. Update sidebar background colors
4. Apply typography system

### Phase 2: Structure
1. Update module headers (L1) with icons
2. Remove icons from L2/L3 items
3. Add optical dividers
4. Update spacing

### Phase 3: Interactions
1. Implement hover states
2. Implement active states with border-left accent
3. Add smooth transitions

### Phase 4: Phase-2 Styling
1. Create Phase-2 container with subtle background
2. Add "⚡ ADVANCED" label
3. Style Phase-2 items distinctly

---

## Validation Checklist

Before marking complete:

- [ ] Inter font loaded and applied
- [ ] All Tailwind tokens added
- [ ] Sidebar background is `#0E0F1A`
- [ ] Only L1 modules have icons
- [ ] Optical dividers between modules
- [ ] Active state has purple left border
- [ ] Hover state is subtle (`bg-white/5`)
- [ ] Phase-2 has distinct container
- [ ] Typography hierarchy is clear
- [ ] No visual fatigue despite menu depth
- [ ] Matches login screen maturity

---

**End of Master Prompt**
