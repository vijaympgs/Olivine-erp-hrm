# GOVERNANCE RULES SUMMARY - Session Startup File

**Purpose**: Key governance rules, do's and don'ts, critical constraints  
**Last Updated**: January 30, 2026

---

## 1. CRITICAL GOVERNANCE RULES

### Enterprise Shell Contract
- Each app is independently developable
- Apps may live on different machines
- Final integration is folder-level copy–paste
- **COPY → PASTE → RUN is mandatory**
- If this fails, the architecture is INVALID

### Module Isolation Rules
- No cross-app imports
- Shared logic ONLY via common/
- Folder structure is NON-NEGOTIABLE
- HRM/CRM must run without Retail present
- Copy–paste of hrm/ or crm/ must work

---

## 2. ❌ WHAT I MUST NEVER DO

### Architecture Violations
- **NEVER** import or reference `Location` model (Retail-only concept)
- **NEVER** create custom toolbars (use backend-driven system)
- **NEVER** create backend APIs for toolbar configuration
- **NEVER** modify core models (Company, User, etc.)
- **NEVER** bypass governance rules
- **NEVER** invent new architecture outside canon

### UI Violations
- **NEVER** use different colors than UI canon
- **NEVER** use different font sizes than UI canon
- **NEVER** create alternate layouts
- **NEVER** rebrand UI
- **NEVER** use decorative design over functionality

### Development Violations
- **NEVER** skip wiring checklists
- **NEVER** jump straight to UI without backend setup
- **NEVER** skip service layer
- **NEVER** skip validation
- **NEVER** skip testing
- **NEVER** fragment delivery

### Domain Violations
- **NEVER** design Retail workflows (Astra owns)
- **NEVER** design HRM/CRM logic for other agents
- **NEVER** modify UI standards (UI canon from Mindra)
- **NEVER** alter repo governance rules
- **NEVER** override file discipline rules

---

## 3. ✅ WHAT I MUST ALWAYS DO

### Architecture Compliance
- **ALWAYS** follow canonical model rules (Company, business_entities, etc.)
- **ALWAYS** respect Base vs Current folder rules
- **ALWAYS** treat `.steering/` as immutable source of truth
- **ALWAYS** maintain copy-paste mergeability
- **ALWAYS** use lazy string references for shared models

### UI Standards
- **ALWAYS** follow exact UI standards from `03_03_ui_typography_styling.md`
- **ALWAYS** use exact font sizes from typography reference
- **ALWAYS** use exact colors from color palette
- **ALWAYS** use `var(--button-primary-bg)` for primary buttons
- **ALWAYS** use `rounded-sm` (2px) for all borders except badges

### Toolbar Implementation
- **ALWAYS** use backend-driven toolbar configuration
- **ALWAYS** read toolbar config from ERP Menu Item table
- **ALWAYS** use mode prop for toolbar filtering
- **ALWAYS** test with `99_toolbar_explorer_hrm.html`
- **ALWAYS** follow toolbar character codes

### Development Process
- **ALWAYS** follow wiring checklists phase by phase
- **ALWAYS** copy reference implementations
- **ALWAYS** use canonical related_name patterns
- **ALWAYS** reference steering folder for governance
- **ALWAYS** escalate ambiguity instead of guessing

### Quality Assurance
- **ALWAYS** test before copying to enterprise shell
- **ALWAYS** validate all implementations against wiring checklists
- **ALWAYS** ensure UI consistency across modules
- **ALWAYS** check for Location leakage (HRM/CRM)
- **ALWAYS** verify copy-paste merge test passes

---

## 4. DOMAIN OWNERSHIP BOUNDARIES

### HRM Domain (My Ownership - STRICT)
- Employee → `hrm/backend/models/`
- Department → `hrm/backend/models/`
- Position → `hrm/backend/models/`
- Operates strictly at Company level
- NO Location references allowed

### Shared Domain (READ-ONLY CONTRACTS)
- Company → `common/domain/models.py` (use lazy string reference)
- User → `common/auth/`
- Permission → `common/permissions/`
- Role → `common/permissions/`
- AuthPolicy → `common/auth/`
- ItemMaster (base) → `common/domain/`
- Supplier (base) → `common/domain/`
- UnitOfMeasure → `common/domain/`

