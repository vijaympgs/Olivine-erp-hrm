# CRM BBP Creation Prompt Template

## **Standard BBP Creation Prompt**

Use this template to create Business Blueprints for any module. Replace the bracketed values with your specific module details.

---

## **BASE PROMPT TEMPLATE**

```
Refer CRM_Template_Prompt.md and create a BBP for [TARGET_FILE_PATH] using the CRM_Template_Reference.md as your comprehensive guide.

The agent should automatically derive:
- Module Number: [X.Y] from the file path (e.g., CRM\02.Lead & Contact Management\2.1 Lead Capture & Scoring (Master).md = 2.1)
- Module Name: [MODULE_NAME] from the file name (e.g., 2.1 Lead Capture & Scoring (Master).md = Lead Capture & Scoring)
- Module Type: [Master/Transaction/Dashboard/Reports/Config/Rule/Setup] based on the module functionality
- Complexity: [Simple/Medium] based on functionality complexity
- Template Type: [Complete/Simplified/Focused] based on module type

Module Details:
- Module Name: [MODULE_NAME] (derived from file name)
- Module Number: [X.Y] (derived from file path)
- Module Type: [Master/Transaction/Dashboard/Reports/Config/Rule/Setup]
- Complexity: [Simple/Medium] based on functionality
- Template Type: [Complete/Simplified/Focused] based on module type
- Target File: [TARGET_FILE_PATH]

Context Requirements:
1. Read CRM_Template_Reference.md completely first for the complete structure and design language standards
2. Read CRM_BBP_Autoretry_Prevention_Guide.md for autoretry and cutoff prevention rules
3. Read the existing target file (if exists) to understand current content
4. Review CRM module structure for module context and numbering
5. Reference similar modules for consistency patterns
6. Confirm template type based on module complexity and requirements

Content Requirements:
1. Use the [TEMPLATE_TYPE] template format from CRM_Template_Reference.md
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
- Follow the exact structure from CRM_Template_Reference.md for [TEMPLATE_TYPE] template
- Fill in all sections with detailed, actionable specifications
- Include code examples where appropriate
- Ensure content is suitable for direct UI development implementation
- Maintain consistency with existing CRM module BBP patterns

Quality Standards:
- All sections must be completed with specific, actionable details
- Technical specifications must be implementable
- UI/UX specifications must follow the design language standards
- Business rules must be clear and comprehensive
- Integration points must be clearly defined with API specifications
- Security requirements must address data privacy and compliance needs
- Content must be appropriate for [TEMPLATE_TYPE] template complexity level

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
Template type: [COMPLETE/SIMPLIFIED/FOCUSED]
Module complexity: [SIMPLE/MEDIUM]

RECOVERY ACTIONS:
1. Read CRM_Template_Reference.md for context
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
- **ALWAYS continue from exact stopping point
- **MAINTAIN state** across multiple responses
- **VERIFY existing content** before adding new content
- **PRESERVE template type and complexity context**

### **SECTION COMPLETION CHECKLIST**
Before writing each section, verify:
- [ ] CRM_Template_Reference.md has been read
- [ ] Target file content has been read
- [ ] Module numbering is correct (X.Y pattern)
- [ ] Section number is sequential
- [ ] 120-line limit will be respected
- [ ] STOP MARKER format is correct
- [ ] No auto-retry will occur
- [ ] Template type is appropriate for module type
- [ ] Complexity level is correctly assessed

### **ERROR RECOVERY PROTOCOL**
If you detect context loss or interruption:
1. **STOP writing immediately**
2. **Announce the issue**: "Context lost - using recovery protocol"
3. **Use the emergency recovery prompt**
4. **Wait for confirmation** before continuing

### **TEMPLATE TYPE SELECTION GUIDELINES**
- **Complete Template (16 Sections):** Use for Master/Transaction modules
- **Simplified Template (4 Sections):** Use for Dashboard/Report modules
- **Focused Template (6 Sections):** Use for Configuration/Setup modules

---

## **MODULE-SPECIFIC PROMPT TEMPLATES**

### **For Master Modules (Complete Template):**
```
Refer CRM_Template_Prompt.md and create a BBP for [TARGET_FILE_PATH] using the CRM_Template_Reference.md as your comprehensive guide.

