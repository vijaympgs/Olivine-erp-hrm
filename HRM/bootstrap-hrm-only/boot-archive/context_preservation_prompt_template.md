# 🚀 HRM Development - Context Preservation Prompt Template

## 📋 MANDATORY BOOTSTRAP READING ORDER (Always read first)
1. `bootstrap/00_bootstrap_master_index.md` - Complete overview and file structure
2. `bootstrap/06_01_next_session_plan.md` - Current priorities and implementation roadmap
3. `bootstrap/06_03_tasks.md` - Task execution guide and current status
4. `bootstrap/06_04_tracker.md` - Progress tracking matrix

## 🎨 UI STANDARDS (Never skip these)
5. `bootstrap/03_03_ui_typography_styling.md` - Exact fonts, colors, form elements
6. `bootstrap/04_01_agent_e_onboarding.md` - Development guidelines and what NOT to do
7. `bootstrap/04_02_toolbar_implementation_guide.md` - Toolbar implementation rules
8. `bootstrap/04_03_toolbar_code_examples.md` - Copy-paste code examples

## 🔧 WIRING SPECIFICATIONS (Choose based on task type)
9. `bootstrap/05_01_wiring_checklists_overview.md` - Understanding wiring checklists
10. `bootstrap/05_02_master_data_wiring_hrm.md` - For Master Data tasks (MST-S/M/C, T1)
11. `bootstrap/05_03_transaction_form_wiring_hrm.md` - For Transaction tasks (TXN-S/M/C)
12. `bootstrap/05_04_workflow_wiring_hrm.md` - For Workflow and business rules

## 🏗️ GOVERNANCE & COMPLIANCE
13. `bootstrap/01_01_governance_foundation.md` - Platform architecture and rules
14. `bootstrap/01_02_platform_onboarding.md` - Windows execution environment
15. `bootstrap/01_03_context_limit_rules.md` - Context management rules
16. `bootstrap/06_02_tasks_checklist.md` - Comprehensive implementation checklist

---

## 🎯 PROMPT TEMPLATE (Copy and paste this)

```
Continue HRM development session.

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
✅ bootstrap/05_02_master_data_wiring_hrm.md [or appropriate wiring guide]
✅ bootstrap/01_01_governance_foundation.md
✅ bootstrap/01_02_platform_onboarding.md
✅ bootstrap/06_02_tasks_checklist.md

🎯 CURRENT SESSION CONTEXT:
- Last Completed: [Previous task number and name]
- Current Task: [Task number and name from bootstrap/06_03_tasks.md]
- Template Type: [MST-S/M/C or TXN-S/M/C or T1 from task mapping]
- Wiring Guide: [Specific wiring document path]
- UI Standards: bootstrap/03_03_ui_typography_styling.md
- Django Root: D:\platform\hrm\backend\manage.py
- Execution Environment: Windows PowerShell only

📋 TASK EXECUTION:
Run Task [X.X] - [Task Name from bootstrap/06_03_tasks.md]

🔧 IMPLEMENTATION REQUIREMENTS:
- Follow [Template Type] specifications from bootstrap/06_03_tasks.md
- Implement all phases from [wiring guide] checklist
- Use exact typography/colors from bootstrap/03_03_ui_typography_styling.md
- Follow Windows execution rules from bootstrap/01_02_platform_onboarding.md
- Implement company scoping: self.request.user.company
- Use canonical naming: <model_name_lower>_<field_name_lower>
- NO cross-app imports, NO Location model references
- Use MasterToolbar with mode management (VIEW/CREATE/EDIT)

📊 PROGRESS TRACKING:
- [ ] Read bootstrap documentation (completed above)
- [ ] Backend model verification and setup
- [ ] Serializer creation with company_name read-only field
- [ ] ViewSet implementation with company scoping
- [ ] URL registration and routing
- [ ] Frontend TypeScript service layer
- [ ] React component with exact UI standards
- [ ] MasterToolbar integration with mode management
- [ ] Testing and validation
- [ ] Update bootstrap/06_04_tracker.md with completion status

🚨 CRITICAL REMINDERS:
- Windows commands only: cd D:\platform\hrm\backend && python manage.py [command]
- Use exact colors: #ff6600 (primary buttons), #0078d4 (focus/links)
- Typography: L1 (20px), L2 (16px), L3 (12px), L4 (14px)
- Border radius: rounded-sm (2px) except badges (rounded-full)
- No custom toolbars - use backend-driven MasterToolbar system
- Test with bootstrap/99_toolbar_explorer_hrm.html
```

---

## 📋 TASK-SPECIFIC WIRING GUIDE MAPPING

### For Master Data Tasks (MST-S/M/C, T1):
- Use: `bootstrap/05_02_master_data_wiring_hrm.md`
- Phases: 11-phase checklist
- Features: List page, search/filter, MasterToolbar, modal forms

### For Transaction Tasks (TXN-S/M/C):
- Use: `bootstrap/05_03_transaction_form_wiring_hrm.md`
- Phases: 14-phase checklist
- Features: TransactionToolbar, header, line items, workflow

### For Workflow Tasks:
- Use: `bootstrap/05_04_workflow_wiring_hrm.md`
- Phases: 10-phase checklist
- Features: Status machines, workflow actions, validation

---

## 🎯 TEMPLATE CLASSIFICATIONS (from bootstrap/06_03_tasks.md)

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

### CRM Master Data:
- Contact → **MST-M** (Medium Master Template)
- Account → **MST-C** (Complex Master Template)
- Product Catalog → **MST-M** (Medium Master Template)

### CRM Transactions:
- Lead → **TXN-M** (Medium Transaction Template)
- Opportunity → **TXN-C** (Complex Transaction Template)
- Campaign → **TXN-M** (Medium Transaction Template)
- Quote → **TXN-M** (Medium Transaction Template)

---

## 🔧 WINDOWS EXECUTION REMINDERS

### Django Commands (ALWAYS from D:\platform\hrm\backend>):
```powershell
cd D:\platform\hrm\backend
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py loaddata [fixture_name]
```

### File Paths (ALWAYS full Windows paths):
- Django Root: `D:\platform\hrm\backend\manage.py`
- Models: `D:\platform\hrm\backend\hrm\models\`
- Serializers: `D:\platform\hrm\backend\hrm\serializers\`
- Views: `D:\platform\hrm\backend\hrm\views\`
- URLs: `D:\platform\hrm\backend\hrm\urls\`

---

## ✅ COMPLETION CHECKLIST

Before marking any task complete:
- [ ] All bootstrap documents read and referenced
- [ ] Wiring checklist phases completed
- [ ] UI standards compliance verified
- [ ] Windows execution rules followed
- [ ] Company scoping implemented
- [ ] MasterToolbar integrated
- [ ] Testing completed
- [ ] bootstrap/06_04_tracker.md updated
- [ ] bootstrap/99_toolbar_explorer_hrm.html tested

---

**Usage**: Copy the entire prompt template above, fill in the bracketed values, and paste it for each new session. This ensures bootstrap standards are never missed and context is preserved across sessions.
