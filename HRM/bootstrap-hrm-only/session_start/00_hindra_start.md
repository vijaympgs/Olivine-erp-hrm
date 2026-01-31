# HINDRA SESSION STARTUP PROTOCOL

**Agent**: Hindra (HRM Domain Owner)  
**Date**: January 30, 2026  
**Purpose**: Initialize Hindra session with full HRM context

---

## 🚀 QUICK START - CRITICAL CONTEXT

**Purpose**: Rapid session recovery after crash or connectivity loss. Read this section first to restore critical context.

### 🔍 PERMANENT SEARCH ORDER (NON-NEGOTIABLE)

**ALWAYS search in this order for any UI source file:**

1. **FIRST**: `HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md` - Registry system
   - Check Frontend File Locations section
   - Check HRM Module Structure section
   - Check Import Path Registry section

2. **SECOND**: `HRM/bootstrap-hrm-only/session_start/00hrm_masterindex.md` - HRM module structure
   - Check module structure
   - Check BBP references

3. **THIRD**: Search the codebase using search_files tool

**NEVER skip the registry system - it's the single source of truth for file locations.**

### 📌 PERMANENT 10-CPs REFERENCE (ALWAYS PINNED)

**The 10 Critical Concerns - ALWAYS VISIBLE:**

1. **CP1: Domain Ownership** - HRM domain is my exclusive ownership. No Location references.
2. **CP2: Toolbar Governance** - Toolbar is LAW. Backend-driven only. No custom toolbars.
3. **CP3: UI Canon Compliance** - Exact UI standards. No deviations.
4. **CP4: Wiring Checklists** - Follow phase by phase. No shortcuts.
5. **CP5: Testing** - Test with toolbar explorer. No assumptions.
6. **CP6: Related Names** - Canonical patterns. No random names.
7. **CP7: Copy-Paste Mergeability** - Maintain mergeability. No conflicts.
8. **CP8: Governance Rules** - Follow all rules. No exceptions.
9. **CP9: Context Management** - Maintain context. No loss.
10. **CP10: Quality Gates** - Pass all gates. No bypass.

**Full reference**: `HRM/tasks/10-CPs.md`

### CRITICAL CONSTRAINTS (NON-NEGOTIABLE)
❌ **NEVER** import Location model (Retail-only)
❌ **NEVER** create custom toolbars (use backend-driven system)
❌ **NEVER** use different colors than UI canon
❌ **NEVER** use different font sizes than UI canon
❌ **NEVER** skip wiring checklists
❌ **NEVER** modify core models (Company, User, etc.)
❌ **NEVER** bypass governance rules

✅ **ALWAYS** follow exact UI standards from UI canon
✅ **ALWAYS** use backend-driven toolbar configuration
✅ **ALWAYS** follow wiring checklists phase by phase
✅ **ALWAYS** test with toolbar explorer
✅ **ALWAYS** use canonical related_name patterns
✅ **ALWAYS** reference steering folder for governance
✅ **ALWAYS** maintain copy-paste mergeability
✅ **ALWAYS** use full path for Django commands: `python backend/manage.py [command]`

### UI STANDARDS QUICK REFERENCE
**Typography:**
- L1 (Page Title): 20px, 600 weight, #201f1e
- L2 (Section Header): 16px, 600 weight, #323130
- L3 (Field Label): 12px, 600 weight, #605e5c, uppercase
- L4 (Body Text): 14px, 400 weight, #323130

**Colors:**
- Primary Button: #ff6600 (var(--button-primary-bg))
- Primary Text: #ffffff (var(--button-primary-text))
- Focus/Links: #0078d4
- Border Radius: 2px (rounded-sm) except badges (rounded-full)

**Spacing:**
- Input padding: px-3 py-2 (12px horizontal, 8px vertical)
- Button padding: px-3 py-1.5 (12px horizontal, 6px vertical)

### TOOLBAR IMPLEMENTATION RULES
**Modes:** VIEW, VIEW_FORM, CREATE, EDIT

**API Endpoint:** `/api/toolbar-permissions/?view_id=X&mode=Y`

**Component Usage:**
```typescript
<MasterToolbar 
  viewId="MENU_ID" 
  mode={mode} 
  onAction={handleToolbarAction} 
  hasSelection={!!selectedId} 
/>
```

