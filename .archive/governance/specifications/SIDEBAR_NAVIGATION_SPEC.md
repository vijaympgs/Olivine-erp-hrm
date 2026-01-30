---
title: "Sidebar Navigation - UI Specification Document"
description: "Complete specification for Sidebar component with FoxPro-style active state"
date: "2025-12-19 19:06:54"
modified: "2025-12-19 19:06:54"
author: "Development Team"
version: "1.0.0"
category: "ui-specification"
tags: [sidebar, navigation, section-a, ui-spec, foxpro-style]
project: "Retail ERP Platform"
component: "Sidebar"
path: "frontend/src/ui/components/Sidebar.tsx"
last_reviewed: "2025-12-19 19:06:54"
review_status: "approved"
---

# Sidebar Navigation - UI Specification Document

## 📋 **Document Overview**

**Component Name**: `Sidebar`  
**Layout Section**: Section A: Sidebar Structure (Left)  
**Width**: 256px (fixed) / 80px (collapsed)  
**Position**: Fixed left side of the application  
**Theme**: Classic FoxPro-inspired active state with modern design  

---

## 🎯 **Purpose & Scope**

This specification defines the complete UI/UX standards for the Sidebar navigation component. The sidebar provides primary navigation for the entire application and features a distinctive FoxPro-style cyan/red active state for selected menu items.

### **Key Objectives**
- ✅ Primary navigation structure for the application
- ✅ FoxPro-style active state (cyan background, red text)
- ✅ Collapsible sidebar functionality
- ✅ Hierarchical menu with expandable sections
- ✅ Optional subtitle display (controlled by flag)
- ✅ User profile section at bottom

---

## 🏗️ **Layout Architecture**

### **Section A Positioning**

The sidebar uses **fixed positioning** on the left side:

```css
position: fixed;
left: 0;
top: 64px;        /* Below Section B: Application Header */
width: 256px;     /* Expanded state */
width: 80px;      /* Collapsed state */
bottom: 0;
```

### **Visual Layout Structure**

```
┌─────────────────────────┐
│  Section B: App Header  │ ← 64px height
├─────────────────────────┤
│ Section A: Sidebar      │
│ (256px width)           │
│                         │
│ ┌─────────────────────┐ │
│ │ Olivine Console  [≡]│ │ ← Header (collapsible)
│ ├─────────────────────┤ │
│ │                     │ │
│ │ Navigation Menu     │ │
│ │ ├─ Dashboard        │ │
│ │ ├─ Sales & Revenue  │ │
│ │ │  ├─ Sales Orders  │ │
│ │ │  └─ Invoices      │ │
│ │█├─ Store Operations█│ │ ← Active (Cyan/Red)
│ │ ├─ Procurement      │ │
│ │ └─ Inventory        │ │
│ │                     │ │
│ │     (scrollable)    │ │
│ │                     │ │
│ ├─────────────────────┤ │
│ │ 👤 Admin User       │ │ ← Footer
│ │    System Admin     │ │
│ └─────────────────────┘ │
└─────────────────────────┘
```

---

## 🎨 **Design System Specifications**

### **Typography**

```css
/* Font Family */
font-family: 'Olivine', sans-serif;

/* Text Sizes */
- Header Title: text-sm (14px), font-semibold
- Menu Items: text-sm (14px), font-semibold (active: font-bold)
- Subtitles: text-xs (12px), text-slate-400
- User Name: text-sm (14px), font-semibold
- User Role: text-xs (12px), text-gray-500
```

### **Color Palette**

```css
/* Background Colors */
--sidebar-bg: #F9FAFB              /* bg-gray-50 */
--sidebar-header-bg: #F9FAFB       /* bg-gray-50 */
--sidebar-footer-bg: #F9FAFB       /* bg-gray-50 */
--submenu-bg: #F3F4F6              /* bg-gray-100 */

/* Active State (FoxPro Style) */
--active-bg: #22D3EE               /* bg-cyan-400 - Bright cyan */
--active-text: #DC2626             /* text-red-600 - Red */
--active-border: #DC2626           /* border-red-600 - Red */

/* Default State */
--default-text: #6B7280            /* text-gray-600 */
--default-hover-bg: #F3F4F6        /* hover:bg-gray-100 */
--default-hover-text: #111827      /* hover:text-gray-900 */

/* Border Colors */
--border-default: #E5E7EB          /* border-gray-200 */
--border-submenu: #E5E7EB          /* border-gray-200 */

/* Subtitle Colors */
--subtitle-text: #94A3B8           /* text-slate-400 */

/* Disabled State */
--disabled-text: #9CA3AF           /* text-gray-500 */
--disabled-opacity: 0.6            /* opacity-60 */
```

### **Spacing System**

