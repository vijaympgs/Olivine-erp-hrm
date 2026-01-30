---
title: "Centralized CSS Configuration - Specification Document"
description: "Complete specification for centralized layout configuration system using CSS variables"
date: "2025-12-19 19:26:51"
modified: "2025-12-19 19:26:51"
author: "Development Team"
version: "1.0.0"
category: "ui-specification"
tags: [css, configuration, layout, css-variables, global-config]
project: "Retail ERP Platform"
component: "Layout Configuration System"
path: "frontend/src/config/layoutConfig.ts, frontend/src/styles/layout.css"
last_reviewed: "2025-12-19 19:26:51"
review_status: "approved"
---

# Centralized CSS Configuration - Specification Document

## 📋 **Document Overview**

**System Name**: Centralized Layout Configuration System  
**Purpose**: Single source of truth for all layout-related settings  
**Approach**: TypeScript configuration + CSS variables + React hooks  
**Storage**: localStorage (client-side) with backend API extensibility  

---

## 🎯 **Purpose & Scope**

This specification defines the centralized configuration system that controls all layout-related settings across the application. It enables dynamic, user-customizable layouts through a combination of TypeScript configuration, CSS variables, and React hooks.

### **Key Objectives**
- ✅ Single source of truth for layout settings
- ✅ Type-safe configuration with TypeScript
- ✅ Dynamic updates via CSS variables
- ✅ User-customizable through UI
- ✅ Persistent across sessions
- ✅ Cross-tab synchronization

---

## 🏗️ **System Architecture**

### **Component Diagram**

```
┌─────────────────────────────────────────────────────────┐
│                   User Interface Layer                   │
│              (Layout Settings Page)                      │
│   - Visual controls for all settings                    │
│   - Live preview                                         │
│   - Preset selection                                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              React Hooks Layer                           │
│   - useLayoutConfig()      (Full config access)         │
│   - useLayoutSection()     (Specific section)           │
│   - useLayoutFeature()     (Individual flags)           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           LayoutManager (Singleton Class)                │
│   - Load configuration from localStorage                │
│   - Save configuration to localStorage                  │
│   - Apply CSS variables to :root                        │
│   - Manage state and updates                            │
│   - Preset management                                   │
└────────────────────┬────────────────────────────────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│   localStorage   │  │  CSS Variables   │
│   (Persistence)  │  │   (:root)        │
│                  │  │                  │
│ Key:             │  │ --sidebar-width  │
│ olivine_layout_  │  │ --header-height  │
│ config           │  │ --active-bg      │
│                  │  │ ... etc          │
└──────────────────┘  └──────────────────┘
```

---

## 📁 **File Structure**

```
frontend/src/
├── config/
│   └── layoutConfig.ts              # Central configuration & LayoutManager
│       ├── LayoutConfig interface   # TypeScript type definitions
│       ├── defaultLayoutConfig      # Default values
│       ├── activeMenuPresets        # Style presets
│       └── LayoutManager class      # Singleton manager
│
├── styles/
│   └── layout.css                   # Global CSS with variables
│       ├── :root variables          # CSS variable definitions
│       ├── Section A-D styles       # Layout section styles
│       ├── Utility classes          # Helper classes
│       └── Theme variations         # Dark mode, compact mode
│
├── hooks/
│   └── useLayoutConfig.ts           # React hooks
│       ├── useLayoutConfig()        # Full config access
│       ├── useLayoutSection()       # Section-specific access
│       └── useLayoutFeature()       # Feature flag access
│
└── pages/admin/
    └── LayoutSettingsPage.tsx       # UI for managing settings
        ├── Sidebar settings         # Width, collapse, subtitles
        ├── Active menu styling      # Colors, presets
        ├── Header settings          # Height, visibility
        ├── Status bar settings      # Height, visibility
        └── General settings         # Theme, compact mode
```

---

## 🔧 **Core Components**

### **1. layoutConfig.ts - Central Configuration**

**Location**: `frontend/src/config/layoutConfig.ts`

#### **LayoutConfig Interface**