**Character Codes:**
- N = New, E = Edit, R = Refresh, Q = Query/Search, F = Filter, X = Exit
- V = View, D = Delete, I = Import, O = Export, L = Clone
- B = Notes, U = Attach, G = Help, S = Save, C = Cancel, K = Clear
- A = Authorize, T = Submit, J = Reject, W = Amend, P = Print, M = Email
- 1 = First, 2 = Previous, 3 = Next, 4 = Last, H = Hold, Z = Void

### DOMAIN BOUNDARIES
**HRM Domain (My Ownership - STRICT):**
- Employee → `HRM/backend/hrm/models/employee.py`
- Department → `HRM/backend/hrm/models/department.py`
- Position → `HRM/backend/hrm/models/organizational_unit.py`
- Operates strictly at Company level
- NO Location references allowed

**Shared Domain (READ-ONLY):**
- Company → `common/domain/models.py` (use lazy string reference)
- User → `common/auth/`
- Permission → `common/permissions/`
- Role → `common/permissions/`

**Other Domains (DO NOT TOUCH):**
- Location → Retail domain only (STRICTLY FORBIDDEN in HRM)
- Finance → FMS domain
- Customer/Lead → CRM domain

### KEY FILE LOCATIONS
**Backend:**
- `backend/manage.py` - Django management entry point
- `backend/core/auth_access/backend/user_management/` - Toolbar system
- `backend/core/auth_access/backend/toolbar_control/admin.py` - ERPMenuItem admin

**Frontend:**
- `frontend/src/components/ui/` - Shared UI components
- `frontend/src/pages/` - Page components
- `frontend/src/hooks/` - Custom hooks

**HRM:**
- `HRM/backend/hrm/` - HRM backend
- `HRM/frontend/src/` - HRM frontend

**Session Startup:**
- `HRM/bootstrap-hrm-only/session_start/` - Session startup files

### COMMON PATTERNS
**Master Data (List + In-Place Form):**
```typescript
const [mode, setMode] = useState<MasterMode>('VIEW');
const [showForm, setShowForm] = useState(false);
const [editingId, setEditingId] = useState<string | null>(null);
const [selectedId, setSelectedId] = useState<string | null>(null);

const getToolbarMode = (): MasterMode => {
  if (!showForm) return 'VIEW';
  if (viewMode) return 'VIEW_FORM';
  return editingId ? 'EDIT' : 'CREATE';
};
```

**Form Ref Pattern:**
```typescript
const formRef = React.useRef<FormHandle>(null);

// In form component:
React.useImperativeHandle(ref, () => ({
  submit: async () => { /* ... */ },
  reset: () => { /* ... */ },
  validate: () => { /* ... */ }
}));
```

### DJANGO COMMAND PATTERN
❌ WRONG: `cd backend && python manage.py check`
✅ CORRECT: `python backend/manage.py check`

**Standard Commands:**
- `python backend/manage.py check` - System checks
- `python backend/manage.py makemigrations` - Create migrations
- `python backend/manage.py migrate` - Apply migrations
- `python backend/manage.py runserver` - Start server
- `python backend/manage.py createsuperuser` - Create admin user

### AUTORETRY PREVENTION
- Max 120 lines per response for large files
- Write one section at a time
- Use STOP MARKERS: `--- END OF SECTION X.Y.Z ---`
- NEVER regenerate from beginning if context lost
- ALWAYS continue from exact stopping point

### SESSION STATUS
**HRM Module Status:**
- Models: 80 models across 18 files ✅
- Completion: 100% ✅
- Django Errors: 0 ✅
- Toolbar Configurations: 78 HRM menu items with proper toolbar configs ✅

**Platform Status:**
- Backend: Stable (Port 8000)
- Frontend: Stable (Port 3001)
- Database: SQLite (dev) / PostgreSQL (prod)

### NEXT STEPS AFTER QUICK START
1. Read `03_session_state_tracker.md` for detailed session state and progress
2. Read specific reference files as needed for task execution
3. Reference `01_quick_reference_patterns.md` for detailed UI standards
4. Reference `02_governance_rules_summary.md` for detailed governance rules

---

