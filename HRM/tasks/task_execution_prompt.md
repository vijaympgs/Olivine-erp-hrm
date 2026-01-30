Continue HRM development session.
n
📚 MANDATORY BOOTSTRAP READING COMPLETED:
✅ bootstrap/00_bootstrap_master_index.md
✅ bootstrap/06_01_next_session_plan.md  
✅ bootstrap/06_03_tasks.md
✅ bootstrap/06_04_tracker.md
✅ bootstrap/03_03_ui_typography_styling.md
✅ bootstrap/04_01_agent_e_onboarding.md
✅ bootstrap/04_02_toolbar_implementation_guide.md
✅ bootstrap/04_03_toolbar_code_examples.md
✅ bootstrap/05_01_wiring_checklists_overview.md
✅ bootstrap/05_02_master_data_wiring_hrm.md
✅ bootstrap/01_01_governance_foundation.md
✅ bootstrap/01_02_platform_onboarding.md
✅ bootstrap/06_02_tasks_checklist.md
✅ bootstrap/06_05_findings_learnings.md (Task 02.1 patterns and solutions)

🎯 CURRENT SESSION CONTEXT:
- Current Task: Task 02.1 - Employee Records from bootstrap/06_03_tasks.md
- Template Type: T1
- Wiring Guide: bootstrap/05_02_master_data_wiring_hrm.md
- UI Standards: bootstrap/03_03_ui_typography_styling.md
- Django Root: D:\platform\hrm\backend\manage.py
- Execution Environment: Windows PowerShell only

📋 TASK EXECUTION:
Run Task 2.1

🔧 IMPLEMENTATION REQUIREMENTS:
**IMMEDIATE ACTION REQUIRED**: Based on the task type, you must:

**For Master Data Tasks (Employee Records, Department, etc.):**
1. **Backend Implementation** - Create/verify Django models, serializers, ViewSets with company scoping
2. **Frontend Service** - Replace mock service with real API calls to backend endpoints
3. **UI Compliance** - Ensure exact typography, colors, spacing from bootstrap/03_03_ui_typography_styling.md
4. **Toolbar Integration** - Connect MasterToolbar to backend configuration (not mock data)
5. **Company Scoping** - Implement `self.request.user.company` filtering in all queries

**For Transaction Tasks (Leave Request, etc.):**
1. **Workflow Implementation** - Status state machine, workflow actions (submit, approve, reject)
2. **Form Integration** - TransactionToolbar with mode-based button visibility
3. **Business Rules** - Validation, authorization, audit trail implementation

**CRITICAL REQUIREMENTS**:
- Follow [Template Type] specifications from bootstrap/06_03_tasks.md
- Implement ALL phases from [wiring guide] checklist (11 phases for master, 14 for transactions)
- Use exact typography/colors from bootstrap/03_03_ui_typography_styling.md
- Follow Windows execution rules from bootstrap/01_02_platform_onboarding.md
- Implement company scoping: self.request.user.company
- Use canonical naming: <model_name_lower>_<field_name_lower>
- NO cross-app imports, NO Location model references
- Use MasterToolbar with mode management (VIEW/CREATE/EDIT)

📊 PROGRESS TRACKING:
- [ ] Read bootstrap documentation (completed above)
- [ ] **BACKEND**: Model verification and setup
- [ ] **BACKEND**: Serializer creation with company_name read-only field
- [ ] **BACKEND**: ViewSet implementation with company scoping
- [ ] **BACKEND**: URL registration and routing
- [ ] **FRONTEND**: Replace mock service with real API calls
- [ ] **FRONTEND**: React component compliance with UI standards
- [ ] **FRONTEND**: MasterToolbar backend configuration integration
- [ ] **TESTING**: CRUD operations and workflow validation
- [ ] **TRACKING**: Update bootstrap/06_04_tracker.md with completion status

🚨 **DO NOT**: Just read files or analyze existing code. You must IMPLEMENT the missing pieces.

🚨 CRITICAL REMINDERS:
- Windows commands only: cd D:\platform\hrm\backend && python manage.py [command]
- Use exact colors: #ff6600 (primary buttons), #0078d4 (focus/links)
- Typography: L1 (20px), L2 (16px), L3 (12px), L4 (14px)
- Border radius: rounded-sm (2px) except badges (rounded-full)
- No custom toolbars - use backend-driven MasterToolbar system
- Test with bootstrap/99_toolbar_explorer_hrm.html
```

---

## 📝 Usage Instructions

**For User Reference Only:**

1. **Copy the prompt above** - This is a reusable template for any HRM task
2. **Fill in the bracketed values**:
   - `{{TASK_NUMBER}}` - Task number from bootstrap/06_03_tasks.md (e.g., 02.1, 03.1, etc.)
   - `{{TASK_NAME}}` - Task name from bootstrap/06_03_tasks.md (e.g., Employee Records, Application Capture)
   - `[Template Type]` - Use template classifications from bootstrap/context_preservation_prompt_template.md
   - `[Specific wiring document path]` - Choose based on task type:
     - Master Data: `bootstrap/05_02_master_data_wiring_hrm.md`
     - Transaction: `bootstrap/05_03_transaction_form_wiring_hrm.md`
     - Workflow: `bootstrap/05_04_workflow_wiring_hrm.md`
3. **Paste and execute** - This ensures all bootstrap standards are followed

**Note**: The system will dynamically resolve both task number and task name from bootstrap/06_03_tasks.md.

## 🔧 Quick Reference for Task Information

- **Task List**: `bootstrap/06_03_tasks.md`
- **Progress Tracker**: `bootstrap/06_04_tracker.md`
- **Next Session Plan**: `bootstrap/06_01_next_session_plan.md`
- **Template Classifications**: See mapping in `bootstrap/context_preservation_prompt_template.md`
- **Wiring Guide Selection**: Based on task type (Master/Transaction/Workflow)

## 🎯 Template Type Mapping (from bootstrap/context_preservation_prompt_template.md)

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
