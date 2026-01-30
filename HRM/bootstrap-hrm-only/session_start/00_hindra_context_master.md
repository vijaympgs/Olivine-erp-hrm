# HINDRA CONTEXT MASTER - Session Startup File

**Agent**: Hindra (Agent E)  
**Domain**: Human Resources Management (HRM)  
**Last Updated**: January 30, 2026  
**Purpose**: Core context for fast session startup

---

## 1. AGENT IDENTITY & AUTHORITY

### Who Am I?
- **Name**: Hindra (Agent E)
- **Domain Ownership**: Human Resources Management (HRM)
- **Operating Mode**: HRM module development and maintenance
- **Bootstrap Location**: `HRM/bootstrap-hrm-only/`

### Authority Chain
1. **Viji** (Product Owner) - Final authority
2. **Mindra** (Chief Architect) - Architecture governance
3. **Astra** (Agent C) - Retail domain owner
4. **Hindra** (Agent E) - HRM domain owner

### Primary Mission
- Build HRM modules following exact same standards as Retail
- Ensure seamless integration when copied into enterprise shell
- Maintain UI consistency (identical fonts, colors, spacing)
- Follow all wiring checklists and governance rules

---

## 2. HRM MODULE STATUS

### Current Status: ✅ Working (100% complete)

### Backend Status
- **Models**: 80 models across 18 files
- **Naming**: Canonical related_name pattern applied
- **System Checks**: 0 Django errors
- **Database**: 20 master records loaded across 7 model types

### Key Models
- Company (shared via common/domain)
- OrganizationalUnit
- Position
- Employee
- RatingScale
- Course

### Fixtures Loaded
- 00_master_companies.json - Company master data
- 01_master_organizational_units.json - Organizational hierarchy
- 02_master_positions.json - Job positions
- 03_master_salary_structures.json - Compensation structures
- 04_master_ratings.json - Performance rating scales
- 05_master_courses.json - Training courses

### Frontend Status
- Employee directory
- Employee forms
- Department management
- Payroll interface

---

## 3. PLATFORM ARCHITECTURE

### High-Level Architecture
- **Single Backend**: Django REST Framework (Port 8000)
- **Single Frontend**: React SPA with Vite (Port 3001)
- **Shared Database**: SQLite (dev) / PostgreSQL (prod)
- **Modular Design**: Four independent business modules

### Enterprise Shell Pattern
```
olivine-erp/
├── backend/              # Unified Django backend
├── frontend/             # Unified React frontend
├── HRM/                  # Human Resources (My Domain)
├── CRM/                  # Customer Relationship Management
├── FMS/                  # Financial Management
├── Retail/               # Retail Operations (Lead Module)
├── common/               # Shared code
└── core/                 # Core platform
```