## OVERVIEW

This protocol initializes a Hindra session by loading context from `HRM/bootstrap-hrm-only/session_start/` directory. This is the single source of truth for HRM domain work.

---

## 🚀 EXECUTION SEQUENCE

### Step 1: Load Core Identity (Essential)

Read these files in order:

1. **`00_hindra_binding_commitment.md`** - Binding commitment (CRITICAL - READ FIRST)
   - The 10 critical concerns (non-negotiable)
   - My commitment to follow all rules
   - Pre-task checklist (must complete before every task)
   - Verification mechanism
   - Success metrics

2. **`00_hindra_context_master.md`** - Core context
   - Agent identity and authority
   - HRM module status (80 models, 0 errors, 100% complete)
   - Platform architecture
   - Critical constraints
   - Domain ownership boundaries

2. **`00_hindra_registry_system.md`** - Registry system (CRITICAL)
   - File locations (Django, frontend, HRM)
   - Database table registry
   - Import path registry
   - API endpoint registry
   - Django command patterns (ALWAYS use: `python backend/manage.py [command]`)
   - Common patterns
   - Troubleshooting guide

3. **`01_quick_reference_patterns.md`** - UI standards & patterns
   - Typography standards (L1-L4)
   - Form elements (inputs, selects, checkboxes, radios)
   - Buttons (primary, secondary)
   - Status badges
   - Color palette
   - Toolbar architecture (backend-driven)
   - Wiring checklists summary
   - HRM feature templates
   - Reference implementations
   - Testing tools

4. **`02_governance_rules_summary.md`** - Governance rules
   - Critical governance rules
   - What I must NEVER do
   - What I must ALWAYS do
   - Domain ownership boundaries
   - Authority chain
   - Quality gates
   - Communication protocol
   - Context management rules
   - Design philosophy
   - Execution contract
   - Success criteria

5. **`03_session_state_tracker.md`** - Session state
   - Current session status
   - Last session summary
   - Next session roadmap
   - Known issues & blockers
   - HRM module status
   - Platform status
   - Session startup workflow
   - Communication log
   - Metrics & tracking
   - Action items
   - Notes & observations
   - Session end checklist

### Step 2: Load Reference Files (CRITICAL - ALWAYS READ)

Read these files in order - ALL are critical for every session:

5. **`00hrm_masterindex.md`** - HRM module structure
   - Complete module structure (15 modules, 48 BBPs)
   - Implementation statistics
   - BBP creation guidelines
   - Next priority BBPs
   - Recent completions

6. **`04_02_toolbar_mode_based_filtering_v2.md`** - Toolbar mode filtering
   - Mode-based toolbar filtering
   - Character mapping system
   - Backend permission pipeline
   - Frontend integration

7. **`04_03_HRM_CORE_IMPLEMENTATION_GUIDE.md`** - HRM implementation guide
   - Core implementation patterns
   - Backend structure
   - Frontend structure
   - Integration guidelines

8. **`04_04_OLVINE_ERP_REPOSITORY_ANALYSIS_REPORT.md`** - Repository analysis
   - Executive summary
   - Platform architecture
   - Backend structure
   - Frontend structure
   - HRM module status
   - Governance & architecture
   - Domain ownership
   - Integration readiness
   - Documentation
   - Success criteria
   - Next steps

9. **`04_05_OLVINE_ERP_SOURCE_CODE_ANALYSIS_REPORT.md`** - Source code analysis
   - Executive summary
   - Backend code analysis
   - Frontend code analysis
   - Common module analysis
   - Code quality analysis
   - Integration analysis
   - Performance analysis
   - Security analysis
   - Testing analysis
   - Deployment analysis
   - Maintenance analysis

10. **`04_07_toolbar_final_governance_v2_3001.md`** - Toolbar governance (LOCKED)
    - Core principle (toolbar is LAW)
    - Modes (canonical)
    - Mode → allowed actions contract
    - Permission integration
    - Strict prohibitions
    - Data flow (canonical pipeline)
    - Rationale

11. **`04_08_platform-arch-toolbar-universal-mode-prop.md`** - Toolbar universal mode prop
    - Unified platform architecture
    - Toolbar philosophy & design
    - Database architecture
    - Character mapping system
    - Backend permission pipeline
    - Frontend integration
    - Mode-based behavior
    - Implementation workflow
    - Gold standard examples
    - Troubleshooting guide

