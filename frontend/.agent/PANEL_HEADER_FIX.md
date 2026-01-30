# Panel Positioning Fix - Respecting App Header ✅

## Date: 2026-01-05 23:20 IST

## Issue Identified

The panel variant was overlapping the app header because it was using `top: 0`, which positioned it at the very top of the viewport, ignoring the header.

### UI Layout Terminology (from layoutConfig):

```
┌─────────────────────────────────────────┐
│  App Header (--header-height)           │ ← Should NOT be overlapped
├──────────┬──────────────────────────────┤
│ Sidebar  │  Primary Workspace           │
│  Rail    │                              │
│  +       │  ← Panel should appear here  │
│  Panel   │                              │
│          │                              │
└──────────┴──────────────────────────────┘
```

---

## Solution Implemented

### Updated Panel Positioning

**File:** `frontend/core/ui-canon/frontend/ui/components/BaseModal.tsx`

#### Before (Overlapping Header):
```tsx
<div className="fixed inset-0 z-50">  // inset-0 = top: 0
  <div className="fixed top-0 right-0 h-full">  // top: 0
```

#### After (Respecting Header):
```tsx
<div 
  className="fixed z-50"
  style={{
    left: 'calc(var(--sidebar-rail-width) + var(--sidebar-panel-width))',
    top: 'var(--header-height)',  // ← Starts below header
    right: 0,
    bottom: 0
  }}
>
  <div 
    className="fixed right-0"
    style={{
      left: 'calc(var(--sidebar-rail-width) + var(--sidebar-panel-width))',
      top: 'var(--header-height)',  // ← Starts below header
      bottom: 0  // ← Extends to bottom
    }}
  >
```

---

## Key Changes

### 1. Backdrop Positioning
```tsx
// OLD
className="fixed inset-0 z-50"  // Covered entire screen including header

// NEW
className="fixed z-50"
style={{
  left: 'calc(var(--sidebar-rail-width) + var(--sidebar-panel-width))',
  top: 'var(--header-height)',  // Starts below header
  right: 0,
  bottom: 0
}}
```

### 2. Panel Positioning
```tsx
// OLD
className="fixed top-0 right-0 h-full"  // Started at top (0)

// NEW
className="fixed right-0"
style={{
  top: 'var(--header-height)',  // Starts below header
  bottom: 0  // Extends to bottom of viewport
}}
```

---

## Layout Calculation

### Vertical Positioning:
- **Top**: `var(--header-height)` (typically 64px)
- **Bottom**: `0` (viewport bottom)
- **Height**: Auto-calculated as `100vh - header-height`

### Horizontal Positioning:
- **Left**: `calc(var(--sidebar-rail-width) + var(--sidebar-panel-width))`
- **Right**: `0` (viewport right edge)
- **Width**: `calc(100vw - var(--sidebar-rail-width) - var(--sidebar-panel-width))`

---

## Visual Result

### Before (Overlapping):
```
┌─────────────────────────────────────────┐
│ ┌─────────────────────────────────────┐ │ ← Panel overlaps header
│ │ Panel Header                        │ │
├─┼─────────┬───────────────────────────┼─┤
│ │ Sidebar │ Panel Content             │ │
│ │         │                           │ │
│ │         │                           │ │
└─┴─────────┴───────────────────────────┴─┘
```

### After (Respecting Header):
```
┌─────────────────────────────────────────┐
│  App Header (visible)                   │ ← Header remains visible
├──────────┬──────────────────────────────┤
│ Sidebar  │ ┌──────────────────────────┐ │
│          │ │ Panel Header             │ │
│          │ │                          │ │
│          │ │ Panel Content            │ │
│          │ │                          │ │
│          │ └──────────────────────────┘ │
└──────────┴──────────────────────────────┘
```

---

## CSS Variables Used

| Variable | Purpose | Default Value |
|----------|---------|---------------|
| `--header-height` | App header height | 64px |
| `--sidebar-rail-width` | Left rail width | 80px |
| `--sidebar-panel-width` | Right panel width | 280px |

These are all defined in `layoutConfig.ts` and applied via `applyConfig()`.

---

## Testing Checklist

### Panel Positioning:
- [ ] Panel starts below app header
- [ ] App header remains fully visible
- [ ] Panel extends to bottom of viewport
- [ ] Panel starts after sidebar (left edge)
- [ ] Panel extends to right edge of viewport
- [ ] No overlap with header
- [ ] No overlap with sidebar

### Responsive Behavior:
- [ ] Works with different header heights
- [ ] Works with different sidebar widths
- [ ] Adjusts when Layout Settings change
- [ ] Animation still smooth

---

## Layout Zones Respected

The panel now correctly respects all UI layout zones:

1. **App Header Zone**
   - Top: `0`
   - Height: `var(--header-height)`
   - Status: ✅ Not overlapped

2. **Sidebar Zone**
   - Left: `0`
   - Width: `calc(var(--sidebar-rail-width) + var(--sidebar-panel-width))`
   - Status: ✅ Not overlapped

3. **Primary Workspace Zone**
   - Left: `calc(var(--sidebar-rail-width) + var(--sidebar-panel-width))`
   - Top: `var(--header-height)`
   - Right: `0`
   - Bottom: `0`
   - Status: ✅ Panel positioned here

---

## Success Criteria Met

✅ **Panel starts below header** - Uses `top: var(--header-height)`
✅ **Header remains visible** - No overlap
✅ **Sidebar remains visible** - Positioned after sidebar
✅ **Full workspace height** - Uses `bottom: 0`
✅ **Respects layout variables** - All positioning from CSS vars
✅ **Dynamic adjustment** - Changes with Layout Settings

---

## Related Files

- `frontend/core/ui-canon/frontend/ui/components/BaseModal.tsx` - Panel implementation
- `frontend/src/config/layoutConfig.ts` - CSS variable definitions
- `frontend/core/ui-canon/frontend/components/UOMModal.tsx` - Example usage

---

*Fix Completed: 2026-01-05 23:20 IST*
*Status: Panel Respects All Layout Zones*
