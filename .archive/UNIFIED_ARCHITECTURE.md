# 🏗️ OLIVINE PLATFORM ARCHITECTURE
**Unified Multi-Module ERP System**

---

## 📐 **SYSTEM ARCHITECTURE DIAGRAM**

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                                │
│                    http://localhost:3001                            │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    FRONTEND (Port 3001)                             │
│                    Single React Application                         │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  App Shell (Layout, Auth, Navigation)                        │  │
│  │  ┌────────────┬──────────────────────────────────────────┐  │  │
│  │  │  Sidebar   │  Main Content Area                       │  │  │
│  │  │            │                                          │  │  │
│  │  │  📦 Retail │  ┌────────────────────────────────────┐  │  │  │
│  │  │  👥 HRM    │  │  Module-Specific Pages:           │  │  │  │
│  │  │  🤝 CRM    │  │                                    │  │  │  │
│  │  │  💰 FMS    │  │  • Retail: POS, Inventory, Sales  │  │  │  │
│  │  │            │  │  • HRM: Employees, Payroll        │  │  │  │
│  │  │            │  │  • CRM: Customers, Leads          │  │  │  │
│  │  │            │  │  • FMS: Accounting, Finance       │  │  │  │
│  │  │            │  │                                    │  │  │  │
│  │  │            │  └────────────────────────────────────┘  │  │  │
│  │  └────────────┴──────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  Frontend Routing:                                                 │
│  • /retail/*  → Retail Module Components                          │
│  • /hrm/*     → HRM Module Components                             │
│  • /crm/*     → CRM Module Components                             │
│  • /fms/*     → FMS Module Components                             │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
                          API Calls via Axios
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    BACKEND (Port 8000)                              │
│                    Single Django Project                            │
│                                                                     │
│  Django URL Router (erp_core/urls.py)                              │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                                                              │  │
│  │  /api/auth/    → Authentication & User Management           │  │
│  │  /api/retail/  → Retail Module APIs                         │  │
│  │  /api/hrm/     → HRM Module APIs                            │  │
│  │  /api/crm/     → CRM Module APIs                            │  │
│  │  /api/fms/     → FMS Module APIs                            │  │
│  │  /admin/       → Django Admin Interface                     │  │
│  │                                                              │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  Django Apps (INSTALLED_APPS):                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  • Core.auth_access.backend.user_management                 │  │
│  │  • Core.licensing.backend.business_entities                 │  │
│  │  • Retail.backend.domain                                    │  │
│  │  • Retail.backend.inventory                                 │  │
│  │  • Retail.backend.pos                                       │  │
│  │  • Retail.backend.sales                                     │  │
│  │  • HRM.backend.hrm                                          │  │
│  │  • CRM.backend.crm                                          │  │
│  │  • FMS.backend.fms                                          │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    DATABASE (SQLite)                                │
│                    backend/db.sqlite3                               │
│                                                                     │
│  Tables for ALL modules:                                           │
│  • auth_user, auth_token (Authentication)                          │
│  • be_company, location (Business Entities)                        │
│  • retail_* (Retail tables)                                        │
│  • hrm_* (HRM tables)                                              │
│  • crm_* (CRM tables)                                              │
│  • fms_* (FMS tables)                                              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 **USER FLOW**

### 1. Login Flow
```
User → http://localhost:3001/login
  ↓
Enter: admin / admin123
  ↓
Frontend → POST /api/auth/login/ → Backend (8000)
  ↓
Backend validates credentials
  ↓
Returns: { token, user, companies }
  ↓
Frontend stores token
  ↓
Redirect to: /location-selection
  ↓
User selects location
  ↓
Redirect to: /retail (default module)
```

### 2. Module Navigation Flow
```
User clicks "HRM" in sidebar
  ↓
Frontend router: /retail → /hrm
  ↓
Main content area updates
  ↓
Loads HRM components
  ↓
HRM components make API calls
  ↓
GET /api/hrm/employees/ → Backend (8000)
  ↓
Backend returns HRM data
  ↓
HRM page renders with data
```

---

## 📂 **DIRECTORY STRUCTURE**

```
olivine-platform/
├── backend/                          # Main Django backend (Port 8000)
│   ├── erp_core/                     # Django project settings
│   │   ├── settings.py               # All apps configured here
│   │   └── urls.py                   # All module routes here
│   ├── manage.py                     # Django management
│   └── db.sqlite3                    # Shared database
│
├── Core/                             # Core functionality
│   ├── auth_access/                  # Authentication
│   └── licensing/                    # Business entities
│
├── Retail/                           # Retail module
│   ├── backend/                      # Retail Django apps
│   └── frontend/                     # Retail React components (@retail/*)
│
├── HRM/                              # HRM module
│   ├── backend/                      # HRM Django apps
│   └── frontend/                     # HRM React components (@hrm/*)
│
├── CRM/                              # CRM module
│   ├── backend/                      # CRM Django apps
│   └── frontend/                     # CRM React components (@crm/*)
│
├── FMS/                              # FMS module
│   ├── backend/                      # FMS Django apps
│   └── frontend/                     # FMS React components (@fms/*)
│
├── frontend/                         # Main React frontend (Port 3001)
│   ├── src/
│   │   ├── components/               # Shared components
│   │   │   └── Sidebar.tsx           # Module navigation
│   │   ├── pages/                    # Module pages
│   │   │   ├── retail/               # Retail pages
│   │   │   ├── hrm/                  # HRM pages
│   │   │   ├── crm/                  # CRM pages
│   │   │   └── fms/                  # FMS pages
│   │   ├── services/                 # API services
│   │   │   ├── api.ts                # Axios instance
│   │   │   ├── retailService.ts      # Retail APIs
│   │   │   ├── hrmService.ts         # HRM APIs
│   │   │   ├── crmService.ts         # CRM APIs
│   │   │   └── fmsService.ts         # FMS APIs
│   │   ├── App.tsx                   # Main app with routing
│   │   └── main.tsx                  # Entry point
│   ├── vite.config.ts                # Vite config (port 3001)
│   └── package.json
│
└── Common/
    └── qa-launcher-console/          # DevOps Center (UI: 5174, API: 3100)
        └── ...                       # For starting/stopping services
```

---

## 🔌 **API ENDPOINT STRUCTURE**

### Authentication
```
POST   /api/auth/login/                    # Login
GET    /api/auth/user-locations/           # Get user locations
GET    /api/auth/me/                       # Current user
POST   /api/auth/logout/                   # Logout
```

### Retail Module
```
GET    /api/retail/products/               # List products
POST   /api/retail/products/               # Create product
GET    /api/retail/inventory/              # Inventory data
POST   /api/retail/pos/transactions/       # POS transactions
```

### HRM Module
```
GET    /api/hrm/employees/                 # List employees
POST   /api/hrm/employees/                 # Create employee
GET    /api/hrm/departments/               # Departments
GET    /api/hrm/payroll/                   # Payroll data
```

### CRM Module
```
GET    /api/crm/customers/                 # List customers
POST   /api/crm/customers/                 # Create customer
GET    /api/crm/leads/                     # Leads
GET    /api/crm/opportunities/             # Opportunities
```

### FMS Module
```
GET    /api/fms/accounts/                  # Chart of accounts
POST   /api/fms/transactions/              # Financial transactions
GET    /api/fms/reports/                   # Financial reports
GET    /api/fms/budgets/                   # Budgets
```

---

## 🎯 **KEY PRINCIPLES**

### 1. Single Source of Truth
- **One Backend**: All business logic in one Django project
- **One Frontend**: All UI in one React application
- **One Database**: All data in one SQLite database (dev) or PostgreSQL (prod)

### 2. Modular Organization
- **Backend**: Organized as Django apps (Retail, HRM, CRM, FMS)
- **Frontend**: Organized as route-based modules
- **Clear Separation**: Each module has its own pages, components, services

### 3. Shared Resources
- **Authentication**: One login for all modules
- **Layout**: Shared header, sidebar, footer
- **Components**: Reusable UI components across modules
- **Services**: Shared API client configuration

### 4. Scalability
- **Horizontal**: Add more modules by adding Django apps + frontend routes
- **Vertical**: Scale backend/frontend independently
- **Deployment**: Can deploy as monolith or split later if needed

---

## 🚀 **DEPLOYMENT ARCHITECTURE**

### Development (Current)
```
Backend:  localhost:8000 (Django dev server)
Frontend: localhost:3001 (Vite dev server)
Database: SQLite file
```

### Production (Future)
```
Backend:  api.olivine.com (Gunicorn + Nginx)
Frontend: app.olivine.com (Static files on CDN)
Database: PostgreSQL (AWS RDS or similar)
```

---

## 🔐 **SECURITY & AUTH**

### Authentication Flow
1. User logs in → Backend issues JWT token
2. Frontend stores token in localStorage
3. All API requests include token in header
4. Backend validates token for each request

### Authorization
- Role-based access control (RBAC)
- Permissions checked at API level
- Frontend hides/shows features based on permissions
- Sidebar modules visible based on user roles

---

## 📊 **DATA FLOW EXAMPLE**

### Example: Viewing Employee List in HRM

```
1. User clicks "HRM" in sidebar
   Frontend: Navigate to /hrm/employees

2. HRM Employees page loads
   Component: useEffect(() => fetchEmployees())

3. API call made
   Service: GET /api/hrm/employees/
   Headers: { Authorization: "Token abc123..." }

4. Backend processes request
   Django: HRM.backend.hrm.views.EmployeeViewSet
   Checks: User authentication, permissions
   Queries: Employee.objects.filter(company=user.company)

5. Backend returns data
   Response: { results: [...employees], count: 50 }

6. Frontend updates UI
   Component: setEmployees(response.results)
   Renders: Employee table with data
```

---

**This is the complete, correct architecture of the Olivine Platform!** 🎯
