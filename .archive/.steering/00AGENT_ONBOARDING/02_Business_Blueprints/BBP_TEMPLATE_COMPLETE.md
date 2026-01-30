# BBP Template - Complete Reference & Template

**Version**: 1.0  
**Date**: 2025-12-28 21:35 IST  
**Status**: Production-Ready  
**Based On**: 4.1 PR BBP + HRM Employee Management BBP Analysis

---

## 📚 **TABLE OF CONTENTS**

### **PART 1: QUICK REFERENCE GUIDE**
- [Quick Start](#quick-start)
- [Section Guide](#section-guide)
- [Template Types](#template-types)
- [Quality Checklist](#quality-checklist)
- [Examples](#examples)
- [Tips & Best Practices](#tips--best-practices)
- [Troubleshooting](#troubleshooting)

### **PART 2: FULL BBP TEMPLATE**
- [Template Structure](#template-structure)
- [All Sections (1-12 + X)](#full-template)

---

# PART 1: QUICK REFERENCE GUIDE

---

## 🎯 **QUICK START**

### **Step 1: Choose Template Type**

| Module Type | Template | Complexity | Use For |
|-------------|----------|------------|---------|
| **Master Data** | `_master_03` | High | Employee, Customer, Item, Supplier |
| **Transaction** | `_txn_02` | Medium | PR, PO, Invoice, Order, Receipt |
| **Dashboard** | `_dashboard_01` | Low | Reports, Analytics, KPIs |

### **Step 2: Copy Template**
Scroll down to [PART 2: FULL BBP TEMPLATE](#full-template) and copy the entire template.

### **Step 3: Replace Placeholders**
- `[MODULE_NAME]` → Your module name (e.g., "Purchase Requisition")
- `[MODULE_NUMBER]` → BBP number (e.g., "4.1")
- `[FILL_IN]` → Your content
- `[table_name]` → Actual table name
- `[field_name]` → Actual field names

### **Step 4: Fill Sections**
Follow the template section by section, filling in all required content.

### **Step 5: Validate**
Use the [Quality Checklist](#quality-checklist) to ensure completeness.

---

## 📋 **SECTION GUIDE**

### **Required Sections** (ALL BBPs must have these)

#### **1. Business Purpose** (Section X.1)
- **What**: Clear statement of module purpose
- **Why**: Business value and goals
- **How**: Key capabilities
- **Length**: 200-500 words

**Example**:
```
The Purchase Requisition (PR) is an internal request to procure 
goods/services, raised by a store, warehouse, or department and 
optionally approved before becoming a Purchase Order.

Goals:
- Capture demand (what, how much, by when)
- Enable approval workflows
- Support both PR → PO and direct PO
- Provide audit trail
```

---

#### **2. Business Scope** (Section X.2)
- **In Scope**: What this module DOES
- **Out of Scope**: What this module DOES NOT do
- **Length**: 100-300 words

**Example**:
```
In Scope:
- Employee master data management
- Organizational hierarchy
- Employee self-service
- Document management
- Lifecycle workflows

Out of Scope:
- Payroll computation
- Time & attendance
- Recruitment
- Performance management
```

---

#### **3. Canonical Domain Mapping** (Section X.3)
- **Domain**: Which domain owns this
- **Aggregate Root**: Primary entity
- **Ownership**: Scope level
- **Data Classification**: Security level
- **Compliance**: Regulations

**Example**:
```
- Domain: HRM
- Aggregate Root: Employee
- Ownership: Company (enterprise-level)
- Nature: Shared master across ERP modules
- Data Classification: PII - Highly Sensitive
- Retention Policy: 7 years post-employment
- Compliance: GDPR, CCPA, SOX, Labor Laws
```

---

#### **4. Core Business Entities & Detailed Schema** (Section X.4)
- **Complete table schemas** with:
  - All fields with types
  - Indexes (PRIMARY, UNIQUE, INDEX)
  - Constraints (FOREIGN KEY, CHECK)
  - Business validations

**Example**:
```
Table: employee
Fields:
- id: UUID (Primary Key)
- company_id: UUID (Foreign Key to company)
- employee_code: VARCHAR(20) (Unique, Indexed)
- first_name: VARCHAR(100) (Required)
...

Indexes:
- PRIMARY KEY (id)
- UNIQUE KEY uk_employee_company_code (company_id, employee_code)
- INDEX idx_company_id (company_id)

Constraints:
- fk_employee_company FOREIGN KEY (company_id) REFERENCES company(id)
- chk_no_circular_reporting CHECK (manager_id != id)
```

---

#### **5. UI/UX Requirements** (Section X.5)
- **List View**: Columns, filters, actions, sorting
- **Form View**: Sections, fields, validations
- **Line Entry**: Grid (for transactions)
- **Approval View**: Approver interface
- **Bulk Operations**: Import/export

**Example**:
```
Screen Name: Employee Master
Path: Human Resources → Employee Management → Employee Master

A) Employee List View
Columns:
- Employee Code
- Employee Name
- Department
- Position
- Employment Status
- Actions (Edit, Delete)

Filters:
- Search (name, email, code)
- Department (multi-select)
- Status (multi-select)
```

---

#### **6. Validation Rules** (Section X.6)
- **Header-level**: Required fields, unique constraints, formats
- **Line-level**: Quantity, references
- **Status/Workflow**: State integrity
- **Cross-field**: Date ranges, conditional logic

**Example**:
```
Required Fields:
- first_name (required, max 100 chars)
- email (required, unique, valid email format)
- date_of_birth (required, must be 18+ years old)

Unique Constraints:
- employee_code unique per company
- work_email globally unique

Format Validations:
- Email: Valid email format (RFC 5322)
- Phone: Valid phone format (E.164)
```

---

#### **7. Workflow** (Section X.7)
- **State Machine**: Visual diagram
- **Valid Transitions**: Table with triggers and approvals
- **Transition Rules**: Detailed for each transition
- **Approval Requirements**: Who approves what
- **Automated Transitions**: Batch jobs, reminders

**Example**:
```
State Flow:
DRAFT → ONBOARDING → ACTIVE → RESIGNED

Valid Transitions:
| From | To | Trigger | Approval |
|------|-------|---------|----------|
| DRAFT | ONBOARDING | Submit | No |
| ONBOARDING | ACTIVE | Complete | Yes (HR) |
```

---

#### **8. Module Metadata & Build Steps** (Section X.8)
- **YAML Metadata**: Dependencies, integrations, compliance
- **Build Steps**: Backend, frontend, integration, security, testing

**Example**:
```yaml
module_type: master
complexity: high
template_ref: _master_03

depends_on:
  - Company (business_entities)
  - Locations (company)
  - Departments (hrm)

used_by:
  - Payroll (hrm.payroll)
  - Attendance (hrm.attendance)
```

---

## 🎨 **TEMPLATE TYPES**

### **Master Module** (_master_03)
**Use For**: Employee, Customer, Item, Supplier, Product

**Key Characteristics**:
- High complexity
- Many fields (40-60+)
- Complete CRUD
- Audit trail
- Soft delete
- Version control

**Required Sections**:
- All 8 core sections
- Access Control (Section 9)
- Integrations (Section 10)
- Audit & Compliance (Section 11)

---

### **Transaction Module** (_txn_02)
**Use For**: PR, PO, Invoice, Order, Receipt, Return

**Key Characteristics**:
- Medium complexity
- Header + Lines
- Workflow states
- Approval process
- Document linking

**Required Sections**:
- All 8 core sections
- Workflow is CRITICAL
- Line Entry in UI/UX
- Status transitions

---

### **Dashboard Module** (_dashboard_01)
**Use For**: Reports, Analytics, KPIs, Dashboards

**Key Characteristics**:
- Low complexity
- Read-only
- Aggregations
- Visualizations
- Filters

**Required Sections**:
- Sections 1-3 (Purpose, Scope, Domain)
- Section 5 (UI/UX for dashboard)
- Section 12 (KPIs)
- Data sources and calculations

---

## ✅ **QUALITY CHECKLIST**

### **Before Submitting BBP**:

**Content Completeness**:
- [ ] All [FILL_IN] placeholders replaced
- [ ] All [MODULE_NAME] replaced
- [ ] All [MODULE_NUMBER] replaced
- [ ] No empty sections (or marked "Out of Scope")

**Schema Quality**:
- [ ] All fields have types
- [ ] All fields have descriptions
- [ ] Primary keys defined
- [ ] Foreign keys defined
- [ ] Unique constraints defined
- [ ] Check constraints defined
- [ ] Indexes defined

**Validation Quality**:
- [ ] Required fields listed
- [ ] Unique constraints listed
- [ ] Format validations specified
- [ ] Cross-field validations specified
- [ ] Business rules documented

**Workflow Quality** (if applicable):
- [ ] State machine diagram present
- [ ] All transitions documented
- [ ] Approval requirements specified
- [ ] Invalid transitions listed

**UI/UX Quality**:
- [ ] List view columns defined
- [ ] Filters specified
- [ ] Actions listed
- [ ] Form sections defined
- [ ] Field types specified

**Metadata Quality**:
- [ ] YAML is valid
- [ ] Dependencies listed
- [ ] Consumers listed
- [ ] Compliance specified
- [ ] Build steps detailed

---

## 📊 **EXAMPLES**

### **Good BBP Examples**:
1. ✅ `4.1_pr_bbp.md` - Purchase Requisition (Transaction)
2. ✅ `1.1 Employee Management.md` + Addendum (Master)

### **Section Examples**:

**Good Business Purpose**:
```
The Employee Management module serves as the authoritative 
enterprise master for managing all employee-related data, 
organizational structure, lifecycle events, and employee-facing 
services. It acts as the single source of truth for workforce 
information and a parent dependency for Payroll, Attendance, 
IAM, POS authorization, and approval workflows.
```

**Good Schema**:
```
Table: purchase_requisition
Fields:
- id: UUID (Primary Key)
- company_id: FK (Yes, Company scope)
- pr_number: String(30) (Yes, Human-readable PR No)
- pr_status: Enum (Yes, DRAFT/SUBMITTED/APPROVED/...)
- requested_by_user_id: FK (User) (Yes, Who raised the PR)
...

Indexes:
- PRIMARY KEY (id)
- UNIQUE KEY uk_pr_company_number (company_id, pr_number)
- INDEX idx_company_id (company_id)

Constraints:
- fk_pr_company FOREIGN KEY (company_id) REFERENCES company(id)
- chk_hire_before_exit CHECK (hire_date <= exit_date OR exit_date IS NULL)
```

---

## 🚀 **TIPS & BEST PRACTICES**

### **Writing Tips**:
1. **Be Specific**: Use exact field names, not "field1, field2"
2. **Be Complete**: Don't skip sections or leave placeholders
3. **Be Consistent**: Use same terminology throughout
4. **Be Clear**: Write for developers who will implement

### **Schema Tips**:
1. **Always include**:
   - Primary key (UUID)
   - Foreign keys (with names)
   - Audit fields (created_at, updated_at, created_by, updated_by)
   - Soft delete (deleted_at)
   - Version (for optimistic locking)

2. **Name constraints**:
   - `fk_[table]_[reference]` for foreign keys
   - `uk_[table]_[fields]` for unique keys
   - `chk_[validation]` for check constraints

3. **Index strategically**:
   - Primary key
   - Foreign keys
   - Unique fields
   - Frequently filtered fields
   - Composite indexes for common queries

### **Validation Tips**:
1. **Cover all levels**:
   - Field-level (format, length, range)
   - Record-level (required, unique)
   - Cross-field (date ranges, conditionals)
   - Business rules (status integrity, workflows)

2. **Be explicit**:
   - "Email must be valid RFC 5322 format"
   - Not just "Email must be valid"

### **Workflow Tips**:
1. **Draw the diagram first**: Visualize all states and transitions
2. **Document invalid transitions**: What CANNOT happen
3. **Specify approvals**: Who approves, when, criteria
4. **Include automation**: Batch jobs, reminders, notifications

---

## 🆘 **TROUBLESHOOTING**

### **Common Issues**:

**Issue**: "I don't know what to put in [FILL_IN]"  
**Solution**: Look at example BBPs (4.1 PR or HRM Employee Management)

**Issue**: "Schema is too complex"  
**Solution**: Start with core fields, add details iteratively

**Issue**: "Workflow is confusing"  
**Solution**: Draw state diagram on paper first, then document

**Issue**: "Too many sections"  
**Solution**: Focus on required sections first (1-8), add others later

---

# PART 2: FULL BBP TEMPLATE

---

<a name="full-template"></a>

# [MODULE_NUMBER] [MODULE_NAME] – Business Blueprint (BBP)

**Template Ref**: [_master_03 | _txn_02 | _dashboard_01]

---

## [MODULE_NUMBER].1 Business Purpose

**[FILL_IN: Clear, concise statement of what this module does and why it exists]**

The **[MODULE_NAME]** module serves as [primary purpose]. It provides [key capabilities] and acts as [role in the system].

### Goals:
- [Goal 1: What business problem does it solve?]
- [Goal 2: What value does it provide?]
- [Goal 3: What processes does it enable?]
- [Goal 4: What integrations does it support?]

### Hybrid Behavior (if applicable):
**[FILL_IN: Config-driven behavior, optional features, or variations]**

- [MODULE_NAME] can be **enabled/disabled** per:
  - Company
  - Location
  - Role
- When enabled, [describe behavior variations]

---

## [MODULE_NUMBER].2 Business Scope

### In Scope
**[FILL_IN: What this module DOES include]**

- [Feature 1]
- [Feature 2]
- [Feature 3]
- [Feature 4]
- [Feature 5]

### Out of Scope
**[FILL_IN: What this module DOES NOT include - must be in other modules]**

- [Excluded feature 1]
- [Excluded feature 2]
- [Excluded feature 3]
- [Excluded feature 4]

---

## [MODULE_NUMBER].3 Canonical Domain Mapping

**[FILL_IN: Domain classification and ownership]**

- **Domain**: [HRM | Finance | Procurement | Inventory | Sales | CRM | POS]
- **Aggregate Root**: [Primary entity name]
- **Ownership**: [Company | Location | User] (scope level)
- **Nature**: [Shared master | Transaction | Configuration | Reporting]
- **Data Classification**: [Public | Internal | Confidential | PII - Highly Sensitive]
- **Retention Policy**: [X years + legal requirements]
- **Compliance**: [GDPR | CCPA | SOX | Labor Laws | Industry-specific]

---

## [MODULE_NUMBER].4 Core Business Entities & Detailed Schema

### [ENTITY_1_NAME] (Aggregate Root)

**[FILL_IN: Primary entity with complete schema]**

```
Table: [table_name]
Fields:
- id: UUID (Primary Key)
- company_id: UUID (Foreign Key to company) [if company-scoped]
- [field_name_1]: [TYPE] (Required/Optional, Description)
- [field_name_2]: [TYPE] (Required/Optional, Description)
- [field_name_3]: [TYPE] (Required/Optional, Description)
...
- created_at: TIMESTAMP (Auto)
- updated_at: TIMESTAMP (Auto)
- created_by_user_id: UUID (Foreign Key to user)
- updated_by_user_id: UUID (Foreign Key to user)
- deleted_at: TIMESTAMP (Soft Delete, nullable)
- version: INTEGER (Default: 1, Optimistic Locking)

Indexes:
- PRIMARY KEY (id)
- UNIQUE KEY uk_[table]_[company]_[code] (company_id, [unique_field])
- INDEX idx_company_id (company_id)
- INDEX idx_[field_name] ([field_name])
- INDEX idx_[composite] ([field1], [field2]) WHERE [condition]

Constraints:
- fk_[table]_company FOREIGN KEY (company_id) REFERENCES company(id)
- fk_[table]_[related] FOREIGN KEY ([related_id]) REFERENCES [related_table](id)
- chk_[validation_name] CHECK ([validation_logic])
- chk_[date_range] CHECK ([start_date] <= [end_date] OR [end_date] IS NULL)
```

**Business Validations**:
- [Validation rule 1]
- [Validation rule 2]
- [Validation rule 3]

---

### [ENTITY_2_NAME]

**[FILL_IN: Supporting entity with complete schema]**

```
Table: [table_name]
Fields:
- id: UUID (Primary Key)
- [parent_entity]_id: UUID (Foreign Key to parent)
- [field_name_1]: [TYPE] (Required/Optional, Description)
...

Indexes:
- PRIMARY KEY (id)
- INDEX idx_[parent]_id ([parent_entity]_id)

Constraints:
- fk_[table]_[parent] FOREIGN KEY ([parent_entity]_id) REFERENCES [parent_table](id)
```

---

### [ENTITY_3_NAME] (if applicable)

**[FILL_IN: Additional entities as needed]**

---

## [MODULE_NUMBER].5 UI/UX Requirements

**[FILL_IN: Complete screen specifications]**

**Screen Name**: [Screen Name]  
**Path**: [Module] → [Submenu] → [Screen Name]

### A) List View

**Columns**:
- [Column 1 Name] ([data type, format])
- [Column 2 Name] ([data type, format])
- [Column 3 Name] ([data type, format])
- [Column 4 Name] ([data type, format])
- [Column 5 Name] ([data type, format])
- Actions (Edit, Delete, [Custom Actions])

**Filters**:
- [Filter 1]: [Type] (dropdown, date range, multi-select)
- [Filter 2]: [Type]
- [Filter 3]: [Type]
- Date Range: [Field Name]
- Status: [Status options]
- Search: [Searchable fields]

**Actions**:
- Create [Entity] (button)
- Bulk Import (CSV/Excel upload)
- Export (CSV/Excel download)
- [Custom Action 1]
- [Custom Action 2]
- Refresh
- Column Customization

**Sorting**:
- [Field 1] (default)
- [Field 2] (A-Z, Z-A)
- [Field 3]
- [Date Field] (newest/oldest)

**Pagination**:
- Page size: [20 | 50 | 100]
- Total count display
- Page navigation

---

### B) Header Form (Create/Edit)

**Form Sections**:

**Section 1: [Section Name]**
- [Field 1 Name] * (required, [type], [validation])
- [Field 2 Name] (optional, [type], [validation])
- [Field 3 Name] (lookup, [source])
- [Field 4 Name] (auto-generated, read-only)

**Section 2: [Section Name]**
- [Field 1 Name]
- [Field 2 Name]
- [Field 3 Name]

**Section 3: System Information** (Read-Only)
- Created By
- Created At
- Updated By
- Updated At
- Version
- Status

**Form Actions**:
- Save as Draft
- Save and Close
- Save and New
- Submit (if workflow)
- Cancel
- Delete (with confirmation)

---

### C) Line Entry (if applicable for transactions)

**Grid Columns**:
- [Line Field 1] (lookup, search)
- [Line Field 2] (quantity, decimal)
- [Line Field 3] (UOM, dropdown)
- [Line Field 4] (calculated, read-only)
- Line Actions (Edit, Delete, Copy)

**Features**:
- Add line via:
  - [Entity] search
  - Barcode scan (optional)
  - Quick add
- Copy line
- Delete line (validation rules)
- Inline validation:
  - [Validation 1]
  - [Validation 2]
- Bulk line operations

---

### D) Approval View (if applicable)

**Approver Interface**:
- List of pending [entities] filtered by:
  - [Filter 1]
  - [Filter 2]
  - Approval threshold

**From Detail View**:
- Approve (with optional comment)
- Reject (reason required)
- Request Changes (with comments)
- Partial edit allowed? [Yes/No, specify fields]

---

### E) Bulk Operations

**Import**:
- Upload CSV/Excel file
- Template download
- Field mapping interface
- Validation preview
- Error report
- Rollback on error

**Export**:
- Select fields to export
- Apply filters
- Choose format (CSV, Excel, PDF)
- Include/exclude sensitive data (permission-based)
- Schedule export (optional)

---

## [MODULE_NUMBER].6 Validation Rules

**[FILL_IN: Complete validation specifications]**

### [MODULE_NUMBER].6.1 Header-Level Validations

**Required Fields**:
- `[field_1]` (required, [constraints])
- `[field_2]` (required, [constraints])
- `[field_3]` (required, [constraints])

**Unique Constraints**:
- `[field_1]` unique per [scope]
- `[field_2]` globally unique
- `[field_3]` unique when [condition]

**Format Validations**:
- [Field]: [Format specification] (e.g., Email: RFC 5322)
- [Field]: [Format specification] (e.g., Phone: E.164)
- [Field]: [Format specification] (e.g., Code: REGEX pattern)

---

### [MODULE_NUMBER].6.2 Line-Level Validations (if applicable)

**Required Fields**:
- Each [entity] must have at least **one line**
- `[line_field_1]` > 0
- `[line_field_2]` must be valid from [source]

**Business Rules**:
- Cannot modify lines once status ≥ [STATUS]
- [Validation rule 1]
- [Validation rule 2]

---

### [MODULE_NUMBER].6.3 Status/Workflow Integrity

**State Transition Rules**:
- Cannot Submit with **no lines** (if applicable)
- Cannot Approve if status not equal to [STATUS]
- Cannot Cancel if [condition]
- [Field tracking] must not exceed [limit]

**Immutability Rules**:
- `[field_1]` is immutable after creation
- `[field_2]` is immutable after [status]
- [Status] records are immutable (cannot edit any field)

---

### [MODULE_NUMBER].6.4 Cross-Field Validations

**Date Validations**:
- `[start_date]` must be <= `[end_date]`
- `[date_field]` must be in [past/future]
- `[date_field]` must be >= `[reference_date]`

**Hierarchy Validations** (if applicable):
- `[parent_id]` cannot be self
- `[parent_id]` must be [active/valid]
- Cannot create circular references

**Conditional Validations**:
- If `[field_1]` is set, `[field_2]` is required
- If `[status]` = [VALUE], `[field]` must be [condition]

---

### [MODULE_NUMBER].6.5 Config Behavior

**Configuration Flags**:
- If `[config_flag]` = false for a company/location:
  - [Behavior 1]
  - [Behavior 2]
- If `[config_flag]` = true:
  - [Enforcement rule]

---

## [MODULE_NUMBER].7 Workflow

**[FILL_IN: Complete workflow state machine]**

### [MODULE_NUMBER].7.1 Status State Machine

```
State Flow:

[STATUS_1]
  ↓ ([Trigger 1])
[STATUS_2]
  ↓ ([Trigger 2])        ↓ ([Trigger 3])
[STATUS_3]              [STATUS_4]
  ↓ ([Trigger 4])
[STATUS_5]
```

**Valid Transitions**:

| From Status | To Status | Trigger | Approval Required |
|-------------|-----------|---------|-------------------|
| [STATUS_1] | [STATUS_2] | [Action] | [Yes/No] ([Role]) |
| [STATUS_2] | [STATUS_3] | [Action] | [Yes/No] ([Role]) |
| [STATUS_3] | [STATUS_4] | [Action] | [Yes/No] ([Role]) |

**Invalid Transitions**:
- [STATUS_X] → Any other status ([reason])
- [STATUS_Y] → [STATUS_Z] ([reason])

---

### [MODULE_NUMBER].7.2 Transition Rules

**[STATUS_1] → [STATUS_2]**:
- **Trigger**: [What initiates this transition]
- **Validations**:
  - [Validation 1]
  - [Validation 2]
- **Approval**: [Role] (if required)
- **Actions**:
  - [Action 1]
  - [Action 2]
  - Trigger `[event_name]` event

**[STATUS_2] → [STATUS_3]**:
- **Trigger**: [What initiates this transition]
- **Validations**:
  - [Validation 1]
  - [Validation 2]
- **Actions**:
  - [Action 1]
  - [Action 2]

[Repeat for all transitions]

---

### [MODULE_NUMBER].7.3 Approval Requirements

**[Approval Type 1]**:
- **Approver**: [Role]
- **Criteria**:
  - [Criterion 1]
  - [Criterion 2]

**[Approval Type 2]**:
- **Approver**: [Role 1] + [Role 2]
- **Criteria**:
  - [Criterion 1]
  - [Criterion 2]

---

### [MODULE_NUMBER].7.4 Automated Transitions

**Auto-transition to [STATUS]**:
- **Trigger**: [Condition]
- **Frequency**: [Daily batch job | Real-time | Scheduled]
- **Action**: [What happens]

**[Reminder/Notification]**:
- **Trigger**: [X days before/after event]
- **Action**: [Send notification to roles]

---

## [MODULE_NUMBER].8 Module Metadata & Build Steps

### Module Metadata

```yaml
module_type: [master | transaction | dashboard]
complexity: [low | medium | high]
template_ref: [_master_03 | _txn_02 | _dashboard_01]

extension_allowed: [true | false]

depends_on:
  - [Dependency 1] ([module.entity])
  - [Dependency 2] ([module.entity])
  - [Dependency 3] ([module.entity])
  - [Dependency 4] ([module.entity])

used_by:
  - [Consumer 1] ([module.entity])
  - [Consumer 2] ([module.entity])
  - [Consumer 3] ([module.entity])

integrates_with:
  - [External System 1] (for [purpose])
  - [External System 2] (for [purpose])
  - [External System 3] (for [purpose])

data_classification: [Public | Internal | Confidential | PII - Highly Sensitive]
retention_policy: [X years + legal requirements]
compliance: [GDPR | CCPA | SOX | Industry-specific]

notes: >
  [Additional context about the module, its role in the system,
  integration patterns, and any special considerations]
```

---

### Build Steps

**You are building a [Complexity] [Type] module for [System Type].**

**Module**: [MODULE_NAME]  
**Template**: [_master_03 | _txn_02 | _dashboard_01]

---

#### Requirements:

**1) Backend (Django + DRF):**

**Models**:
- `[model_1]` ([description])
- `[model_2]` ([description])
- `[model_3]` ([description])

**Serializers**:
- `[Serializer1]` ([purpose])
- `[Serializer2]` ([purpose])
- `[Serializer3]` ([purpose])

**ViewSets**:
- `[ViewSet1]` ([permissions])
  - Filter by: [filters]
  - Search: [fields]
  - Ordering: [fields]
  - Actions/endpoints:
    - `[action_1]`
    - `[action_2]`
    - `[action_3]`

**Business Rules**:
- [Rule 1]
- [Rule 2]
- [Rule 3]

---

**2) Frontend (React + Vite + Tailwind):**

**[Page 1 Name]**:
- [Component 1]
- [Component 2]
- [Feature 1]
- [Feature 2]

**[Page 2 Name]**:
- [Component 1]
- [Component 2]
- [Feature 1]
- [Feature 2]

---

**3) Integration:**

**Axios Service**:
- All [Entity] CRUD operations
- Workflow endpoints ([actions])
- Bulk operations ([import/export])
- Search and filter operations

**Event Publishing**:
- `[entity].[event_1]`
- `[entity].[event_2]`
- `[entity].[event_3]`

**Event Subscriptions**:
- `[source].[event]` → [Action]
- `[source].[event]` → [Action]

---

**4) Security & Permissions:**

**Permission Levels**:
- `[module].[entity].view` ([role])
- `[module].[entity].create` ([role])
- `[module].[entity].edit` ([role])
- `[module].[entity].delete` ([role])
- `[module].[entity].[custom_action]` ([role])

**Data Encryption**:
- Encrypt at rest: [fields]
- Encrypt in transit: HTTPS/TLS
- Mask in logs: [sensitive fields]

**Audit Requirements**:
- Log all CRUD operations
- Log all [workflow transitions]
- Log all [sensitive field access]
- Retain audit logs for [X years]

---

**5) Testing:**

**Unit Tests**:
- Model validations
- Business rule enforcement
- [Specific validation 1]
- [Specific validation 2]

**Integration Tests**:
- API endpoints
- Workflow transitions
- Bulk operations
- Event publishing

**UI Tests**:
- Form validations
- Search and filter
- CRUD operations
- Permission enforcement

---

## [MODULE_NUMBER].9 Access Control & Permissions

**[FILL_IN: Role-based access control]**

### Role Capability Matrix

| Role | View | Create | Update | Approve | Delete | Bulk Ops |
|------|------|--------|--------|---------|--------|----------|
| [Role 1] | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Role 2] | ✅ | ❌ | ⚠️ Limited | ✅ | ❌ | ❌ |
| [Role 3] | ✅ (Self) | ❌ | ⚠️ ESS | ❌ | ❌ | ❌ |
| [Role 4] | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Legend**:
- ✅ Full access
- ⚠️ Limited/Conditional access
- ❌ No access

---

## [MODULE_NUMBER].10 Integrations & Dependencies

**[FILL_IN: System integrations]**

### Upstream Dependencies
- **[Module 1]**: [What data/functionality is consumed]
- **[Module 2]**: [What data/functionality is consumed]

### Downstream Consumers
- **[Module 1]**: [What data/functionality is provided]
- **[Module 2]**: [What data/functionality is provided]

### External Integrations
- **[System 1]**: [Integration purpose and method]
- **[System 2]**: [Integration purpose and method]

---

## [MODULE_NUMBER].11 Audit, Compliance & Controls

**[FILL_IN: Audit and compliance requirements]**

### Audit Trail
- Complete audit trail for all [operations]
- Track [field changes]
- Retention: [X years]

### Compliance
- [Regulation 1]: [Compliance requirement]
- [Regulation 2]: [Compliance requirement]
- [Regulation 3]: [Compliance requirement]

### Controls
- Role-based access enforcement
- Data encryption (at rest and in transit)
- Document retention policies
- [Custom control 1]
- [Custom control 2]

---

## [MODULE_NUMBER].12 KPIs & Monitoring

**[FILL_IN: Key performance indicators]**

### Business KPIs
- [KPI 1]: [Measurement method]
- [KPI 2]: [Measurement method]
- [KPI 3]: [Measurement method]

### Technical KPIs
- API response time: [Target]
- Error rate: [Target]
- Uptime: [Target]

---

## [MODULE_NUMBER].X Domain Events

**[FILL_IN: Events published by this module]**

- `[entity].[event_1]`
- `[entity].[event_2]`
- `[entity].[event_3]`
- `[entity].[event_4]`

---

## [MODULE_NUMBER].X Explicit Domain Exclusions

**[FILL_IN: What is explicitly NOT in this module]**

The following are **explicitly out of scope** and must be modeled in their respective BBPs:
- [Excluded feature 1]
- [Excluded feature 2]
- [Excluded feature 3]
- [Excluded feature 4]

---

## [MODULE_NUMBER].X Architectural Notes

**[FILL_IN: Architecture and design notes]**

- [Entity] is a **[shared enterprise master | transaction | configuration]**
- Changes are **audit-mandatory**
- Downstream modules must integrate via **[reference | events | API]**
- [Additional architectural note]

---

## [MODULE_NUMBER].X Reference Role & Governance Contract

**[FILL_IN: How other modules should interact with this module]**

### Reference Role
This BBP serves as the **[PRIMARY | SECONDARY] CANONICAL [DOMAIN] REFERENCE** for [scope].

Downstream BBPs MAY:
- [Allowed interaction 1]
- [Allowed interaction 2]
- [Allowed interaction 3]

Downstream BBPs MUST NOT:
- [Prohibited interaction 1]
- [Prohibited interaction 2]
- [Prohibited interaction 3]

---

**END OF TEMPLATE**

---

## 📚 **REFERENCE**

### **Example BBPs**:
- `4.1_pr_bbp.md` - Purchase Requisition (Transaction)
- `1.1 Employee Management.md` + Addendum - Employee Management (Master)

### **Analysis Documents**:
- `HRM_BBP_ALIGNMENT_ANALYSIS.md` - Alignment analysis
- `HRM_BBP_100PCT_COMPLETE.md` - Completion summary

---

**Template Version**: 1.0  
**Last Updated**: 2025-12-28 21:35 IST  
**Status**: Production-Ready  
**Based On**: 4.1 PR BBP + HRM Employee Management BBP Analysis
