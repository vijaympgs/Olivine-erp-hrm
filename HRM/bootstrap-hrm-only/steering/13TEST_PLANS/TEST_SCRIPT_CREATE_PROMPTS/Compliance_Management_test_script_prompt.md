# Compliance (Regulatory & Vendor Compliance) — Test Script Prompt
File to be created by Agent:
**Compliance_Management_test_script.py**

---

## OBJECTIVE

Validate **end-to-end Compliance Management** behavior covering:
- Vendor compliance tracking
- Document expiry management
- Regulatory requirement validation
- Compliance alerts and notifications
- Audit trail and reporting
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
   - Supplier
   - Users / Roles
4. ❌ DO NOT auto-create master data inside tests
5. ✅ FAIL FAST if required master data is missing
6. ✅ Use Django ORM models only
7. ✅ Each test must be transactional and isolated
8. ✅ Follow BBP Compliance rules strictly

---

## TEST SCRIPT STRUCTURE

```python
# file: Compliance_Management_test_script.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date, timedelta
from django.utils import timezone

# TODO: Import Compliance specific models and serializers
from procurement.models import (
    VendorCompliance,
    ComplianceDocument,
    ComplianceRequirement,
    ComplianceAlert,
    Supplier
)

from master.models import (
    Company, Location
)
```

---

## BASE TEST SETUP (SHARED CONTEXT)

```python
class ComplianceManagementTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.filter(is_active=True).first()
        cls.location = Location.objects.filter(company=cls.company, is_active=True).first()
        cls.supplier = Supplier.objects.filter(is_active=True).first()
        cls.user = get_user_model().objects.filter(is_active=True).first()
        
        assert cls.company, "Missing active Company master"
        assert cls.location, "Missing active Location master"
        assert cls.supplier, "Missing active Supplier master"
        assert cls.user, "Missing active User"
```

---

## TEST CASES

> **Agent Instruction**:
> Based on BBP Compliance requirements for **Vendor Compliance Management**:
> 
> **Core Test Cases to Implement:**
> 
> ### COMP-TS-01: Create Compliance Requirement
> - Define compliance requirement (license, certification, insurance)
> - Set requirement type and category
> - Set mandatory/optional flag
> - Verify requirement created
> 
> ### COMP-TS-02: Assign Compliance to Vendor
> - Assign compliance requirement to vendor
> - Set due date/expiry date
> - Verify vendor-compliance linkage
> - Verify compliance status = PENDING
> 
> ### COMP-TS-03: Upload Compliance Document
> - Upload document (PDF, image)
> - Link to compliance requirement
> - Set document expiry date
> - Verify document stored and accessible
> 
> ### COMP-TS-04: Compliance Document Verification
> - Submit document for verification
> - Verify status = UNDER_REVIEW
> - Approve document
> - Verify status = COMPLIANT
> 
> ### COMP-TS-05: Compliance Document Rejection
> - Submit document for verification
> - Reject document with reason
> - Verify status = NON_COMPLIANT
> - Verify rejection reason logged
> 
> ### COMP-TS-06: Document Expiry Tracking
> - Set document expiry date
> - Verify expiry date tracked
> - Verify status changes to EXPIRED after expiry
> - Verify vendor compliance status updated
> 
> ### COMP-TS-07: Expiry Alert Generation
> - Set document expiry 30 days in future
> - Verify alert generated at 30-day threshold
> - Verify alert at 15-day threshold
> - Verify alert at 7-day threshold
> 
> ### COMP-TS-08: Compliance Renewal
> - Upload renewed document before expiry
> - Verify new document linked
> - Verify expiry date extended
> - Verify compliance status maintained
> 
> ### COMP-TS-09: Multiple Compliance Requirements
> - Assign multiple requirements to vendor
> - Track compliance for each requirement
> - Verify overall vendor compliance status
> - Verify all requirements must be met
> 
> ### COMP-TS-10: Vendor Compliance Dashboard
> - View vendor compliance summary
> - Verify compliant/non-compliant count
> - Verify expiring documents count
> - Verify expired documents count
> 
> ### COMP-TS-11: Compliance Blocking PO Creation
> - Attempt PO creation with non-compliant vendor
> - Verify PO blocked (if configured)
> - Verify warning message displayed
> - Verify override permission required
> 
> ### COMP-TS-12: Compliance Reporting
> - Generate compliance report by vendor
> - Generate compliance report by requirement type
> - Generate expiry forecast report
> - Verify report accuracy
> 
> ### COMP-TS-13: Regulatory Requirement Types
> - Test business license compliance
> - Test insurance certificate compliance
> - Test tax registration compliance
> - Test quality certification compliance
> 
> ### COMP-TS-14: Compliance Notification
> - Verify vendor notified of expiring documents
> - Verify procurement team notified
> - Verify escalation for overdue compliance
> - Verify notification preferences respected
> 
> ### COMP-TS-15: Compliance History Tracking
> - Track document upload history
> - Track verification history
> - Track renewal history
> - Verify complete audit trail
> 
> ### COMP-TS-16: Company/Location Context
> - Verify compliance requirements per company
> - Verify location-specific requirements
> - Verify multi-tenancy isolation
> 
> ### COMP-TS-17: Permission Checks
> - Test unauthorized user access
> - Test document upload permissions
> - Test verification/approval permissions
> - Verify role-based restrictions
> 
> ### COMP-TS-18: Invalid Data Validation
> - Missing required fields
> - Invalid document format
> - Past expiry date on upload
> - Invalid file size/type
> 
> ### COMP-TS-19: Audit Trail Verification
> - Verify created_at, updated_at timestamps
> - Verify created_by, updated_by user tracking
> - Verify status change history
> - Verify document upload/verification audit
> 
> ### COMP-TS-20: Compliance Integration with Procurement
> - Verify compliance check in PR creation
> - Verify compliance check in RFQ
> - Verify compliance check in PO creation
> - Verify compliance override workflow

---

## AGENT EXECUTION INSTRUCTION (LOCKED)

**Run Task:** Compliance (Regulatory & Vendor Compliance) — Test Automation

- Create `Compliance_Management_test_script.py` in `backend/domain/procurement/compliance/tests/`
- Implement COMP-TS-01 through COMP-TS-20 exactly as defined
- Enforce real master dependency
- Do not simplify or shortcut validations
- Follow BBP Compliance rules strictly
- Ensure tests cover: Document management, Expiry tracking, Alerts, Verification workflow, PO blocking, Reporting

**Acceptance Criteria:**
- All 20 test cases pass
- No mock data used
- Real master data validated before execution
- Document expiry logic verified
- Alert generation tested
- PO blocking validated
- Notification logic tested
- Proper error handling for missing data
- Transaction isolation maintained

**Critical Integration Points:**
- Vendor → Compliance requirements
- Compliance → PO creation blocking
- Compliance → Alert generation
- Compliance → Notification system
- Compliance → Reporting

**Business Logic to Validate:**
- Expiry Alert: Alert generated at 30, 15, 7 days before expiry
- Compliance Status: COMPLIANT if all requirements met and not expired
- PO Blocking: Block PO if vendor NON_COMPLIANT (unless override)
- Overall Status: Vendor COMPLIANT only if ALL requirements COMPLIANT

Failure to meet any rule = test suite rejection.
