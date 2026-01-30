# ⚡ TOOLBAR QUICK START GUIDE

**For**: Agent E (HRM/CRM)  
**Time to Read**: 5 minutes  
**Status**: Ready to Use

---

## 🎯 **3-Step Implementation**

### **Step 1: Add to Django Admin (2 minutes)**

1. Open: `http://localhost:8000/admin/`
2. Go to: **Toolbar Control** → **ERP Menu Items**
3. Click: **Add ERP Menu Item**
4. Fill in:

```
Menu ID: HRM_LEAVE_APPLICATION
Name: Leave Application
View Type: TRANSACTION
Config: NESCKZTJAVPMRDX1234QF
Module: HRM
Is Active: ✓
```

5. Click **Save**

---

### **Step 2: Add Toolbar to Frontend (3 minutes)**

```tsx
import { MasterToolbar, MasterMode } from '@/components/MasterToolbarConfigDriven';
import { useState } from 'react';

export const LeaveApplicationPage = () => {
  const [mode, setMode] = useState<MasterMode>('VIEW');

  const handleAction = (actionId: string) => {
    switch (actionId) {
      case 'new': setMode('CREATE'); break;
      case 'edit': setMode('EDIT'); break;
      case 'save': 
        saveData();
        setMode('VIEW'); 
        break;
      case 'cancel': setMode('VIEW'); break;
      case 'exit': navigate('/dashboard'); break;
      // ... add other actions as needed
    }
  };

  return (
    <>
      <MasterToolbar 
        viewId="HRM_LEAVE_APPLICATION"
        mode={mode}
        onAction={handleAction}
      />
      <div className="content">
        {/* Your page content */}
      </div>
    </>
  );
};
```

---

### **Step 3: Test (1 minute)**

1. Open your page
2. Verify buttons appear
3. Click "New" → Should show Save/Cancel buttons
4. Click "Cancel" → Should show New/Edit buttons

✅ **Done!**

---

## 📋 **Config Strings Cheat Sheet**

Copy-paste these into Django Admin:

| Screen Type | Config String | Use For |
|-------------|---------------|---------|
| **Simple Master** | `NESCKVDXRQF` | Departments, Designations, Leave Types |
| **Advanced Master** | `NESCKVDXRQFIO` | Employees, Customers, Suppliers |
| **Transaction** | `NESCKZTJAVPMRDX1234QF` | Leave Applications, Expense Claims |
| **Report** | `VRXPYQFG` | Attendance Reports, Payroll Reports |
| **Settings** | `ESCKXR` | System Settings, Preferences |

---

## 🔤 **Character Legend (Top 15)**

| Code | Action | When Visible | Shortcut |
|------|--------|--------------|----------|
| **N** | New | VIEW mode | F2 |
| **E** | Edit | VIEW mode | F3 |
| **S** | Save | CREATE/EDIT mode | F8 |
| **C** | Cancel | CREATE/EDIT mode | Esc |
| **K** | Clear | CREATE/EDIT mode | F5 |
| **V** | View | VIEW mode | F7 |
| **D** | Delete | VIEW mode | F4 |
| **X** | Exit | Always | Esc |
| **R** | Refresh | VIEW mode | F9 |
| **Q** | Search | VIEW mode | Ctrl+F |
| **F** | Filter | VIEW mode | Alt+F |
| **I** | Import | VIEW mode | Ctrl+I |
| **O** | Export | VIEW mode | Ctrl+E |
| **Z** | Authorize | VIEW mode | F10 |
| **T** | Submit | VIEW mode | Alt+S |

**Full legend**: See `TOOLBAR_IMPLEMENTATION_EXPLAINED.md` Section 3

---

## 🎨 **Mode Behavior**

### **VIEW Mode** (Browsing)
Shows: New, Edit, Delete, Refresh, Search, Filter, Exit  
Hides: Save, Cancel, Clear

### **CREATE Mode** (Adding New)
Shows: Save, Cancel, Clear, Exit  
Hides: New, Edit, Delete, Refresh, Search, Filter

### **EDIT Mode** (Editing Existing)
Shows: Save, Cancel, Clear, Exit  
Hides: New, Edit, Delete, Refresh, Search, Filter

---

## 🔄 **Mode Transitions**

```
VIEW → Click "New" → CREATE
CREATE → Click "Save" → VIEW
CREATE → Click "Cancel" → VIEW

VIEW → Click "Edit" → EDIT
EDIT → Click "Save" → VIEW
EDIT → Click "Cancel" → VIEW
```

---

## ✅ **Verification Checklist**

After implementation, verify:

- [ ] Django Admin has entry with correct `menu_id`
- [ ] Frontend component imports `MasterToolbar`
- [ ] `viewId` prop matches Django `menu_id`
- [ ] `mode` state variable exists
- [ ] `handleAction` function handles all actions
- [ ] Clicking "New" changes mode to CREATE
- [ ] Clicking "Save" changes mode to VIEW
- [ ] Clicking "Cancel" changes mode to VIEW
- [ ] Buttons appear/hide correctly based on mode

---

## 🆘 **Troubleshooting**

### **Problem**: No buttons appear
**Solution**: Check `menu_id` matches between Django and frontend

### **Problem**: Wrong buttons appear
**Solution**: Verify `mode` prop is correct (VIEW/CREATE/EDIT)

### **Problem**: Buttons don't respond
**Solution**: Check `onAction` handler is wired correctly

### **Problem**: Config not found
**Solution**: Verify `is_active = True` in Django Admin

---

## 📚 **Full Documentation**

For complete details, see:
- **`TOOLBAR_IMPLEMENTATION_EXPLAINED.md`** - Complete guide with examples
- **`01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md`** - Full character reference
- **`01_ESSENTIAL/toolbar-explorer.html`** - Interactive visual tool

---

## 🎯 **Example: HRM Leave Application**

### **Django Admin Entry**
```
Menu ID: HRM_LEAVE_APPLICATION
Name: Leave Application
View Type: TRANSACTION
Config: NESCKZTJAVPMRDX1234QF
Module: HRM
```

### **Frontend Component**
```tsx
<MasterToolbar 
  viewId="HRM_LEAVE_APPLICATION"
  mode={mode}
  onAction={handleAction}
/>
```

### **Result**
- ✅ 21 toolbar buttons configured
- ✅ Automatic mode-based filtering
- ✅ Keyboard shortcuts enabled
- ✅ Consistent with entire platform

---

**Ready to implement?** Start with Step 1! 🚀

---

**Document Owner**: Astra  
**Status**: ⚡ ACTIVE  
**Version**: 1.0  
**Date**: 2026-01-10
