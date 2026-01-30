# Section C Positioning - Migration Guide

## 🎯 Purpose

This guide helps you migrate existing forms and components to use the centralized CSS variable-based positioning system instead of hardcoded values.

## ⚠️ Problem

Forms using hardcoded positioning values break when layout settings change:

```tsx
// ❌ BAD - Hardcoded values
<div style={{
  left: '256px',    // Breaks when sidebar width changes
  top: '64px',      // Breaks when header height changes
  bottom: '48px'    // Breaks when status bar height changes
}}>
```

## ✅ Solution

Use CSS classes that reference CSS variables:

```tsx
// ✅ GOOD - Uses CSS variables
<div className="section-c-container">
  {/* Content */}
</div>
```

---

## 📐 Available CSS Classes

### 1. `.section-c-fixed`
**Use for**: Basic fixed positioning within Section C

```css
.section-c-fixed {
  position: fixed;
  left: var(--sidebar-width);
  top: var(--header-height);
  right: 0;
  bottom: var(--statusbar-height);
}
```

**Example**:
```tsx
<div className="section-c-fixed">
  <YourComponent />
</div>
```

---

### 2. `.section-c-container`
**Use for**: Forms with internal structure (header, content, footer)

```css
.section-c-container {
  position: fixed;
  left: var(--sidebar-width);
  top: var(--header-height);
  right: 0;
  bottom: var(--statusbar-height);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  background-color: var(--workspace-bg);
}
```

**Example**:
```tsx
<div className="section-c-container">
  <div className="flex-shrink-0">{/* Header */}</div>
  <div className="flex-1 overflow-y-auto">{/* Scrollable Content */}</div>
  <div className="flex-shrink-0">{/* Footer */}</div>
</div>
```

**Best for**:
- Employee Form
- Terminal Form
- Any form with fixed header/footer

---

### 3. `.section-c-scrollable`
**Use for**: Simple scrollable content

```css
.section-c-scrollable {
  position: fixed;
  left: var(--sidebar-width);
  top: var(--header-height);
  right: 0;
  bottom: var(--statusbar-height);
  overflow-y: auto;
  overflow-x: hidden;
  background-color: var(--workspace-bg);
}
```

**Example**:
```tsx
<div className="section-c-scrollable">
  <div className="p-6">
    {/* Your scrollable content */}
  </div>
</div>
```

**Best for**:
- Item Master
- Customer Master
- Supplier Master
- Simple list views

---

### 4. `.section-c-full`
**Use for**: Full-height components without scroll

```css
.section-c-full {
  position: fixed;
  left: var(--sidebar-width);
  top: var(--header-height);
  right: 0;
  bottom: var(--statusbar-height);
  background-color: var(--workspace-bg);
}
```

**Example**:
```tsx
<div className="section-c-full">
  <YourFullHeightComponent />
</div>
```

**Best for**:
- POS Screen
- Dashboard
- Full-screen components

---

## 🔄 Migration Examples

### Example 1: Employee Form (Already Updated)

**Before**:
```tsx
<div style={{
  left: '256px',
  top: '64px',
  right: '0',
  bottom: '48px'
}}>
```

**After**:
```tsx
<div className="section-c-container">
```

---

### Example 2: Item Master / Customer Master

**Before**:
```tsx
<div className="fixed" style={{
  left: '256px',
  top: '64px',
  right: 0,
  bottom: '48px',
  overflow: 'auto'
}}>
```

**After**:
```tsx
<div className="section-c-scrollable">
  <div className="p-6">
    {/* Content */}
  </div>
</div>
```

---

### Example 3: POS Screen

**Before**:
```tsx
<div className="h-screen" style={{
  marginLeft: '256px',
  marginTop: '64px'
}}>
```

**After**:
```tsx
<div className="section-c-full">
  {/* POS Content */}
</div>
```

---

## 🛠️ Step-by-Step Migration

### Step 1: Identify Current Positioning

Look for these patterns in your component:
- `style={{ left: '256px', ... }}`
- `style={{ marginLeft: '256px', ... }}`
- Hardcoded `256`, `64`, `48` values
- Fixed positioning with specific pixel values

