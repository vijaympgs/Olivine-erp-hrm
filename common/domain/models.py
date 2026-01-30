"""
Shared domain models for the enterprise platform
Following governance: Shared models for cross-module use
"""
import uuid
from django.db import models
from core.licensing.backend.business_entities.models import Company as BusinessEntityCompany

# Note: Company model resides in Core.licensing.backend.business_entities.models


class UnitOfMeasure(models.Model):
    """Unit of Measure Master - Platform Contract"""
    UOM_TYPE_CHOICES = [
        ('STOCK', 'Stock'),
        ('PURCHASE', 'Purchase'),
        ('SALES', 'Sales'),
        ('GENERIC', 'Generic'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='common_uoms')
    uom_code = models.CharField(max_length=20)
    uom_name = models.CharField(max_length=100)
    uom_type = models.CharField(max_length=20, choices=UOM_TYPE_CHOICES)
    decimal_allowed = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'common_unit_of_measure'
        ordering = ['uom_code']
        constraints = [
            models.UniqueConstraint(fields=['company', 'uom_code'], name='uq_common_uom_company_code'),
        ]

    def __str__(self):
        return f"{self.uom_name} ({self.uom_code})"


class ItemMaster(models.Model):
    """Item Master - Platform Contract (Style Level)"""
    class ItemType(models.TextChoices):
        STOCKED = "STOCKED", "Stocked"
        SERVICE = "SERVICE", "Service"
        KIT = "KIT", "Kit"
        ASSET = "ASSET", "Asset"

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        ACTIVE = "ACTIVE", "Active"
        BLOCKED = "BLOCKED", "Blocked"
        DISCONTINUED = "DISCONTINUED", "Discontinued"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='common_items')
    item_code = models.CharField(max_length=50)
    item_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    item_type = models.CharField(max_length=20, choices=ItemType.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    stock_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, related_name='items_as_stock_uom')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'common_item_master'
        ordering = ['item_code']
        constraints = [
            models.UniqueConstraint(fields=['company', 'item_code'], name='uq_common_item_company_code'),
        ]

    def __str__(self):
        return f"{self.item_name} ({self.item_code})"


class ItemVariant(models.Model):
    """Item Variant - Platform Contract (SKU Level)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, related_name='variants')
    sku_code = models.CharField(max_length=80)
    variant_name = models.CharField(max_length=200)
    is_default_variant = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'common_item_variant'
        ordering = ['sku_code']
        constraints = [
            models.UniqueConstraint(fields=['item', 'sku_code'], name='uq_common_item_variant_sku'),
        ]

    def __str__(self):
        return f"{self.variant_name} ({self.sku_code})"


class Customer(models.Model):
    """Customer Master - Platform Contract"""
    class CustomerType(models.TextChoices):
        INDIVIDUAL = 'INDIVIDUAL', 'Individual'
        BUSINESS = 'BUSINESS', 'Business'

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        BLOCKED = "BLOCKED", "Blocked"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='common_customers')
    customer_code = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=200)
    customer_type = models.CharField(max_length=20, choices=CustomerType.choices)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    
    # Intercompany Trade (ICT) Fields - BBP 4.11
    is_intercompany_customer = models.BooleanField(default=False, help_text="True if this customer is a group company")
    linked_company_id = models.ForeignKey(
        BusinessEntityCompany,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='as_intercompany_customer',
        help_text="Which company this customer represents (for IC transactions)"
    )
    auto_accept_ic_so = models.BooleanField(default=False, help_text="Auto-confirm IC Sales Orders to this entity")
    default_ic_price_list_id = models.UUIDField(null=True, blank=True, help_text="Transfer price list reference")
    default_tax_profile_id = models.UUIDField(null=True, blank=True, help_text="Intercompany tax behavior")
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'common_customer'
        ordering = ['customer_name']
        constraints = [
            models.UniqueConstraint(fields=['company', 'customer_code'], name='uq_common_customer_company_code'),
        ]

    def __str__(self):
        return f"{self.customer_name} ({self.customer_code})"


class Supplier(models.Model):
    """Supplier Master - Platform Contract"""
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        BLOCKED = "BLOCKED", "Blocked"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(BusinessEntityCompany, on_delete=models.PROTECT, related_name='common_suppliers')
    supplier_code = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    
    # Intercompany Trade (ICT) Fields - BBP 4.11
    is_intercompany_supplier = models.BooleanField(default=False, help_text="True if this supplier is a group company")
    linked_company_id = models.ForeignKey(
        BusinessEntityCompany,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='as_intercompany_supplier',
        help_text="Which company this supplier represents (for IC transactions)"
    )
    auto_accept_ic_po = models.BooleanField(default=False, help_text="Auto-approve incoming IC Purchase Orders")
    default_ic_price_list_id = models.UUIDField(null=True, blank=True, help_text="Transfer price reference")
    default_tax_profile_id = models.UUIDField(null=True, blank=True, help_text="Intercompany tax behavior")
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'common_supplier'
        ordering = ['supplier_name']
        constraints = [
            models.UniqueConstraint(fields=['company', 'supplier_code'], name='uq_common_supplier_company_code'),
        ]

    def __str__(self):
        return f"{self.supplier_name} ({self.supplier_code})"

# ==============================================================================
# TEST COMPATIBILITY ALIASES
# ==============================================================================
OperationalSupplier = Supplier
OperationalCustomer = Customer