```css
/* Padding Values */
--sidebar-padding: 12px            /* p-3 */
--menu-item-padding-x: 8px         /* px-2 */
--menu-item-padding-y: 4px         /* py-1 */
--header-padding: 12px             /* p-3 */
--footer-padding: 16px             /* p-4 */

/* Margin Values */
--nested-margin-left: 24px         /* ml-6 */
--subtitle-margin-top: 4px         /* mt-1 */
--subtitle-margin-bottom: 8px      /* mb-2 */
--subtitle-margin-left: 8px        /* ml-2 */

/* Gap Values */
--menu-spacing: 4px                /* space-y-1 */
--header-spacing: 12px             /* space-x-3 */
```

### **Border & Radius**

```css
/* Border Width */
--border-width: 1px                /* border */
--active-border-width: 2px         /* border-l-2 */

/* Border Radius */
--menu-item-radius: 6px            /* rounded-md */
--submenu-radius: 8px              /* rounded-lg */
```

---

## 📐 **Component Structure**

### **1. Sidebar Header**

**Purpose**: Display application branding and collapse toggle  
**Height**: Variable (based on content)  
**Background**: bg-gray-50  
**Border**: border-b  

```tsx
<div className="flex items-center justify-between p-3 border-b border-gray-200/80 bg-gray-50">
  <div className="flex items-center space-x-3">
    {!isCollapsed && (
      <h1 className="text-gray-900 font-semibold text-sm tracking-tight">
        Olivine Console
      </h1>
    )}
  </div>
  <button
    onClick={() => setIsCollapsed(!isCollapsed)}
    className="p-1.5 rounded-md hover:bg-gray-200 text-gray-600 hover:text-gray-900"
    aria-label={isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'}
  >
    <ChevronRight className={`w-5 h-5 transform transition-transform ${isCollapsed ? '' : 'rotate-180'}`} />
  </button>
</div>
```

**Elements**:
- **Title**: "Olivine Console" (hidden when collapsed)
- **Toggle Button**: ChevronRight icon with rotation animation
- **Spacing**: space-x-3 between elements

### **2. Navigation Menu**

**Purpose**: Primary navigation with hierarchical structure  
**Overflow**: overflow-y-auto (scrollable)  
**Padding**: py-4  

```tsx
<nav className="flex-1 overflow-y-auto py-4 scrollbar-thin scrollbar-thumb-gray-300">
  <div className="space-y-1 px-3">
    {menuConfig.map((item) => (
      <MenuSection key={item.id} item={item} {...props} />
    ))}
  </div>
</nav>
```

**Features**:
- Scrollable content area
- Custom scrollbar styling
- Space between menu items (space-y-1)

### **3. Menu Item States**

#### **Default State**

```css
/* Base Classes */
display: flex;
align-items: center;
padding: 4px 8px;                  /* px-2 py-1 */
border-radius: 6px;                /* rounded-md */
font-size: 14px;                   /* text-sm */
color: #6B7280;                    /* text-gray-600 */
transition: all 200ms;             /* transition-colors duration-200 */

/* Hover State */
background-color: #F3F4F6;         /* hover:bg-gray-100 */
color: #111827;                    /* hover:text-gray-900 */
```

#### **Active State (FoxPro Style)**

```css
/* Active/Selected Item */
background-color: #22D3EE;         /* bg-cyan-400 - Bright cyan */
color: #DC2626;                    /* text-red-600 - Red */
border-left: 2px solid #DC2626;    /* border-l-2 border-red-600 */
font-weight: 700;                  /* font-bold */
box-shadow: 0 1px 2px rgba(0,0,0,0.05); /* shadow-sm */
```

**Visual Representation**:
```
┌─────────────────────────┐
│  Regular Item           │ ← Gray text (#6B7280)
├─────────────────────────┤
│█ Active Item           █│ ← Cyan bg (#22D3EE), RED text (#DC2626), BOLD
├─────────────────────────┤
│  Regular Item           │ ← Gray text (#6B7280)
└─────────────────────────┘
```

#### **Disabled State**

```css
opacity: 0.6;                      /* opacity-60 */
cursor: default;                   /* cursor-default */
color: #9CA3AF;                    /* text-gray-500 */
user-select: none;                 /* select-none */
```

#### **Focus State**

```css
outline: none;                     /* focus:outline-none */
box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.7); /* focus-visible:ring-2 */
```

### **4. Expandable Menu Items**

**Purpose**: Parent items with child menu items  
**Indicator**: ChevronDown icon (rotates when expanded)  

```tsx
<button
  onClick={() => toggleExpanded(item.id)}
  className={`${baseClasses} ${activeClasses} w-full text-left`}
  aria-expanded={isExpanded}
>
  <span className="flex-1 font-semibold truncate">{item.label}</span>
  <ChevronDown className={`w-3 h-3 transition-transform ${isExpanded ? 'rotate-180' : ''}`} />
</button>
```