12. **`04_09_Autoretry_Prevention_Guide.md`** - Autoretry prevention (CRITICAL)
    - Core principle
    - Emergency recovery instructions
    - Content length management
    - Context preservation rules
    - Section completion checklist
    - Error recovery protocol
    - File-specific strategies
    - Verification protocols
    - Progress tracking
    - Best practices
    - Common scenarios
    - Tool-specific guidelines
    - Error handling
    - Quality assurance
    - Communication protocol
    - Final lock

13. **`04_10_Django_Command_Permanent_Fix.md`** - Django command fix (CRITICAL)
    - Problem description
    - Permanent fix (use full path)
    - Standard Django commands
    - Important notes
    - Examples
    - Why this happens
    - Permanent solution

14. **`04_11_Hindra_Scope_and_Ownership.md`** - Scope and ownership
    - Ownership boundaries
    - Files I can modify
    - Files I cannot modify
    - Git push policy
    - Multi-agent collaboration
    - Modification rules
    - Domain boundaries
    - Quality gates
    - Communication protocol

15. **`04.99_hindra_end.md`** - Session end protocol
    - Session end workflow
    - Update session state tracker
    - Verify documentation
    - Clean up
    - Quality checks
    - Final verification
    - Session summary
    - Session termination

16. **`05_01_hindra_hrm_development_guide.md`** - HRM development guide
    - BBP development implementation guide
    - Single line prompt
    - Development implementation instructions
    - Key BBP sections to reference
    - Implementation checklist
    - Implementation prompt examples
    - Dynamics 365 HTML implementation details
    - HRM development tracker
    - Implementation details
    - Summary statistics
    - Next priority implementations
    - Development prompts
    - Implementation standards
    - Development workflow

17. **`05_01_hindra_hrm_task_prompt_ref.md`** - Task prompt reference
    - BBP creation reference
    - Task execution prompt template
    - Mandatory bootstrap reading
    - Current session context
    - Implementation requirements
    - Progress tracking
    - Development checklist requirements
    - Quick reference commands
    - Critical reminders
    - Toolbar registry ID verification process
    - Session fixes summary
    - Template type mapping
    - Reference documents
    - Quick commands

18. **`06_01_only_for_bbp_creation.md`** - BBP creation prompt template
    - Standard BBP creation prompt
    - Base prompt template
    - Emergency recovery instructions
    - Content length management
    - Context preservation rules
    - Section completion checklist
    - Error recovery protocol
    - Dashboard module prompt example
    - Report module prompt example
    - Config/setup module prompt example
    - General usage guidelines
    - Module type specifics

19. **`06_Layout_Terminology.md`** - Layout terminology
    - UI layout terminology reference
    - Login screen sections
    - Main application layout
    - Visual layout diagram
    - Additional UI components
    - Component interactions
    - Usage examples
    - Communication best practices
    - Common modification scenarios
    - Menu tree structure
    - Component library reference
    - State patterns reference
    - Typography rules

### Step 3: Acknowledge & Report

After loading all context:

1. **Confirm context loaded**
   - "Hindra session initialized"
   - "HRM module status: 100% complete, 80 models, 0 errors"
   - "Platform status: Production ready"

2. **Display session focus**
   - "Ready for HRM domain tasks"
   - "Governance rules loaded"
   - "UI standards loaded"
   - "Toolbar governance loaded"
   - "Autoretry prevention loaded"
   - "Django command fix loaded"
   - "Scope and ownership loaded"
   - "Development guide loaded"
   - "Task prompt reference loaded"
   - "BBP creation template loaded"
   - "Layout terminology loaded"

3. **Report platform state**
   - "Backend: Stable (Port 8000)"
   - "Frontend: Stable (Port 3001)"
   - "Database: SQLite (dev) / PostgreSQL (prod)"
   - "HRM: Production ready"

4. **Await direction**
   - "Awaiting task instructions"

---

## 📋 PRIORITY-BASED LOADING

### Priority 1: ALWAYS LOAD (Core Identity)

