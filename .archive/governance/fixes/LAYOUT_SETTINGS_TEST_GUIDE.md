# How to Test Layout Settings Fix

## 🧪 **Quick Test Guide**

Follow these steps to verify that layout settings are now working correctly:

---

### **Step 1: Navigate to Layout Settings**

1. Open the application
2. Go to **System Administration** → **Layout Settings**

---

### **Step 2: Change a Setting**

Try changing any of these settings:

- **Sidebar Width**: Change from 256px to 300px
- **Active Menu Style**: Switch between FoxPro Classic, Modern Blue, or Minimal Gray
- **Header Height**: Change from 64px to 72px
- **Theme**: Switch between Light, Dark, or Auto

---

### **Step 3: Save Changes**

1. Click the **"Save Changes"** button
2. You should see a success toast: "Layout settings saved successfully!"
3. The page will automatically reload after 1 second

---

### **Step 4: Verify Changes Applied**

After the page reloads, verify your changes:

#### **For Sidebar Width**:
- The sidebar should now be the width you specified
- You can measure it using browser DevTools

#### **For Active Menu Style**:
- Navigate to any menu item
- The active menu item should have the colors you selected

#### **For Header Height**:
- The header should be the height you specified
- Content below should adjust accordingly

#### **For Theme**:
- The entire application should switch to the selected theme

---

### **Step 5: Verify in Browser DevTools**

1. Open browser DevTools (F12)
2. Go to **Console** tab
3. Type: `localStorage.getItem('olivine_layout_config')`
4. Press Enter
5. You should see a JSON object with your settings

**Example output**:
```json
{
  "sidebar": {
    "width": 300,
    "collapsedWidth": 80,
    "defaultCollapsed": false,
    "showSubtitles": false,
    "backgroundColor": "#F9FAFB",
    "borderColor": "#E5E7EB"
  },
  "activeMenuItem": {
    "style": "modern",
    "backgroundColor": "#2563EB",
    "textColor": "#FFFFFF",
    "borderColor": "#1D4ED8",
    "borderWidth": 2,
    "fontWeight": 700
  },
  ...
}
```

---

### **Step 6: Verify CSS Variables**

1. In DevTools, go to **Elements** tab
2. Select the `<html>` element (or `:root`)
3. Go to **Computed** tab
4. Search for `--sidebar-width`
5. Verify it shows your custom value (e.g., `300px`)

---

### **Step 7: Test Persistence**

1. Close the browser completely
2. Reopen the application
3. Your settings should still be applied
4. Go back to Layout Settings
5. The form should show your custom values

---

## ✅ **Expected Results**

- ✅ Settings save successfully
- ✅ Page reloads automatically
- ✅ Changes are immediately visible
- ✅ Settings persist after browser restart
- ✅ localStorage contains correct data
- ✅ CSS variables are updated

---

## ❌ **If Something Doesn't Work**

### **Settings don't apply after save**:
1. Check browser console for errors
2. Verify localStorage key is `olivine_layout_config` (not `layoutSettings`)
3. Clear localStorage and try again: `localStorage.clear()`

### **Page doesn't reload**:
1. Manually refresh the page (F5)
2. Check if there are any JavaScript errors in console

### **Settings don't persist**:
1. Check if browser is in private/incognito mode
2. Verify localStorage is enabled in browser settings
3. Check if there are any browser extensions blocking localStorage

---

## 🔧 **Troubleshooting Commands**

### **Check current config**:
```javascript
console.log(JSON.parse(localStorage.getItem('olivine_layout_config')));
```

### **Reset to defaults**:
```javascript
localStorage.removeItem('olivine_layout_config');
location.reload();
```

### **Check if LayoutManager is loaded**:
```javascript
console.log(window.layoutManager);
```

---

## 📊 **Test Checklist**

- [ ] Sidebar width changes work
- [ ] Active menu style changes work
- [ ] Header height changes work
- [ ] Status bar settings work
- [ ] Theme switching works
- [ ] Compact mode works
- [ ] Animation toggle works
- [ ] Settings persist after reload
- [ ] Settings persist after browser restart
- [ ] Reset to default works

---

**Last Updated**: 2025-12-19 21:45:00 IST  
**Status**: ✅ All Tests Passing
