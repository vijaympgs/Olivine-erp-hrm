# LOOKUP UI CANON - IMPLEMENTATION COMPLETE

**Date**: 2025-12-23  
**Status**: ✅ ENFORCED  
**Applies To**: ALL lookup modals in Olivine/EnterpriseGPT

---

## 🎯 CANON SUMMARY

**RULE**: Lookups are an extension of Sidebar + App Header, NOT independent components.

**IMPLEMENTATION**: All lookups MUST use `LookupContainer.tsx`

---

## ✅ COMPLIANCE CHECKLIST

### 1. Theme Identity ✅
- [x] Lookup header uses SAME background as App Header
- [x] Lookup header uses SAME gradient (`#14162A` → `#101223`)
- [x] Lookup icons use SAME brand color (`#22D3EE`)
- [x] Lookup text uses SAME colors as Header
- [x] NO bright blue headers
- [x] NO hardcoded colors

### 2. Structure ✅
- [x] Shared `LookupContainer` component created
- [x] All lookups use the container
- [x] Consistent header layout
- [x] Consistent search bar placement
- [x] Consistent results area

### 3. Typography & Icons ✅
- [x] Uses Lucide icons (same as Sidebar)
- [x] Same font family as App Header
- [x] Same font weights
- [x] Consistent icon sizing

### 4. Interaction ✅
- [x] Keyboard-first (Escape closes)
- [x] Auto-focus on search input
- [x] Hover states match Sidebar
- [x] Click to select

### 5. Theme Awareness ✅
- [x] Uses `useLayoutConfig` hook
- [x] Reads theme from config
- [x] NO hardcoded colors
- [x] Adapts to light/dark/auto

### 6. Reusability ✅
- [x] Single `LookupContainer` component
- [x] All lookups use it
- [x] Lookups differ ONLY in data + columns
- [x] NOT in look & feel

---

## 📁 FILES CREATED/MODIFIED

### Created:
1. ✅ `frontend/src/ui/components/LookupContainer.tsx`
   - Canonical lookup shell
   - Theme-aware
   - Matches App Header exactly

### Refactored:
2. ✅ `frontend/src/ui/components/SupplierLookupModal.tsx`
   - Removed hardcoded `bg-[#0078d4]`
   - Now uses `LookupContainer`
   - Matches App Header theme

3. ✅ `frontend/src/ui/components/ProductLookupModal.tsx`
   - Removed hardcoded `backgroundColor: '#0078d4'`
   - Now uses `LookupContainer`
   - Matches App Header theme

---

## 🎨 THEME EXTRACTION

### From App Header Config:
```typescript
// Header Background
headerBgStyle: 'gradient'
headerGradientStart: '#14162A'
headerGradientEnd: '#101223'

// Brand Colors
brandColor: '#22D3EE' (cyan)
iconColor: '#6F7396' (muted purple-gray)
```

### Applied To Lookups:
```typescript
// Lookup Header
background: linear-gradient(to bottom, #14162A, #101223)
icon color: #22D3EE
text color: #FFFFFF
close button color: #6F7396

// Lookup Body
background: white
hover: gray-50
border: gray-100
```

---

## 🚀 USAGE GUIDE

### For Future Lookups:

```typescript
import { LookupContainer } from './LookupContainer';
import { YourIcon } from 'lucide-react';

export const YourLookupModal = ({ isOpen, onClose, onSelect }) => {
  // Your state and logic here
  
  const searchBar = (
    <div className="relative">
      <Search className="absolute left-3 top-2.5 text-gray-400" size={16} />
      <input
        type="text"
        placeholder="Search..."
        className="w-full pl-9 pr-3 py-2 border border-gray-300 rounded-sm text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>
  );

  const resultsContent = (
    <div>
      {/* Your results here */}
    </div>
  );

  return (
    <LookupContainer
      isOpen={isOpen}
      onClose={onClose}
      title="Your Lookup"
      icon={<YourIcon size={20} />}
      searchBar={searchBar}
    >
      {resultsContent}
    </LookupContainer>
  );
};
```

---

## ❌ PROHIBITIONS

### DO NOT:
- ❌ Use `bg-[#0078d4]` or any hardcoded blue
- ❌ Use `backgroundColor: '#0078d4'` in style props
- ❌ Create custom lookup headers
- ❌ Ignore `LookupContainer`
- ❌ Use bright brand colors in lookup body
- ❌ Mix light header with dark sidebar
- ❌ Style lookups independently

### DO:
- ✅ Always use `LookupContainer`
- ✅ Use theme tokens from `useLayoutConfig`
- ✅ Match App Header colors exactly
- ✅ Keep lookups visually consistent
- ✅ Test in light AND dark themes

---

## 🧪 VERIFICATION

### Visual Check:
1. Open any lookup (Supplier, Item, etc.)
2. Compare header color to App Header
3. Should be SAME dark gradient
4. Should NOT be bright blue

### Code Check:
```bash
# Search for violations
grep -r "bg-\[#0078d4\]" frontend/src/ui/components/*Lookup*.tsx
grep -r "backgroundColor.*0078d4" frontend/src/ui/components/*Lookup*.tsx

# Should return NO results
```

---

## 📊 BEFORE vs AFTER

### BEFORE (WRONG):
```tsx
// ❌ Hardcoded bright blue
<div className="... bg-[#0078d4] text-white">
  <Search size={20} />
  <h2>Supplier Lookup</h2>
</div>
```

### AFTER (CORRECT):
```tsx
// ✅ Uses LookupContainer with theme colors
<LookupContainer
  title="Supplier Lookup"
  icon={<Search size={20} />}
  // Header automatically matches App Header
/>
```

---

## ✅ SUCCESS CRITERIA

A user should feel that:
- ✅ Lookup belongs to the same product as Sidebar
- ✅ Lookup feels like a native ERP panel
- ✅ Switching between modules does NOT change lookup look
- ✅ Lookup header matches App Header exactly
- ✅ All lookups look identical (except data)

**If any lookup looks visually different from another, the implementation is WRONG.**

---

## 🔒 ENFORCEMENT

This canon is **LOCKED** and **NON-NEGOTIABLE**.

Any future lookup MUST:
1. Use `LookupContainer`
2. Match App Header theme
3. Follow the structure defined here

**NO EXCEPTIONS.**

---

**Canon Established**: 2025-12-23  
**Enforced By**: Antigravity Agent  
**Authority**: Viji (Product Owner)  
**Status**: ✅ ACTIVE
