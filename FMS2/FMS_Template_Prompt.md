# FMS BBP Creation Prompt Template

## **Standard BBP Creation Prompt**

Use this template to create Business Blueprints for any module. Replace the bracketed values with your specific module details.

---

## **BASE PROMPT TEMPLATE**

```
Refer FMS_Template_Prompt.md and create a BBP for [TARGET_FILE_PATH] using the FMS_Template_Reference.md as your comprehensive guide.

The agent should automatically derive:
- Module Number: [X.Y] from the file path (e.g., FMS\01.Finance Setup & Configuration\1.1 Chart of Accounts.md = 1.1)
- Module Name: [MODULE_NAME] from the file name (e.g., 1.1 Chart of Accounts.md = Chart of Accounts)
- Module Type: [Master/Transaction/Dashboard/Reports/Config/Rule/Setup] based on the module functionality

Module Details:
- Module Name: [MODULE_NAME] (derived from file name)
- Module Number: [X.Y] (derived from file path)
- Module Type: [Master/Transaction/Dashboard/Reports/Config/Rule/Setup]
- Target File: [TARGET_FILE_PATH]

Context Requirements:
1. Read FMS_Template_Reference.md completely first for the complete structure and design language standards
2. Read FMS_BBP_Autoretry_Prevention_Guide.md for autoretry and cutoff prevention rules
3. Read the existing target file (if exists) to understand current content
4. Review FMS/00.masterindex.md for module context and numbering
5. Reference similar modules for consistency patterns

Content Requirements:
1. Use the [Master/Transaction/Dashboard/Reports/Config] template format from BBP_Template_Reference.md
2. Focus on [SPECIFIC_BUSINESS_AREA] including:
   - [KEY_FEATURE_1]
   - [KEY_FEATURE_2]
   - [KEY_FEATURE_3]
   - [KEY_FEATURE_4]
3. Include Django models with proper relationships, indexes, and constraints
4. Define comprehensive business rules for data validation and business logic
5. Specify detailed UI/UX requirements following the design language standards from the template
6. Include complete design system specifications (typography, colors, spacing, components)
7. Add security requirements for data protection and access control
8. Define integration points with related systems
9. Include API specifications for data operations
10. Specify testing requirements and deployment procedures

Technical Requirements:
- Follow Django naming conventions and best practices
- Include company_id for multi-tenant support
- Add audit fields (created_by_user_id, created_at, updated_at)
- Define proper indexing strategy for performance
- Include comprehensive error handling and validation
- Specify responsive design requirements
- Include accessibility standards (WCAG compliance)

Output Format:
- Follow the exact structure from BBP_Template_Reference.md
- Fill in all sections with detailed, actionable specifications
- Include code examples where appropriate
- Ensure content is suitable for direct UI development implementation
- Maintain consistency with existing BBP patterns

Quality Standards:
- All sections must be completed with specific, actionable details
- Technical specifications must be implementable
- UI/UX specifications must follow the design language standards
- Business rules must be clear and comprehensive
- Integration points must be clearly defined with API specifications

## **CRITICAL: AUTORETRY AND CUT ISSUE PREVENTION**

### **EMERGENCY RECOVERY INSTRUCTIONS**
If context is lost, auto-retry occurs, or content gets cut off:

1. **STOP IMMEDIATELY** - Do not continue or regenerate from beginning
2. **USE THIS RECOVERY PROMPT:**
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

### **CONTENT LENGTH MANAGEMENT**
- **Maximum 120 lines per response** to prevent cutting
- **Write one section at a time** - never multiple sections
- **Use STOP MARKERS** after each section: `--- END OF SECTION X.Y.Z ---`
- **If section exceeds 120 lines**, split into subsections with proper numbering

### **CONTEXT PRESERVATION RULES**
- **NEVER auto-retry** or restart from beginning
- **NEVER regenerate completed sections**
- **ALWAYS continue from exact stopping point**
- **MAINTAIN state** across multiple responses
- **VERIFY existing content** before adding new content

### **SECTION COMPLETION CHECKLIST**
Before writing each section, verify:
- [ ] BBP_Template_Reference.md has been read
- [ ] Target file content has been read
- [ ] Module numbering is correct (X.Y pattern)
- [ ] Section number is sequential
- [ ] 120-line limit will be respected
- [ ] STOP MARKER format is correct
- [ ] No auto-retry will occur

### **ERROR RECOVERY PROTOCOL**
If you detect context loss or interruption:
1. **STOP writing immediately**
2. **Announce the issue**: "Context lost - using recovery protocol"
3. **Use the emergency recovery prompt**
4. **Wait for confirmation** before continuing
```

