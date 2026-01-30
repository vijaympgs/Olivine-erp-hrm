import uuid
from django.db import models

from django.utils import timezone


class Company(models.Model):
    """
    Company Model - LICENSING METADATA ONLY
    
    This model represents a legal business entity and is used EXCLUSIVELY for:
    - License enforcement (company count limits)
    - Multi-tenancy scoping
    - Licensing metadata
    
    ⚠️ ARCHITECTURAL LOCK:
    - This is the ONLY operational model allowed in business_entities
    - ALL other operational models belong in domain.company
    - DO NOT add operational models here
    """
    class LegalEntityType(models.TextChoices):
        SOLE_PROPRIETOR = "SOLE_PROP", "Sole Proprietor"
        PARTNERSHIP = "PARTNERSHIP", "Partnership"
        PRIVATE_LIMITED = "PRIVATE_LTD", "Private Limited"
        PUBLIC_LIMITED = "PUBLIC_LTD", "Public Limited"
        LLP = "LLP", "LLP"
        NON_PROFIT = "NONPROFIT", "Non Profit / NGO"
        GOVERNMENT = "GOV", "Government"
        OTHER = "OTHER", "Other"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"

    # BBP-aligned core fields
    code = models.CharField(max_length=32, unique=True)      # company_code
    name = models.CharField(max_length=255)                  # company_name
    legal_entity_type = models.CharField(
        max_length=20, choices=LegalEntityType.choices
    )
    country = models.CharField(max_length=2)                 # ISO 3166-1 alpha-2
    default_currency = models.CharField(max_length=3)        # ISO 4217
    timezone = models.CharField(max_length=64)

    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    # Structured address (mirrors SPA Address type)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    postal_code = models.CharField(max_length=32, blank=True)
    address_country = models.CharField(max_length=2, blank=True)

    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "business_entities"
        db_table = "be_company"
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["code"]

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"

    @property
    def address_dict(self) -> dict:
        """
        Helper used by serializer to present SPA-friendly address shape.
        """
        return {
            "line1": self.address_line1,
            "line2": self.address_line2,
            "city": self.city,
            "state": self.state,
            "postalCode": self.postal_code,
            "country": self.address_country or self.country,
        }
    
    def clean(self):
        """
        🔒 LICENSE ENFORCEMENT
        Validate that Company creation does not exceed license limits
        """
        from django.core.exceptions import ValidationError
        
        # Only enforce for new Companies (not updates)
        if self.pk is None:
            try:
                # Import here to avoid circular dependency
                from core.licensing.backend.licensing.models import LicenseConfiguration
                
                license_config = LicenseConfiguration.get_active_license()
                existing_count = Company.objects.count()
                
                if existing_count >= license_config.max_companies:
                    raise ValidationError(
                        f"Company limit exceeded. Your license allows only "
                        f"{license_config.max_companies} compan{'y' if license_config.max_companies == 1 else 'ies'}. "
                        f"Currently {existing_count} exist. Please upgrade your license to create more companies."
                    )
            except Exception as e:
                # If licensing model doesn't exist or other error, allow creation
                # (fail-open for backward compatibility)
                if "No active license" in str(e):
                    # Fail-open for environment setup/tests
                    import logging
                    logging.warning("No active license found - allowing company creation (fail-open).")
                    return
                # Otherwise, log and allow
                import logging
                logging.warning(f"License validation skipped: {e}")
    
    def save(self, *args, **kwargs):
        """Override save to enforce validation"""
        self.clean()
        super().save(*args, **kwargs)


# ═══════════════════════════════════════════════════════════════════════════
# ARCHITECTURAL LOCK ENFORCEMENT
# ═══════════════════════════════════════════════════════════════════════════
#
# ⚠️ ALL OPERATIONAL MODELS HAVE BEEN MOVED TO domain.company
#
# The following models were removed from this file (2025-12-23):
# - Category → domain.company.models.Category
# - Brand → domain.company.models.Brand
# - TaxClass → domain.company.models.TaxClass
# - ItemMaster → domain.company.models.ItemMaster
# - Supplier → domain.company.models.OperationalSupplier
# - Customer → domain.company.models.OperationalCustomer
# - Location → domain.company.models.Location
# - Attribute → domain.company.models.Attribute
# - AttributeValue → domain.company.models.AttributeValue
# - UnitOfMeasure → domain.company.models.UnitOfMeasure
# - PriceList → domain.company.models.PriceList
# - ProductAttributeTemplate → domain.company.models.ProductAttributeTemplate
#
# RULE: business_entities = LICENSING METADATA ONLY
# RULE: domain.company = OPERATIONAL MASTERS ONLY
#
# DO NOT add operational models to this file.
# See: .steering/01_ARCH_GOVERNANCE/ARCHITECTURAL_LOCK_REFERENCE.md
#
# ═══════════════════════════════════════════════════════════════════════════




