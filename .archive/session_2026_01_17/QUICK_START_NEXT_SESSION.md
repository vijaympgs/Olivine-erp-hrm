# ⚡ QUICK START CHECKLIST - Next Session (CORRECTED)
**Architecture**: UNIFIED (One Backend + One Frontend with Sidebar)

---

## 🏗️ **CORRECT ARCHITECTURE REMINDER**

```
ONE Backend (8000) → Serves ALL modules (Retail, HRM, CRM, FMS)
ONE Frontend (3000) → Sidebar navigation for ALL modules
```

**NOT** separate backends/frontends on different ports!

---

## 🔍 **STEP 1: Verify Current Setup**

### Check Backend Structure
```bash
cd c:\00mindra\olivine-platform\backend

# Check if all module routes exist
cat erp_core/urls.py

# Look for these patterns:
# path('api/retail/', ...)
# path('api/hrm/', ...)
# path('api/crm/', ...)
# path('api/fms/', ...)
```

### Check Frontend Structure
```bash
cd c:\00mindra\olivine-platform\frontend

# Check port configuration (should be 3000, not 3001)
cat vite.config.ts | grep port

# Check if sidebar exists
ls src/components/ | grep -i sidebar

# Check if all module pages exist
ls src/pages/
```

### Check What's Running
```bash
# Should see ONLY:
# - 8000 (Backend)
# - 3000 or 3001 (Frontend)
# - 3100 (QA Launcher)
netstat -ano | findstr "8000 3000 3001 3100"

# Should NOT see:
# - 8001, 8002, 8003 (separate backends)
# - 3002, 3003, 3004 (separate frontends)
```

---

## 🎯 **STEP 2: Fix Backend Integration**

### Check Backend URLs File
```bash
cd c:\00mindra\olivine-platform\backend
code erp_core/urls.py  # or cat/view
```

### Add Missing Module Routes (if needed)
```python
# In backend/erp_core/urls.py
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Auth
    path('api/auth/', include('Core.auth_access.backend.user_management.urls')),
    
    # Modules - ALL in ONE backend
    path('api/retail/', include('Retail.backend.urls')),  # Should exist
    path('api/hrm/', include('HRM.backend.urls')),        # Add if missing
    path('api/crm/', include('CRM.backend.urls')),        # Add if missing
    path('api/fms/', include('FMS.backend.urls')),        # Add if missing
    
    # Other routes...
]
```

### Verify Backend Starts Successfully
```bash
cd c:\00mindra\olivine-platform\backend
python manage.py check
python manage.py runserver 8000
```

---

## 🎯 **STEP 3: Fix Frontend Integration**

### Check Frontend Port
```typescript
// In frontend/vite.config.ts
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,  // Should be 3000, not 3001
    host: true
  }
})
```

### Check Sidebar Component
```bash
cd c:\00mindra\olivine-platform\frontend\src

# Find sidebar component
find . -name "*Sidebar*" -o -name "*sidebar*"

# Check its contents
cat components/Sidebar.tsx  # or whatever the file is
```

### Add Module Navigation (if missing)
```typescript
// In frontend/src/components/Sidebar.tsx (or similar)
import { ShoppingCart, Users, UserCheck, DollarSign } from 'lucide-react';

const modules = [
  {
    name: 'Retail',
    path: '/retail',
    icon: ShoppingCart,
    description: 'POS, Inventory, Sales'
  },
  {
    name: 'HRM',
    path: '/hrm',
    icon: Users,
    description: 'Employees, Payroll, Attendance'
  },
  {
    name: 'CRM',
    path: '/crm',
    icon: UserCheck,
    description: 'Customers, Leads, Opportunities'
  },
  {
    name: 'FMS',
    path: '/fms',
    icon: DollarSign,
    description: 'Accounting, Finance, Budgets'
  }
];
```

### Check Routing Configuration
```typescript
// In frontend/src/App.tsx or routes config
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/retail/*" element={<RetailModule />} />
        <Route path="/hrm/*" element={<HRMModule />} />      // Add if missing
        <Route path="/crm/*" element={<CRMModule />} />      // Add if missing
        <Route path="/fms/*" element={<FMSModule />} />      // Add if missing
      </Routes>
    </BrowserRouter>
  );
}
```

---

## 🎯 **STEP 4: Test Complete Flow**

### Start Services (ONLY These)
```bash
# Terminal 1: Backend
cd c:\00mindra\olivine-platform\backend
python manage.py runserver 8000

# Terminal 2: Frontend
cd c:\00mindra\olivine-platform\frontend
npm run dev  # Should start on port 3000

# Terminal 3: QA Launcher (optional)
cd c:\00mindra\olivine-platform\Common\qa-launcher-console
npm start  # Port 3100
```