```typescript
export interface LayoutConfig {
  // Section A: Sidebar
  sidebar: {
    width: number;                    // 256 (default)
    collapsedWidth: number;           // 80
    defaultCollapsed: boolean;        // false
    showSubtitles: boolean;           // false
    backgroundColor: string;          // '#F9FAFB'
    borderColor: string;              // '#E5E7EB'
  };

  // Active Menu Item Styling
  activeMenuItem: {
    style: 'foxpro' | 'modern' | 'minimal' | 'custom';
    backgroundColor: string;          // '#22D3EE' (cyan)
    textColor: string;                // '#DC2626' (red)
    borderColor: string;              // '#DC2626'
    borderWidth: number;              // 2
    fontWeight: number;               // 700
  };

  // Section B: Application Header
  header: {
    height: number;                   // 64
    backgroundColor: string;          // '#FFFFFF'
    borderColor: string;              // '#E5E7EB'
    showUserMenu: boolean;            // true
    showNotifications: boolean;       // true
    showSearch: boolean;              // true
  };

  // Section C: Primary Workspace
  workspace: {
    backgroundColor: string;          // '#FFFFFF'
    padding: number;                  // 16
  };

  // Section D: Status Bar
  statusBar: {
    height: number;                   // 48
    show: boolean;                    // true
    backgroundColor: string;          // '#F9FAFB'
    borderColor: string;              // '#E5E7EB'
    showConnectionStatus: boolean;    // true
    showSessionInfo: boolean;         // true
  };

  // Section E: Lookup Panel
  lookup: {
    width: string;                    // '650px'
    startPosition: 'right' | 'left';  // 'right'
    hasBackdrop: boolean;             // false
    headerStyle: 'flat' | 'gradient'; // 'flat'
    animationDuration: number;        // 300
    zIndex: number;                   // 40
  };

  // General Settings
  general: {
    theme: 'light' | 'dark' | 'auto';
    compactMode: boolean;             // false
    animationsEnabled: boolean;       // true
    fontFamily: string;
    fontSize: {
      xs: string;                     // '12px'
      sm: string;                     // '14px'
      base: string;                   // '16px'
      lg: string;                     // '18px'
      xl: string;                     // '20px'
    };
  };

  // Form Settings
  forms: {
    defaultGridColumns: number;       // 3
    inputPadding: string;             // '6px 8px'
    labelFontSize: string;            // '12px'
    errorColor: string;               // '#DC2626'
  };
}
```

#### **LayoutManager Class**

```typescript
export class LayoutManager {
  private static instance: LayoutManager;
  private config: LayoutConfig;
  private readonly STORAGE_KEY = 'olivine_layout_config';

  // Singleton pattern
  static getInstance(): LayoutManager;

  // Configuration management
  loadConfig(): LayoutConfig;
  saveConfig(config: LayoutConfig): void;
  resetConfig(): void;

  // CSS variable application
  applyConfig(): void;

  // Section updates
  updateSection<K extends keyof LayoutConfig>(
    section: K,
    updates: Partial<LayoutConfig[K]>
  ): void;

  // Preset management
  applyActiveMenuPreset(preset: 'foxpro' | 'modern' | 'minimal'): void;
}
```

---

### **2. layout.css - Global CSS Variables**

**Location**: `frontend/src/styles/layout.css`

#### **CSS Variables**

```css
:root {
  /* Section A: Sidebar */
  --sidebar-width: 256px;
  --sidebar-collapsed-width: 80px;
  --sidebar-bg: #F9FAFB;
  --sidebar-border: #E5E7EB;

  /* Active Menu Item (FoxPro Style) */
  --active-bg: #22D3EE;           /* Cyan */
  --active-text: #DC2626;         /* Red */
  --active-border: #DC2626;       /* Red */
  --active-border-width: 2px;
  --active-font-weight: 700;

  /* Section B: Header */
  --header-height: 64px;
  --header-bg: #FFFFFF;
  --header-border: #E5E7EB;

  /* Section C: Workspace */
  --workspace-bg: #FFFFFF;
  --workspace-padding: 16px;

  /* Section D: Status Bar */
  --statusbar-height: 48px;
  --statusbar-bg: #F9FAFB;
  --statusbar-border: #E5E7EB;

  /* Typography */
  --font-family: 'Inter', sans-serif;
  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-base: 16px;
  --font-size-lg: 18px;
  --font-size-xl: 20px;

  /* Forms */
  --form-error-color: #DC2626;
  --form-input-border: #D1D5DB;
  --form-input-focus: #3B82F6;

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 12px;
  --spacing-lg: 16px;
  --spacing-xl: 24px;

  /* Animations */
  --transition-fast: 150ms;
  --transition-normal: 200ms;
  --transition-slow: 300ms;
}
```

#### **Utility Classes**

```css
/* Section C Positioning */
.section-c-fixed {
  position: fixed;
  left: var(--sidebar-width);
  top: var(--header-height);
  right: 0;
  bottom: var(--statusbar-height);
}

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

.section-c-full {
  position: fixed;
  left: var(--sidebar-width);
  top: var(--header-height);
  right: 0;
  bottom: var(--statusbar-height);
  background-color: var(--workspace-bg);
}

/* ERP Specific Component Styles */
.erp-page-title {
  font-family: var(--font-family);
  font-size: 1.5rem;
  font-weight: 600;
  color: #111827;
  letter-spacing: normal;
}

.erp-table-header {
  font-family: var(--font-family);
  font-size: var(--font-size-xs);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #6b7280;
}
```

