# AUTORETRY PREVENTION GUIDE - Universal File Update Protocol

**Agent**: Hindra (HRM Domain Owner)  
**Date**: January 30, 2026  
**Purpose**: Prevent autoretry, cutoff, and file loss issues for ANY file update (source code, documentation, BBPs, etc.)

---

## 1. CORE PRINCIPLE

**NEVER regenerate from beginning when context is lost or content gets cut off.**

Always continue from the exact stopping point where the previous operation ended.

---

## 2. EMERGENCY RECOVERY INSTRUCTIONS

### When Context is Lost or Content Gets Cut Off:

1. **STOP IMMEDIATELY** - Do not continue or regenerate from beginning
2. **USE THIS RECOVERY PROMPT:**

```
EMERGENCY: Context lost during file update for [TARGET_FILE_PATH]

Current status: [DESCRIBE WHAT WAS BEING DONE]
Last completed section: [LAST_SECTION_COMPLETED]
Next section to update: [NEXT_SECTION_NUMBER]

RECOVERY ACTIONS:
1. Read target file to see current content
2. Identify exact stopping point
3. Continue from exact stopping point
4. Write ONLY the next section/update
5. End with STOP MARKER if applicable
6. WAIT for next instruction before continuing
```

---

## 3. CONTENT LENGTH MANAGEMENT

### For Large File Updates:

**Maximum 120 lines per response** to prevent cutting

**Strategies:**
- **Write one section at a time** - never multiple sections
- **Use STOP MARKERS** after each section: `--- END OF SECTION [SECTION_NAME] ---`
- **If section exceeds 120 lines**, split into subsections with proper numbering
- **Use chunking** for very large files (read, process, write in chunks)

### For Source Code Files:

**Maximum 100 lines per response** to prevent cutting

**Strategies:**
- **Write one function/class at a time**
- **Use clear section markers**: `// --- FUNCTION: [FUNCTION_NAME] ---`
- **If function exceeds 100 lines**, split into logical parts
- **Test after each chunk** to ensure code compiles

### For Documentation Files:

**Maximum 150 lines per response** to prevent cutting

**Strategies:**
- **Write one section at a time**
- **Use markdown headers** to mark sections: `## [SECTION_NAME]`
- **If section exceeds 150 lines**, split into subsections
- **Use STOP MARKERS**: `--- END OF SECTION [SECTION_NAME] ---`

---

## 4. CONTEXT PRESERVATION RULES

### NEVER DO:

- **NEVER auto-retry** or restart from beginning
- **NEVER regenerate completed sections**
- **NEVER assume content was written correctly**
- **NEVER skip verification steps**

### ALWAYS DO:

- **ALWAYS continue from exact stopping point**
- **ALWAYS MAINTAIN state** across multiple responses
- **ALWAYS VERIFY existing content** before adding new content
- **ALWAYS read target file** before making changes

---

## 5. SECTION COMPLETION CHECKLIST

### Before Writing Each Section/Update:

- [ ] Target file content has been read
- [ ] Exact stopping point has been identified
- [ ] Section/update number is sequential
- [ ] Line limit will be respected (120/100/150 based on file type)
- [ ] STOP MARKER format is correct (if applicable)
- [ ] No auto-retry will occur
- [ ] Recovery protocol is ready if needed

---

## 6. ERROR RECOVERY PROTOCOL

### If You Detect Context Loss or Interruption:

1. **STOP writing immediately**
2. **Announce the issue**: "Context lost - using recovery protocol"
3. **Read the target file** to see current state
4. **Identify exact stopping point**
5. **Use the emergency recovery prompt**
6. **Wait for confirmation** before continuing

### If Content Gets Cut Off Mid-Response:

1. **STOP immediately**
2. **Read the target file** to see what was written
3. **Identify where content was cut off**
4. **Continue from exact cutoff point**
5. **Complete the section/update**
6. **Verify file integrity**

---

## 7. FILE-SPECIFIC STRATEGIES

### 7.1 Source Code Files (.py, .ts, .tsx, .js, .jsx)

**Strategy: Function-by-Function**

```
Step 1: Read file to see current state
Step 2: Identify next function to write/update
Step 3: Write one function (max 100 lines)
Step 4: Use marker: // --- FUNCTION: [FUNCTION_NAME] ---
Step 5: Verify syntax (if possible)
Step 6: Wait for confirmation
Step 7: Repeat for next function
```

**Example:**

```python
# --- FUNCTION: calculate_payroll ---
def calculate_payroll(employee_id, pay_period):
    """
    Calculate payroll for an employee for a given pay period.
    
    Args:
        employee_id: UUID of the employee
        pay_period: Pay period identifier
        
    Returns:
        dict: Payroll calculation results
    """
    # Implementation here (max 100 lines)
    pass
# --- END OF FUNCTION: calculate_payroll ---
```

