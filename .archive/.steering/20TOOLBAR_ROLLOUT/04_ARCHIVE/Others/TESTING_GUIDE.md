# ✅ **PHASE 2D: TESTING & VALIDATION GUIDE**

**Date**: 2026-01-10 09:50 IST  
**Agent**: Astra  
**Status**: TESTING GUIDE COMPLETE

---

## 🎯 **TESTING OVERVIEW**

This document provides comprehensive testing instructions for the toolbar permission system.

---

## 📋 **TESTING CHECKLIST**

### **Backend Tests** ✅

#### **Test 1: Database Schema**
**Objective**: Verify new fields exist in RolePermission model

**Steps**:
1. Open Django admin: `http://localhost:8000/admin/`
2. Navigate to: User Management → Role Permissions
3. Click on any permission record
4. **Verify**: Fields `toolbar_string` and `toolbar_permissions` are visible

**Expected Result**: ✅ Both fields exist and are editable

---

#### **Test 2: Permission Resolution Service**
**Objective**: Test the 5-step resolution pipeline

**Steps**:
1. Open Django shell: `python manage.py shell`
2. Run:
```python
from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.services.toolbar_permission_service import resolve_toolbar_permissions

User = get_user_model()
admin = User.objects.get(username='admin')

# Test VIEW mode
result = resolve_toolbar_permissions(admin.id, 'INVENTORY_UOM_SETUP', 'VIEW')
print(f"VIEW Mode: {result['allowed_actions']}")

# Test NEW mode
result = resolve_toolbar_permissions(admin.id, 'INVENTORY_UOM_SETUP', 'NEW')
print(f"NEW Mode: {result['allowed_actions']}")
```

**Expected Results**:
- ✅ VIEW mode: Returns actions like `['new', 'edit', 'view', 'delete', 'refresh', 'search', 'filter', 'exit']`
- ✅ NEW mode: Returns ONLY `['save', 'cancel', 'clear', 'exit']` (+ optional notes, attach, help)
- ✅ Admin gets full permissions (all 1s in mask)

---

#### **Test 3: API Endpoint**
**Objective**: Verify `/api/user-management/toolbar-permissions/` works

**Steps**:
1. Login to frontend: `http://localhost:3000/login`
2. Open browser DevTools → Network tab
3. Navigate to any screen (e.g., UOM Setup)
4. Look for API call to `/toolbar-permissions/`

**Expected Result**: ✅ API returns JSON with `allowed_actions` array

**Manual Test (using browser console)**:
```javascript
fetch('/api/user-management/toolbar-permissions/?menu_id=INVENTORY_UOM_SETUP&mode=VIEW', {
  headers: {
    'Authorization': 'Token YOUR_TOKEN'
  }
})
.then(r => r.json())
.then(data => console.log(data));
```

---

### **Frontend Tests** ✅

#### **Test 4: Toolbar Rendering**
**Objective**: Verify toolbar shows correct buttons based on mode

**Steps**:
1. Navigate to UOM Setup: `http://localhost:3000/retail/inventory/uom-setup`
2. **VIEW Mode**: Verify toolbar shows: New, Edit, View, Delete, Refresh, Search, Filter, Exit
3. Click "New" button
4. **NEW Mode**: Verify toolbar shows ONLY: Save, Cancel, Clear, Exit (+ optional Notes, Attach, Help)
5. **Verify**: NO Search, NO Refresh, NO New, NO Edit in NEW mode

**Expected Results**:
- ✅ VIEW mode: Shows data operations (N, E, V, D, R, Q, F, X)
- ✅ NEW mode: Shows ONLY form operations (S, C, K, X)
- ✅ Mode Law is strictly enforced

---

#### **Test 5: Permission Matrix UI**
**Objective**: Verify permission assignment UI uses toolbar characters

**Steps**:
1. Navigate to: `http://localhost:3000/security/user-permissions`
2. Go to "Role Permissions Matrix" tab
3. **Verify**: Column headers show: N, E, S, C, K, V, D, X, R, Q, F (NOT A, V, C, E, D)
4. Toggle a checkbox for "New" (N) permission
5. Click "Save Permissions"
6. Refresh page
7. **Verify**: Checkbox state persists

**Expected Results**:
- ✅ Headers show toolbar characters (N, E, S, C, K, etc.)
- ✅ 11 columns per role (not 5)
- ✅ Checkboxes toggle correctly
- ✅ Save functionality works

---

### **Mode Law Validation** ✅

#### **Test 6: VIEW Mode Law**
**Objective**: Verify VIEW mode NEVER shows S, C, K

**Test Cases**:
| Screen | Mode | Should Show | Should NOT Show |
|--------|------|-------------|-----------------|
| UOM Setup | VIEW | N, E, V, D, R, Q, F, X | S, C, K |
| Customer Master | VIEW | N, E, V, D, R, Q, F, X | S, C, K |
| Purchase Order | VIEW | N, E, V, D, R, Q, F, X | S, C, K |

**Expected Result**: ✅ Save, Cancel, Clear NEVER appear in VIEW mode

---

