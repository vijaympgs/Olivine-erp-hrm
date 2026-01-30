# 📋 PHASE 3: TOOLBAR CONFIGURATION CLEANUP - MANUAL STEPS
**Date**: 2026-01-09 14:50 IST  
**Agent**: Astra  
**Status**: ⏳ **REQUIRES MANUAL DJANGO ADMIN UPDATE**

---

## 🎯 OBJECTIVE
Update 4 menu items with correct toolbar strings as per `toolbar-revisit-checklist.md`.

---

## 📝 REQUIRED UPDATES

### **Method 1: Django Admin (Recommended)** ✅

1. **Access Django Admin**:
   - Navigate to: `http://localhost:8000/admin/`
   - Login with admin credentials
   - Go to: **Toolbar Control** → **Items** (ERPMenuItem)

2. **Update Each Menu Item**:

| Menu ID | Current Config | New Config | Description |
|---------|---------------|------------|-------------|
| `MOVEMENT_TYPES` | (check current) | `NRQFX` | List view: New, Refresh, Search, Filter, Exit |
| `VALUATION_METHODS` | (check current) | `VRX` | View, Refresh, Exit only |
| `INV_PARAMETERS` | (check current) | `ESCKXR` | Edit, Save, Cancel, Clear, Exit, Refresh |
| `APPROVAL_RULES` | (check current) | `NRQFX` | List view: New, Refresh, Search, Filter, Exit |

3. **Steps for Each Item**:
   - Search for the `menu_id` (e.g., "MOVEMENT_TYPES")
   - Click to edit
   - Update the `applicable_toolbar_config` field
   - Click **Save**

---

### **Method 2: Django Shell** (Alternative)

1. **Start Django Shell**:
```powershell
cd backend\domain\master
python manage.py shell
```

2. **Run Update Script**:
```python
from core.auth_access.backend.menu_registry.models import ERPMenuItem

# Update configurations
updates = {
    'MOVEMENT_TYPES': 'NRQFX',
    'VALUATION_METHODS': 'VRX',
    'INV_PARAMETERS': 'ESCKXR',
    'APPROVAL_RULES': 'NRQFX'
}

print("Updating toolbar configurations...")
for menu_id, config in updates.items():
    try:
        item = ERPMenuItem.objects.get(menu_id=menu_id)
        old_config = item.applicable_toolbar_config
        item.applicable_toolbar_config = config
        item.save()
        print(f"✓ {menu_id}: {old_config} → {config}")
    except ERPMenuItem.DoesNotExist:
        print(f"✗ {menu_id}: NOT FOUND")

print("\nDone!")
```

3. **Exit Shell**:
```python
exit()
```

---

### **Method 3: Direct SQL** (Advanced)

```sql
-- Update MOVEMENT_TYPES
UPDATE auth_access_erpmenuitem 
SET applicable_toolbar_config = 'NRQFX' 
WHERE menu_id = 'MOVEMENT_TYPES';

-- Update VALUATION_METHODS
UPDATE auth_access_erpmenuitem 
SET applicable_toolbar_config = 'VRX' 
WHERE menu_id = 'VALUATION_METHODS';

-- Update INV_PARAMETERS
UPDATE auth_access_erpmenuitem 
SET applicable_toolbar_config = 'ESCKXR' 
WHERE menu_id = 'INV_PARAMETERS';

-- Update APPROVAL_RULES
UPDATE auth_access_erpmenuitem 
SET applicable_toolbar_config = 'NRQFX' 
WHERE menu_id = 'APPROVAL_RULES';

-- Verify updates
SELECT menu_id, applicable_toolbar_config 
FROM auth_access_erpmenuitem 
WHERE menu_id IN ('MOVEMENT_TYPES', 'VALUATION_METHODS', 'INV_PARAMETERS', 'APPROVAL_RULES');
```

---

## 📖 TOOLBAR STRING REFERENCE