### 7.2 Documentation Files (.md)

**Strategy: Section-by-Section**

```
Step 1: Read file to see current state
Step 2: Identify next section to write
Step 3: Write one section (max 150 lines)
Step 4: Use marker: --- END OF SECTION [SECTION_NAME] ---
Step 5: Verify markdown formatting
Step 6: Wait for confirmation
Step 7: Repeat for next section
```

**Example:**

```markdown
## 2. BACKEND STRUCTURE

### 2.1 Unified Backend (backend/)

**Core Components:**
- `manage.py` - Single Django management entry point
- `erp_core/` - Core platform configuration and settings
- `domain/` - Shared domain models (Company, User, etc.)

--- END OF SECTION 2.1 ---
```

### 7.3 Business Blueprint Files (.md)

**Strategy: BBP Section-by-Section**

```
Step 1: Read BBP_Template_Reference.md for structure
Step 2: Read target file to see current content
Step 3: Identify next BBP section (e.g., 02.1.3)
Step 4: Write one BBP section (max 120 lines)
Step 5: Use marker: --- END OF SECTION [SECTION_NUMBER] ---
Step 6: Verify BBP structure compliance
Step 7: Wait for confirmation
Step 8: Repeat for next section
```

**Example:**

```markdown
### 02.1.3 Core Models (Django)

**Employee Model:**

```python
class Employee(models.Model):
    employee_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # ... more fields
```

--- END OF SECTION 02.1.3 ---
```

### 7.4 Configuration Files (.json, .yaml, .xml)

**Strategy: Object-by-Object**

```
Step 1: Read file to see current state
Step 2: Identify next object to write/update
Step 3: Write one object (max 80 lines)
Step 4: Use marker: # --- OBJECT: [OBJECT_NAME] ---
Step 5: Verify syntax (if possible)
Step 6: Wait for confirmation
Step 7: Repeat for next object
```

**Example:**

```json
{
  "employee_records": {
    "menu_id": "EMPLOYEE_RECORDS",
    "menu_name": "Employee Records",
    "toolbar_list": "NRQFVIOX",
    "toolbar_view": "X",
    "toolbar_edit": "SCX",
    "toolbar_create": "SCX"
  }
}
# --- END OF OBJECT: employee_records ---
```

### 7.5 Large Text Files (.txt, .log)

**Strategy: Chunk-by-Chunk**

```
Step 1: Read file to see current state
Step 2: Determine chunk size (max 200 lines)
Step 3: Write one chunk
Step 4: Use marker: --- CHUNK [CHUNK_NUMBER] ---
Step 5: Verify content integrity
Step 6: Wait for confirmation
Step 7: Repeat for next chunk
```

---

## 8. VERIFICATION PROTOCOLS

### After Each Write Operation:

1. **Read the file** to verify content was written correctly
2. **Check for truncation** - ensure no content was cut off
3. **Verify syntax** - if applicable (code, JSON, YAML, etc.)
4. **Check formatting** - ensure proper indentation, spacing, etc.
5. **Verify completeness** - ensure all intended content is present

### Before Moving to Next Section:

1. **Confirm previous section** is complete and correct
2. **Get user confirmation** to proceed
3. **Update progress tracker** if applicable
4. **Prepare next section** based on current state

---

## 9. PROGRESS TRACKING

### Maintain Progress State:

**For Multi-Section Files:**

```
## Progress Tracker

- [x] Section 1: Introduction
- [x] Section 2: Architecture
- [ ] Section 3: Backend Structure (CURRENT)
- [ ] Section 4: Frontend Structure
- [ ] Section 5: Integration
```

**For Multi-Function Files:**

```
## Progress Tracker

- [x] Function: calculate_payroll
- [x] Function: process_timesheets
- [ ] Function: generate_payslip (CURRENT)
- [ ] Function: send_notifications
```

---

## 10. BEST PRACTICES

### Before Starting File Update:

1. **Read the entire file** to understand current state
2. **Identify exact scope** of changes needed
3. **Plan the update strategy** (section-by-section, function-by-function, etc.)
4. **Estimate line count** for each section/update
5. **Prepare recovery protocol** in case of issues

### During File Update:

1. **Write one section at a time**
2. **Use clear markers** to identify sections
3. **Respect line limits** (120/100/150 based on file type)
4. **Verify after each write**
5. **Wait for confirmation** before proceeding

### After File Update:

1. **Read the entire file** to verify completeness
2. **Check for errors** (syntax, formatting, etc.)
3. **Test functionality** (if applicable)
4. **Update progress tracker**
5. **Document changes** (if applicable)

---

## 11. COMMON SCENARIOS

### Scenario 1: Creating a New File

```
Step 1: Create file with initial structure
Step 2: Write first section (max line limit)
Step 3: Use STOP MARKER
Step 4: Wait for confirmation
Step 5: Continue with next section
```

### Scenario 2: Updating an Existing File

```
Step 1: Read file to see current state
Step 2: Identify section to update
Step 3: Read section to understand context
Step 4: Update section (max line limit)
Step 5: Use STOP MARKER
Step 6: Wait for confirmation
Step 7: Continue with next section
```

### Scenario 3: Appending to a File

```
Step 1: Read file to see current state
Step 2: Identify where to append
Step 3: Write new content (max line limit)
Step 4: Use STOP MARKER
Step 5: Wait for confirmation
Step 6: Continue if more content to add
```

### Scenario 4: Replacing Content in a File

```
Step 1: Read file to see current state
Step 2: Identify content to replace
Step 3: Use replace_in_file tool with SEARCH/REPLACE blocks
Step 4: Verify replacement was successful
Step 5: Wait for confirmation
Step 6: Continue with next replacement
```

---

## 12. TOOL-SPECIFIC GUIDELINES

### Using write_to_file:

- **Use for creating new files** or **completely overwriting existing files**
- **Provide COMPLETE content** - no truncation
- **Respect line limits** (120/100/150 based on file type)
- **Use STOP MARKERS** for multi-section files

### Using replace_in_file:

- **Use for targeted edits** to specific parts of a file
- **Use SEARCH/REPLACE blocks** for exact matches
- **Include complete lines** in SEARCH blocks
- **Use multiple SEARCH/REPLACE blocks** for multiple changes
- **List blocks in order** they appear in the file

### Using read_file:

- **Always read file before making changes**
- **Understand current state** before updating
- **Identify exact stopping point** if continuing
- **Verify content** after write operations

---

## 13. ERROR HANDLING

### If File Write Fails:

1. **Check error message** for details
2. **Verify file path** is correct
3. **Check file permissions**
4. **Verify content format** is correct
5. **Retry with smaller chunk** if content is too large

### If Content Gets Truncated:

1. **Read file** to see what was written
2. **Identify truncation point**
3. **Continue from truncation point**
4. **Complete the section/update**
5. **Verify file integrity**

### If Syntax Errors Occur:

1. **Read file** to identify error location
2. **Fix syntax error**
3. **Verify fix** (if possible)
4. **Continue with next section**
5. **Test functionality** (if applicable)

---

## 14. QUALITY ASSURANCE

### Before Marking File Complete:

- [ ] All sections written
- [ ] No truncation detected
- [ ] Syntax verified (if applicable)
- [ ] Formatting correct
- [ ] Content complete
- [ ] File tested (if applicable)

### Final Verification:

1. **Read entire file** to verify completeness
2. **Check for errors** (syntax, formatting, etc.)
3. **Verify all sections** are present
4. **Test functionality** (if applicable)
5. **Get user confirmation** that file is complete

---

## 15. COMMUNICATION PROTOCOL

### When Starting File Update:

```
Starting file update: [TARGET_FILE_PATH]
Strategy: [SECTION-BY-SECTION / FUNCTION-BY-FUNCTION / CHUNK-BY-CHUNK]
Estimated sections: [NUMBER]
Line limit: [120 / 100 / 150]
```

### After Each Section:

```
Section [SECTION_NAME] completed.
Lines written: [NUMBER]
Status: [COMPLETE / NEEDS VERIFICATION]
Next section: [NEXT_SECTION_NAME]
```

### When File is Complete:

```
File update complete: [TARGET_FILE_PATH]
Total sections: [NUMBER]
Total lines: [NUMBER]
Status: [COMPLETE / NEEDS TESTING]
```

---

## 16. FINAL LOCK

### Non-Negotiable Rules:

- **NEVER regenerate from beginning** when context is lost
- **ALWAYS continue from exact stopping point**
- **ALWAYS verify content** after each write operation
- **ALWAYS respect line limits** (120/100/150 based on file type)
- **ALWAYS use STOP MARKERS** for multi-section files
- **ALWAYS wait for confirmation** before proceeding

### Governance Breach:

Any violation of these rules = **Governance Breach**

---

**END OF AUTORETRY PREVENTION GUIDE**

**Version**: 1.0  
**Last Updated**: January 30, 2026  
**Applies To**: All file updates (source code, documentation, BBPs, configuration files, etc.)
