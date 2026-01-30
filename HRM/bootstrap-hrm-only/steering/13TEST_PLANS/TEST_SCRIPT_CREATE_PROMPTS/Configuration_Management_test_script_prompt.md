# Configuration (Procurement System Configuration) — Test Script Prompt
File to be created by Agent:
**Configuration_Management_test_script.py**

---

## OBJECTIVE

Validate **end-to-end Procurement Configuration Management** behavior covering:
- Approval workflow configuration
- Tolerance and threshold settings
- Numbering sequence configuration
- Email notification templates
- System defaults and preferences
- Data integrity & Persistence
- Permission enforcement

This test suite must execute critical scenarios using **real reference master data only**.

---

## GLOBAL EXECUTION RULES (MANDATORY)

1. ❌ NO mock data
2. ❌ NO factories, fixtures, or fake generators
3. ✅ USE ONLY existing reference masters from DB:
   - Company
   - Location
   - Users / Roles
4. ❌ DO NOT auto-create master data inside tests
5. ✅ FAIL FAST if required master data is missing
6. ✅ Use Django ORM models only
7. ✅ Each test must be transactional and isolated
8. ✅ Follow BBP Configuration rules strictly

---

## TEST SCRIPT STRUCTURE

```python
# file: Configuration_Management_test_script.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal

# TODO: Import Configuration specific models and serializers
from procurement.models import (
    ProcurementConfig,
    ApprovalRule,
    ToleranceConfig,
    NumberingSequence,
    NotificationTemplate
)

from master.models import (
    Company, Location
)
```

---

## BASE TEST SETUP (SHARED CONTEXT)

```python
class ConfigurationManagementTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.filter(is_active=True).first()
        cls.location = Location.objects.filter(company=cls.company, is_active=True).first()
        cls.user = get_user_model().objects.filter(is_active=True).first()
        
        assert cls.company, "Missing active Company master"
        assert cls.location, "Missing active Location master"
        assert cls.user, "Missing active User"
```

---

## TEST CASES