### Step 2: Choose Appropriate Class

| Component Type | Use Class |
|---------------|-----------|
| Form with header/footer | `.section-c-container` |
| Simple scrollable list | `.section-c-scrollable` |
| Full-screen component | `.section-c-full` |
| Basic fixed positioning | `.section-c-fixed` |

### Step 3: Replace Inline Styles

```tsx
// Remove this
<div 
  className="fixed flex flex-col bg-white overflow-hidden"
  style={{
    left: '256px',
    top: '64px',
    right: '0',
    bottom: '48px'
  }}
>

// Replace with this
<div className="section-c-container">
```

### Step 4: Test

1. Open the component
2. Toggle sidebar collapse
3. Change layout settings (if available)
4. Verify positioning adjusts correctly

---

## 📋 Components to Update

### High Priority
- [ ] POS Screen (`PosPage.tsx`)
- [ ] Item Master (`ItemMasterSetup.tsx` or `ItemPage.tsx`)
- [ ] Customer Master (`CustomerSetup.tsx` or `CustomerPage.tsx`)
- [ ] Supplier Master (`SupplierSetup.tsx` or `SupplierPage.tsx`)

### Medium Priority
- [ ] Terminal Configuration
- [ ] Day Open/Close pages
- [ ] Session pages
- [ ] Other master data pages

### Already Updated
- [x] Employee Form (`EmployeeFormStandalone.tsx`)
- [x] Layout Settings Page (`LayoutSettingsPage.tsx`)

---

## 🎨 CSS Variables Reference

These are automatically controlled by the Layout Configuration System:

```css
--sidebar-width: 256px;           /* Default sidebar width */
--sidebar-collapsed-width: 80px;  /* Collapsed sidebar width */
--header-height: 64px;            /* Header height */
--statusbar-height: 48px;         /* Status bar height */
--workspace-bg: #FFFFFF;          /* Workspace background */
```

**User can change these via**: System Administration → Layout Settings

---

## 🔍 Finding Components to Update

### Search for Hardcoded Values

```bash
# Find files with hardcoded 256px (sidebar width)
grep -r "256px" frontend/src/

# Find files with hardcoded 64px (header height)
grep -r "64px" frontend/src/

# Find files with hardcoded 48px (status bar height)
grep -r "48px" frontend/src/
```

### Common Patterns to Replace

```tsx
// Pattern 1: Inline style object
style={{ left: '256px', top: '64px', right: '0', bottom: '48px' }}

// Pattern 2: Tailwind with margins
className="ml-[256px] mt-[64px]"

// Pattern 3: Fixed positioning
className="fixed left-[256px] top-[64px]"
```

---

## ✅ Benefits After Migration

1. **Dynamic Layout**: Components adjust when layout settings change
2. **Consistent Positioning**: All components use same positioning logic
3. **Easier Maintenance**: Change once in config, applies everywhere
4. **Better UX**: Sidebar collapse works correctly
5. **Theme Support**: Respects compact mode and other settings

---

## 🚨 Common Mistakes

### ❌ Mistake 1: Mixing Approaches
```tsx
// Don't mix CSS classes with inline styles
<div className="section-c-container" style={{ left: '256px' }}>
```

### ❌ Mistake 2: Not Removing Old Styles
```tsx
// Remove ALL hardcoded positioning
<div className="fixed left-[256px] section-c-container">
```

### ❌ Mistake 3: Wrong Class Choice
```tsx
// Don't use .section-c-container for simple scrollable content
// Use .section-c-scrollable instead
```

---

## 📞 Need Help?

If you encounter issues:

1. Check browser DevTools → Elements → Computed styles
2. Verify CSS variables are set correctly
3. Ensure `layout.css` is imported
4. Check for conflicting inline styles

---

**Last Updated**: 2025-12-19  
**Related Docs**: 
- `docs/LAYOUT_CONFIGURATION_SYSTEM.md`
- `docs/specifications/EMPLOYEE_FORM_SPEC.md`
- `frontend/src/styles/layout.css`