Module Details:
- Module Name: [MODULE_NAME] (derived from file name)
- Module Number: [X.Y] (derived from file path)
- Module Type: Master
- Complexity: [Simple/Medium] based on functionality
- Template: Complete (16 sections)

Context Requirements:
1. Read CRM_Template_Reference.md completely first for the complete structure and design language standards
2. Read CRM_BBP_Autoretry_Prevention_Guide.md for autoretry and cutoff prevention rules
3. Read the existing target file (if exists) to understand current content
4. Review CRM module structure for module context and numbering
5. Reference similar modules for consistency patterns

Content Requirements:
1. Use the complete Master template format from CRM_Template_Reference.md
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
- Follow the exact structure from CRM_Template_Reference.md
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
```

### **For Transaction Modules (Complete Template):**
```
Refer CRM_Template_Prompt.md and create a BBP for [TARGET_FILE_PATH] using the CRM_Template_Reference.md as your comprehensive guide.

Module Details:
- Module Name: [MODULE_NAME] (derived from file name)
- Module Number: [X.Y] (derived from file path)
- Module Type: Transaction
- Complexity: [Simple/Complex] based on workflow complexity
- Template: Complete (16 sections)

Context Requirements:
1. Read CRM_Template_Reference.md completely first for the complete structure and design language standards
2. Read CRM_BBP_Autoretry_Prevention_Guide.md for autoretry and cutoff prevention rules
3. Read the existing target file (if exists) to understand current content
4. Review CRM module structure for module context and numbering
5. Reference similar modules for consistency patterns

Content Requirements:
1. Use the complete Transaction template format from CRM_Template_Reference.md
2. Focus on transaction processing including:
   - [TRANSACTION_FEATURE_1]
   - [TRANSACTION_FEATURE_2]
   - [TRANSACTION_FEATURE_3]
   - [TRANSACTION_FEATURE_4]
3. Include Django models with proper relationships, indexes, and constraints
4. Define comprehensive business rules for transaction validation and workflow
5. Specify detailed UI/UX requirements following the design language standards from the template
6. Include complete design system specifications (typography, colors, spacing, components)
7. Add security requirements for transaction data and access control
8. Define integration points with related CRM modules
9. Include API specifications for transaction operations
10. Specify testing requirements and deployment procedures

Technical Requirements:
- Follow Django naming conventions and best practices
- Include company_id for multi-tenant support
- Add audit fields (created_by_user_id, created_at, updated_at)
- Define proper indexing strategy for transaction performance
- Include comprehensive error handling and validation
- Specify responsive design requirements
- Include accessibility standards (WCAG compliance)

Output Format:
- Follow the exact structure from CRM_Template_Reference.md
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
```

### **For Dashboard Modules (Simplified Template):**
```
Refer CRM_Template_Prompt.md and create a BBP for [TARGET_FILE_PATH] using the CRM_Template_Reference.md as your comprehensive guide.

Module Details:
- Module Name: [MODULE_NAME] (derived from file name)
- Module Number: [X.Y] (derived from file path)
- Module Type: Dashboard
- Complexity: Simple
- Template: Simplified (4 sections)

Context Requirements:
1. Read CRM_Template_Reference.md completely first for the simplified dashboard template structure
2. Read CRM_BBP_Autoretry_Prevention_Guide.md for autoretry and cutoff prevention rules
3. Read the existing target file (if exists) to understand current content
4. Review CRM module structure for module context and numbering
5. Reference similar dashboard modules for consistency patterns

Content Requirements:
1. Use the simplified Dashboard template format:
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

Quality Standards:
- All sections must be completed with specific, actionable details
- Metrics and KPIs must be clearly defined
- UI/UX specifications must follow design language standards
- Data visualization requirements must be comprehensive
```

### **For Report Modules (Simplified Template):**
```
Refer CRM_Template_Prompt.md and create a BBP for [TARGET_FILE_PATH] using the CRM_Template_Reference.md as your comprehensive guide.