**Expanded Submenu**:
```tsx
<div className="mt-1 space-y-0.5 bg-gray-100 rounded-lg mx-2 p-1 border border-gray-200">
  {/* Child menu items */}
</div>
```

**Submenu Styling**:
- Background: bg-gray-100
- Border: border-gray-200
- Padding: p-1
- Margin: mx-2 (horizontal margin)
- Spacing: space-y-0.5 (between items)

### **5. Subtitle Display**

**Purpose**: Optional descriptive text below menu items  
**Control**: `SHOW_SUBTITLES` flag (line 7 in Sidebar.tsx)  

```tsx
// Global flag to show/hide subtitles
const SHOW_SUBTITLES = false; // Set to true to show subtitles
```

**Subtitle Styling**:
```tsx
{SHOW_SUBTITLES && !isCollapsed && item.subtitle && (
  <div className="text-xs text-slate-400 mt-1 mb-2 truncate ml-2">
    {item.subtitle}
  </div>
)}
```

```css
font-size: 12px;                   /* text-xs */
color: #94A3B8;                    /* text-slate-400 */
margin-top: 4px;                   /* mt-1 */
margin-bottom: 8px;                /* mb-2 */
margin-left: 8px;                  /* ml-2 */
text-overflow: ellipsis;           /* truncate */
```

### **6. Sidebar Footer**

**Purpose**: Display user information  
**Position**: Bottom of sidebar  
**Background**: bg-gray-50  
**Border**: border-t  

```tsx
{!isCollapsed && (
  <div className="p-4 border-t border-gray-200 bg-gray-50">
    <div className="flex items-center space-x-3 text-sm">
      <div className="flex-1 min-w-0">
        <p className="font-semibold text-gray-900 truncate text-sm">Admin User</p>
        <p className="text-xs text-gray-500 truncate">System Administrator</p>
      </div>
    </div>
  </div>
)}
```

**Elements**:
- **User Name**: text-sm, font-semibold, text-gray-900
- **User Role**: text-xs, text-gray-500
- **Truncation**: Both text elements truncate if too long

---

## 🔄 **State Management**

### **Component State**

```typescript
const [expandedItems, setExpandedItems] = useState<Set<string>>(new Set(['dashboard']));
const [isCollapsed, setIsCollapsed] = useState(false);
```

### **Menu Configuration**

```typescript
interface MenuItem {
  id: string;
  label: string;
  icon?: string;
  path?: string;
  badge?: string;
  children?: MenuItem[];
  disabled?: boolean;
  divider?: boolean;
  subtitle?: string;
}
```

---

## 🎯 **Interaction Patterns**

### **Menu Item Click Behavior**

1. **Parent Items (with children)**:
   - Click → Toggle expand/collapse
   - Show/hide submenu with animation
   - Rotate chevron icon

2. **Link Items (with path)**:
   - Click → Navigate to route
   - Apply active state
   - Update URL

3. **Disabled Items**:
   - No click interaction
   - Visual feedback (opacity, cursor)

### **Keyboard Navigation**

```typescript
// Arrow Keys
- ArrowRight: Expand collapsed parent
- ArrowLeft: Collapse expanded parent
- Enter/Space: Toggle expansion or navigate

// Tab Navigation
- Tab: Move to next focusable item
- Shift+Tab: Move to previous focusable item
```

### **Collapse/Expand Behavior**

**Collapsed State (80px)**:
- Hide all text labels
- Hide subtitles
- Show icons only (if available)
- Show tooltip on hover with full label

**Expanded State (256px)**:
- Show all text labels
- Show subtitles (if SHOW_SUBTITLES = true)
- Show full menu structure

---

## 📱 **Responsive Behavior**

### **Desktop (≥1024px)**
- Full sidebar (256px)
- All features visible
- Collapsible functionality

### **Tablet (768px - 1023px)**
- Sidebar remains at 256px
- May overlay content on smaller tablets
- Collapsible functionality

### **Mobile (<768px)**
- Sidebar hidden by default
- Accessible via hamburger menu
- Overlay mode when opened

---

## ♿ **Accessibility Standards**

### **ARIA Labels**

```tsx
<nav role="navigation" aria-label="Primary sidebar">
<button aria-label="Collapse sidebar" aria-expanded={isExpanded}>
<div role="separator" aria-hidden="true">
```

### **Keyboard Support**
- ✅ Full keyboard navigation
- ✅ Focus indicators
- ✅ Screen reader support
- ✅ Logical tab order

### **Focus Management**
- Visible focus rings
- Skip to main content link
- Focus trap in expanded menus

---

## 🎨 **FoxPro Style Guide**

