# TASK PROMPT REFERENCE - Consolidated Guide

**Agent**: Hindra (HRM Domain Owner)  
**Date**: January 30, 2026  
**Purpose**: Consolidated task execution reference for HRM development

---

## 📋 BBP CREATION REFERENCE

### When You Need to Create a BBP First

Before implementing a module, you may need to create a Business Blueprint (BBP) if one doesn't exist.

**Reference**: `HRM_Template_Prompt.md` for complete BBP creation guidance

### Quick BBP Creation Prompt

```
Refer BBP_Template_Prompt.md and create a BBP for [TARGET_FILE_PATH] using the BBP_Template_Reference.md as your comprehensive guide.

Module Details:
- Module Name: [MODULE_NAME] (derived from file name)
- Module Number: [X.Y] (derived from file path)
- Module Type: [Master/Transaction/Dashboard/Reports/Config/Rule/Setup]
- Target File: [TARGET_FILE_PATH]
```

### Module Type Templates

**For Master Data (Employee Records, Department, Position, etc.):**
- Use Master template format
- Include Django models with proper relationships
- Define comprehensive business rules
- Specify detailed UI/UX requirements

**For Transaction Forms (Leave Request, Timesheets, etc.):**
- Use Transaction template format
- Include workflow state machine
- Define status transitions
- Specify validation rules

**For Dashboards:**
- Use simplified Dashboard template
- Focus on metrics and KPIs
- Specify data visualization requirements

**For Reports:**
- Use simplified Reports template
- Focus on data points and reporting needs
- Specify export capabilities

### Critical BBP Creation Rules

- **Maximum 120 lines per response** to prevent cutting
- **Write one section at a time** - never multiple sections
- **Use STOP MARKERS** after each section: `--- END OF SECTION X.Y.Z ---`
- **NEVER auto-retry** or restart from beginning
- **ALWAYS continue from exact stopping point**

### Emergency Recovery for BBP Creation

If context is lost during BBP creation:

```
EMERGENCY: Context lost during BBP creation for [TARGET_FILE_PATH]

Current status: Creating BBP for [MODULE_NAME] ([MODULE_NUMBER])
Last completed section: [LAST_SECTION_COMPLETED]
Next section to create: [NEXT_SECTION_NUMBER]

RECOVERY ACTIONS:
1. Read BBP_Template_Reference.md for context
2. Read target file to see current content
3. Continue from exact stopping point
4. Write ONLY the next section ([NEXT_SECTION_NUMBER])
5. End with STOP MARKER: --- END OF SECTION [NEXT_SECTION_NUMBER] ---
6. WAIT for next instruction before continuing
```

---

## 📋 TASK EXECUTION PROMPT TEMPLATE

### Copy and Paste This Template for Task Execution