Module Details:
- Module Name: [MODULE_NAME] (derived from file name)
- Module Number: [X.Y] (derived from file path)
- Module Type: Reports
- Complexity: Simple
- Template: Simplified (4 sections)

Context Requirements:
1. Read CRM_Template_Reference.md completely first for the simplified report template structure
2. Read CRM_BBP_Autoretry_Prevention_Guide.md for autoretry and cutoff prevention rules
3. Read the existing target file (if exists) to understand current content
4. Review CRM module structure for module context and numbering
5. Reference similar report modules for consistency patterns

Content Requirements:
1. Use the simplified Reports template format:
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

Quality Standards:
- All sections must be completed with specific, actionable details
- Data points and calculations must be clearly defined
- UI/UX specifications must follow design language standards
- Export requirements must be comprehensive
```

### **For Configuration Modules (Focused Template):**
```
Refer CRM_Template_Prompt.md and create a BBP for [TARGET_FILE_PATH] using the CRM_Template_Reference.md as your comprehensive guide.

Module Details:
- Module Name: [MODULE_NAME] (derived from file name)
- Module Number: [X.Y] (derived from file path)
- Module Type: Config/Rule/Setup
- Complexity: Simple/Medium
- Template: Focused (6 sections)

Context Requirements:
1. Read CRM_Template_Reference.md completely first for the focused configuration template structure
2. Read CRM_BBP_Autoretry_Prevention_Guide.md for autoretry and cutoff prevention rules
3. Read the existing target file (if exists) to understand current content
4. Review CRM module structure for module context and numbering
5. Reference similar configuration modules for consistency patterns

Content Requirements:
1. Use template with:
   - Purpose
   - Type: Config/Rule/Setup
   - Core Models (Django)
   - Business Rules/Validations
   - UI/UX Spec
   - Sections 8-16: Not Applicable
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

Quality Standards:
- All sections must be completed with specific, actionable details
- Technical specifications must be implementable
- UI/UX specifications must follow design language standards
- Business rules must be comprehensive and clear
- Setup procedures must be user-friendly
```

---

## **EXAMPLE: LEAD CAPTURE & SCORING BBP PROMPT**

```
Create a BBP for CRM\02.Lead & Contact Management\2.1 Lead Capture & Scoring (Master).md using the CRM_Template_Reference.md as your comprehensive guide.

Module Details:
- Module Name: Lead Capture & Scoring
- Module Number: 2.1
- Module Type: Master
- Complexity: Medium
- Template Type: Complete (16 sections)
- Target File: CRM\02.Lead & Contact Management\2.1 Lead Capture & Scoring (Master).md

Context Requirements:
1. Read CRM_Template_Reference.md completely first for the complete structure and design language standards
2. Read CRM_BBP_Autoretry_Prevention_Guide.md for autoretry and cutoff prevention rules
3. Read the existing target file to understand current content
4. Review CRM module structure for module context and numbering
5. Reference similar modules like 2.2 Contact Directory for consistency patterns

Content Requirements:
1. Use the complete Master template format from CRM_Template_Reference.md
2. Focus on lead management including:
   - Lead capture from multiple sources (web forms, email, social media, imports)
   - Lead scoring models and qualification criteria
   - Lead segmentation and categorization
   - Lead status management and lifecycle tracking
   - Lead assignment and routing rules
3. Include Django models with proper relationships, indexes, and constraints
4. Define comprehensive business rules for lead validation, duplicate detection, and data quality
5. Specify detailed UI/UX requirements following the design language standards from the template
6. Include complete design system specifications (typography, colors, spacing, components)
7. Add security requirements for lead data privacy, role-based access, and compliance (GDPR)
8. Define integration points with marketing automation, email systems, and CRM modules
9. Include API specifications for CRUD operations, lead scoring, and data synchronization
10. Specify testing requirements and deployment procedures

Technical Requirements:
- Follow Django naming conventions and best practices
- Include company_id for multi-tenant support
- Add audit fields (created_by_user_id, created_at, updated_at)
- Define proper indexing strategy for performance on frequently queried fields
- Include comprehensive error handling and validation for lead data
- Specify responsive design requirements for mobile and desktop access
- Include accessibility standards (WCAG 2.1 AA compliance)

