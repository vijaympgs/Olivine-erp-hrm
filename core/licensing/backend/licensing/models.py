"""
License Configuration Model
Defines platform limits for Companies and Locations
Platform Admin Only
"""
from django.db import models
from django.core.exceptions import ValidationError


class LicenseConfiguration(models.Model):
    """
    🔒 LICENSE CONFIGURATION (Platform Governance)
    
    Defines limits for:
    - Number of Companies that can be created
    - Number of Locations per Company
    
    ⚠️ Platform Admin Only - NOT exposed to business users
    """
    # Identification
    license_key = models.CharField(max_length=255, unique=True, help_text="Unique license identifier")
    licensee_name = models.CharField(max_length=255, help_text="Organization name")
    
    # Limits
    max_companies = models.PositiveIntegerField(
        default=1,
        help_text="Maximum number of Companies that can be created"
    )
    max_locations_per_company = models.PositiveIntegerField(
        default=5,
        help_text="Maximum number of Locations per Company"
    )
    max_total_locations = models.PositiveIntegerField(
        default=10,
        help_text="Maximum total Locations across all Companies"
    )
    
    # Status
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField(null=True, blank=True, help_text="Leave blank for perpetual")
    
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'licensing'
        db_table = 'licensing_configuration'
        verbose_name = 'License Configuration'
        verbose_name_plural = 'License Configurations'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.licensee_name} - {self.license_key}"
    
    def clean(self):
        """Ensure only one active license at a time"""
        if self.is_active:
            existing_active = LicenseConfiguration.objects.filter(
                is_active=True
            ).exclude(pk=self.pk)
            
            if existing_active.exists():
                raise ValidationError(
                    "Only one active license configuration is allowed. "
                    "Deactivate the existing license before activating a new one."
                )
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    @classmethod
    def get_active_license(cls):
        """Get the currently active license configuration"""
        try:
            return cls.objects.get(is_active=True)
        except cls.DoesNotExist:
            raise ValidationError(
                "No active license configuration found. "
                "Please contact your platform administrator."
            )
        except cls.MultipleObjectsReturned:
            raise ValidationError(
                "Multiple active licenses found. "
                "Please contact your platform administrator."
            )


# Proxy model for Business Entity view in Licensing section
from core.licensing.backend.business_entities.models import Company

class LicensedEntity(Company):
    """
    🏢 LICENSED ENTITY (Proxy Model)
    
    Read-only view of Companies from a licensing perspective.
    This is a proxy - actual data is in business_entities.Company
    """
    class Meta:
        proxy = True
        app_label = 'licensing'
        verbose_name = 'Business Entity'
        verbose_name_plural = 'Business Entities'
    
    def __str__(self):
        return f"{self.name} ({self.code}) - {self.legal_entity_type}"





