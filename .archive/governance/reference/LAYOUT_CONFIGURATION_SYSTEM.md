# Layout Configuration System

## 📋 Overview

The Layout Configuration System provides centralized control over all layout-related settings in the application. It uses a combination of TypeScript configuration, CSS variables, and React hooks to enable dynamic, user-customizable layouts.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   User Interface                         │
│              (Layout Settings Page)                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              React Hooks Layer                           │
│         (useLayoutConfig, useLayoutSection)              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           LayoutManager (Singleton)                      │
│   - Load/Save Configuration                              │
│   - Apply CSS Variables                                  │
│   - Manage State                                         │
└────────────────────┬────────────────────────────────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│   localStorage   │  │  CSS Variables   │
│  (Persistence)   │  │   (:root)        │
└──────────────────┘  └──────────────────┘
```

## 📁 File Structure

```
frontend/src/
├── config/
│   └── layoutConfig.ts          # Central configuration & LayoutManager
├── styles/
│   └── layout.css               # Global CSS with variables
├── hooks/
│   └── useLayoutConfig.ts       # React hooks for config access
└── pages/admin/
    └── LayoutSettingsPage.tsx   # UI for managing settings
```

## 🔧 Core Files

### 1. `layoutConfig.ts` - Central Configuration

**Purpose**: Single source of truth for all layout settings

**Key Components**:
- `LayoutConfig` interface - TypeScript definition
- `defaultLayoutConfig` - Default values
- `LayoutManager` class - Singleton for managing config
- `activeMenuPresets` - Predefined style presets

**Usage**:
```typescript
import { layoutManager, getLayoutConfig } from '@/config/layoutConfig';

// Get current config
const config = getLayoutConfig();

// Update config
layoutManager.saveConfig(newConfig);

// Reset to defaults
layoutManager.resetConfig();

// Apply a preset
layoutManager.applyActiveMenuPreset('foxpro');
```

### 2. `layout.css` - CSS Variables

**Purpose**: Define CSS variables controlled by LayoutManager

**Key Variables**:
```css
/* Sidebar */
--sidebar-width: 256px;
--active-bg: #22D3EE;
--active-text: #DC2626;

/* Header */
--header-height: 64px;

/* Status Bar */
--statusbar-height: 48px;

/* Typography */
--font-family: 'Inter', sans-serif;
--font-size-base: 16px;
```

**Usage in Components**:
```css
.my-component {
  width: var(--sidebar-width);
  background: var(--active-bg);
  color: var(--active-text);
}
```

### 3. `useLayoutConfig.ts` - React Hooks

**Purpose**: React integration for layout configuration

**Hooks**:

#### `useLayoutConfig()`
Get full configuration with update methods
```tsx
const { config, updateConfig, resetConfig, updateSection } = useLayoutConfig();
```

#### `useLayoutSection(section)`
Get specific section of configuration
```tsx
const sidebarConfig = useLayoutSection('sidebar');
console.log(sidebarConfig.width); // 256
```

#### `useLayoutFeature(section, feature)`
Get specific feature flag
```tsx
const showSubtitles = useLayoutFeature('sidebar', 'showSubtitles');
const compactMode = useLayoutFeature('general', 'compactMode');
```

## 📐 Configuration Structure

```typescript
interface LayoutConfig {
  sidebar: {
    width: number;                    // 256
    collapsedWidth: number;           // 80
    defaultCollapsed: boolean;        // false
    showSubtitles: boolean;           // false
    backgroundColor: string;          // '#F9FAFB'
    borderColor: string;              // '#E5E7EB'
  };

  activeMenuItem: {
    style: 'foxpro' | 'modern' | 'minimal' | 'custom';
    backgroundColor: string;          // '#22D3EE' (cyan)
    textColor: string;                // '#DC2626' (red)
    borderColor: string;              // '#DC2626' (red)
    borderWidth: number;              // 2
    fontWeight: number;               // 700
  };

  header: {
    height: number;                   // 64
    backgroundColor: string;          // '#FFFFFF'
    borderColor: string;              // '#E5E7EB'
    showUserMenu: boolean;            // true
    showNotifications: boolean;       // true
    showSearch: boolean;              // true
  };

  workspace: {
    backgroundColor: string;          // '#FFFFFF'
    padding: number;                  // 16
  };

  statusBar: {
    height: number;                   // 48
    show: boolean;                    // true
    backgroundColor: string;          // '#F9FAFB'
    borderColor: string;              // '#E5E7EB'
    showConnectionStatus: boolean;    // true
    showSessionInfo: boolean;         // true
  };

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

  forms: {
    defaultGridColumns: number;       // 3
    inputPadding: string;             // '6px 8px'
    labelFontSize: string;            // '12px'
    errorColor: string;               // '#DC2626'
  };
}
```

## 🎨 Style Presets

### FoxPro Classic (Default)
```typescript
{
  backgroundColor: '#22D3EE',  // Cyan
  textColor: '#DC2626',        // Red
  borderColor: '#DC2626',      // Red
}
```

### Modern Blue
```typescript
{
  backgroundColor: '#2563EB',  // Blue
  textColor: '#FFFFFF',        // White
  borderColor: '#1D4ED8',      // Dark Blue
}
```

### Minimal Gray
```typescript
{
  backgroundColor: '#F3F4F6',  // Light Gray
  textColor: '#111827',        // Dark Gray
  borderColor: '#3B82F6',      // Blue
}
```

## 💻 Usage Examples

### Example 1: Using in a Component

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

### Example 2: Updating Configuration

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

### Example 3: Using CSS Variables

```tsx
const MyStyledComponent = () => {
  return (
    <div className="my-component">
      Content
    </div>
  );
};

