# HINDRA SESSION STARTUP PROTOCOL

**Agent**: Hindra (HRM Domain Owner)  
**Date**: January 30, 2026  
**Purpose**: Initialize Hindra session with full HRM context

---

## OVERVIEW

This protocol initializes a Hindra session by loading context from `HRM/bootstrap-hrm-only/session_start/` directory. This is the single source of truth for HRM domain work.

---

## 🚀 EXECUTION SEQUENCE

### Step 1: Load Core Identity (Essential)

Read these files in order:

1. **`00_hindra_context_master.md`** - Core context
   - Agent identity and authority
   - HRM module status (22 models, 0 errors, 100% complete)
   - Platform architecture
   - Critical constraints
   - Domain ownership boundaries

2. **`01_quick_reference_patterns.md`** - UI standards & patterns
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

3. **`02_governance_rules_summary.md`** - Governance rules
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

4. **`03_session_state_tracker.md`** - Session state
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

### Step 2: Load Reference Files (As Needed)

Read these files only when needed for specific tasks:

5. **`04_04_OLVINE_ERP_REPOSITORY_ANALYSIS_REPORT.md`** - Repository analysis
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

6. **`04_05_OLVINE_ERP_SOURCE_CODE_ANALYSIS_REPORT.md`** - Source code analysis
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

7. **`04_07_toolbar_final_governance_v2_3001.md`** - Toolbar governance (LOCKED)
   - Core principle (toolbar is LAW)
   - Modes (canonical)
   - Mode → allowed actions contract
   - Permission integration
   - Strict prohibitions
   - Data flow (canonical pipeline)
   - Rationale

8. **`04_09_Autoretry_Prevention_Guide.md`** - Autoretry prevention
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

9. **`HRM_Template_Prompt.md`** - BBP creation prompt template
   - Base prompt template
   - Autoretry and cutoff prevention
   - Content length management
   - Context preservation rules
   - Section completion checklist
   - Error recovery protocol
   - Example prompts
   - General usage guidelines
   - Module type specifics

10. **`HRM_Development_Implementation_Prompt.md`** - BBP development implementation guide
    - Single line prompt
    - Development implementation instructions
    - Key BBP sections to reference
    - Implementation checklist
    - Implementation prompt examples
    - Dynamics 365 HTML implementation details

### Step 3: Acknowledge & Report

After loading core context:

1. **Confirm context loaded**
   - "Hindra session initialized"
   - "HRM module status: 100% complete, 22 models, 0 errors"
   - "Platform status: Production ready"

2. **Display session focus**
   - "Ready for HRM domain tasks"
   - "Governance rules loaded"
   - "UI standards loaded"
   - "Toolbar governance loaded"

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

### Priority 2: LOAD AS NEEDED (Reference)

| File | Purpose |
|------|---------|
| `04_04_OLVINE_ERP_REPOSITORY_ANALYSIS_REPORT.md` | Repository analysis (12 sections) |
| `04_05_OLVINE_ERP_SOURCE_CODE_ANALYSIS_REPORT.md` | Source code analysis (12 sections) |
| `04_07_toolbar_final_governance_v2_3001.md` | Toolbar governance (LOCKED) |
| `04_09_Autoretry_Prevention_Guide.md` | Autoretry prevention (16 sections) |
| `HRM_Template_Prompt.md` | BBP creation prompt template |
| `HRM_Development_Implementation_Prompt.md` | BBP development implementation guide |

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

### During Task Execution:

1. **Follow governance rules** strictly
2. **Use UI standards** exactly as specified
3. **Implement toolbar** using backend-driven system
4. **Apply autoretry prevention** for file updates
5. **Verify no Location leakage** in HRM code

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

**Version**: 1.0  
**Last Updated**: January 30, 2026  
**Agent**: Hindra (HRM Domain Owner)