> **Agent Instruction**:
> Based on BBP Configuration requirements for **Procurement System Configuration**:
> 
> **Core Test Cases to Implement:**
> 
> ### CFG-TS-01: Create Approval Rule
> - Define approval rule (amount-based)
> - Set approval threshold (e.g., >$10,000)
> - Assign approver role/user
> - Verify rule created
> 
> ### CFG-TS-02: Multi-Level Approval Configuration
> - Create Level 1 approval (Manager, <$10K)
> - Create Level 2 approval (Director, $10K-$50K)
> - Create Level 3 approval (VP, >$50K)
> - Verify approval chain
> 
> ### CFG-TS-03: Approval Rule Application
> - Create PR below threshold
> - Verify auto-approval (if configured)
> - Create PR above threshold
> - Verify approval required
> 
> ### CFG-TS-04: Tolerance Configuration - Price Variance
> - Set price tolerance (e.g., ±5%)
> - Create invoice with price within tolerance
> - Verify auto-approval
> - Create invoice with price outside tolerance
> - Verify approval required
> 
> ### CFG-TS-05: Tolerance Configuration - Quantity Variance
> - Set quantity tolerance (e.g., ±10%)
> - Create GRN with quantity within tolerance
> - Verify auto-approval
> - Create GRN with quantity outside tolerance
> - Verify approval required
> 
> ### CFG-TS-06: Numbering Sequence - PR
> - Configure PR numbering (e.g., PR-{YYYY}-{####})
> - Create PR
> - Verify PR number follows sequence
> - Verify sequential increment
> 
> ### CFG-TS-07: Numbering Sequence - PO
> - Configure PO numbering (e.g., PO-{YYYY}-{####})
> - Create PO
> - Verify PO number follows sequence
> - Verify year reset (if configured)
> 
> ### CFG-TS-08: Numbering Sequence - GRN
> - Configure GRN numbering (e.g., GRN-{LOC}-{####})
> - Create GRN
> - Verify GRN number includes location code
> - Verify location-specific sequence
> 
> ### CFG-TS-09: Email Notification Template - PR Approval
> - Configure PR approval notification template
> - Submit PR for approval
> - Verify email sent to approver
> - Verify template variables populated
> 
> ### CFG-TS-10: Email Notification Template - PO Confirmation
> - Configure PO confirmation template
> - Approve PO
> - Verify email sent to supplier
> - Verify PO details included
> 
> ### CFG-TS-11: System Defaults - PR
> - Set default required date offset (e.g., +7 days)
> - Create PR
> - Verify required date auto-populated
> - Verify default suggested supplier (if configured)
> 
> ### CFG-TS-12: System Defaults - RFQ
> - Set default RFQ deadline (e.g., +14 days)
> - Create RFQ
> - Verify deadline auto-populated
> - Verify default minimum suppliers (e.g., 3)
> 
> ### CFG-TS-13: System Defaults - PO
> - Set default payment terms (e.g., Net 30)
> - Create PO
> - Verify payment terms auto-populated from supplier
> - Verify override allowed
> 
> ### CFG-TS-14: Configuration Hierarchy
> - Set global (company-level) config
> - Set location-specific override
> - Verify location config takes precedence
> - Verify fallback to global if no local config
> 
> ### CFG-TS-15: Configuration Versioning
> - Update approval threshold
> - Verify existing PRs use old threshold
> - Verify new PRs use new threshold
> - Verify configuration change audit
> 
> ### CFG-TS-16: Configuration Validation
> - Attempt invalid tolerance (e.g., -5%)
> - Attempt invalid threshold (negative amount)
> - Verify validation errors
> - Verify configuration not saved
> 
> ### CFG-TS-17: Company/Location Context
> - Verify configuration per company
> - Verify location-specific overrides
> - Verify multi-tenancy isolation
> 
> ### CFG-TS-18: Permission Checks
> - Test unauthorized user access
> - Test configuration edit permissions
> - Verify only admin/config manager can edit
> - Verify role-based restrictions
> 
> ### CFG-TS-19: Configuration Export/Import
> - Export configuration to JSON/YAML
> - Modify configuration
> - Import configuration
> - Verify configuration restored
> 
> ### CFG-TS-20: Audit Trail Verification
> - Verify created_at, updated_at timestamps
> - Verify created_by, updated_by user tracking
> - Verify configuration change history
> - Verify before/after values logged

---

## AGENT EXECUTION INSTRUCTION (LOCKED)

**Run Task:** Configuration (Procurement System Configuration) — Test Automation

- Create `Configuration_Management_test_script.py` in `backend/domain/procurement/tests/` or `backend/domain/config/tests/`
- Implement CFG-TS-01 through CFG-TS-20 exactly as defined
- Enforce real master dependency
- Do not simplify or shortcut validations
- Follow BBP Configuration rules strictly
- Ensure tests cover: Approval rules, Tolerance settings, Numbering sequences, Email templates, System defaults, Configuration hierarchy

**Acceptance Criteria:**
- All 20 test cases pass
- No mock data used
- Real master data validated before execution
- Approval rules applied correctly
- Tolerance logic verified
- Numbering sequences tested
- Email templates validated
- Configuration hierarchy tested
- Proper error handling for invalid config
- Transaction isolation maintained

**Critical Integration Points:**
- Config → Approval workflow
- Config → Tolerance validation
- Config → Numbering generation
- Config → Email notifications
- Config → System defaults

**Business Logic to Validate:**
- Approval Threshold: If Amount > Threshold, Approval Required
- Tolerance: If |Actual - Expected| / Expected × 100 ≤ Tolerance%, Auto-approve
- Numbering: Sequential, no gaps, year/location-specific (if configured)
- Hierarchy: Location Config > Company Config > System Default

Failure to meet any rule = test suite rejection.