---

## **EXAMPLE: CHART OF ACCOUNTS BBP PROMPT**

```
Create a BBP for FMS\01.Finance Setup & Configuration\1.1 Chart of Accounts.md using the FMS_Template_Reference.md as your comprehensive guide.

Module Details:
- Module Name: Chart of Accounts
- Module Number: 1.1
- Module Type: Master
- Target File: FMS\01.Finance Setup & Configuration\1.1 Chart of Accounts.md

Context Requirements:
1. Read FMS_Template_Reference.md completely first for the complete structure and design language standards
2. Read the existing target file to understand current content
3. Review FMS/00.masterindex.md for module context and numbering
4. Reference similar modules like 1.2 Account Groups for consistency patterns

Content Requirements:
1. Use the Master template format from FMS_Template_Reference.md
2. Focus on financial account management including:
   - Account structure and hierarchy (account codes, names, types, groups)
   - Account classifications (assets, liabilities, equity, revenue, expenses)
   - Account categories and subcategories for detailed reporting
   - Opening balances and historical data management
   - Account status management (active, inactive, frozen)
3. Include Django models with proper relationships, indexes, and constraints
4. Define comprehensive business rules for financial data validation, accounting standards compliance, and data integrity
5. Specify detailed UI/UX requirements following the design language standards from the template
6. Include complete design system specifications (typography, colors, spacing, components)
7. Add security requirements for financial data, role-based access, and audit trails
8. Define integration points with ledgers, transactions, reports, and tax systems
9. Include API specifications for CRUD operations, bulk updates, and data exports
10. Specify testing requirements and deployment procedures

Technical Requirements:
- Follow Django naming conventions and best practices
- Include company_id for multi-tenant support
- Add audit fields (created_by_user_id, created_at, updated_at)
- Define proper indexing strategy for performance on frequently queried fields
- Include comprehensive error handling and validation for financial data
- Specify responsive design requirements for mobile and desktop access
- Include accessibility standards (WCAG 2.1 AA compliance)

Output Format:
- Follow the exact structure from FMS_Template_Reference.md
- Fill in all sections with detailed, actionable specifications
- Include Django model code examples with proper field definitions
- Ensure content is suitable for direct UI development implementation
- Maintain consistency with existing FMS module BBP patterns

Quality Standards:
- All sections must be completed with specific, actionable details
- Technical specifications must be implementable by development team
- UI/UX specifications must follow the design language standards exactly
- Business rules must be clear and comprehensive for financial governance
- Integration points must be clearly defined with complete API specifications
- Security requirements must address financial data privacy and compliance needs
```

---

## **DASHBOARD MODULE PROMPT EXAMPLE**

```
Create a BBP for [DASHBOARD_MODULE_PATH] using the BBP_Template_Reference.md as your guide.

Module Details:
- Module Name: [DASHBOARD_NAME]
- Module Number: [X.Y]
- Module Type: Dashboard
- Target File: [DASHBOARD_MODULE_PATH]

Context Requirements:
1. Read BBP_Template_Reference.md completely first
2. Use the simplified Dashboard template format (Purpose, Type, Functional Capture, UI/UX Spec)
3. Focus on metrics, KPIs, and data visualization requirements
4. Keep technical details minimal, focus on functional specifications

Content Requirements:
1. Use simplified template:
   - Purpose
   - Type: Dashboard
   - Functional Capture
   - UI/UX Spec
2. Focus on metrics and visualization requirements
3. Include data refresh frequencies and real-time update needs
4. Specify export capabilities and sharing features
5. Define user roles and access levels for dashboard views
6. Include mobile responsiveness requirements for dashboard viewing

Output Format:
- Use simplified structure for Dashboard modules
- Focus on functional specifications rather than technical implementation
- Include specific metrics and KPI definitions
- Specify visualization types and data presentation requirements
```