// In CSS file:
// .my-component {
//   width: var(--sidebar-width);
//   background: var(--active-bg);
//   color: var(--active-text);
// }
```

### Example 4: Conditional Rendering

```tsx
import { useLayoutFeature } from '@/hooks/useLayoutConfig';

const SubtitleComponent = () => {
  const showSubtitles = useLayoutFeature('sidebar', 'showSubtitles');

  if (!showSubtitles) return null;

  return <div className="subtitle">Subtitle text</div>;
};
```

## 🔄 How It Works

### 1. Initialization
```
App Starts → LayoutManager.getInstance() → Load from localStorage → Apply CSS Variables
```

### 2. User Changes Settings
```
User Updates → LayoutSettingsPage → useLayoutConfig.updateConfig() 
→ LayoutManager.saveConfig() → Save to localStorage → Apply CSS Variables → Re-render
```

### 3. CSS Variables Application
```typescript
// LayoutManager.applyConfig()
const root = document.documentElement;
root.style.setProperty('--sidebar-width', `${config.sidebar.width}px`);
root.style.setProperty('--active-bg', config.activeMenuItem.backgroundColor);
// ... etc
```

### 4. Cross-Tab Synchronization
```
Tab 1 Updates → localStorage → Storage Event → Tab 2 Listens → Updates Config → Re-render
```

## 🎯 Benefits

### ✅ Centralized Control
- Single source of truth for all layout settings
- Easy to maintain and update
- Consistent across the application

### ✅ Type Safety
- Full TypeScript support
- Compile-time error checking
- IntelliSense autocomplete

### ✅ Dynamic Updates
- Changes apply immediately
- No page reload required (for most settings)
- Live preview in settings page

### ✅ Persistence
- Settings saved to localStorage
- Survives page refreshes
- Can be extended to backend API

### ✅ Performance
- CSS variables are performant
- Minimal re-renders with React hooks
- Singleton pattern prevents multiple instances

### ✅ Flexibility
- Easy to add new settings
- Preset system for common configurations
- Custom values supported

## 🔌 Integration Points

### Adding a New Setting

1. **Update Interface** (`layoutConfig.ts`):
```typescript
export interface LayoutConfig {
  // ... existing config
  myNewSection: {
    myNewSetting: string;
  };
}
```

2. **Update Default Config** (`layoutConfig.ts`):
```typescript
export const defaultLayoutConfig: LayoutConfig = {
  // ... existing defaults
  myNewSection: {
    myNewSetting: 'default value',
  },
};
```

3. **Add CSS Variable** (`layoutConfig.ts` - `applyConfig` method):
```typescript
root.style.setProperty('--my-new-setting', this.config.myNewSection.myNewSetting);
```

4. **Define CSS Variable** (`layout.css`):
```css
:root {
  --my-new-setting: 'default value';
}
```

5. **Add UI Control** (`LayoutSettingsPage.tsx`):
```tsx
<input
  value={settings.myNewSection.myNewSetting}
  onChange={(e) => handleChange('myNewSetting', e.target.value)}
/>
```

## 📱 Responsive Behavior

The system includes built-in responsive adjustments:

```css
@media (max-width: 768px) {
  :root {
    --sidebar-width: 0px;
    --sidebar-collapsed-width: 0px;
  }
}
```

## 🌙 Theme Support

### Light Theme (Default)
```css
:root {
  --sidebar-bg: #F9FAFB;
  --workspace-bg: #FFFFFF;
}
```

### Dark Theme
```css
.dark {
  --sidebar-bg: #1F2937;
  --workspace-bg: #111827;
}
```

### Auto Theme
Automatically switches based on system preference:
```typescript
if (config.general.theme === 'auto') {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  // Apply appropriate theme
}
```

## 🚀 Performance Considerations

- **CSS Variables**: Native browser feature, very fast
- **Singleton Pattern**: Only one LayoutManager instance
- **Memoization**: React hooks prevent unnecessary re-renders
- **localStorage**: Synchronous but fast for small data

## 🔒 Security

- All settings stored in localStorage (client-side only)
- No sensitive data in configuration
- Can be extended to validate settings before applying
- Backend API integration possible for enterprise features

## 📚 Related Documentation

- **Layout Specifications**: `docs/specifications/SIDEBAR_NAVIGATION_SPEC.md`
- **Employee Form Spec**: `docs/specifications/EMPLOYEE_FORM_SPEC.md`
- **UI Layout Terminology**: `docs/steering/UI_LAYOUT_TERMINOLOGY.md`

## 🐛 Troubleshooting

### Settings Not Applying
1. Check browser console for errors
2. Verify localStorage is enabled
3. Try resetting to defaults
4. Clear browser cache

### CSS Variables Not Working
1. Ensure `layout.css` is imported
2. Check browser DevTools → Elements → Computed styles
3. Verify CSS variable names match

### Cross-Tab Sync Not Working
1. Check if both tabs are on same origin
2. Verify storage event listener is attached
3. Test in different browser

---

**Version**: 1.0.0  
**Last Updated**: 2025-12-19  
**Maintainer**: Development Team