---

### **3. useLayoutConfig.ts - React Hooks**

**Location**: `frontend/src/hooks/useLayoutConfig.ts`

#### **Available Hooks**

```typescript
// Full configuration access
export const useLayoutConfig = () => {
  const config: LayoutConfig;
  const updateConfig: (newConfig: LayoutConfig) => void;
  const resetConfig: () => void;
  const updateSection: <K extends keyof LayoutConfig>(
    section: K,
    updates: Partial<LayoutConfig[K]>
  ) => void;
  
  return { config, updateConfig, resetConfig, updateSection };
};

// Section-specific access
export const useLayoutSection = <K extends keyof LayoutConfig>(
  section: K
): LayoutConfig[K];

// Feature flag access
export const useLayoutFeature = <
  K extends keyof LayoutConfig,
  F extends keyof LayoutConfig[K]
>(
  section: K,
  feature: F
): LayoutConfig[K][F];
```

---

## 🎨 **Style Presets**

### **FoxPro Classic (Default)**

```typescript
{
  label: 'FoxPro Classic',
  description: 'Cyan background with red text (nostalgic)',
  backgroundColor: '#22D3EE',  // Cyan
  textColor: '#DC2626',        // Red
  borderColor: '#DC2626',      // Red
}
```

**Visual**:
```
┌─────────────────────────┐
│█ Active Menu Item      █│ ← Cyan bg, RED text, BOLD
└─────────────────────────┘
```

### **Modern Blue**

```typescript
{
  label: 'Modern Blue',
  description: 'Blue background with white text',
  backgroundColor: '#2563EB',  // Blue
  textColor: '#FFFFFF',        // White
  borderColor: '#1D4ED8',      // Dark Blue
}
```

### **Minimal Gray**

```typescript
{
  label: 'Minimal Gray',
  description: 'Light gray background with dark text',
  backgroundColor: '#F3F4F6',  // Light Gray
  textColor: '#111827',        // Dark Gray
  borderColor: '#3B82F6',      // Blue
}
```

---

## 💻 **Usage Examples**

### **Example 1: Using in a Component**

```tsx
import { useLayoutConfig } from '@/hooks/useLayoutConfig';

const MyComponent = () => {
  const { config } = useLayoutConfig();

  return (
    <div style={{
      width: config.sidebar.width,
      backgroundColor: config.activeMenuItem.backgroundColor,
      color: config.activeMenuItem.textColor,
    }}>
      Content
    </div>
  );
};
```

### **Example 2: Using CSS Variables**

```tsx
const MyStyledComponent = () => {
  return (
    <div className="my-component">
      Content
    </div>
  );
};
```

```css
/* In CSS file */
.my-component {
  width: var(--sidebar-width);
  background: var(--active-bg);
  color: var(--active-text);
  padding: var(--spacing-md);
}
```

### **Example 3: Section C Positioning**

```tsx
const EmployeeForm = () => {
  return (
    <div className="section-c-container">
      <div className="flex-shrink-0 border-b bg-gray-50 px-4 py-3">
        {/* Header */}
      </div>
      <div className="flex-1 overflow-y-auto p-4">
        {/* Scrollable Content */}
      </div>
      <div className="flex-shrink-0 border-t bg-gray-50 px-4 py-3">
        {/* Footer with action buttons */}
      </div>
    </div>
  );
};
```

### **Example 4: Updating Configuration**

```tsx
import { useLayoutConfig } from '@/hooks/useLayoutConfig';

const SettingsComponent = () => {
  const { config, updateSection } = useLayoutConfig();

  const handleWidthChange = (newWidth: number) => {
    updateSection('sidebar', { width: newWidth });
  };

  return (
    <input
      type="number"
      value={config.sidebar.width}
      onChange={(e) => handleWidthChange(parseInt(e.target.value))}
    />
  );
};
```

### **Example 5: Conditional Rendering**

```tsx
import { useLayoutFeature } from '@/hooks/useLayoutConfig';

const SubtitleComponent = () => {
  const showSubtitles = useLayoutFeature('sidebar', 'showSubtitles');

  if (!showSubtitles) return null;

  return <div className="subtitle">Subtitle text</div>;
};
```

---

## 🔄 **Data Flow**

### **1. User Changes Settings**

```
User clicks "Save" in Layout Settings Page
  ↓
LayoutSettingsPage calls updateConfig()
  ↓
useLayoutConfig hook calls LayoutManager.saveConfig()
  ↓
LayoutManager saves to localStorage
  ↓
LayoutManager.applyConfig() updates CSS variables
  ↓
Components re-render with new values
```

