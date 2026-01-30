import uuid
"""
DEPRECATED MODULE (Phase 4)
This module contains legacy duplicate models (Company, Customer, Supplier) which have been soft-decommissioned.
These models are READ-ONLY and strictly for historical reference or legacy app compatibility (e.g. POS).
Use domain.business_entities for new development.
"""
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
import warnings
from core.shared.backend.common.legacy_manager import LegacyReadonlyManager
from core.licensing.backend.business_entities.models import Company as BusinessEntityCompany



class Company(models.Model):
    objects = LegacyReadonlyManager()
    LEGACY_DEPRECATED = True

    def delete(self, *args, **kwargs):
        raise ValidationError("Legacy domain.company.Company is Read-Only (Phase 4).")


    """
    Company Master - Defines the legal entity operating the retail business.
    Acts as the root master for configuration, reporting boundaries, stock ownership,
    financial settings, and business hierarchies.
    """
    
    LEGAL_ENTITY_CHOICES = [
        ('SOLE_PROPRIETOR', 'Sole Proprietor'),
        ('PARTNERSHIP', 'Partnership'),
        ('LLP', 'LLP'),
        ('PVT_LTD', 'Pvt Ltd'),
        ('FRANCHISE', 'Franchise'),
    ]
    
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_code = models.CharField(
        max_length=20, 
        unique=True,
        help_text="Short code identifier (auto-generated from company name, editable)"
    )
    company_name = models.CharField(max_length=100, help_text="Legal name")
    legal_entity_type = models.CharField(
        max_length=20, 
        choices=LEGAL_ENTITY_CHOICES,
        help_text="Legal entity type"
    )
    address = models.JSONField(
        blank=True, 
        null=True,
        help_text="Registered address details"
    )
    default_currency = models.CharField(
        max_length=10, 
        default='INR',
        help_text="ISO currency code"
    )
    timezone = models.CharField(
        max_length=50, 
        default='Asia/Kolkata',
        help_text="Olson timezone (e.g., Asia/Kolkata)"
    )
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='ACTIVE'
    )
    
    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn("domain.company.Company is a Legacy/Duplicate model. Use domain.business_entities.Company instead.", DeprecationWarning)

    
    class Meta:
        db_table = 'company'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['company_name']
    
    def __str__(self):
        return f"{self.company_name} ({self.company_code})"
    
    def save(self, *args, **kwargs):
        if not getattr(self, '_permit_legacy_creation', False):
             raise ValidationError("Legacy domain.company.Company is Read-Only. Use domain.business_entities.Company.")
        # Auto-generate company_code from company_name if not provided


        if not self.company_code and self.company_name:
            base_code = slugify(self.company_name).upper().replace('-', '_')[:20]
            # Ensure uniqueness
            counter = 1
            code = base_code
            while Company.objects.filter(company_code=code).exclude(id=self.id).exists():
                code = f"{base_code[:17]}_{counter:02d}"
                counter += 1
            self.company_code = code
        
        super().save(*args, **kwargs)
    
    def clean(self):
        """Custom validation"""
        super().clean()
        
        # Ensure at least one active company exists
        if self.status == 'INACTIVE':
            active_companies = Company.objects.filter(status='ACTIVE').exclude(id=self.id)
            if not active_companies.exists():
                raise ValidationError("At least one active company must exist in the system.")
    
    @classmethod
    def get_active_companies(cls):
        """Get all active companies"""
        return cls.objects.filter(status='ACTIVE')
    
    @property
    def is_active(self):
        """Check if company is active"""
        return self.status == 'ACTIVE'


class OperationalCompany(BusinessEntityCompany):
    class Meta:
        proxy = True
        app_label = 'company'
        verbose_name = 'Application Company'
        verbose_name_plural = 'Application Companies'

    def __str__(self):
        return self.name



# ==============================================================================
# LOCATION MODEL - MOVED TO Retail.backend.DOMAIN
# ==============================================================================
# Location is now Retail-exclusive and defined in Retail.backend.domain.models
# This legacy definition is commented out to avoid conflicts.
# Migration: 2026-01-02 - Mergeability Architecture
# ==============================================================================