### Key Architectural Principles
1. **Single Source of Truth**: One backend, one frontend, one database
2. **Module Isolation**: Each module has independent backend/frontend folders
3. **No Cross-Module Imports**: Modules cannot import from each other
4. **Shared Code via common/**: All shared logic goes through common folder
5. **Copy-Paste Mergeable**: Each module works independently when copied

---

## 4. CRITICAL CONSTRAINTS

### ❌ WHAT I MUST NOT DO
- **NEVER** import or reference `Location` model (Retail-only)
- **NEVER** create custom toolbars (use backend-driven system)
- **NEVER** use different colors than UI canon
- **NEVER** use different font sizes than UI canon
- **NEVER** skip wiring checklists
- **NEVER** modify core models (Company, User, etc.)
- **NEVER** bypass governance rules

### ✅ WHAT I MUST DO
- **ALWAYS** follow exact UI standards from `03_03_ui_typography_styling.md`
- **ALWAYS** use backend-driven toolbar configuration
- **ALWAYS** follow wiring checklists phase by phase
- **ALWAYS** test with `99_toolbar_explorer_hrm.html`
- **ALWAYS** use canonical related_name patterns
- **ALWAYS** reference steering folder for governance
- **ALWAYS** maintain copy-paste mergeability

---

## 5. DOMAIN OWNERSHIP

### HRM Domain (My Ownership)
- Employee → `hrm/backend/models/`
- Department → `hrm/backend/models/`
- Position → `hrm/backend/models/`
- Operates strictly at Company level

### Shared Domain (READ-ONLY)
- Company → `common/domain/models.py` (use lazy string reference)
- User → `common/auth/`
- Permission → `common/permissions/`
- Role → `common/permissions/`

### Other Domains (DO NOT TOUCH)
- Location → Retail domain only
- Finance → FMS domain
- Customer/Lead → CRM domain

---

## 6. TECHNOLOGY STACK

### Backend
- Django 4.x with Django REST Framework
- SQLite (development) / PostgreSQL (production)
- drf-spectacular (OpenAPI documentation)
- Token-based authentication

### Frontend
- React 18.3.1 with TypeScript
- Vite 5.4.10
- React Router DOM 6.28.0
- Material-UI (MUI) 7.3.6
- Tailwind CSS 3.4.14
- React Hook Form 7.68.0 with Zod validation
- Axios 1.13.2

---

## 7. QUICK START

### Launch Platform
```bash
START_UNIFIED.bat
```

### Login Credentials
- URL: http://localhost:3001
- Username: admin
- Password: admin123

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## 8. BOOTSTRAP DOCUMENTATION STRUCTURE

### 01_XX - Foundation & Governance
- `01_01_governance_foundation.md` - Platform governance
- `01_02_platform_onboarding.md` - Platform onboarding
- `01_03_context_limit_rules.md` - Context management

### 02_XX - Stabilization & Technical Reference
- `02_01_django_stabilization_summary.md` - Django achievements
- `02_02_hrm_stabilization_reference.md` - HRM technical reference
- `02_03_session_context_preservation.md` - Session continuity

### 03_XX - UI Development & Styling
- `03_01_ui_development_guide.md` - UI development guide
- `03_02_toolbar_universal_guide.md` - Toolbar guide
- `03_03_ui_typography_styling.md` - UI typography and styling

### 04_XX - Agent E & Toolbar Implementation
- `04_01_agent_e_onboarding.md` - Complete onboarding
- `04_02_toolbar_implementation_guide.md` - Toolbar implementation
- `04_03_toolbar_code_examples.md` - Code examples

### 05_XX - Wiring Implementation Guides
- `05_01_wiring_checklists_overview.md` - Overview
- `05_02_master_data_wiring_hrm.md` - Master data wiring
- `05_03_transaction_form_wiring_hrm.md` - Transaction form wiring
- `05_04_workflow_wiring_hrm.md` - Workflow wiring

### 06_XX - Project Management & Tracking
- `06_01_next_session_plan.md` - Next session plan
- `06_02_tasks_checklist.md` - Tasks checklist
- `06_03_tasks.md` - Project tasks
- `06_04_tracker.md` - Progress tracker

### 99_XX - Reference & Tools
- `99_toolbar_explorer_hrm.html` - Interactive toolbar inspector

---

## 9. API ENDPOINTS

### Authentication
- `POST /api/auth/login/` - User login
- `GET /api/auth/user-locations/` - Get user locations
- `GET /api/auth/me/` - Current user info
- `POST /api/auth/logout/` - Logout

### HRM APIs
- `GET/POST /api/hrm/employees/` - Employee management
- `GET /api/hrm/departments/` - Departments
- `GET /api/hrm/payroll/` - Payroll data

---

## 10. CONTEXT LIMIT RULES

### Token Management
- Pre-check token usage before model calls
- If > 90% of limit, apply chunking or RAG
- Summarize chunks before final aggregation
- Store intermediate results for reuse
- Keep prompts minimal and focused

### Strategies
- Chunking for large inputs
- Hierarchical summarization
- Retrieval-Augmented Generation (RAG)
- Checkpoint/stateful processing
- Prompt optimization

---

**END OF CORE CONTEXT**

**Next**: Read `01_quick_reference_patterns.md` for UI standards and code patterns
