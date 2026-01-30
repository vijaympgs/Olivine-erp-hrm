# POS Screen - Cart Header Alignment Fix

## 🐛 **Issue**
The cart header in the POS screen is being overlapped by the application header (Section B).

## 📍 **Location**
**File**: `frontend/src/modules/pos/billing/PosDesktop.tsx`  
**Line**: 711-713

## 🔧 **Fix Required**

### **Current Code** (Line 711-713):
```tsx
return (
  <div className="flex flex-col h-full overflow-hidden" style={{ backgroundColor: '#f5f5f5' }}>
    {/* Section 2: Main Content - 70/30 Split */}
    <main className="relative flex-1 flex overflow-hidden gap-1" id="section-2-main-content">
```

### **Updated Code**:
```tsx
return (
  <div className="flex flex-col overflow-hidden" style={{ 
    backgroundColor: '#f5f5f5',
    marginTop: 'var(--header-height, 64px)',
    height: 'calc(100vh - var(--header-height, 64px) - var(--statusbar-height, 48px))'
  }}>
    {/* Section 2: Main Content - 70/30 Split */}
    <main className="relative flex-1 flex overflow-hidden gap-1" id="section-2-main-content">
```

## 📝 **Explanation**

The fix adds:
1. **`marginTop: 'var(--header-height, 64px)'`** - Pushes content down by header height
2. **`height: calc(...)`** - Calculates exact height accounting for header and status bar
3. Uses CSS variables so it adapts to layout configuration changes

## ✅ **Benefits**

- ✅ Cart header no longer overlapped
- ✅ Proper spacing from application header
- ✅ Respects layout configuration changes
- ✅ Works with sidebar collapse/expand

## 🎯 **Alternative Simple Fix**

If CSS variables aren't working, use fixed values:

```tsx
style={{ 
  backgroundColor: '#f5f5f5',
  marginTop: '64px',
  height: 'calc(100vh - 64px - 48px)'
}}
```

---

**Created**: 2025-12-19 19:34:58  
**Priority**: High  
**Status**: Ready to apply
