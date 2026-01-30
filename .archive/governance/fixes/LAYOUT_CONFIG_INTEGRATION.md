# Layout Configuration Integration Fix

## 🐛 **Problem**
User reported that layout settings (specifically "Enable Subtitles") were not persisting or applying correctly after login/logout.
Upon investigation, it was found that:
1. `Sidebar.tsx` was using a hardcoded `const SHOW_SUBTITLES = false` constant, completely ignoring the global layout configuration.
2. `AppHeader.tsx` was not checking layout configuration for elements like "Search" or "User Menu", rendering them unconditionally.
3. React components were not subscribed to layout updates, so changes in the Settings page wouldn't reflect immediately without a full reload in some cases (though `Sidebar` had no logic to read them anyway).

## 🔧 **Solution Implemented**

### **1. Sidebar Integration (`Sidebar.tsx`)**
- Replaced hardcoded `SHOW_SUBTITLES` constant.
- Integrated `useLayoutConfig` hook to read `config.sidebar.showSubtitles`.
- Initialized `isCollapsed` state from `config.sidebar.defaultCollapsed`.
- Updates to settings now trigger immediate re-renders of the Sidebar.

### **2. Header Integration (`AppHeader.tsx`)**
- Integrated `useLayoutConfig` hook.
- Added conditional rendering for:
  - **Search Button**: Controlled by `config.header.showSearch`.
  - **User Menu**: Controlled by `config.header.showUserMenu`.
- Updated `Ctrl+K` shortcut listener to respect the `showSearch` setting (shortcut is disabled if search is hidden).

### **3. Architecture Alignment**
- Both components now adhere to the specification in `docs/specifications/CENTRALIZED_CSS_CONFIG.md`.
- They function as reactive consumers of the `LayoutManager` state.

## 📁 **Files Modified**
- `frontend/src/ui/components/Sidebar.tsx`
- `frontend/src/ui/components/AppHeader.tsx`

## 🎯 **Verification**
1. **Subtitles**:
   - Go to Admin > Layout Settings.
   - Toggle "Show Subtitles" ON.
   - **Expectation**: Subtitles appear immediately in the sidebar.
   - Logout and Login.
   - **Expectation**: Subtitles are still visible.

2. **Header Elements**:
   - Go to Admin > Layout Settings.
   - Toggle "Show Search" OFF.
   - **Expectation**: Search icon disappears from header. `Ctrl+K` does nothing.
   - Toggle "Show User Menu" OFF.
   - **Expectation**: User icon (avatar) disappears from header.

3. **Persistence**:
   - Change multiple settings.
   - Reload page (F5).
   - **Expectation**: All settings match what was saved.

---
**Date**: 2025-12-19
**Status**: ✅ Fixed