```
E, implement [Human Resources › Employee Management › Employee Records] for HRM module

TASK DETAILS:
Human Resources › Employee Management › Employee Records

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

## 📚 MANDATORY BOOTSTRAP READING

### Before Starting Any Task:

✅ `00_bootstrap_master_index.md` - Master index
✅ `06_01_next_session_plan.md` - Next session plan
✅ `06_03_tasks.md` - Task list
✅ `06_04_tracker.md` - Progress tracker
✅ `03_03_ui_typography_styling.md` - UI standards
✅ `04_01_agent_e_onboarding.md` - Agent E onboarding
✅ `04_02_toolbar_implementation_guide.md` - Toolbar guide
✅ `04_03_toolbar_code_examples.md` - Code examples
✅ `05_01_wiring_checklists_overview.md` - Wiring overview
✅ `05_02_master_data_wiring_hrm.md` - Master data wiring
✅ `01_01_governance_foundation.md` - Governance foundation
✅ `01_02_platform_onboarding.md` - Platform onboarding
✅ `06_02_tasks_checklist.md` - Tasks checklist
✅ `06_05_findings_learnings.md` - Findings and learnings

---

## 🎯 CURRENT SESSION CONTEXT

### Session Information:
- **Current Task**: Task 02.1 - Employee Records from `06_03_tasks.md`
- **Template Type**: T1
- **Wiring Guide**: `05_02_master_data_wiring_hrm.md`
- **UI Standards**: `03_03_ui_typography_styling.md`
- **Django Root**: D:\platform\hrm\backend\manage.py
- **Execution Environment**: Windows PowerShell only

---

## 🔧 IMPLEMENTATION REQUIREMENTS

### For Master Data Tasks (Employee Records, Department, etc.):

1. **Backend Implementation**
   - Create/verify Django models
   - Create serializers with company scoping
   - Create ViewSets with company scoping
   - Implement URL registration and routing

2. **Frontend Service**
   - Replace mock service with real API calls to backend endpoints
   - Implement proper error handling
   - Add loading states

3. **UI Compliance**
   - Ensure exact typography, colors, spacing from `03_03_ui_typography_styling.md`
   - Follow established UI patterns (mst01, mst02, mst03)
   - Implement responsive design

4. **Toolbar Integration**
   - Connect MasterToolbar to backend configuration (not mock data)
   - Implement mode-based filtering (VIEW/EDIT/CREATE)
   - Use backend-driven toolbar system

5. **Company Scoping**
   - Implement `self.request.user.company` filtering in all queries
   - Add company_name read-only field to serializers

### For Transaction Tasks (Leave Request, etc.):

1. **Workflow Implementation**
   - Status state machine
   - Workflow actions (submit, approve, reject)
   - State transitions

2. **Form Integration**
   - TransactionToolbar with mode-based button visibility
   - Form validation
   - Error handling

3. **Business Rules**
   - Validation
   - Authorization
   - Audit trail implementation

---

## 📊 PROGRESS TRACKING

### Task Execution Checklist:

- [ ] Read bootstrap documentation (completed above)
- [ ] **BACKEND**: Model verification and setup
- [ ] **BACKEND**: Serializer creation with company_name read-only field
- [ ] **BACKEND**: ViewSet implementation with company scoping
- [ ] **BACKEND**: URL registration and routing
- [ ] **FRONTEND**: Replace mock service with real API calls
- [ ] **FRONTEND**: React component compliance with UI standards
- [ ] **FRONTEND**: MasterToolbar backend configuration integration
- [ ] **TESTING**: CRUD operations and workflow validation
- [ ] **TRACKING**: Update `06_04_tracker.md` with completion status

---

## 📝 DEVELOPMENT CHECKLIST REQUIREMENTS

### Pre-Development Checklist (Must complete before starting):

- [ ] Checked existing models for reuse
- [ ] Verified ERPMenuItem table entries
- [ ] Analyzed existing UI components
- [ ] Tested UI through sidebar menu
- [ ] Checked for existing Python files (seed, fix, debug, check, verify)
- [ ] Reviewed development standards in E-bootstrap.md

### Development Checklist (During implementation):

- [ ] Models follow existing patterns
- [ ] UI uses established templates (mst/txn)
- [ ] Backend implements proper validation
- [ ] Frontend follows typography standards (L1-L4)
- [ ] Toolbar integration implemented
- [ ] Permissions properly configured
- [ ] Company scoping applied (currentCompanyId)

### Post-Development Checklist (Before completion):

- [ ] UI loads through sidebar menu
- [ ] All CRUD operations functional
- [ ] Toolbar buttons work correctly (F-key shortcuts)
- [ ] Form validation implemented
- [ ] Error handling in place
- [ ] Git commit follows HRM-only boundaries
- [ ] Development checklist completed and verified

---

## 🎯 QUICK REFERENCE COMMANDS

### Model Analysis:

```bash
# Check existing models
python backend/manage.py showmigrations
python backend/manage.py inspectdb

# Check HRM specific models
python backend/manage.py shell -c "from django.apps import apps; print([m.name for m in apps.get_app_configs() if 'hrm' in m.name.lower()])"
```

### ERPMenuItem Verification:

```bash
# Check ERPMenuItem table for HRM entries
python backend/manage.py shell -c "from core.models import ERPMenuItem; print(list(ERPMenuItem.objects.filter(module_name='HRM').values('menu_name', 'route_url', 'toolbar_registry_string')))"

