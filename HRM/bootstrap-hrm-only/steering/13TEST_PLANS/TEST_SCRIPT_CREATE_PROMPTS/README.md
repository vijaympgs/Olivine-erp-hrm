# Test Script Prompt Library

## 📋 Overview

This directory contains **comprehensive, expert-crafted test script prompts** for all procurement module components. These prompts are designed to be used by AI agents to generate high-quality, BBP-compliant test scripts.

---

## 🎯 Purpose

**Problem Solved**: 
- Eliminates dependency on AI conversation memory
- Survives model switches and session changes
- Provides consistent, high-quality test script generation
- Version-controlled and easily maintainable

---

## 📁 Directory Structure

```
TEST_SCRIPT_CREATE_PROMPTS/
├── Core Procurement (BBP 4.x)
│   ├── 4.1_Purchase_Requisition_test_script_prompt.md (10 test cases)
│   ├── 4.2_Request_for_Quotation_test_script_prompt.md (21 test cases)
│   ├── 4.3_Purchase_Order_test_script_prompt.md (12 test cases)
│   ├── 4.5_Advance_Shipment_Notice_test_script_prompt.md (18 test cases)
│   ├── 4.6_Goods_Receipts_test_script_prompt.md (14 test cases)
│   ├── 4.7_Invoice_Matching_test_script_prompt.md (18 test cases)
│   └── 4.8_Purchase_Returns_test_script_prompt.md (20 test cases)
│
├── Supporting Components
│   ├── Vendors_Master_Data_test_script_prompt.md (18 test cases)
│   ├── Payments_Processing_test_script_prompt.md (20 test cases)
│   ├── Compliance_Management_test_script_prompt.md (20 test cases)
│   └── Configuration_Management_test_script_prompt.md (20 test cases)
│
├── Documentation
│   ├── TEST_EXECUTION_HISTORY.md (Test progress tracking)
│   ├── DEFECT_RESOLUTION_LOG.md (Defect tracking)
│   └── PROMPT_LIBRARY_MAP.py (Component → Prompt mapping)
│
└── README.md (This file)
```

**Total**: 191 test cases across 11 components

---

## 🚀 How to Use

### **Method 1: Via Test Console UI (Recommended)**

1. Open Test Console (`/test-console`)
2. Select a component (e.g., "Purchase Orders")
3. Click **"GEN PROMPT"** button
4. System loads the corresponding detailed prompt
5. Copy prompt and paste to AI agent
6. AI generates the test script

### **Method 2: Direct File Access**

1. Navigate to this directory
2. Open the relevant `.md` file (e.g., `4.3_Purchase_Order_test_script_prompt.md`)
3. Copy entire content
4. Paste to AI agent for test script generation

### **Method 3: Programmatic Access**

```python
from PROMPT_LIBRARY_MAP import PROMPT_LIBRARY, PROMPT_BASE_PATH
import os

# Get prompt for a component
component_id = "purchase-orders"
prompt_file = PROMPT_LIBRARY.get(component_id)

if prompt_file:
    full_path = os.path.join(PROMPT_BASE_PATH, prompt_file)
    with open(full_path, 'r') as f:
        prompt_content = f.read()
    # Use prompt_content with AI agent
```

---

## 📝 Prompt Structure (Standardized)

Each prompt file follows this structure:

```markdown
# [Component Name] — Test Script Prompt

## OBJECTIVE
[Clear statement of what's being tested]

## GLOBAL EXECUTION RULES (MANDATORY)
1. ❌ NO mock data
2. ❌ NO factories, fixtures, or fake generators
3. ✅ USE ONLY existing reference masters from DB
[... 8 rules total ...]

## TEST SCRIPT STRUCTURE
[Python imports and boilerplate]

## BASE TEST SETUP (SHARED CONTEXT)
[setUpTestData with real master data queries]

## TEST CASES
[Detailed test cases with acceptance criteria]

## AGENT EXECUTION INSTRUCTION (LOCKED)
[Specific instructions for AI agent]
```

---

## ✅ Benefits of This System

| Benefit | Description |
|---------|-------------|
| **Session Independent** | Works regardless of AI conversation history |
| **Model Agnostic** | Same prompts work with any AI model |
| **Version Controlled** | All prompts tracked in git |
| **Easy Maintenance** | Update .md files, no code changes needed |
| **Consistent Quality** | Expert-crafted, standardized prompts |
| **Reusable** | Same prompt can generate scripts multiple times |
| **Documented** | Self-documenting with clear instructions |

---

## 🔄 Workflow Example

**Scenario**: Generate test script for Purchase Orders

```
1. User opens Test Console
2. Selects "Purchase Orders" component
3. Clicks "GEN PROMPT"
   ↓
4. System checks PROMPT_LIBRARY_MAP.py
   → Finds: "purchase-orders" → "4.3_Purchase_Order_test_script_prompt.md"
   ↓
5. System loads file content
   ↓
6. Displays in modal with:
   - Full prompt text (12 test cases: PO-TS-01 to PO-TS-12)
   - Copy button
   - File path reference
   ↓
7. User copies prompt
8. Pastes to AI agent (Claude, ChatGPT, etc.)
9. AI generates: backend/domain/procurement/po/tests/test_4_3_purchase_order.py
10. User runs tests: python manage.py test procurement.po.tests
```

---

## 🛠️ Maintenance

### **Adding a New Prompt:**

1. Create new `.md` file following the standard structure
2. Add entry to `PROMPT_LIBRARY_MAP.py`
3. Commit to git

### **Updating an Existing Prompt:**

1. Edit the `.md` file directly
2. Commit changes to git
3. No code changes needed!

### **Removing a Prompt:**

1. Delete `.md` file
2. Remove entry from `PROMPT_LIBRARY_MAP.py`
3. Commit to git

---

## 📊 Coverage Summary

| BBP | Component | Test Cases | Status |
|-----|-----------|------------|--------|
| 4.1 | Purchase Requisition | 10 | ✅ Complete |
| 4.2 | Request for Quotation | 21 | ✅ Complete |
| 4.3 | Purchase Order | 12 | ✅ Complete |
| 4.5 | Advance Shipment Notice | 18 | ✅ Complete |
| 4.6 | Goods Receipts | 14 | ✅ Complete |
| 4.7 | Invoice Matching | 18 | ✅ Complete |
| 4.8 | Purchase Returns | 20 | ✅ Complete |
| - | Vendors (Master Data) | 18 | ✅ Complete |
| - | Payments | 20 | ✅ Complete |
| - | Compliance | 20 | ✅ Complete |
| - | Configuration | 20 | ✅ Complete |

**Total**: 191 test cases ready for generation

---

## 🎓 Best Practices

1. **Always use the detailed prompts** - Don't create ad-hoc prompts
2. **Update prompts when BBP changes** - Keep in sync with business requirements
3. **Version control all changes** - Track prompt evolution
4. **Test generated scripts** - Verify AI output matches expectations
5. **Document defects** - Use DEFECT_RESOLUTION_LOG.md

---

## 📞 Support

For questions or issues:
1. Check this README
2. Review PROMPT_LIBRARY_MAP.py for component mappings
3. Consult TEST_EXECUTION_HISTORY.md for test progress
4. Check DEFECT_RESOLUTION_LOG.md for known issues

---

**Last Updated**: 2025-12-27  
**Maintained By**: Development Team  
**Version**: 1.0
