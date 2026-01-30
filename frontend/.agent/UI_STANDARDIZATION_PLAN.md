# UI Standardization & Audit Implementation Plan

## Overview
This document outlines the implementation of centralized UI styling for modals and forms, plus a comprehensive audit of Retail module UI completion status.

## Phase 1: Centralized Typography & Modal Configuration

### 1.1 Extend LayoutConfig Interface
Add new configuration sections for:
- **Modal Settings**: Width constraints, positioning, backdrop styling
- **Typography Hierarchy**: L1-L4 font sizes, weights, colors
- **Form Typography**: Input labels, field text, validation messages

### 1.2 CSS Variable Mapping
Create CSS variables for:
```css
--modal-max-width
--modal-bg
--modal-border
--modal-backdrop

--typography-l1-size (Page Titles)
--typography-l2-size (Section Headers)
--typography-l3-size (Subsection Headers)
--typography-l4-size (Form Labels & Body Text)
--typography-l4-color
--typography-l4-weight

--form-label-size
--form-label-color
--form-input-size
--form-input-color
```

### 1.3 Apply to Existing Components
Update all modal and form components to use centralized variables instead of hardcoded Tailwind classes.

## Phase 2: UI Audit Report

### 2.1 Automated Audit via Test Console
Use the existing Test Console infrastructure to:
1. Scan all Retail menu items from `menuConfig.ts`
2. Check for corresponding route definitions in `router.tsx`
3. Verify component file existence
4. Generate comprehensive CSV report

### 2.2 Report Structure
```
Menu ID | Component Name | Path | Route Exists | Component Exists | UI Status | Notes
```

### 2.3 Categorization
- ✅ **Complete**: Route + Component + Functional UI
- 🚧 **In Progress**: Route exists but component incomplete
- ❌ **Missing**: No route or component
- 📝 **Placeholder**: Route exists but shows placeholder/stub

## Implementation Steps

### Step 1: Update LayoutConfig
- Add `modal` configuration section
- Add `typography` configuration section with L1-L4 hierarchy
- Add default values matching current L4 styling

### Step 2: Update CSS Variable Application
- Extend `applyConfig()` method in `LayoutManager`
- Map new config properties to CSS variables

### Step 3: Create Modal Base Component
- Create `BaseModal.tsx` that consumes centralized styling
- Ensure all modals fit within workspace bounds
- Apply L4 typography to all form content

### Step 4: Update Layout Settings Page
- Add new UI controls for Modal settings
- Add Typography hierarchy controls
- Group under new "UI Standards" accordion

### Step 5: Generate UI Audit Report
- Create utility script to scan menu config
- Cross-reference with router and file system
- Generate detailed CSV report
- Identify all missing/incomplete UIs

## Expected Outcomes

1. **Centralized Control**: All modal sizes, typography controlled from Layout Settings
2. **Consistency**: All forms use identical L4 styling
3. **Visibility**: Clear audit report showing UI completion status
4. **Maintainability**: Single source of truth for UI standards

## Files to Modify

### Configuration
- `frontend/src/config/layoutConfig.ts`

### Components
- `frontend/core/ui-canon/frontend/ui/components/BaseModal.tsx` (new)
- All existing modal components (to extend BaseModal)

### Pages
- `frontend/src/pages/admin/LayoutSettingsPage.tsx`

### Utilities
- `frontend/src/utils/uiAudit.ts` (new)
- Update Test Console report generation

## Timeline
- Phase 1 (Centralization): 2-3 hours
- Phase 2 (Audit): 1 hour
- Testing & Refinement: 1 hour

---
*Document Created: 2026-01-05*