### **Classic FoxPro Color Scheme**

The active state uses the iconic **FoxPro/DOS** color combination:

```css
/* FoxPro Classic Colors */
--foxpro-cyan: #22D3EE    /* Bright cyan background */
--foxpro-red: #DC2626     /* Red text */
--foxpro-bold: 700        /* Bold font weight */
```

**Historical Context**:
- FoxPro (1984-2007) used cyan/red for selected items
- Provided high contrast in CRT monitors
- Instantly recognizable to users
- Nostalgic and distinctive

**Modern Adaptation**:
- Maintained color scheme
- Added smooth transitions
- Included shadow for depth
- Rounded corners for modern feel

---

## 🔧 **Configuration Options**

### **Subtitle Toggle**

```typescript
// In Sidebar.tsx (line 7)
const SHOW_SUBTITLES = false; // Change to true to show subtitles
```

**When to Show Subtitles**:
- ✅ First-time users need guidance
- ✅ Complex menu structures
- ✅ Training environments

**When to Hide Subtitles**:
- ✅ Experienced users
- ✅ Cleaner, more compact UI
- ✅ Limited vertical space

### **Default Expanded Items**

```typescript
const [expandedItems, setExpandedItems] = useState<Set<string>>(
  new Set(['dashboard']) // Add IDs of items to expand by default
);
```

---

## 📊 **Menu Structure Example**

```typescript
export const menuConfig: MenuItem[] = [
  {
    id: 'dashboard',
    label: 'Dashboard',
    subtitle: 'Overview and analytics',
    path: '/dashboard',
  },
  {
    id: 'divider-1',
    label: '',
    divider: true,
  },
  {
    id: 'sales',
    label: 'Sales & Revenue',
    subtitle: 'Manage sales orders and pricing',
    children: [
      { 
        id: 'orders', 
        label: 'Sales Orders', 
        path: '/sales/orders',
        subtitle: 'Order processing'
      },
      // ... more children
    ],
  },
  // ... more menu items
];
```

---

## 🎯 **Usage Guidelines**

### **When to Use This Pattern**
- ✅ Primary navigation for the application
- ✅ Hierarchical menu structures
- ✅ Need for collapsible sidebar
- ✅ Want distinctive active state

### **Best Practices**
- ✅ Keep menu depth to 2 levels maximum
- ✅ Use clear, concise labels
- ✅ Group related items logically
- ✅ Provide visual feedback on interaction
- ✅ Maintain consistent spacing

### **Avoid**
- ❌ Too many top-level items (>12)
- ❌ Deep nesting (>2 levels)
- ❌ Overly long labels
- ❌ Too many disabled items

---

## 🔗 **Related Components**

- **Application Header**: Section B (top bar)
- **Primary Workspace**: Section C (main content)
- **Status Bar**: Section D (bottom bar)
- **Menu Configuration**: `frontend/src/app/menuConfig.ts`

---

## 📚 **References**

- **UI Layout Terminology**: `docs/steering/UI_LAYOUT_TERMINOLOGY.md`
- **Component Library**: `docs/steering/COMPONENT_LIBRARY.md`
- **Menu Configuration**: `frontend/src/app/menuConfig.ts`
- **FoxPro History**: Classic database management system (1984-2007)

---

## 📝 **Implementation Checklist**

- [x] Fixed positioning for Section A
- [x] FoxPro-style active state (cyan/red)
- [x] Collapsible functionality
- [x] Expandable menu sections
- [x] Subtitle toggle flag
- [x] User profile footer
- [x] Smooth transitions
- [x] Keyboard navigation
- [x] Accessibility compliance
- [x] Responsive behavior
- [x] Custom scrollbar styling

---

## 🔄 **Version History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-12-19 | Development Team | Initial specification with FoxPro styling |

---

## 💡 **Tips & Tricks**

### **Customizing Active State Colors**

To change the FoxPro colors, update these values in `Sidebar.tsx`:

```tsx
// Current: Cyan background, red text
const activeClasses = isActive
  ? 'bg-cyan-400 text-red-600 border-l-2 border-red-600 shadow-sm font-bold'
  : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900';

// Alternative: Blue background, white text (modern)
const activeClasses = isActive
  ? 'bg-blue-600 text-white border-l-2 border-blue-800 shadow-sm font-bold'
  : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900';
```

### **Adding Icons**

Icons can be added to menu items via the `icon` property in `menuConfig.ts`:

```typescript
{
  id: 'dashboard',
  label: 'Dashboard',
  icon: 'LayoutDashboard', // Lucide icon name
  path: '/dashboard',
}
```

---

**Document Status**: ✅ Approved  
**Last Updated**: 2025-12-19 19:06:54  
**Next Review**: 2026-01-19