### **2. Page Load**

```
App initializes
  ↓
LayoutManager.getInstance() creates singleton
  ↓
LayoutManager.loadConfig() reads from localStorage
  ↓
LayoutManager.applyConfig() sets CSS variables
  ↓
Components render with configured values
```

### **3. Cross-Tab Synchronization**

```
Tab 1: User changes settings
  ↓
localStorage updated
  ↓
Storage event fired
  ↓
Tab 2: useLayoutConfig listens to storage event
  ↓
Tab 2: Updates config state
  ↓
Tab 2: Components re-render
```

---

## ✅ **Benefits**

### **1. Single Source of Truth**
- All layout settings in one place
- No scattered hardcoded values
- Easy to maintain and update

### **2. Type Safety**
- Full TypeScript support
- Compile-time error checking
- IntelliSense autocomplete

### **3. Dynamic Updates**
- Changes apply immediately
- No page reload required
- Live preview in settings

### **4. User Customization**
- Users can personalize layout
- Settings persist across sessions
- Multiple preset options

### **5. Developer Experience**
- Simple API with React hooks
- CSS variables for styling
- Utility classes for positioning

### **6. Performance**
- CSS variables are native and fast
- Singleton pattern prevents duplication
- Minimal re-renders with hooks

---

## 📊 **Configuration Coverage**

| Section | Configurable Properties | CSS Variables |
|---------|------------------------|---------------|
| **Sidebar** | Width, collapse state, subtitles, colors | `--sidebar-width`, `--sidebar-bg`, `--sidebar-border` |
| **Active Menu** | Background, text, border colors, style preset | `--active-bg`, `--active-text`, `--active-border` |
| **Header** | Height, visibility toggles, colors | `--header-height`, `--header-bg`, `--header-border` |
| **Workspace** | Background, padding | `--workspace-bg`, `--workspace-padding` |
| **Status Bar** | Height, visibility, colors | `--statusbar-height`, `--statusbar-bg` |
| **Typography** | Font family, sizes | `--font-family`, `--font-size-*` |
| **Forms** | Grid columns, padding, colors | `--form-error-color`, `--form-input-*` |
| **Spacing** | All spacing values | `--spacing-*` |
| **Theme** | Light/dark/auto | `.dark` class |

---

## 🔌 **Integration Points**

### **Required Imports**

```tsx
// In main App.tsx or index.tsx
import '@/styles/layout.css';

// Initialize LayoutManager
import { layoutManager } from '@/config/layoutConfig';
layoutManager.applyConfig(); // Apply on app start
```

### **Using in Components**

```tsx
// Option 1: React Hooks
import { useLayoutConfig } from '@/hooks/useLayoutConfig';

// Option 2: Direct Access
import { getLayoutConfig } from '@/config/layoutConfig';

// Option 3: CSS Variables (no import needed)
// Just use var(--variable-name) in CSS
```

---

## 🎯 **Best Practices**

### **✅ DO**
- Use CSS variables for styling
- Use utility classes for Section C positioning
- Use React hooks for dynamic values
- Test with different layout configurations
- Document custom CSS variables

### **❌ DON'T**
- Hardcode layout values (256px, 64px, etc.)
- Mix inline styles with CSS variables
- Bypass LayoutManager for updates
- Modify CSS variables directly in code
- Use fixed positioning without CSS variables

---

## 🐛 **Troubleshooting**

### **Settings Not Applying**
1. Check browser console for errors
2. Verify `layout.css` is imported
3. Check localStorage for saved config
4. Try resetting to defaults

### **CSS Variables Not Working**
1. Ensure `:root` variables are defined
2. Check browser DevTools → Computed styles
3. Verify variable names match exactly
4. Check for CSS specificity issues

### **Cross-Tab Sync Not Working**
1. Verify both tabs are same origin
2. Check storage event listener
3. Test in different browser
4. Clear localStorage and retry

---

## 📚 **Related Documentation**

- **Layout Configuration System**: `docs/LAYOUT_CONFIGURATION_SYSTEM.md`
- **Section C Migration Guide**: `docs/SECTION_C_MIGRATION_GUIDE.md`
- **Sidebar Specification**: `docs/specifications/SIDEBAR_NAVIGATION_SPEC.md`
- **Employee Form Specification**: `docs/specifications/EMPLOYEE_FORM_SPEC.md`
- **UI Layout Terminology**: `docs/steering/UI_LAYOUT_TERMINOLOGY.md`

---

## 🔄 **Version History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-12-19 | Development Team | Initial specification with centralized CSS system |

---

**Document Status**: ✅ Approved  
**Last Updated**: 2025-12-19 19:26:51  
**Next Review**: 2026-01-19