from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)

class LegacyBridge:
    """
    Adapter service to bridge duplicates between Legacy (company, user_management)
    and Canonical (business_entities, hr) models.
    """

    @staticmethod
    def get_canonical_company(legacy_company_id):
        """
        Resolves legacy company (domain.company.Company) to canonical (domain.business_entities.Company).
        Matching Strategy: company_code == code
        """
        LegacyCompany = apps.get_model('company', 'Company')
        CanonicalCompany = apps.get_model('business_entities', 'Company')
        
        try:
            legacy = LegacyCompany.objects.get(pk=legacy_company_id)
            return CanonicalCompany.objects.filter(code=legacy.company_code).first()
        except (LegacyCompany.DoesNotExist, AttributeError):
            return None

    @staticmethod
    def get_legacy_company(canonical_company_id):
        """
        Resolves canonical company to legacy.
        """
        LegacyCompany = apps.get_model('company', 'Company')
        CanonicalCompany = apps.get_model('business_entities', 'Company')
        
        try:
            canonical = CanonicalCompany.objects.get(pk=canonical_company_id)
            return LegacyCompany.objects.filter(company_code=canonical.code).first()
        except (CanonicalCompany.DoesNotExist, AttributeError):
            return None

    @staticmethod
    def get_canonical_customer(legacy_customer_id):
        """
        Resolves legacy customer to canonical.
        Matching Strategy: customer_code
        """
        LegacyCustomer = apps.get_model('company', 'Customer')
        CanonicalCustomer = apps.get_model('business_entities', 'Customer')
        
        try:
            legacy = LegacyCustomer.objects.get(pk=legacy_customer_id)
            return CanonicalCustomer.objects.filter(customer_code=legacy.customer_code).first()
        except (LegacyCustomer.DoesNotExist, AttributeError):
            return None

    @staticmethod
    def get_canonical_employee(legacy_employee_id):
        """
        Resolves legacy employee (user_management) to canonical (hr).
        Matching Strategy: employee_code
        """
        LegacyEmployee = apps.get_model('user_management', 'Employee')
        CanonicalEmployee = apps.get_model('hr', 'Employee')

        try:
            legacy = LegacyEmployee.objects.get(pk=legacy_employee_id)
            return CanonicalEmployee.objects.filter(employee_code=legacy.employee_code).first()
        except (LegacyEmployee.DoesNotExist, AttributeError):
            return None