# class Location(models.Model):
#     LOCATION_TYPE_CHOICES = [
#         ('STORE', 'Store'),
#         ('WAREHOUSE', 'Warehouse'),
#         ('OFFICE', 'Office'),
#         ('OTHER', 'Other'),
#     ]
# 
#     CHANNEL_TYPE_CHOICES = [
#         ('RETAIL', 'Retail'),
#         ('ONLINE', 'Online'),
#         ('WHOLESALE', 'Wholesale'),
#         ('FRANCHISE', 'Franchise'),
#     ]
# 
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_locations')
#     location_code = models.CharField(max_length=20)
#     name = models.CharField(max_length=200)
#     display_name = models.CharField(max_length=100, blank=True, null=True)
#     location_type = models.CharField(max_length=20, choices=LOCATION_TYPE_CHOICES)
#     channel_type = models.CharField(max_length=20, choices=CHANNEL_TYPE_CHOICES, blank=True, null=True)
#     parent_location = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='child_locations')
#     address_line1 = models.CharField(max_length=255)
#     address_line2 = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=20, blank=True, null=True)
#     phone = models.CharField(max_length=30, blank=True, null=True)
#     email = models.EmailField(max_length=100, blank=True, null=True)
#     timezone = models.CharField(max_length=50, blank=True, null=True)
#     opening_date = models.DateField(blank=True, null=True)
#     closing_date = models.DateField(blank=True, null=True)
#     is_pos_enabled = models.BooleanField(default=False)
#     is_dc = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
# 
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# 
#     class Meta:
#         db_table = 'location'
#         ordering = ['name']
#         constraints = [
#             models.UniqueConstraint(fields=['company', 'location_code'], name='uq_location_company_code'),
#         ]
# 
#     def __str__(self):
#         return f"{self.name} ({self.location_code})"
# 
#     def clean(self):
#         super().clean()
# 
#         if self.is_pos_enabled and self.location_type != 'STORE':
#             raise ValidationError({'is_pos_enabled': 'POS can be enabled only for STORE locations.'})
# 
#         if self.parent_location_id:
#             if self.parent_location_id == self.id:
#                 raise ValidationError({'parent_location': 'A location cannot be its own parent.'})\
# 
#             if self.company_id and self.parent_location.company_id != self.company_id:
#                 raise ValidationError({'parent_location': 'Parent location must belong to the same company.'})



