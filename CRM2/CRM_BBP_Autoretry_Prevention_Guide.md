# CRM BBP Autoretry Prevention Guide

## __Preventive Lines for Autoretry, Cutoff, File Loss Issues:__

### __EMERGENCY RECOVERY INSTRUCTIONS__

- STOP IMMEDIATELY - Do not continue or regenerate from beginning
- USE THIS RECOVERY PROMPT: [recovery prompt template]
- Read CRM_Template_Reference.md for context
- Read target file to see current content
- Continue from exact stopping point
- Write ONLY the next section ([NEXT_SECTION_NUMBER])
- End with STOP MARKER: --- END OF SECTION [NEXT_SECTION_NUMBER] ---
- WAIT for next instruction before continuing

### __CONTENT LENGTH MANAGEMENT__

- Maximum 120 lines per response to prevent cutting
- Write one section at a time - never multiple sections
- Use STOP MARKERS after each section: `--- END OF SECTION X.Y.Z ---`
- If section exceeds 120 lines, split into subsections with proper numbering

### __CONTEXT PRESERVATION RULES__

- NEVER auto-retry or restart from beginning
- NEVER regenerate completed sections
- ALWAYS continue from exact stopping point
- MAINTAIN state across multiple responses
- VERIFY existing content before adding new content

### __SECTION COMPLETION CHECKLIST__

- CRM_Template_Reference.md has been read
- Target file content has been read
- Module numbering is correct (X.Y pattern)
- Section number is sequential
- 120-line limit will be respected
- STOP MARKER format is correct
- No auto-retry will occur

### __ERROR RECOVERY PROTOCOL__

- STOP writing immediately
- Announce the issue: "Context lost - using recovery protocol"
- Use the emergency recovery prompt
- Wait for confirmation before continuing

### __ENHANCED RECOVERY STRATEGIES (LEARNED FROM HRM/FMS)__

#### **Context State Management**
- Always maintain context of current module type (Master/Transaction/Dashboard/Reports/Config)
- Track current section number and subsection level
- Preserve template type being used (complete vs simplified)
- Remember any custom modifications or deviations from standard template

#### **Template Type Awareness**
- **Master/Transaction:** Use complete 16-section template
- **Dashboard:** Use simplified 4-section template (Purpose, Type, Functional Capture, UI/UX Spec)
- **Reports:** Use simplified 4-section template (Purpose, Type, Functional Capture, UI/UX Spec)
- **Configuration:** Use focused 6-section template (Purpose, Type, Core Models, Business Rules, UI/UX Spec, Sections 8-16: Not Applicable)

#### **Module Complexity Tracking**
- **MST-S:** Simple Master - Basic data management
- **MST-M:** Medium Master - Complex relationships and business rules
- **TXN-S:** Simple Transaction - Basic transaction processing
- **TXN-C:** Complex Transaction - Multi-step workflows and validations

#### **BBP Type Confirmation Process**
Before starting any BBP, confirm:
1. Module Number: X.Y (from file path)
2. Module Name: (from file name)
3. Module Type: (Master/Transaction/Dashboard/Reports/Config)
4. Complexity Level: (Simple/Medium based on functionality)
5. Template Type: (Complete/Simplified/Focused based on module type)

### __ADVANCED AUTORETRY PREVENTION__

#### **Pre-Writing Validation**
Before writing any section:
1. Verify CRM_Template_Reference.md has been read completely
2. Check target file exists and read current content
3. Confirm module type and template selection
4. Validate section numbering sequence
5. Ensure 120-line limit compliance
6. Verify STOP MARKER format

#### **Writing Process Controls**
- Write sections in sequential order only
- Never skip sections or jump ahead
- Use exact section numbering from template
- Include all required subsections
- Maintain consistent formatting and structure

#### **Content Quality Checks**
- Ensure all sections are completed with specific details
- Verify technical specifications are implementable
- Check UI/UX specifications follow design standards
- Validate business rules are comprehensive
- Confirm integration points are clearly defined

#### **Error Detection and Recovery**
- Monitor for context loss indicators
- Watch for cutoff warnings or incomplete responses
- Detect template structure deviations
- Identify missing or incomplete sections
- Recognize formatting inconsistencies

### __RECOVERY PROMPT TEMPLATES__

#### **Standard Recovery Prompt:**
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

#### **Template-Specific Recovery:**
```
EMERGENCY: Context lost during [TEMPLATE_TYPE] BBP creation
Module: [MODULE_NAME] ([MODULE_NUMBER]) - [MODULE_TYPE]
Template: [COMPLETE/SIMPLIFIED/FOCUSED] template
Last section: [LAST_SECTION_COMPLETED]
Next section: [NEXT_SECTION_NUMBER]

RECOVERY ACTIONS:
1. Read CRM_Template_Reference.md section for [TEMPLATE_TYPE] template
2. Read target file current content
3. Continue from exact stopping point using [TEMPLATE_TYPE] template
4. Write ONLY section [NEXT_SECTION_NUMBER]
5. End with STOP MARKER: --- END OF SECTION [NEXT_SECTION_NUMBER] ---
6. WAIT for confirmation
```

### __QUALITY ASSURANCE CHECKPOINTS__

#### **Before Starting BBP:**
- [ ] Module identification confirmed (X.Y, Name, Type)
- [ ] Template type selected correctly
- [ ] Complexity level assessed
- [ ] CRM_Template_Reference.md read completely
- [ ] Target file checked for existing content
- [ ] Recovery protocol understood

#### **During BBP Creation:**
- [ ] Writing one section at a time
- [ ] 120-line limit respected
- [ ] STOP MARKERS used correctly
- [ ] Section numbering sequential
- [ ] Template structure followed
- [ ] Content quality maintained

#### **After Each Section:**
- [ ] Section completed fully
- [ ] STOP MARKER properly formatted
- [ ] Context preserved for next section
- [ ] No auto-retry triggers present
- [ ] Ready for continuation instruction

### __TEMPLATE SELECTION GUIDELINES__

#### **Complete Template (16 Sections) - Use For:**
- Master modules (MST-S, MST-M)
- Transaction modules (TXN-S, TXN-C)
- Complex configuration modules
- Modules requiring full technical specification

#### **Simplified Template (4 Sections) - Use For:**
- Dashboard modules
- Report modules
- Simple analytics modules
- Visualization-focused modules

#### **Focused Template (6 Sections) - Use For:**
- Configuration modules
- Setup modules
- Rule-based modules
- Modules with emphasis on business rules over technical implementation

### __SUCCESS METRICS__

#### **Prevention Success Indicators:**
- Zero auto-retry occurrences
- No content cutoff incidents
- Complete section delivery
- Proper template usage
- Sequential section completion

#### **Quality Indicators:**
- All sections completed with specific details
- Technical specifications implementable
- UI/UX specifications follow design standards
- Business rules comprehensive and clear
- Integration points clearly defined

#### **Efficiency Metrics:**
- Minimal recovery prompt usage
- Fast context restoration
- Quick error detection and correction
- Smooth continuation process
- High first-time completion rate

---

**VERSION:** 2.0  
**LAST UPDATED:** December 31, 2025  
**LEARNINGS INTEGRATED:** HRM/FMS BBP Implementation Experience  
**COMPATIBLE:** All CRM BBP Template Reference versions
