# 📚 STEERING DOCUMENTATION MAP - COMPLETE REFERENCE

**Purpose**: Complete index of all steering documentation for agent context loading  
**Last Updated**: 2026-01-09 11:15 IST  
**Latest Updates**: Session 2 (Toolbar Governance) COMPLETE, Unified POS Roadmap integration  
**Use Case**: When switching models/agents or starting new sessions, use this as a checklist

---

## 🎯 CRITICAL - MUST READ FIRST

### Session Initialization (Priority 1)
1. **README.md** (Root - If exists) or **ASTRA-BOOTSTRAP.md**
2. **NEXT_SESSION.md** (Root) - Current session tasks
3. **.steering/00AGENT_ONBOARDING/** - Complete onboarding sequence

---

## 📂 00AGENT_ONBOARDING (START HERE)

### Core Onboarding Files (Read in Order)
- `01_Onboarding_Context.md` - Project context and current status
- `02_Architecture_Rules.md` - Architecture rules and model locations
- `03_Development_Standards.md` - Development standards and ELOBS workflow
- `04_Frontend_UI_Canon.md` - Frontend structure and UI patterns

### 01_Governance (Architectural Rules)
- `CANONICAL_RULESET.md` - **MASTER RULESET** (Non-negotiable)
- `ARCHITECTURAL_LOCK_REFERENCE.md` - Entity locks and terminology
- `README2_IMPORTANT_FORAGENTS.md` - Critical agent instructions
- `governance.md` - Complete governance framework
- `system-rules.md` - System-level rules

### 02_Business_Blueprints (Domain Logic)
- `00masterbbp.md` - Master blueprint overview
- **Procurement (4.x series)**:
  - `4.1_pr.md` - Purchase Requisition
  - `4.2_rfq.md` - Request for Quotation
  - `4.3_po.md` - Purchase Order
  - `4.4_asn.md` - Advance Shipment Notice
  - `4.5_grn.md` - Goods Receipt Note
  - `4.6_invoice_matching.md` - Invoice Matching
  - `4.7_returns.md` - Purchase Returns
  - `4.8_payments.md` - Payments
  - `4.9_compliance.md` - Compliance
- `inventory_bbp.md` - Inventory module blueprint
- `pos_bbp.md` - Point of Sale blueprint

### 03_Navigation_Canon (Menu Structure)
- `MENU_REORGANIZATION_COMPLETE.md` - Complete menu structure
- `SIDEBAR_QUICK_REFERENCE.md` - Sidebar navigation reference

### 04_UI_Canon_Templates (Design Patterns)
- `CONSOLIDATED_DESIGN_SYSTEM.md` - Complete design system
- `CONSOLIDATED_IMPLEMENTATION_SPECS.md` - Implementation specifications
- `LOOKUP_CANON.md` - Lookup modal patterns
- `Refer_this_before_new_UI_module.md` - UI module creation guide
- **Master Patterns**:
  - `mst01.md` - Simple master pattern
  - `mst02.md` - Complex master pattern
  - `mst03.md` - Advanced master pattern
- **Transaction Patterns**:
  - `txn01.md` - Simple transaction pattern
  - `txn02.md` - Complex transaction pattern
  - `txn03.md` - Advanced transaction pattern

### 05_Agent_Execution (Agent Behavior)
- `agent.olivine_ruleset.md` - Agent execution rules
- `olivine_ai_governance_agent_rules.md` - AI governance rules

### 06_QA_Testing (Testing Standards)
- `01_Procurement_BBP_4x_Test_Mapping.md` - Test mapping
- `PHASE_0_MASTER_DATA_READINESS_FINAL.md` - Master data readiness
- `TESTING_STANDARDS.md` - Testing standards and patterns

---

## 📂 01_ARCH_GOVERNANCE (Architecture)

### Critical Architecture Files
- `CANONICAL_RULESET.md` - Canonical ruleset (duplicate for quick access)
- `ARCHITECTURAL_LOCK_REFERENCE.md` - Entity and terminology locks
- `ARCHITECTURE_CANONICAL_MODELS.md` - Canonical model definitions
- `README2_IMPORTANT_FORAGENTS.md` - Agent-specific instructions
- `README2_Stabilization_Checklist.md` - Stabilization checklist
- `README3_IMPPORTANT_FORAGENTS_SPA_STRUCTURE.md` - SPA structure rules
- `agent.olivine_ruleset.md` - Olivine agent ruleset
- `olivine_ai_governance_agent_rules.md` - AI governance
- `system-rules.md` - System rules

---

## 📂 02_PROMPT_LIBRARY (Prompt Templates)

### Core Prompts
- `01prompt-governance-core.md` - Governance core prompt
- `02prompt-phase0-master-data-readiness.md` - Master data readiness
- `03prompt-hold-and-resume-control.md` - Hold and resume control
- `PROMPT_GUIDE.MD` - Prompt guide and best practices
- `backup/EXECUTION_CONTRACT.md` - Execution contract (archived)

---

## 📂 03_DESIGN_SYSTEM (Visual Design)

### Design Documentation
- `color-palette.md` - Color palette definitions
- `typography.md` - Typography standards
- `spacing.md` - Spacing system
- `components.md` - Component library

---

## 📂 04_EXECUTION_PLANS (Implementation Plans)

### Execution Tracking
- **`RETAIL_IMPLEMENTATION_TRACKER.md`** - **Single source of truth** for Retail module progress
  - Phase 4-5: UI Wiring & Standardization (2026-01-07)
  - Intercompany Transfer implementation status (COMPLETE)
  - Pending tasks with priorities and estimates
- **`RETAIL_MASTER_DATA_INVENTORY.md`** ⭐ - Complete catalog of 20 master data pages
- **`TOOLBAR_CONFIG_REFACTOR.md`** ⭐ COMPLETE - Backend-driven toolbar configuration system
  - Character-based config (N,E,S,C,X)
  - Registry organized under "Toolbar Control" group
- Feature rollout plans
- Module implementation roadmaps

---

## 📂 06_REPORTS_AUDITS (Historical Reports)

### Audit Reports
- `DJANGO_CODEBASE_AUDIT_REPORT.md` - Django codebase audit
- `LICENSE_ENFORCEMENT_REPORT.md` - License enforcement
- `EXECUTION_REPORT_*.md` - Various execution reports
- Session summaries and historical records

---

## 📂 07_CREDENTIALS_AND_OPS (Operations)

### Credentials Management
- `CREDENTIALS_MAINTENANCE.md` - Credential maintenance
- `LOGIN_CREDENTIALS.md` - Login credentials
- `STANDARD_CREDENTIALS.md` - Standard credentials
- `USER_CREDENTIALS.md` - User credentials

---

## 📂 08_MASTER_REFERENCE (Reference Data)

### Master Data Reference
- Master data structures
- Reference data definitions
- Canonical master data

---

## 📂 09_QUALITY_GOVERNANCE (Quality Standards)

### Quality Standards
- `TESTING_STANDARDS.md` - Testing standards
- Quality governance rules
- Test automation patterns

---

## 📂 11_PROCUREMENT_STABILIZATION (Procurement)

### Procurement Specific
- Procurement stabilization documentation
- Procurement-specific rules and patterns

---

## 📂 13TEST_PLANS (Test Automation)

### Test Script Prompts
- `TEST_SCRIPT_CREATE_PROMPTS/` - All test script generation prompts
  - `README.md` - Test automation system overview
  - `QUICK_START.md` - Quick start guide
  - `COMPLETION_SUMMARY.md` - Procurement completion summary
  - `4.1_Purchase_Requisition_test_script_prompt.md`
  - `4.2_Request_for_Quotation_test_script_prompt.md`
  - `4.3_Purchase_Order_test_script_prompt.md`
  - `4.5_Advance_Shipment_Notice_test_script_prompt.md`
  - `4.6_Goods_Receipts_test_script_prompt.md`
  - `4.7_Invoice_Matching_test_script_prompt.md`
  - `4.8_Purchase_Returns_test_script_prompt.md`
  - `Vendors_Master_Data_test_script_prompt.md`
  - `Payments_Processing_test_script_prompt.md`
  - `Compliance_Management_test_script_prompt.md`
  - `Configuration_Management_test_script_prompt.md`

### Session Summaries
- `SESSION_SUMMARY_2025-12-27.md` - Last session summary

---

## 📂 14UI_CANON (UI Standards)

### UI Patterns and Standards (Reorganized 2026-01-07)

**Governance & Standards (01-09)**:
- `01_Onboarding_Context.md` - Project context and current status
- `02_Architecture_Rules.md` - Architecture rules and model locations
- `03_Development_Standards.md` - Development standards and ELOBS workflow
- `04_Frontend_UI_Canon.md` - Frontend structure and UI patterns
- `05_UI_Menu_Template_Mapping.md` - Menu to template mapping
- `06_Layout_Terminology.md` - Layout & design system (was: CONSOLIDATED_DESIGN_SYSTEM.md)
- `07_Governance_Market_References.md` - Governance & market inspiration (was: CONSOLIDATED_GOVERNANCE_RULES.md)
- `08_Sidebar_Implementation.md` - Sidebar specifications (was: CONSOLIDATED_IMPLEMENTATION_SPECS.md)
- `09_Lookup_Canon.md` - Lookup modal patterns (was: LOOKUP_CANON.md)

**Functional Templates (10-15)**:
- **Master Templates**:
  - `10_Master_Simple_Template.md` - Simple master pattern (was: MST-S.md)
  - `11_Master_Medium_Template.md` - Medium master pattern (was: MST-M.md)
  - `12_Master_Complex_Template.md` - Complex master pattern (was: MST-C.md)
- **Transaction Templates**:
  - `13_Transaction_Simple_Template.md` - Simple transaction pattern (was: TXN-S.md)
  - `14_Transaction_Medium_Template.md` - Medium transaction pattern (was: TXN-M.md)
  - `15_Transaction_Complex_Template.md` - Complex transaction pattern (was: TXN-C.md)

---

## 📂 18_WIRING_CHECKLISTS (Implementation Guides) ⭐ NEW

### Practical Step-by-Step Wiring Guides (Created 2026-01-07, Sequential Numbering Added)

**Purpose**: HOW to wire UI components (not WHAT to build - see 14UI_CANON for that)

- **`00_README.md`** - Overview and clear distinction from 14UI_CANON
  - Quick decision tree
  - When to use which checklist
  - Must-read prerequisites

- **`01_MASTER_DATA_WIRING.md`** - Master data list pages (Customer, Item, UOM, Supplier, Location)
  - 11 phases covering complete implementation
  - Backend setup, service layer, UI components, actions, modals, testing
  - Reference: CustomerSetup.tsx, UOMSetup.tsx

- **`02_TRANSACTION_FORM_WIRING.md`** - Transaction forms (PO, Sales Order, Intercompany Transfer)
  - 14 phases covering complete implementation
  - TransactionToolbar integration, header, line items, lookups, workflow
  - Reference: PurchaseOrderFormPage.tsx (564 lines), IntercompanyTransferFormPage.tsx (620 lines)

- **`03_WORKFLOW_WIRING.md`** - Workflow, validation, business rules
  - 10 phases covering state machines and authorization
  - Status state machine, workflow actions, validation, authorization, audit trail
  - Reference: PurchaseOrderViewSet, procurement.service.ts

- **`04_UI_TYPOGRAPHY_STYLING_REFERENCE.md`** ⭐ NEW - Complete UI styling guide
  - Typography levels (L1-L4) with exact font sizes
  - All form elements (labels, textboxes, LOV, checkbox, radio button)
  - Button styles (primary, secondary, link, icon)
  - Table styles, status badges, color palette
  - Copy-paste code snippets for common patterns

- **`05_AGENT_E_ONBOARDING.md`** ⭐ NEW - Comprehensive onboarding for Agent E (HRM/CRM)
  - Complete UI development guidelines
  - What NOT to do (critical mistakes to avoid)
  - What TO do (best practices and patterns)
  - HRM/CRM specific guidance
  - Integration checklist for copying to enterprise shell

**Key Difference from 14UI_CANON**:
- 14UI_CANON = Standards, rules, functional patterns (WHAT to build, WHY it works)
- 18_WIRING_CHECKLISTS = Implementation steps (HOW to wire it up)

---

## 📂 15RENDER (Deployment)

### Deployment Documentation
- `README.md` - Render deployment overview
- `README_RENDER_DEPLOY.md` - Render deployment guide
- `DEPLOYMENT_MATURITY_CHECKLIST.md` - Deployment checklist
- `DNS_HTTPS.md` - DNS and HTTPS configuration
- `backend/README_SENTRY.md` - Sentry integration
- `db/backup_restore.md` - Database backup/restore
- `redis/redis_strategy.md` - Redis strategy
- `migration/AWS_GCP_BLUEPRINT.md` - Cloud migration blueprint

---

## 🎯 QUICK LOAD SEQUENCE FOR NEW SESSIONS

### Minimum Context Load (5-10 minutes)
1. **ASTRA-BOOTSTRAP.md**
2. **NEXT_SESSION.md** (Root)
3. **.steering/00AGENT_ONBOARDING/01_Onboarding_Context.md**
4. **.steering/00AGENT_ONBOARDING/02_Architecture_Rules.md**
5. **.steering/00AGENT_ONBOARDING/01_Governance/CANONICAL_RULESET.md**

### Full Context Load (20-30 minutes)
1. All files in **00AGENT_ONBOARDING/** (complete sequence)
2. **01_ARCH_GOVERNANCE/CANONICAL_RULESET.md**
3. **14UI_CANON/LOOKUP_CANON.md**
4. **13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/COMPLETION_SUMMARY.md**
5. Relevant BBP files for current module

### Deep Dive (As Needed)
- Specific BBP files for the module you're working on
- UI patterns (10-15_Master/Transaction templates) for the component type
- **Wiring checklists (18_WIRING_CHECKLISTS)** for step-by-step implementation
- Test prompts for reference
- Historical reports for context
- **RETAIL_IMPLEMENTATION_TRACKER.md** for current Retail module status

---

## 📋 VERIFICATION CHECKLIST

When starting a new session, verify you've loaded:
- [ ] ASTRA-BOOTSTRAP.md session initialization protocol
- [ ] NEXT_SESSION.md for current tasks
- [ ] All 6 folders in 00AGENT_ONBOARDING/
- [ ] CANONICAL_RULESET.md (governance)
- [ ] Current module BBP (e.g., inventory_bbp.md)
- [ ] Relevant UI patterns (14UI_CANON: 10-15_Master/Transaction templates)
- [ ] 09_Lookup_Canon.md (if building UI)
- [ ] **18_WIRING_CHECKLISTS** (if implementing UI components)
- [ ] **RETAIL_IMPLEMENTATION_TRACKER.md** (if working on Retail module)

---

**Last Updated**: 2026-01-09 11:15 IST  
**Total Files**: 80+ markdown files in .steering/  
**Latest Additions**: 18_WIRING_CHECKLISTS (4 files), 14UI_CANON reorganized (11 files renamed)  
**Purpose**: Ensure zero context loss when switching models/agents