class Attribute(models.Model):
    INPUT_TYPE_CHOICES = [
        ('TEXT', 'Text'),
        ('NUMBER', 'Number'),
        ('BOOLEAN', 'Boolean'),
        ('LIST', 'List'),
        ('MULTI', 'Multi'),
    ]

    VALUE_SOURCE_CHOICES = [
        ('FIXED_LIST', 'Fixed List'),
        ('FREE_TEXT', 'Free Text'),
        ('DERIVED', 'Derived'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_attributes')
    attribute_code = models.CharField(max_length=50)
    attribute_name = models.CharField(max_length=100)
    input_type = models.CharField(max_length=20, choices=INPUT_TYPE_CHOICES)
    value_source = models.CharField(max_length=20, choices=VALUE_SOURCE_CHOICES)
    is_variant_dimension = models.BooleanField(default=False)
    is_search_facet = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'attribute'
        ordering = ['attribute_name']
        constraints = [
            models.UniqueConstraint(fields=['company', 'attribute_code'], name='uq_attribute_company_code'),
        ]

    def __str__(self):
        return f"{self.attribute_name} ({self.attribute_code})"

    def clean(self):
        super().clean()

        if self.input_type in ['LIST', 'MULTI'] and self.value_source != 'FIXED_LIST':
            raise ValidationError({'value_source': 'LIST/MULTI attributes must use FIXED_LIST value source.'})


class AttributeValue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_attribute_values')
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, related_name='values')
    value_code = models.CharField(max_length=50)
    value_label = models.CharField(max_length=100)
    sort_order = models.IntegerField(blank=True, null=True)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'attribute_value'
        ordering = ['sort_order', 'value_label']
        constraints = [
            models.UniqueConstraint(fields=['attribute', 'value_code'], name='uq_attribute_value_code'),
        ]

    def __str__(self):
        return f"{self.value_label} ({self.value_code})"

    def clean(self):
        super().clean()

        if self.attribute_id and self.company_id and self.attribute.company_id != self.company_id:
            raise ValidationError({'company': 'Company must match the selected attribute company.'})

        if self.attribute_id and self.attribute.input_type not in ['LIST', 'MULTI']:
            raise ValidationError({'attribute': 'Attribute Values are allowed only for LIST/MULTI attribute types.'})


class ProductAttributeTemplate(models.Model):
    TEMPLATE_MODE_CHOICES = [
        ('SIMPLE', 'Simple'),
        ('VARIANT_MATRIX', 'Variant Matrix'),
        ('HYBRID', 'Hybrid'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_product_attribute_templates')
    template_code = models.CharField(max_length=50)
    template_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    template_mode = models.CharField(max_length=20, choices=TEMPLATE_MODE_CHOICES)
    is_core_template = models.BooleanField(default=False)
    is_editable = models.BooleanField(default=True)
    item_type_scope = models.CharField(max_length=50, blank=True, null=True)
    category_scope_id = models.UUIDField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    version_no = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_attribute_template'
        ordering = ['template_code']
        constraints = [
            models.UniqueConstraint(fields=['company', 'template_code'], name='uq_pat_company_code'),
        ]

    def __str__(self):
        return f"{self.template_code} - {self.template_name}"


class ProductAttributeTemplateLine(models.Model):
    VALUE_MODE_CHOICES = [
        ('SINGLE', 'Single'),
        ('MULTI', 'Multi'),
        ('DERIVED', 'Derived'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    template = models.ForeignKey(ProductAttributeTemplate, on_delete=models.CASCADE, related_name='lines')
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, related_name='template_lines')
    is_required = models.BooleanField(default=True)
    is_variant_dimension = models.BooleanField(default=False)
    value_mode = models.CharField(max_length=20, choices=VALUE_MODE_CHOICES)
    default_value = models.ForeignKey(AttributeValue, on_delete=models.PROTECT, blank=True, null=True)
    sequence_no = models.IntegerField(default=1)
    is_search_facet = models.BooleanField(default=False)
    is_pricing_relevant = models.BooleanField(default=False)
    is_reporting_relevant = models.BooleanField(default=False)
    is_pos_visible = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_attribute_template_line'
        ordering = ['sequence_no']
        constraints = [
            models.UniqueConstraint(fields=['template', 'attribute'], name='uq_pat_line_template_attribute'),
        ]

    def __str__(self):
        return f"{self.template.template_code}:{self.sequence_no} - {self.attribute.attribute_code}"

    def clean(self):
        super().clean()

        if self.attribute_id and self.template_id and self.attribute.company_id != self.template.company_id:
            raise ValidationError({'attribute': 'Attribute must belong to the same company as the template.'})

        if self.default_value_id:
            if self.default_value.attribute_id != self.attribute_id:
                raise ValidationError({'default_value': 'Default value must belong to the selected attribute.'})


class UnitOfMeasure(models.Model):
    """Unit of Measure Master (BBP 2.4)"""

    UOM_TYPE_CHOICES = [
        ('STOCK', 'Stock'),
        ('PURCHASE', 'Purchase'),
        ('SALES', 'Sales'),
        ('GENERIC', 'Generic'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_uoms')
    uom_code = models.CharField(max_length=20)
    uom_name = models.CharField(max_length=100)
    uom_type = models.CharField(max_length=20, choices=UOM_TYPE_CHOICES)
    decimal_allowed = models.BooleanField(default=True)
    rounding_precision = models.IntegerField(blank=True, null=True)
    is_core_uom = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'unit_of_measure'
        ordering = ['uom_code']
        constraints = [
            models.UniqueConstraint(fields=['company', 'uom_code'], name='uq_uom_company_code'),
        ]

    def __str__(self):
        return f"{self.uom_name} ({self.uom_code})"


class UOMConversion(models.Model):
    """UOM Conversion mapping (BBP 2.4)"""

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_uom_conversions')
    from_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, related_name='conversions_from')
    to_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, related_name='conversions_to')
    conversion_factor = models.DecimalField(max_digits=18, decimal_places=6)
    applies_to_item_id = models.UUIDField(blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    retail_price = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'uom_conversion'
        ordering = ['from_uom__uom_code', 'to_uom__uom_code']

    def __str__(self):
        return f"{self.from_uom.uom_code} -> {self.to_uom.uom_code} ({self.conversion_factor})"

    def clean(self):
        super().clean()

        if self.from_uom_id and self.to_uom_id and self.from_uom_id == self.to_uom_id:
            raise ValidationError({'to_uom': 'From and To UOM cannot be the same.'})

        if self.from_uom_id and self.company_id and self.from_uom.company_id != self.company_id:
            raise ValidationError({'from_uom': 'From UOM must belong to the same company.'})

        if self.to_uom_id and self.company_id and self.to_uom.company_id != self.company_id:
            raise ValidationError({'to_uom': 'To UOM must belong to the same company.'})


class Item(models.Model):
    """Item Master - Parent/Style level (BBP 2.5)"""

    ITEM_TYPE_CHOICES = [
        ('STOCKED', 'Stocked'),
        ('SERVICE', 'Service'),
        ('KIT', 'Kit'),
        ('GIFT', 'Gift'),
    ]

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('BLOCKED', 'Blocked'),
        ('DISCONTINUED', 'Discontinued'),
        ('ARCHIVED', 'Archived'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_items')
    item_code = models.CharField(max_length=50)
    item_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    attribute_template = models.ForeignKey(ProductAttributeTemplate, on_delete=models.PROTECT, blank=True, null=True, related_name='items')
    category_id = models.UUIDField(blank=True, null=True)
    brand_id = models.UUIDField(blank=True, null=True)
    stock_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, related_name='items_as_stock_uom')
    tax_class_id = models.UUIDField(blank=True, null=True)
    is_serialized = models.BooleanField(default=False)
    is_lot_tracked = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item'
        ordering = ['item_code']
        constraints = [
            models.UniqueConstraint(fields=['company', 'item_code'], name='uq_item_company_code'),
        ]

    def __str__(self):
        return f"{self.item_name} ({self.item_code})"


class ItemVariant(models.Model):
    """Item Variant / SKU (BBP 2.5)"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey('ItemMaster', on_delete=models.CASCADE, related_name='variants')
    sku_code = models.CharField(max_length=80)
    variant_name = models.CharField(max_length=200)
    is_default_variant = models.BooleanField(default=False)
    sales_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, related_name='variants_as_sales_uom')
    purchase_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, blank=True, null=True, related_name='variants_as_purchase_uom')
    stock_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, related_name='variants_as_stock_uom')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item_variant'
        ordering = ['sku_code']
        constraints = [
            models.UniqueConstraint(fields=['item', 'sku_code'], name='uq_item_variant_sku'),
        ]

    def __str__(self):
        return f"{self.variant_name} ({self.sku_code})"


class VariantAttribute(models.Model):
    """Variant Attribute assignment (BBP 2.5)"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_variant = models.ForeignKey(ItemVariant, on_delete=models.CASCADE, related_name='variant_attributes')
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, related_name='variant_assignments')
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.PROTECT, related_name='variant_assignments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'variant_attribute'
        constraints = [
            models.UniqueConstraint(fields=['item_variant', 'attribute'], name='uq_variant_attribute'),
        ]

    def __str__(self):
        return f"{self.item_variant.sku_code}: {self.attribute.attribute_code}={self.attribute_value.value_code}"

    def clean(self):
        super().clean()
        if self.attribute_id and self.attribute_value_id and self.attribute_value.attribute_id != self.attribute_id:
            raise ValidationError({'attribute_value': 'Attribute value must belong to the selected attribute.'})


class VariantUOM(models.Model):
    """Variant UOM/Barcode/Price mapping (BBP 2.5)"""

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_variant = models.ForeignKey(ItemVariant, on_delete=models.CASCADE, related_name='uom_mappings')
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, related_name='variant_uom_mappings')
    is_default_sales = models.BooleanField(default=False)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    retail_price = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'variant_uom'
        constraints = [
            models.UniqueConstraint(fields=['item_variant', 'uom'], name='uq_variant_uom'),
        ]

    def __str__(self):
        return f"{self.item_variant.sku_code} - {self.uom.uom_code}"


class PriceList(models.Model):
    """Price List Header (BBP 2.6)"""

    PRICE_LIST_TYPE_CHOICES = [
        ('RETAIL', 'Retail'),
        ('WHOLESALE', 'Wholesale'),
        ('EMPLOYEE', 'Employee'),
        ('DISTRIBUTOR', 'Distributor'),
    ]

    CHANNEL_CHOICES = [
        ('STORE', 'Store'),
        ('ONLINE', 'Online'),
        ('WHOLESALE', 'Wholesale'),
        ('ALL', 'All Channels'),
    ]

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('EXPIRED', 'Expired'),
        ('ARCHIVED', 'Archived'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_price_lists')
    price_list_code = models.CharField(max_length=50)
    price_list_name = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    price_list_type = models.CharField(max_length=20, choices=PRICE_LIST_TYPE_CHOICES)
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES, blank=True, null=True)
    valid_from = models.DateField()
    valid_to = models.DateField(blank=True, null=True)
    is_default = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'price_list'
        ordering = ['price_list_code']
        constraints = [
            models.UniqueConstraint(fields=['company', 'price_list_code'], name='uq_price_list_company_code'),
        ]

    def __str__(self):
        return f"{self.price_list_name} ({self.price_list_code})"


class PriceListLine(models.Model):
    """Price List Line (BBP 2.6)"""

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE, related_name='lines')
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='price_list_lines')
    item_variant = models.ForeignKey(ItemVariant, on_delete=models.PROTECT, related_name='price_list_lines')
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, related_name='price_list_lines')
    base_price = models.DecimalField(max_digits=18, decimal_places=4)
    tax_inclusive = models.BooleanField(default=False)
    # location_scope removed - Location is Retail-only model
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'price_list_line'
        ordering = ['item__item_code', 'item_variant__sku_code']

    def __str__(self):
        return f"{self.price_list.price_list_code}: {self.item_variant.sku_code} @ {self.base_price}"

    def clean(self):
        super().clean()
        if self.item_variant_id and self.item_id and self.item_variant.item_id != self.item_id:
            raise ValidationError({'item_variant': 'Variant must belong to the selected item.'})


