# 🎯 BENCHMARK STABILIZATION REPORT

**Date**: 2026-01-09 19:45 IST  
**Screens**: UOM Setup + Purchase Order List  
**Status**: ⚠️ DISCREPANCIES FOUND - REQUIRES FIXES

---

## 📊 CURRENT STATE ANALYSIS

### **1. UOM SETUP** (Masters - Simple)

#### **Backend (Django)**:
```json
{
  "menu_id": "inventory_uom_setup",
  "menu_name": "UOM Setup",
  "view_type": "CONFIGURATION",
  "applicable_toolbar_config": "ESCKXR",
  "route_path": "/inventory/uoms"
}
```

#### **Frontend** (`UOMSetup.tsx`):
```typescript
<MasterToolbar
  viewId="INVENTORY_UOM_SETUP"  // ❌ MISMATCH - Backend has lowercase
  mode={getToolbarMode()}
  onAction={handleToolbarAction}
  hasSelection={!!selectedUOMId}
/>
```

#### **🔴 ISSUES IDENTIFIED**:
1. **viewId Mismatch**: Frontend uses `INVENTORY_UOM_SETUP`, backend has `inventory_uom_setup`
2. **View Type Wrong**: Backend has `CONFIGURATION`, should be `MASTER`
3. **Config Wrong**: Backend has `ESCKXR` (Config screen), should be `NESCKVDXRQF` (Masters - Simple)

---

### **2. PURCHASE ORDER LIST** (Transactions)

#### **Backend (Django)**:
```json
{
  "menu_id": "PURCHASE_ORDERS",
  "menu_name": "Purchase Orders",
  "view_type": "TRANSACTION",
  "applicable_toolbar_config": "NESCKZTJAVPMRDX1234QF",
  "route_path": "/procurement/orders"
}
```

#### **Frontend** (`PurchaseOrderListPage.tsx`):
```typescript
<MasterToolbar
  viewId="PURCHASE_ORDERS"  // ✅ MATCHES
  mode={mode}
  onAction={handleToolbarAction}
  hasSelection={selectedIds.length > 0}
  allowedActions={[...]}  // ❌ HARDCODED - Should be removed
/>
```

#### **🔴 ISSUES IDENTIFIED**:
1. **Hardcoded allowedActions**: Should be removed to let backend drive
2. **This is a LIST VIEW page**: Should have separate entry with `view_type: LIST_VIEW` and config `NRQFX`

---

## ✅ REQUIRED FIXES

### **Fix 1: UOM Setup Backend**
Update Django Admin entry:
- **menu_id**: Change to `INVENTORY_UOM_SETUP` (uppercase to match frontend)
- **view_type**: Change from `CONFIGURATION` to `MASTER`
- **applicable_toolbar_config**: Change from `ESCKXR` to `NESCKVDXRQF`

### **Fix 2: UOM Setup Frontend**
No changes needed - already correct!

### **Fix 3: Purchase Order List Frontend**
Remove hardcoded `allowedActions` prop:
```typescript
<MasterToolbar
  viewId="PURCHASE_ORDERS"
  mode={mode}
  onAction={handleToolbarAction}
  hasSelection={selectedIds.length > 0}
  showLabels={false}
  // ❌ REMOVE: allowedActions={[...]}
/>
```

### **Fix 4: Purchase Order - Create List View Entry**
Add new Django Admin entry for the list/index page:
- **menu_id**: `purchase-orders` (lowercase, hyphenated)
- **menu_name**: "Purchase Orders List"
- **view_type**: `LIST_VIEW`
- **applicable_toolbar_config**: `NRQFX`
- **route_path**: `/procurement/purchase-orders`

---

## 🎯 EXPECTED FINAL STATE

### **UOM Setup**:
| Field | Value |
|-------|-------|
| menu_id | `INVENTORY_UOM_SETUP` |
| view_type | `MASTER` |
| config | `NESCKVDXRQF` |
| route | `/inventory/uoms` |

### **Purchase Orders (Transaction)**:
| Field | Value |
|-------|-------|
| menu_id | `PURCHASE_ORDERS` |
| view_type | `TRANSACTION` |
| config | `NESCKZTJAVPMRDX1234QF` |
| route | `/procurement/orders` |

### **Purchase Orders (List View)** - NEW:
| Field | Value |
|-------|-------|
| menu_id | `purchase-orders` |
| view_type | `LIST_VIEW` |
| config | `NRQFX` |
| route | `/procurement/purchase-orders` |

---

## 📋 VERIFICATION CHECKLIST

### **After Fixes**:
- [ ] UOM: Backend `menu_id` matches frontend `viewId`
- [ ] UOM: `view_type` is `MASTER`
- [ ] UOM: Config is `NESCKVDXRQF`
- [ ] UOM: All toolbar buttons work correctly
- [ ] UOM: Mode transitions (VIEW ↔ CREATE ↔ EDIT) work
- [ ] UOM: Filter toggle works
- [ ] PO List: Hardcoded `allowedActions` removed
- [ ] PO List: Toolbar driven by backend
- [ ] PO List: All buttons work correctly
- [ ] Both screens tested in live app

---

## 🚀 NEXT STEPS

1. **Update Backend** - Fix UOM entry in Django Admin
2. **Update Frontend** - Remove hardcoded allowedActions from PO List
3. **Test Both Screens** - Verify all functionality works
4. **Document as Benchmarks** - Create reference guide for rollout

---

**Status**: ⚠️ AWAITING FIXES  
**Priority**: P0 (Critical - Blocks Phase 2 rollout)