#### **Test 7: NEW/EDIT Mode Law**
**Objective**: Verify NEW/EDIT mode ONLY shows S, C, K, X (+ optional B, G, ?)

**Test Cases**:
| Screen | Mode | Should Show | Should NOT Show |
|--------|------|-------------|-----------------|
| UOM Setup | NEW | S, C, K, X | N, E, V, D, R, Q, F |
| Customer Master | EDIT | S, C, K, X | N, E, V, D, R, Q, F |
| Purchase Order | NEW | S, C, K, X | N, E, V, D, R, Q, F |

**Expected Result**: ✅ ONLY form actions appear in NEW/EDIT mode

---

### **Role-Based Permission Tests** ✅

#### **Test 8: Admin Permissions**
**Objective**: Verify admin always gets full permissions

**Steps**:
1. Login as admin (admin/admin123)
2. Navigate to any screen in VIEW mode
3. **Verify**: ALL actions visible (N, E, V, D, R, Q, F, X)
4. Switch to NEW mode
5. **Verify**: Only S, C, K, X visible (Mode Law still applies!)

**Expected Result**: ✅ Admin sees all permitted actions, but Mode Law still enforced

---

#### **Test 9: Restricted User Permissions**
**Objective**: Verify users without Delete permission never see Delete button

**Steps**:
1. In Permission Matrix, uncheck "Delete" (D) for "Back Office User" role
2. Save permissions
3. Login as a Back Office User
4. Navigate to UOM Setup
5. **Verify**: Delete button is NOT visible

**Expected Result**: ✅ Delete button hidden for users without permission

---

### **Screen-Specific Tests** ✅

#### **Test 10: Customer Master (NESCKVDXRQF)**
**Objective**: Verify Customer Master toolbar config

**Steps**:
1. Navigate to Customer Master
2. **VIEW Mode**: Verify shows N, E, V, D, R, Q, F, X (NO S, C, K)
3. Click "New"
4. **NEW Mode**: Verify shows ONLY S, C, K, X

**Expected Result**: ✅ Toolbar matches config string `NESCKVDXRQF`

---

#### **Test 11: Purchase Order (NESCKZTJAVPMRDX1234QF)**
**Objective**: Verify Purchase Order toolbar config (more complex)

**Steps**:
1. Navigate to Purchase Order
2. **VIEW Mode**: Verify shows N, E, V, D, R, Q, F, X, Z, T, J, A, P, M, 1, 2, 3, 4
3. Click "New"
4. **NEW Mode**: Verify shows ONLY S, C, K, X

**Expected Result**: ✅ Toolbar matches config string, Mode Law enforced

---

## 🎯 **VALIDATION CRITERIA (8 Tests)**

| # | Criteria | Status |
|---|----------|--------|
| 1 | Admin sees all actions in VIEW mode | ⏳ Test |
| 2 | Admin sees only S,C,K,X in NEW/EDIT mode | ⏳ Test |
| 3 | User without Delete never sees Delete | ⏳ Test |
| 4 | User with Submit does NOT see Submit in EDIT | ⏳ Test |
| 5 | No screen shows Save in VIEW mode | ⏳ Test |
| 6 | No screen shows Search in EDIT mode | ⏳ Test |
| 7 | Customer Master (NESCKVDXRQF) behaves correctly | ⏳ Test |
| 8 | Purchase Order (NESCKZTJAVPMRDX...) behaves correctly | ⏳ Test |

---

## 🚀 **QUICK START TESTING**

### **Fastest Way to Test**:

1. **Start Backend**: `python manage.py runserver` (already running ✅)
2. **Start Frontend**: `npm run dev` (in frontend directory)
3. **Login**: admin/admin123
4. **Test Sequence**:
   - Go to UOM Setup → Verify VIEW mode toolbar
   - Click "New" → Verify NEW mode toolbar
   - Go to User Permissions → Verify character-based matrix
   - Toggle permissions → Save → Verify persistence

---

## 📊 **EXPECTED BEHAVIOR SUMMARY**

### **VIEW Mode**:
- ✅ Shows: N, E, V, D, R, Q, F, X (data operations)
- ❌ Never shows: S, C, K (form operations)

### **NEW/EDIT Mode**:
- ✅ Shows: S, C, K, X (form operations)
- ❌ Never shows: N, E, V, D, R, Q, F (data operations)

### **Admin User**:
- ✅ Gets all permissions (all 1s in mask)
- ✅ Mode Law still applies (no Save in VIEW, no Search in EDIT)

### **Permission Matrix**:
- ✅ Shows 11 columns per role (N E S C K V D X R Q F)
- ✅ Checkboxes toggle toolbar_N, toolbar_E, etc.
- ✅ Save converts to permission mask string

---

## 🎯 **TESTING COMPLETE**

**All tests documented!**

**Next Steps**:
1. Run manual tests following this guide
2. Report any failures
3. Fix issues if found
4. Mark validation criteria as complete

---

**Last Updated**: 2026-01-10 09:50 IST  
**Agent**: Astra  
**Status**: TESTING GUIDE READY