# Use the consolidated toolbar registry checker
python backend/check_toolbar_registry_ids.py
```

### Existing Files Check:

```bash
# Check existing Python files
ls D:\olvine-erp\HRM\hrm-boot-and-dev-reference\hrm\*.py
ls *.py | grep -E "(seed|fix|debug|check|verify)" | head -10
```

---

## ⚠️ CRITICAL REMINDERS

### Before Starting Any Task:

1. **Read session state tracker** to understand last session's work
2. **Review governance rules** to ensure compliance
3. **Check UI standards** for proper implementation
4. **Verify toolbar governance** for correct implementation
5. **Apply autoretry prevention** for large file updates

### During Task Execution:

1. **Follow governance rules** strictly
2. **Use UI standards** exactly as specified
3. **Implement toolbar** using backend-driven system
4. **Apply autoretry prevention** for file updates
5. **Verify no Location leakage** in HRM code

### Important Notes:

- **Employee Records and Organization Chart are COMPLETED** - Don't recreate
- **Always check existing files before creating new ones**
- **Follow HRM-only git boundaries**
- **Use shared components from core/ and common/**
- **Implement proper toolbar integration**
- **Complete development checklist for each feature**
- **Test UI through sidebar menu before marking complete

### Windows Commands Only:

- Use exact colors: #ff6600 (primary buttons), #0078d4 (focus/links)
- Typography: L1 (20px), L2 (16px), L3 (12px), L4 (14px)
- Border radius: rounded-sm (2px) except badges (rounded-full)
- No custom toolbars - use backend-driven MasterToolbar system
- Test with `99_toolbar_explorer_hrm.html`

---

## 🔍 TOOLBAR REGISTRY ID VERIFICATION PROCESS

### Critical Development Process: Always Verify Backend First

During Employee Self Service implementation, a critical process was established for toolbar registry ID verification:

#### ❌ Common Mistake: Hardcoded Values

- **Problem**: Assuming toolbar registry IDs without checking backend
- **Result**: 404 errors when fetching toolbar permissions
- **Issue**: Frontend viewId doesn't match backend menu_id

#### ✅ Correct Process: Backend-First Verification

- **Step 1**: Query ERPMenuItem table to find correct registry IDs
- **Step 2**: Use backend script to verify menu configurations
- **Step 3**: Implement frontend with verified menu_id values
- **Result**: Successful toolbar permissions integration

### 🔧 Toolbar Registry ID Verification Script

**MANDATE**: Always verify toolbar registry IDs from backend before implementing frontend components.

**PURPOSE**: The `backend/check_toolbar_registry_ids.py` script is the single source of truth for fetching correct view IDs from the ERPMenuItem table for toolbar registry integration.

**Usage Examples:**

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

**Key Features:**

- Queries ERPMenuItem table for accurate toolbar registry strings
- Provides frontend/backend implementation examples
- Identifies missing toolbar configurations
- Validates menu_id naming conventions
- Prevents hardcoded value errors in frontend components

### 📋 Implementation Process

1. **Run Verification Script**: Query backend for correct menu IDs
2. **Use Verified IDs**: Implement frontend with backend-confirmed values
3. **Update Backend**: Configure toolbar_views.py with correct menu_id
4. **Test Integration**: Verify toolbar permissions endpoint works

### ⚠️ Important Development Guidelines

- **NEVER hardcode toolbar registry IDs** without backend verification
- **ALWAYS run the verification script** before implementing new modules
- **USE consistent naming convention**: Menu Name → MENU_NAME format
- **TEST frontend-backend integration** early in development process
- **DOCUMENT the correct menu IDs** for future reference

### 🛠️ Script Output Example

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

### 📚 Reference Files

- **Verification Script**: `backend/check_toolbar_registry_ids.py`
- **Backend Views**: `backend/core/auth_access/backend/user_management/toolbar_views.py`
- **Frontend Component**: `HRM/frontend/src/pages/EmployeeSelfService.tsx`

---

## 📋 SESSION FIXES SUMMARY

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

## 🎯 TEMPLATE TYPE MAPPING

### HRM Master Data:

- Employee Master → **T1** (Complex Master Template)
- Department → **MST-S** (Simple Master Template)
- Position → **MST-S** (Simple Master Template)
- Organizational Unit → **MST-M** (Medium Master Template)

### HRM Transactions:

- Leave Request → **TXN-M** (Medium Transaction Template)
- Attendance Adjustment → **TXN-S** (Simple Transaction Template)
- Expense Claim → **TXN-M** (Medium Transaction Template)
- Performance Review → **TXN-C** (Complex Transaction Template)

---

## 📚 REFERENCE DOCUMENTS

### Bootstrap Documentation:

- **E-bootstrap.md**: Agent initialization and governance
- **QUICK_START.md**: Development process and detailed checklists
- **README.md**: HRM module overview and architecture
- **bootstrap/**: Technical documentation and patterns
- **steering/**: Development standards and guidelines

### Session Startup Files:

- **START.md**: Session startup protocol
- **end.md**: Session end protocol
- **00_hindra_context_master.md**: Core context
- **01_quick_reference_patterns.md**: UI standards & patterns
- **02_governance_rules_summary.md**: Governance rules
- **03_session_state_tracker.md**: Session state
- **04_04_OLVINE_ERP_REPOSITORY_ANALYSIS_REPORT.md**: Repository analysis
- **04_05_OLVINE_ERP_SOURCE_CODE_ANALYSIS_REPORT.md**: Source code analysis
- **04_07_toolbar_final_governance_v2_3001.md**: Toolbar governance (LOCKED)
- **04_09_Autoretry_Prevention_Guide.md**: Autoretry prevention

### Task Reference:

- **06_03_tasks.md**: Task list
- **06_04_tracker.md**: Progress tracker
- **06_01_next_session_plan.md**: Next session plan
- **06_02_tasks_checklist.md**: Tasks checklist
- **06_05_findings_learnings.md**: Findings and learnings

---

## 🔑 QUICK COMMANDS

| Command | Action |
|---------|--------|
| `/start` | Run session startup workflow |
| `/end` | Run session end workflow |
| `/checkpoint` | Save session state |

---

**END OF TASK PROMPT REFERENCE**

**Version**: 1.0  
**Last Updated**: January 30, 2026  
**Agent**: Hindra (HRM Domain Owner)
