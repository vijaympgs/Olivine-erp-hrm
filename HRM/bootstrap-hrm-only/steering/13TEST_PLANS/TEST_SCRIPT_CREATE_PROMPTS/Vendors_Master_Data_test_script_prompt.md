# Vendors (Supplier Master Data) — Test Script Prompt
File to be created by Agent:
**Vendors_Master_Data_test_script.py**

---

## OBJECTIVE

Validate **end-to-end Vendor/Supplier Master Data Management** behavior covering:
- Vendor creation and maintenance
- Contact management
- Payment terms configuration
- Tax and compliance settings
- Vendor classification and categorization
- Multi-location vendor mapping
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
   - Tax configurations
4. ❌ DO NOT auto-create master data inside tests
5. ✅ FAIL FAST if required master data is missing
6. ✅ Use Django ORM models only
7. ✅ Each test must be transactional and isolated
8. ✅ Follow BBP Master Data rules strictly

---

## TEST SCRIPT STRUCTURE

```python
# file: Vendors_Master_Data_test_script.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal

# TODO: Import Vendor specific models and serializers
from master.models import (
    Supplier,
    SupplierContact,
    PaymentTerm,
    TaxConfiguration
)

from company.models import (
    Company,
    Location
)
```

---

## BASE TEST SETUP (SHARED CONTEXT)

```python
class VendorsMasterDataTestCase(TestCase):

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
> Based on BBP Master Data requirements for **Vendors/Suppliers**:
> 
> **Core Test Cases to Implement:**
> 
> ### VEN-TS-01: Create New Vendor
> - Create vendor with basic details (name, code, type)
> - Set vendor category (domestic/international)
> - Verify status = ACTIVE
> - Verify unique vendor code
> 
> ### VEN-TS-02: Vendor Contact Management
> - Add primary contact (name, email, phone)
> - Add secondary contacts
> - Verify contact linkage to vendor
> - Verify contact validation (email format, phone)
> 
> ### VEN-TS-03: Payment Terms Configuration
> - Set payment terms (Net 30, Net 60, etc.)
> - Configure credit limit
> - Set payment method preferences
> - Verify terms applied to POs
> 
> ### VEN-TS-04: Tax Configuration
> - Set vendor tax ID (GST, PAN, etc.)
> - Configure tax applicability
> - Set tax exemption (if applicable)
> - Verify tax calculation in transactions
> 
> ### VEN-TS-05: Vendor Classification
> - Set vendor type (manufacturer, distributor, service provider)
> - Set vendor rating (A, B, C)
> - Set preferred vendor flag
> - Verify classification filters
> 
> ### VEN-TS-06: Multi-Location Vendor Mapping
> - Map vendor to multiple locations
> - Set location-specific terms
> - Verify location-based vendor availability
> - Verify multi-tenancy isolation
> 
> ### VEN-TS-07: Vendor Bank Details
> - Add bank account information
> - Set default payment account
> - Verify bank details validation
> - Verify payment processing integration
> 
> ### VEN-TS-08: Vendor Address Management
> - Add billing address
> - Add shipping address
> - Add multiple addresses
> - Verify address validation
> 
> ### VEN-TS-09: Vendor Approval Workflow
> - Create vendor in DRAFT status
> - Submit for approval
> - Approve vendor (DRAFT → ACTIVE)
> - Verify only approved vendors available for PO
> 
> ### VEN-TS-10: Vendor Deactivation
> - Deactivate vendor
> - Verify status = INACTIVE
> - Verify not available for new POs
> - Verify existing POs not affected
> 
> ### VEN-TS-11: Vendor Reactivation
> - Reactivate inactive vendor
> - Verify status = ACTIVE
> - Verify available for new POs
> - Verify audit trail
> 
> ### VEN-TS-12: Duplicate Vendor Detection
> - Attempt to create vendor with existing code
> - Attempt to create vendor with existing name
> - Verify duplicate validation
> - Verify error messages
> 
> ### VEN-TS-13: Vendor Search and Filtering
> - Search by vendor name
> - Filter by vendor type
> - Filter by location
> - Filter by active/inactive status
> 
> ### VEN-TS-14: Vendor Performance Tracking
> - Track on-time delivery rate
> - Track quality rating
> - Track return rate
> - Verify performance metrics calculation
> 
> ### VEN-TS-15: Company Context Validation
> - Verify vendor created for correct company
> - Verify multi-tenancy isolation
> - Verify vendor not visible to other companies
> 
> ### VEN-TS-16: Permission Checks
> - Test unauthorized user access
> - Test create/edit permissions
> - Verify role-based restrictions
> - Test vendor vs buyer permissions
> 
> ### VEN-TS-17: Invalid Data Validation
> - Missing required fields (name, code)
> - Invalid email format
> - Invalid phone format
> - Invalid tax ID format
> 
> ### VEN-TS-18: Audit Trail Verification
> - Verify created_at, updated_at timestamps
> - Verify created_by, updated_by user tracking
> - Verify status change history
> - Verify modification audit trail

---

## AGENT EXECUTION INSTRUCTION (LOCKED)

**Run Task:** Vendors (Supplier Master Data) — Test Automation

- Create `Vendors_Master_Data_test_script.py` in `backend/domain/master/tests/` or `backend/domain/company/tests/`
- Implement VEN-TS-01 through VEN-TS-18 exactly as defined
- Enforce real master dependency
- Do not simplify or shortcut validations
- Follow BBP Master Data rules strictly
- Ensure tests cover: CRUD operations, Contact management, Payment terms, Tax config, Classification, Multi-location mapping

**Acceptance Criteria:**
- All 18 test cases pass
- No mock data used
- Real master data validated before execution
- Duplicate detection verified
- Approval workflow tested
- Multi-tenancy isolation validated
- Proper error handling for missing data
- Transaction isolation maintained

**Critical Integration Points:**
- Vendor → PO creation (vendor availability)
- Vendor → Payment terms application
- Vendor → Tax calculation
- Vendor → Performance metrics

**Business Logic to Validate:**
- Vendor Code: Must be unique per company
- Credit Limit: Enforced in PO creation
- Payment Terms: Applied to all POs for vendor
- Tax ID: Validated per country/region rules

Failure to meet any rule = test suite rejection.