class Customer(models.Model):
    objects = LegacyReadonlyManager()
    LEGACY_DEPRECATED = True

    def delete(self, *args, **kwargs):
        raise ValidationError("Legacy domain.company.Customer is Read-Only (Phase 4).")


    """Customer Master (BBP 3.1)"""

    CUSTOMER_TYPE_CHOICES = [
        ('INDIVIDUAL', 'Individual'),
        ('BUSINESS', 'Business'),
    ]

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('BLACKLISTED', 'Blacklisted'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_customers')
    customer_code = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=200)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPE_CHOICES)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    billing_address = models.JSONField(blank=True, null=True)
    shipping_address = models.JSONField(blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    credit_blocked = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn("domain.company.Customer is a Legacy/Duplicate model. Use domain.business_entities.Customer instead.", DeprecationWarning)


    class Meta:
        db_table = 'customer'
        ordering = ['customer_name']
        constraints = [
            models.UniqueConstraint(fields=['company', 'customer_code'], name='uq_customer_company_code'),
        ]

    def save(self, *args, **kwargs):
        if not getattr(self, '_permit_legacy_creation', False):
             raise ValidationError("Legacy domain.company.Customer is Read-Only. Use domain.business_entities.Customer.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} ({self.customer_code})"


class Supplier(models.Model):
    """Supplier Master (BBP 3.2)"""
    objects = LegacyReadonlyManager()
    LEGACY_DEPRECATED = True

    def delete(self, *args, **kwargs):
        raise ValidationError("Legacy domain.company.Supplier is Read-Only (Phase 4).")



    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('BLOCKED', 'Blocked'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='legacy_suppliers')
    supplier_code = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    gst_vat_no = models.CharField(max_length=50, blank=True, null=True)
    pan_no = models.CharField(max_length=20, blank=True, null=True)
    address = models.JSONField(blank=True, null=True)
    payment_terms = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    lead_time_days = models.PositiveIntegerField(blank=True, null=True)
    is_preferred = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn("domain.company.Supplier is a Legacy/Duplicate model. Use domain.business_entities.Supplier instead.", DeprecationWarning)


    class Meta:
        db_table = 'supplier'
        ordering = ['supplier_name']
        constraints = [
            models.UniqueConstraint(fields=['company', 'supplier_code'], name='uq_supplier_company_code'),
        ]

    def save(self, *args, **kwargs):
        if not getattr(self, '_permit_legacy_creation', False):
             raise ValidationError("Legacy domain.company.Supplier is Read-Only. Use domain.business_entities.Supplier.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.supplier_name} ({self.supplier_code})""""
OPERATIONAL MASTERS (Moved from business_entities)
These models are the canonical operational masters for the company app.
They were moved from core.licensing.backend.business_entities to domain.company as part of
the architectural correction to ensure business_entities contains ONLY licensing metadata.
"""
from django.db import models
from django.utils import timezone
from core.licensing.backend.business_entities.models import Company


class Category(models.Model):
    """Product Category - Operational Master"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'company'
        db_table = 'be_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    """Product Brand - Operational Master"""
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'company'
        db_table = 'be_brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']

    def __str__(self):
        return self.name


class TaxClass(models.Model):
    """Tax Classification - Operational Master"""
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'company'
        db_table = 'be_tax_class'
        verbose_name = 'Tax Class'
        verbose_name_plural = 'Tax Classes'
        ordering = ['name']

    def __str__(self):
        return self.name


class ItemMaster(models.Model):
    """
    Item Master - CANONICAL OPERATIONAL MASTER
    This is the authoritative item model for all operational purposes.
    The 'Item' model in this app is deprecated.
    """
    class ItemType(models.TextChoices):
        STOCKED = "STOCKED", "Stocked"
        SERVICE = "SERVICE", "Service"
        KIT = "KIT", "Kit"
        GIFT = "GIFT", "Gift"

    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.CASCADE, related_name='items')
    item_code = models.CharField(max_length=50, unique=True)  # SKU
    item_name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500, blank=True, null=True)
    item_type = models.CharField(max_length=10, choices=ItemType.choices)
    attribute_template = models.ForeignKey('ProductAttributeTemplate', on_delete=models.PROTECT, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, blank=True)
    stock_uom = models.ForeignKey('UnitOfMeasure', on_delete=models.PROTECT, related_name='stock_items')
    price_list = models.ForeignKey('PriceList', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    mrp = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    cost = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    tax_class = models.ForeignKey('TaxClass', on_delete=models.SET_NULL, null=True, blank=True)

    stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)
    safety_stock = models.IntegerField(default=0)
    lead_time_days = models.IntegerField(null=True, blank=True)

    tags = models.JSONField(null=True, blank=True)  # key-value pairs
    attributes = models.JSONField(null=True, blank=True)
    suppliers = models.JSONField(null=True, blank=True)

    length_cm = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    width_cm = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    height_cm = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    weight_kg = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    status = models.CharField(max_length=20)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_id = models.IntegerField(null=True, blank=True)
    updated_by_id = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'company'
        db_table = 'be_item_master'
        verbose_name = 'Item Master'
        verbose_name_plural = 'Item Masters'
        ordering = ['item_code']

    def __str__(self):
        return f'{self.item_code} - {self.item_name}'


# OPERATIONAL SUPPLIER AND CUSTOMER (Moved from business_entities)
class OperationalSupplier(models.Model):
    """
    Operational Supplier Master - CANONICAL
    This is the authoritative supplier model for all operational purposes.
    The legacy 'Supplier' model above is deprecated.
    """
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        INACTIVE = 'INACTIVE', 'Inactive'
        BLOCKED = 'BLOCKED', 'Blocked'

    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.CASCADE, related_name='operational_suppliers')
    supplier_code = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    gst_vat_no = models.CharField(max_length=50, blank=True)
    pan_no = models.CharField(max_length=20, blank=True)
    address = models.JSONField(blank=True, null=True)
    payment_terms = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=10, blank=True)
    lead_time_days = models.IntegerField(null=True, blank=True)
    is_preferred = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=Status.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'company'
        unique_together = ('company', 'supplier_code')
        db_table = 'be_supplier'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['supplier_code']

    def __str__(self):
        return f'{self.supplier_code} - {self.supplier_name}'


class OperationalCustomer(models.Model):
    """
    Operational Customer Master - CANONICAL
    This is the authoritative customer model for all operational purposes.
    The legacy 'Customer' model above is deprecated.
    """
    class CustomerType(models.TextChoices):
        INDIVIDUAL = 'INDIVIDUAL', 'Individual'
        BUSINESS = 'BUSINESS', 'Business'

    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.CASCADE, related_name='operational_customers')
    customer_code = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=200)
    customer_type = models.CharField(max_length=10, choices=CustomerType.choices)
    phone = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    billing_address = models.JSONField(blank=True, null=True)
    shipping_address = models.JSONField(blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    credit_blocked = models.BooleanField(default=False)
    status = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'company'
        unique_together = ('company', 'customer_code')
        db_table = 'be_customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['customer_code']

    def __str__(self):
        return f'{self.customer_code} - {self.customer_name}'


# ==============================================================================
# ARCHITECTURAL BRIDGE FOR LEGACY IMPORTS (Phase 4)
# ==============================================================================
# The following import provides backward compatibility for apps and tests
# that still reference Location from the old 'company' app.
# ------------------------------------------------------------------------------
try:
    from Retail.backend.domain.models import Location
except ImportError:
    # Location not available (e.g. non-retail installation)
    pass