### **Character Map**
| Char | Button | F-Key | Permission |
|------|--------|-------|------------|
| N | New | F2 | can_create |
| E | Edit | F4 | can_edit |
| S | Save | F8 | (UI state) |
| C | Cancel | ESC | (UI state) |
| K | Clear | F5 | (UI state) |
| V | View | F7 | can_view |
| R | Refresh | F9 | (always) |
| Q | Search | Ctrl+F | (always) |
| F | Filter | Ctrl+Shift+F | (always) |
| X | Exit | ESC | (always) |

### **Common Patterns**
- **List View**: `NRQFX` (New, Refresh, Search, Filter, Exit)
- **View Only**: `VRX` (View, Refresh, Exit)
- **Edit Form**: `ESCKXR` (Edit, Save, Cancel, Clear, Exit, Refresh)
- **Master Data**: `NESCKPVDXRQ` (All except workflow actions)
- **Transaction**: `NESCKPVDXRTJZ` (All including workflow)

---

## ✅ VERIFICATION STEPS

After updating, verify the changes:

### **1. Check Database**
```python
from core.auth_access.backend.menu_registry.models import ERPMenuItem

for menu_id in ['MOVEMENT_TYPES', 'VALUATION_METHODS', 'INV_PARAMETERS', 'APPROVAL_RULES']:
    item = ERPMenuItem.objects.get(menu_id=menu_id)
    print(f"{menu_id}: {item.applicable_toolbar_config}")
```

### **2. Test Frontend**
1. Navigate to each page:
   - `/inventory/config/movement-types`
   - `/inventory/config/valuation-methods`
   - `/inventory/config/settings`
   - `/inventory/config/approval-rules`

2. Verify toolbar buttons match expected config
3. Test keyboard shortcuts (F2, F9, ESC, etc.)

---

## 🎯 EXPECTED RESULTS

### **MOVEMENT_TYPES** (`NRQFX`)
**Visible Buttons**: New, Refresh, Search, Filter, Exit  
**Hidden Buttons**: Edit, Save, Cancel, Delete, etc.  
**Use Case**: List of movement types (GRN, Issue, Transfer, etc.)

### **VALUATION_METHODS** (`VRX`)
**Visible Buttons**: View, Refresh, Exit  
**Hidden Buttons**: New, Edit, Save, Delete, etc.  
**Use Case**: View-only page showing FIFO/LIFO/Weighted Avg settings

### **INV_PARAMETERS** (`ESCKXR`)
**Visible Buttons**: Edit, Save, Cancel, Clear, Exit, Refresh  
**Hidden Buttons**: New, Delete, etc.  
**Use Case**: Edit global inventory settings (no create/delete)

### **APPROVAL_RULES** (`NRQFX`)
**Visible Buttons**: New, Refresh, Search, Filter, Exit  
**Hidden Buttons**: Edit, Save, Cancel, Delete, etc.  
**Use Case**: List of approval rules with ability to create new

---

## 📊 PHASE 3 STATUS

| Task | Status | Method |
|------|--------|--------|
| Identify menu items | ✅ Complete | Checklist review |
| Determine correct configs | ✅ Complete | Pattern analysis |
| Create update scripts | ✅ Complete | Python + SQL |
| **Execute updates** | ⏳ **PENDING** | **Manual Django Admin** |
| Verify changes | ⏳ Pending | After updates |
| Test frontend | ⏳ Pending | After updates |

---

## 🚀 NEXT STEPS

1. **YOU (Viji)**: Update the 4 menu items using Django Admin (Method 1)
2. **Astra**: Verify updates and test frontend behavior
3. **Proceed**: Move to Phase 4 (Inventory UI Development)

---

## 📁 FILES CREATED

1. `backend/update_toolbar_configs.py` - Automated update script (Django setup issues)
2. `update_toolbar_simple.py` - Simple shell script (ready to use)
3. This document - Manual update guide

---

**Prepared By**: Astra  
**Date**: 2026-01-09 14:50 IST  
**Status**: ⏳ **AWAITING MANUAL UPDATE**  
**Estimated Time**: 5-10 minutes (Django Admin method)
