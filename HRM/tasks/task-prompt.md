# 🚀 HRM Development Task Prompt Template

## 📋 **Copy and Paste This Template for Task Execution**

```
E, implement [Human Resourcesscr
›
Employee Management
›
cur
TASK DETAILS:
Human Resources
›
Employee Management
›
Employee Records

DEVELOPMENT REQUIREMENTS:
1. Check existing models in backend before creating new ones
2. Verify ERPMenuItem table entries for UI toolbar registry strings
3. Analyze existing UI components before writing new ones
4. Reuse existing Python files where possible (seed, fix, debug, check, verify)
5. Follow established UI patterns (mst01, mst02, mst03, txn01, txn02, txn03)
6. Implement proper toolbar integration with mode-based filtering
7. Verify UI existence through sidebar menu and load testing
8. Use shared components from core/ and common/ only

DELIVERABLES:
- Backend models and API endpoints (if needed)
- Frontend components with proper validation
- Toolbar integration with mode-based filtering (VIEW/EDIT/CREATE)
- Menu item configuration in ERPMenuItem table
- Development checklist completion (Pre/Development/Post)
- Git commit following HRM-only boundaries

BOUNDARIES:
- Work only in D:\olvine-erp\HRM\ folder (implementation)
- Reference: D:\olvine-erp\HRM\hrm-boot-and-dev-reference\ (bootstrap)
- Use shared components from core/ and common/ for HRM functionality
- Git pushes only from HRM folder
- Follow established development standards
- Core/Common fixes allowed only for HRM backend/frontend functionality

EXECUTION MODE:
- Auto-execution: ACTIVE
- Stop Gates: Input missing OR governance violation
- File Touch Discipline: ACTIVE (HRM-only)

COMPLETED FEATURES REFERENCE:
- Employee Records: COMPLETED ✅
- Organization Chart: COMPLETED ✅

Please proceed with auto-execution mode and provide completion checklist.
```

---

## 📝 **Development Checklist Requirements**

### **Pre-Development Checklist** (Must complete before starting)
- [ ] Checked existing models for reuse
- [ ] Verified ERPMenuItem table entries
- [ ] Analyzed existing UI components
- [ ] Tested UI through sidebar menu
- [ ] Checked for existing Python files (seed, fix, debug, check, verify)
- [ ] Reviewed development standards in E-bootstrap.md

### **Development Checklist** (During implementation)
- [ ] Models follow existing patterns
- [ ] UI uses established templates (mst/txn)
- [ ] Backend implements proper validation
- [ ] Frontend follows typography standards (L1-L4)
- [ ] Toolbar integration implemented
- [ ] Permissions properly configured
- [ ] Company scoping applied (currentCompanyId)

### **Post-Development Checklist** (Before completion)
- [ ] UI loads through sidebar menu
- [ ] All CRUD operations functional
- [ ] Toolbar buttons work correctly (F-key shortcuts)
- [ ] Form validation implemented
- [ ] Error handling in place
- [ ] Git commit follows HRM-only boundaries
- [ ] Development checklist completed and verified

---

## 🎯 **Quick Reference Commands**

### **Model Analysis**
```bash
# Check existing models
python backend/manage.py showmigrations
python backend/manage.py inspectdb

# Check HRM specific models
python backend/manage.py shell -c "from django.apps import apps; print([m.name for m in apps.get_app_configs() if 'hrm' in m.name.lower()])"
```

### **ERPMenuItem Verification**
```bash
# Check ERPMenuItem table for HRM entries
python backend/manage.py shell -c "from core.models import ERPMenuItem; print(list(ERPMenuItem.objects.filter(module_name='HRM').values('menu_name', 'route_url', 'toolbar_registry_string')))"

# Use the consolidated toolbar registry checker
python backend/check_toolbar_registry_ids.py
```

### **Existing Files Check**
```bash
# Check existing Python files
ls D:\olvine-erp\HRM\hrm-boot-and-dev-reference\hrm\*.py
ls *.py | grep -E "(seed|fix|debug|check|verify)" | head -10
```

---

## ⚠️ **Important Notes**