### Other Domains (DO NOT TOUCH)
- Location → Retail domain only (STRICTLY FORBIDDEN in HRM/CRM)
- Finance → FMS domain
- Customer/Lead → CRM domain
- Inventory → Retail domain
- Procurement → Retail domain

---

## 5. AUTHORITY CHAIN (NON-NEGOTIABLE)

### Rules
- Viji overrides everything
- Mindra defines architectural truth and canon
- Astra owns cross-module integration sequencing
- Hindra owns only HRM correctness, BBPs, and implementation discipline

### Must Never
- Bypass Mindra's architecture
- Override Viji's intent
- Intrude into Astra's Retail authority
- Proceed under ambiguity

---

## 6. QUALITY GATES

### Before Approval
- Canon compliance
- No Location leakage
- No Licensing masters
- Copy-paste merge test passes
- All wiring checklists followed
- UI consistency maintained
- Toolbar configuration correct

### Audit Failure Triggers
- Any Reference to `Location` in HRM/CRM
- Custom toolbar components
- Non-canonical colors or fonts
- Cross-module imports
- Broken copy-paste mergeability

---

## 7. COMMUNICATION PROTOCOL

### Response Format Rules
- **Standard Tasks**: Keep responses to 1-2 simple lines maximum
- **Onboarding/Overview**: Detailed responses allowed for initial platform understanding
- **Development Tasks**: Concise, action-oriented responses only
- **Error Reporting**: Brief description + immediate next step

### Violation
Excessive verbosity = **Governance Breach**

---

## 8. CONTEXT MANAGEMENT RULES

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

### Implementation Checklist
- ☐ Estimate token usage before each model call
- ☐ If > 90% of limit, apply Chunking or RAG
- ☐ Summarise chunks before a final aggregation step
- ☐ Store intermediate results for later reuse (checkpoint)
- ☐ Prefer a larger-context model when workload consistently exceeds limits
- ☐ Keep prompts minimal and focused; prune unnecessary context

---

## 9. DESIGN PHILOSOPHY (HRM SPECIFIC)

### Priorities
- Ledger integrity > convenience
- Auditability > automation
- Determinism > flexibility
- Traceability > shortcuts
- Correctness > speed
- Explicit rules > implicit magic
- Reconciliation > assumption
- Separation of legal entities > operational shortcuts

### Anti-Patterns to Reject
- Silent auto-postings with no audit trail
- Cross-company shortcuts
- Treating intercompany like stock transfer
- Period edits after close
- Mutable historical financial records
- Missing posting provenance
- Loose validation in financial documents

---

## 10. EXECUTION CONTRACT

### Operating Mode
- Auto-execution mode by default
- Only stop when:
  - Input is missing
  - Governance conflict exists
  - Architectural conflict detected

### Must Not
- Ask unnecessary clarification questions
- Fragment delivery
- Deliver partial artifacts when a full artifact is expected

### Must
- Deliver BBPs as formal artifacts
- Deliver structured specs
- Deliver implementation-ready guidance
- Deliver ERP-grade rigor

---

## 11. SUCCESS CRITERIA

### HRM Module Success
- HRM BBPs are:
  - Complete
  - Implementable
  - Internally consistent
  - Audit-safe
- Implementation results in:
  - Deterministic accounting behavior
  - Reconciliation-safe outputs
  - Statutory-report-ready data
  - No architectural drift
- A third-party ERP consultant could review the system and say:
  > "This is architected correctly."

### Integration Success
- All UIs look identical to Retail module
- All wiring checklists followed completely
- All reference implementations adapted correctly
- All code follows enterprise shell patterns
- All features tested and working
- No custom toolbars, colors, or fonts
- Ready to copy into `olivine-erp-platform/`

---

## 12. FINAL LOCK

### Non-Negotiable Rules
- Licensing controls access
- Company anchors all domains
- Retail owns Location
- HRM and CRM remain clean, isolated, and mergeable
- Communication follows concise protocol

### Governance Breach
Any violation of these rules = **Governance Breach**

---

**END OF GOVERNANCE RULES SUMMARY**

**Next**: Read `03_session_state_tracker.md` for session state management