### Test Navigation
1. **Open**: http://localhost:3000
2. **Login**: admin / admin123
3. **Check Sidebar**: Should show Retail, HRM, CRM, FMS
4. **Click Each Module**: Verify navigation works
5. **Check URLs**: Should be `/retail`, `/hrm`, `/crm`, `/fms`

---

## ✅ **VERIFICATION CHECKLIST**

### Backend (Port 8000)
- [ ] Backend running without errors
- [ ] Has `/api/retail/` endpoints
- [ ] Has `/api/hrm/` endpoints
- [ ] Has `/api/crm/` endpoints
- [ ] Has `/api/fms/` endpoints
- [ ] Single authentication for all modules

### Frontend (Port 3000)
- [ ] Frontend running on port 3000 (not 3001)
- [ ] Sidebar visible with all 4 modules
- [ ] Can click Retail in sidebar
- [ ] Can click HRM in sidebar
- [ ] Can click CRM in sidebar
- [ ] Can click FMS in sidebar
- [ ] URL changes when clicking modules
- [ ] Content changes when clicking modules

### Integration
- [ ] Login once, access all modules
- [ ] No port conflicts
- [ ] No separate backends running (8001-8003)
- [ ] No separate frontends running (3002-3004)

---

## 🚨 **STOP If You See These**

### ❌ Multiple Backends Running
```
8000 - Backend ✅ CORRECT
8001 - HRM Backend ❌ WRONG - Stop this
8002 - CRM Backend ❌ WRONG - Stop this
8003 - FMS Backend ❌ WRONG - Stop this
```

**Fix**: Kill processes on 8001-8003. Only 8000 should run.

### ❌ Multiple Frontends Running
```
3000 - Frontend ✅ CORRECT
3001 - Retail Frontend ❌ WRONG - Stop this
3002 - HRM Frontend ❌ WRONG - Stop this
3003 - CRM Frontend ❌ WRONG - Stop this
3004 - FMS Frontend ❌ WRONG - Stop this
```

**Fix**: Kill processes on 3001-3004. Only 3000 should run.

---

## 🔧 **COMMON ISSUES & FIXES**

### Issue: "Module not found" when clicking sidebar
**Cause**: Frontend routing not configured for that module
**Fix**: Add route in `App.tsx`:
```typescript
<Route path="/hrm/*" element={<HRMModule />} />
```

### Issue: "404 Not Found" for API calls
**Cause**: Backend doesn't have that module's URLs
**Fix**: Add to `backend/erp_core/urls.py`:
```python
path('api/hrm/', include('HRM.backend.urls')),
```

### Issue: Sidebar doesn't show all modules
**Cause**: Sidebar component not updated
**Fix**: Add module to sidebar menu items array

### Issue: Frontend on wrong port (3001 instead of 3000)
**Cause**: vite.config.ts has wrong port
**Fix**: Change port to 3000 in vite.config.ts

---

## 📊 **CORRECT vs INCORRECT SETUP**

### ✅ CORRECT (Unified Architecture)
```
Backend (8000)
  ├── /api/retail/
  ├── /api/hrm/
  ├── /api/crm/
  └── /api/fms/

Frontend (3000)
  ├── Sidebar
  │   ├── Retail → /retail
  │   ├── HRM → /hrm
  │   ├── CRM → /crm
  │   └── FMS → /fms
  └── Shared Layout
```

### ❌ INCORRECT (Separate Apps)
```
Retail Backend (8000) + Frontend (3001)  ❌
HRM Backend (8001) + Frontend (3002)     ❌
CRM Backend (8002) + Frontend (3003)     ❌
FMS Backend (8003) + Frontend (3004)     ❌
```

---

## 🎯 **SUCCESS = This View**

When you open http://localhost:3000, you should see:

```
┌─────────────────────────────────────────┐
│ Olivine Platform                    👤  │
├──────────┬──────────────────────────────┤
│          │                              │
│ Sidebar  │  Main Content Area           │
│          │                              │
│ 📦 Retail│  [Current Module Content]    │
│ 👥 HRM   │                              │
│ 🤝 CRM   │                              │
│ 💰 FMS   │                              │
│          │                              │
└──────────┴──────────────────────────────┘
```

Clicking any sidebar item changes the main content area, NOT the entire page/port.

---

**This is the correct architecture! Much simpler and cleaner.** 🚀