Output Format:
- Follow the exact structure from CRM_Template_Reference.md
- Fill in all sections with detailed, actionable specifications
- Include Django model code examples with proper field definitions
- Ensure content is suitable for direct UI development implementation
- Maintain consistency with existing CRM module BBP patterns

Quality Standards:
- All sections must be completed with specific, actionable details
- Technical specifications must be implementable by development team
- UI/UX specifications must follow the design language standards exactly
- Business rules must be clear and comprehensive for lead management governance
- Integration points must be clearly defined with complete API specifications
- Security requirements must address lead data privacy and compliance needs
```

---

## **GENERAL USAGE GUIDELINES**

### **Before Creating BBP:**
1. Always read CRM_Template_Reference.md first
2. Check existing target file for current content
3. Review module structure documentation
4. Identify similar modules for pattern reference
5. Confirm module type and complexity level
6. Select appropriate template type

### **During BBP Creation:**
1. Follow the exact template structure for the module type
2. Include specific, actionable details in all sections
3. Use the design language standards from the template
4. Ensure technical specifications are implementable
5. Include comprehensive business rules and validations
6. Maintain consistency with existing BBP patterns

### **Quality Assurance:**
1. All sections must be completed
2. Technical details must be accurate
3. UI/UX specifications must follow design standards
4. Business rules must be comprehensive
5. Integration points must be clearly defined
6. Security requirements must be addressed

### **Module Type Specifics:**
- **Master/Transaction:** Use complete template with all sections (16 sections)
- **Dashboard:** Use simplified template (4 sections: Purpose, Type, Functional Capture, UI/UX Spec)
- **Reports:** Use simplified template (4 sections: Purpose, Type, Functional Capture, UI/UX Spec)
- **Config/Setup:** Use focused template (6 sections: Purpose, Type, Core Models, Business Rules, UI/UX Spec, Sections 8-16: Not Applicable)

### **Complexity Level Guidelines:**
- **Simple:** Basic data management, straightforward workflows
- **Medium:** Complex relationships, advanced business rules, multiple integrations
- **Complex:** Highly complex workflows, extensive integrations, advanced business logic

---

## **TEMPLATE TYPE SELECTION MATRIX**

| Module Type | Template Type | Sections | Complexity | Use Case |
|-------------|--------------|---------|------------|----------|
| Master | Complete | 16 sections | Simple/Medium | Data management, reference data |
| Transaction | Complete | 16 sections | Simple/Complex | Business processes, workflows |
| Dashboard | Simplified | 4 sections | Simple | Analytics, visualization |
| Reports | Simplified | 4 sections | Simple | Data reporting, exports |
| Configuration | Focused | 6 sections | Simple/Medium | System setup, configuration |

---

## **MODULE COMPLEXITY ASSESSMENT**

### **Simple (S)**
- Basic data management with standard CRUD operations
- Straightforward business rules and validations
- Limited integration requirements
- Simple user workflows
- Basic security requirements

### **Medium (M)**
- Complex relationships and data models
- Advanced business rules and validation logic
- Multiple integration points
- Multi-step workflows
- Enhanced security and compliance requirements

### **Complex (C)**
- Highly complex data relationships
- Sophisticated business logic and workflows
- Extensive integration requirements
- Multi-system dependencies
- Advanced security and compliance needs

---

## **ENHANCED FEATURES (LEARNED FROM HRM/FMS)**

### **Template Type Awareness**
- Automatic template type selection based on module functionality
- Complexity assessment for appropriate template usage
- Consistent template application across similar modules

### **Context Preservation**
- Enhanced recovery protocols with template type tracking
- Improved context state management
- Better error detection and recovery

### **Quality Assurance**
- Pre-creation validation checklists
- Post-creation quality standards
- Template adherence verification
- Comprehensive error recovery procedures

---

**TEMPLATE VERSION:** 2.0  
**LAST UPDATED:** December 31, 2025  
**ENHANCEMENTS:** HRM/FMS implementation learnings, template type matrix, complexity assessment  
**COMPATIBLE:** All CRM BBP Template Reference versions