---

## **REPORT MODULE PROMPT EXAMPLE**

```
Create a BBP for [REPORT_MODULE_PATH] using the BBP_Template_Reference.md as your guide.

Module Details:
- Module Name: [REPORT_NAME]
- Module Number: [X.Y]
- Module Type: Reports
- Target File: [REPORT_MODULE_PATH]

Context Requirements:
1. Read BBP_Template_Reference.md completely first
2. Use the simplified Reports template format (Purpose, Type, Functional Capture, UI/UX Spec)
3. Focus on data points, reporting requirements, and export capabilities
4. Keep technical details minimal, focus on functional specifications

Content Requirements:
1. Use simplified template:
   - Purpose
   - Type: Reports
   - Functional Capture
   - UI/UX Spec
2. Focus on data points and reporting needs
3. Include export capabilities (PDF, Excel, CSV formats)
4. Specify scheduling and automation requirements
5. Define report parameters and filter options
6. Include data retention and archiving policies

Output Format:
- Use simplified structure for Report modules
- Focus on functional specifications rather than technical implementation
- Include specific data fields and calculations
- Specify export formats and delivery methods
```

---

## **CONFIG/SETUP MODULE PROMPT EXAMPLE**

```
Create a BBP for [CONFIG_MODULE_PATH] using the BBP_Template_Reference.md as your guide.

Module Details:
- Module Name: [CONFIG_NAME]
- Module Number: [X.Y]
- Module Type: Config/Rule/Setup
- Target File: [CONFIG_MODULE_PATH]

Context Requirements:
1. Read BBP_Template_Reference.md completely first
2. Use the Config/Setup template format (Purpose, Type, Core Models, Business Rules, UI/UX Spec)
3. Focus on configuration logic and user experience
4. Include setup procedures and validation requirements

Content Requirements:
1. Use template with:
   - Purpose
   - Type: Config/Rule/Setup
   - Core Models (Django)
   - Business Rules/Validations
   - UI/UX Spec
2. Focus on configuration logic and user experience
3. Include setup procedures and validation requirements
4. Define configuration dependencies and impact analysis
5. Specify rollback and recovery procedures
6. Include configuration testing and validation requirements

Output Format:
- Use Config/Setup structure for configuration modules
- Focus on configuration models and business rules
- Include setup procedures and user guidance
- Specify validation and testing requirements
```

---

## **GENERAL USAGE GUIDELINES**

### **Before Creating BBP:**
1. Always read BBP_Template_Reference.md first
2. Check existing target file for current content
3. Review module structure documentation
4. Identify similar modules for pattern reference

### **During BBP Creation:**
1. Follow the exact template structure for the module type
2. Include specific, actionable details in all sections
3. Use the design language standards from the template
4. Ensure technical specifications are implementable
5. Include comprehensive business rules and validations

### **Quality Assurance:**
1. All sections must be completed
2. Technical details must be accurate
3. UI/UX specifications must follow design standards
4. Business rules must be comprehensive
5. Integration points must be clearly defined

### **Module Type Specifics:**
- **Master (_M)/Transaction (_T):** Use complete template with all sections including Django models, business rules, APIs, security, testing, deployment
- **Dashboard (_D):** Use simplified template (Purpose, Type, Functional Capture, UI/UX Spec) - **NO technical sections**
- **Reports (_R):** Use simplified template (Purpose, Type, Functional Capture, UI/UX Spec) - **NO technical sections**
- **Config (_C)/Setup (_S)/Workflow (_W):** Use focused template (Purpose, Type, Core Models, Business Rules, UI/UX Spec)

### **Type-Based Template Selection:**
- **_M & _T Modules:** Full technical specification with Django models, APIs, security, testing, deployment
- **_D & _R Modules:** Functional specification only - focus on metrics, data points, visualization, exports
- **_C, _S, _W Modules:** Configuration-focused with models and business rules, simplified technical sections

---

**TEMPLATE VERSION:** 1.0
**LAST UPDATED:** December 29, 2025
**COMPATIBLE:** All BBP Template Reference versions