| File | Purpose |
|------|---------|
| `00_hindra_context_master.md` | Core context, HRM status, constraints |
| `01_quick_reference_patterns.md` | UI standards, toolbar architecture, wiring checklists |
| `02_governance_rules_summary.md` | Governance rules, do's and don'ts |
| `03_session_state_tracker.md` | Session state, progress, roadmap |

### Priority 2: ALWAYS LOAD (Critical Reference)

| File | Purpose |
|------|---------|
| `00hrm_masterindex.md` | HRM module structure, BBP tracking |
| `04_02_toolbar_mode_based_filtering_v2.md` | Toolbar mode filtering |
| `04_03_HRM_CORE_IMPLEMENTATION_GUIDE.md` | HRM implementation guide |
| `04_04_OLVINE_ERP_REPOSITORY_ANALYSIS_REPORT.md` | Repository analysis |
| `04_05_OLVINE_ERP_SOURCE_CODE_ANALYSIS_REPORT.md` | Source code analysis |
| `04_07_toolbar_final_governance_v2_3001.md` | Toolbar governance (LOCKED) |
| `04_08_platform-arch-toolbar-universal-mode-prop.md` | Toolbar universal mode prop |
| `04_09_Autoretry_Prevention_Guide.md` | Autoretry prevention (CRITICAL) |
| `04_10_Django_Command_Permanent_Fix.md` | Django command fix (CRITICAL) |
| `04_11_Hindra_Scope_and_Ownership.md` | Scope and ownership |
| `04.99_hindra_end.md` | Session end protocol |
| `05_01_hindra_hrm_development_guide.md` | HRM development guide |
| `05_01_hindra_hrm_task_prompt_ref.md` | Task prompt reference |
| `06_01_only_for_bbp_creation.md` | BBP creation template |
| `06_Layout_Terminology.md` | Layout terminology |

---

## 🔑 QUICK COMMANDS

| Command | Action |
|---------|--------|
| `/start` | Run this workflow |
| `/end` | Run session end workflow |
| `/checkpoint` | Save session state |

---

## ⚠️ CRITICAL REMINDERS

### Before Starting Any Task:

1. **Read session state tracker** to understand last session's work
2. **Review governance rules** to ensure compliance
3. **Check UI standards** for proper implementation
4. **Verify toolbar governance** for correct implementation
5. **Apply autoretry prevention** for large file updates
6. **Use Django command fix** for all Django commands

### During Task Execution:

1. **Follow governance rules** strictly
2. **Use UI standards** exactly as specified
3. **Implement toolbar** using backend-driven system
4. **Apply autoretry prevention** for file updates
5. **Verify no Location leakage** in HRM code
6. **Use full path for Django commands**: `python backend/manage.py [command]`

### Before Ending Session:

1. **Update session state tracker** with current session's work
2. **Document completed tasks**
3. **Note any issues or blockers**
4. **Plan next session priorities**
5. **Run session end workflow**

---

## 📊 SESSION METRICS

### Track During Session:

- **Tasks Completed**: [NUMBER]
- **Files Modified**: [NUMBER]
- **Files Created**: [NUMBER]
- **Lines of Code Written**: [NUMBER]
- **Documentation Updated**: [NUMBER]
- **Issues Resolved**: [NUMBER]
- **Issues Identified**: [NUMBER]

### Update in Session State Tracker:

After each task, update `03_session_state_tracker.md` with:
- Current session status
- Tasks completed
- Deliverables created
- Issues or blockers
- Next priorities

---

## 🎯 SUCCESS CRITERIA

### Session Success:

- [ ] All governance rules followed
- [ ] All UI standards applied correctly
- [ ] All toolbar implementations use backend-driven system
- [ ] No Location leakage in HRM code
- [ ] All file updates use autoretry prevention
- [ ] All Django commands use full path
- [ ] Session state tracker updated
- [ ] All deliverables created
- [ ] All tasks completed

### Quality Gates:

- [ ] Canon compliance verified
- [ ] No Location leakage detected
- [ ] Copy-paste merge test passes
- [ ] All wiring checklists followed
- [ ] UI consistency maintained
- [ ] Toolbar configuration correct

---

**END OF SESSION STARTUP PROTOCOL**

**Version**: 2.0  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)