- **Employee Records and Organization Chart are COMPLETED** - Don't recreate
- **Always check existing files before creating new ones**
- **Follow HRM-only git boundaries**
- **Use shared components from core/ and common/**
- **Implement proper toolbar integration**
- **Complete development checklist for each feature**
- **Test UI through sidebar menu before marking complete**

---

## 🔍 **Toolbar Registry ID Verification Process**

### **Critical Development Process: Always Verify Backend First**
During Employee Self Service implementation, a critical process was established for toolbar registry ID verification:

#### **❌ Common Mistake: Hardcoded Values**
- **Problem**: Assuming toolbar registry IDs without checking backend
- **Result**: 404 errors when fetching toolbar permissions
- **Issue**: Frontend viewId doesn't match backend menu_id

#### **✅ Correct Process: Backend-First Verification**
- **Step 1**: Query ERPMenuItem table to find correct registry IDs
- **Step 2**: Use backend script to verify menu configurations
- **Step 3**: Implement frontend with verified menu_id values
- **Result**: Successful toolbar permissions integration

#### **🔧 Toolbar Registry ID Verification Script**
**MANDATE**: Always verify toolbar registry IDs from backend before implementing frontend components.

**PURPOSE**: The `backend/check_toolbar_registry_ids.py` script is the single source of truth for fetching correct view IDs from the ERPMenuItem table for toolbar registry integration.

**Usage Examples**:
```bash
# Check all HRM menu items with their toolbar registry strings
python backend/check_toolbar_registry_ids.py

# Search for specific menu patterns
python backend/check_toolbar_registry_ids.py "Employee"
python backend/check_toolbar_registry_ids.py "Self Service"

# Check specific menu_id configuration
python backend/check_toolbar_registry_ids.py HRM_EMPLOYEE_SELF_SERVICE

# List all available menu IDs in the system
python backend/check_toolbar_registry_ids.py --all
```

**Key Features**:
- Queries ERPMenuItem table for accurate toolbar registry strings
- Provides frontend/backend implementation examples
- Identifies missing toolbar configurations
- Validates menu_id naming conventions
- Prevents hardcoded value errors in frontend components

#### **📋 Implementation Process**
1. **Run Verification Script**: Query backend for correct menu IDs
2. **Use Verified IDs**: Implement frontend with backend-confirmed values
3. **Update Backend**: Configure toolbar_views.py with correct menu_id
4. **Test Integration**: Verify toolbar permissions endpoint works

#### **⚠️ Important Development Guidelines**
- **NEVER hardcode toolbar registry IDs** without backend verification
- **ALWAYS run the verification script** before implementing new modules
- **USE consistent naming convention**: Menu Name → MENU_NAME format
- **TEST frontend-backend integration** early in development process
- **DOCUMENT the correct menu IDs** for future reference

#### **🛠️ Script Output Example**
```
🔍 Toolbar Registry ID Checker

📋 Found X HRM menu items:

🏷️  Menu Name: Employee Self Service
📍 Route URL: /hr/employees/self-service
🔧 Toolbar Registry: NESCKVDXRQF
🆔 Menu ID (for frontend): EMPLOYEE_SELF_SERVICE
📂 Module: HRM
----------------------------------------
```

#### **📚 Reference Files**
- **Verification Script**: `backend/check_toolbar_registry_ids.py`
- **Backend Views**: `backend/core/auth_access/backend/user_management/toolbar_views.py`
- **Frontend Component**: `HRM/frontend/src/pages/EmployeeSelfService.tsx`

---

## 📋 **Session Fixes Summary**

### Toolbar Registry ID Consolidation
**Subject**: Consolidated duplicate toolbar registry checker scripts into single authoritative source
**Briefing**: Merged 3 duplicate files into `backend/check_toolbar_registry_ids.py` with comprehensive functionality for fetching correct view IDs from ERPMenuItem table

### Documentation Updates
**Subject**: Updated HRM documentation with toolbar registry checker mandate and purpose
**Briefing**: Added authoritative script usage guidelines to `task-prompt.md` and `E-bootstrap.md` for development workflow compliance

### ESS UI Pattern Implementation
**Subject**: Implemented Employee Records search/status pattern and stagnant toolbar for ESS
**Briefing**: Added conditional rendering to hide search/status in NEW/EDIT modes and fixed toolbar positioning to remain stagnant during form scrolling

### TypeScript Error Resolution
**Subject**: Fixed duplicate React import and JSX type errors in ESS component
**Briefing**: Resolved compilation issues by removing duplicate imports and ensuring proper React type definitions

### ESS Command Buttons Removal
**Subject**: Removed form command buttons to enforce toolbar-only operations
**Briefing**: Eliminated Clear and Submit buttons from ESS form, making toolbar the exclusive control interface for all operations

---

## 📚 **Reference Documents**

- **E-bootstrap.md**: Agent initialization and governance
- **QUICK_START.md**: Development process and detailed checklists
- **README.md**: HRM module overview and architecture
- **bootstrap/**: Technical documentation and patterns
- **steering/**: Development standards and guidelines

---

**Last Updated**: 2026-01-22  
**Maintained by**: Agent E (HRM Development)  
**Approved by**: Viji (Product Owner)


Start with /start.md and refer @session_summary.md to continue seamlessly.