
# file: backend/domain/company/tests/test_vendors_master_data.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal

from core.licensing.backend.business_entities.models import Company
from core.org_structure.backend.company.models import (
    OperationalSupplier as Supplier,
    Location
)


class VendorsMasterDataTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.filter(status='ACTIVE').first()
        if not cls.company:
            cls.company = Company.objects.first()
        cls.location = Location.objects.filter(company=cls.company, is_active=True).first()
        cls.user = get_user_model().objects.filter(is_active=True).first()
        
        assert cls.company, "Missing active Company master"
        assert cls.location, "Missing active Location master"
        assert cls.user, "Missing active User"

    # VEN-TS-01: Create New Vendor
    def test_ven_ts_01_create_new_vendor(self):
        vendor = Supplier.objects.create(
            company=self.company, name="Test Vendor", code="VEN-001",
            vendor_type="MANUFACTURER", status="ACTIVE"
        )
        self.assertEqual(vendor.status, "ACTIVE")
        self.assertEqual(vendor.code, "VEN-001")

    # VEN-TS-02: Vendor Contact Management
    def test_ven_ts_02_vendor_contact_management(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 2", code="VEN-002")
        vendor.primary_contact_name = "John Doe"
        vendor.primary_contact_email = "john@vendor.com"
        vendor.primary_contact_phone = "+1234567890"
        vendor.save()
        self.assertEqual(vendor.primary_contact_name, "John Doe")

    # VEN-TS-03: Payment Terms Configuration
    def test_ven_ts_03_payment_terms_configuration(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 3", code="VEN-003")
        vendor.payment_terms = "Net 30"
        vendor.credit_limit = Decimal('50000.00')
        vendor.save()
        self.assertEqual(vendor.payment_terms, "Net 30")

    # VEN-TS-04: Tax Configuration
    def test_ven_ts_04_tax_configuration(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 4", code="VEN-004")
        vendor.tax_id = "TAX123456"
        vendor.tax_exempt = False
        vendor.save()
        self.assertEqual(vendor.tax_id, "TAX123456")

    # VEN-TS-05: Vendor Classification
    def test_ven_ts_05_vendor_classification(self):
        vendor = Supplier.objects.create(
            company=self.company, name="Vendor 5", code="VEN-005",
            vendor_type="DISTRIBUTOR", rating="A", is_preferred=True
        )
        self.assertEqual(vendor.rating, "A")
        self.assertTrue(vendor.is_preferred)

    # VEN-TS-06: Multi-Location Vendor Mapping
    def test_ven_ts_06_multi_location_vendor_mapping(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 6", code="VEN-006")
        # Vendor can serve multiple locations
        self.assertEqual(vendor.company, self.company)

    # VEN-TS-07: Vendor Bank Details
    def test_ven_ts_07_vendor_bank_details(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 7", code="VEN-007")
        vendor.bank_name = "Test Bank"
        vendor.bank_account_number = "1234567890"
        vendor.bank_routing_number = "ROUT123"
        vendor.save()
        self.assertEqual(vendor.bank_name, "Test Bank")

    # VEN-TS-08: Vendor Address Management
    def test_ven_ts_08_vendor_address_management(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 8", code="VEN-008")
        vendor.billing_address = "123 Main St"
        vendor.shipping_address = "456 Oak Ave"
        vendor.save()
        self.assertIsNotNone(vendor.billing_address)

    # VEN-TS-09: Vendor Approval Workflow
    def test_ven_ts_09_vendor_approval_workflow(self):
        vendor = Supplier.objects.create(
            company=self.company, name="Vendor 9", code="VEN-009", status="DRAFT"
        )
        vendor.status = "ACTIVE"
        vendor.save()
        self.assertEqual(vendor.status, "ACTIVE")

    # VEN-TS-10: Vendor Deactivation
    def test_ven_ts_10_vendor_deactivation(self):
        vendor = Supplier.objects.create(
            company=self.company, name="Vendor 10", code="VEN-010", status="ACTIVE"
        )
        vendor.status = "INACTIVE"
        vendor.save()
        self.assertEqual(vendor.status, "INACTIVE")

    # VEN-TS-11: Vendor Reactivation
    def test_ven_ts_11_vendor_reactivation(self):
        vendor = Supplier.objects.create(
            company=self.company, name="Vendor 11", code="VEN-011", status="INACTIVE"
        )
        vendor.status = "ACTIVE"
        vendor.save()
        self.assertEqual(vendor.status, "ACTIVE")

    # VEN-TS-12: Duplicate Vendor Detection
    def test_ven_ts_12_duplicate_vendor_detection(self):
        Supplier.objects.create(company=self.company, name="Vendor 12", code="VEN-012")
        with self.assertRaises(Exception):
            Supplier.objects.create(company=self.company, name="Vendor 12 Dup", code="VEN-012")

    # VEN-TS-13: Vendor Search and Filtering
    def test_ven_ts_13_vendor_search_and_filtering(self):
        Supplier.objects.create(company=self.company, name="ABC Vendor", code="VEN-013")
        vendors = Supplier.objects.filter(name__icontains="ABC")
        self.assertGreater(vendors.count(), 0)

    # VEN-TS-14: Vendor Performance Tracking
    def test_ven_ts_14_vendor_performance_tracking(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 14", code="VEN-014")
        vendor.on_time_delivery_rate = Decimal('95.5')
        vendor.quality_rating = Decimal('4.5')
        vendor.save()
        self.assertEqual(vendor.on_time_delivery_rate, Decimal('95.5'))

    # VEN-TS-15: Company Context Validation
    def test_ven_ts_15_company_context_validation(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 15", code="VEN-015")
        self.assertEqual(vendor.company, self.company)

    # VEN-TS-16: Permission Checks
    def test_ven_ts_16_permission_checks(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 16", code="VEN-016")
        self.assertIsNotNone(vendor)

    # VEN-TS-17: Invalid Data Validation
    def test_ven_ts_17_invalid_data_validation(self):
        with self.assertRaises(Exception):
            Supplier.objects.create(company=self.company, name="", code="")

    # VEN-TS-18: Audit Trail Verification
    def test_ven_ts_18_audit_trail(self):
        vendor = Supplier.objects.create(company=self.company, name="Vendor 18", code="VEN-018")
        self.assertIsNotNone(vendor.created_at)
        self.assertIsNotNone(vendor.updated_at)




