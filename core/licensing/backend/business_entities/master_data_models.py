"""
Master Data Models - Payment Methods, Enhanced Tax Classes, Customer Groups, etc.
These are cross-cutting master data used across multiple modules.
"""

from django.db import models
from django.utils import timezone


class PaymentMethod(models.Model):
    """
    Payment methods available for transactions (POS, Sales, etc.)
    D365 Equivalent: RetailTenderTypeTable
    """
    class PaymentType(models.TextChoices):
        CASH = 'CASH', 'Cash'
        CARD = 'CARD', 'Card (Credit/Debit)'
        UPI = 'UPI', 'UPI'
        WALLET = 'WALLET', 'Digital Wallet'
        BANK_TRANSFER = 'BANK_TRANSFER', 'Bank Transfer'
        GIFT_CARD = 'GIFT_CARD', 'Gift Card/Voucher'
        CREDIT = 'CREDIT', 'Credit/Account'

    company = models.ForeignKey('Company', on_delete=models.PROTECT, related_name='payment_methods')
    payment_code = models.CharField(max_length=20)
    payment_name = models.CharField(max_length=100)
    
    payment_type = models.CharField(max_length=20, choices=PaymentType.choices)
    
    # POS Integration
    is_pos_enabled = models.BooleanField(default=True, help_text="Available in POS")
    requires_approval = models.BooleanField(default=False)
    open_cash_drawer = models.BooleanField(default=False, help_text="Open cash drawer when selected")
    
    # Limits
    min_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    max_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    # Accounting
    gl_account = models.CharField(max_length=50, null=True, blank=True, help_text="General Ledger account code")
    
    # Display
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    icon_name = models.CharField(max_length=50, null=True, blank=True, help_text="Icon identifier for UI")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'business_entities'
        db_table = 'be_payment_method'
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'
        ordering = ['display_order', 'payment_name']
        unique_together = [['company', 'payment_code']]

    def __str__(self):
        return f"{self.payment_name} ({self.payment_type})"


class TaxClassEnhanced(models.Model):
    """
    Enhanced Tax Class with GST support for India
    D365 Equivalent: TaxTable
    """
    class TaxType(models.TextChoices):
        GST = 'GST', 'GST (India)'
        VAT = 'VAT', 'VAT'
        SALES_TAX = 'SALES_TAX', 'Sales Tax'
        EXEMPT = 'EXEMPT', 'Tax Exempt'

    company = models.ForeignKey('Company', on_delete=models.PROTECT, related_name='tax_classes_enhanced')
    tax_code = models.CharField(max_length=20)
    tax_name = models.CharField(max_length=100)
    
    tax_type = models.CharField(max_length=20, choices=TaxType.choices, default=TaxType.GST)
    
    # Standard tax rate
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Total tax rate (e.g., 18.00 for 18%)")
    
    # India GST specific (CGST + SGST = IGST)
    cgst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Central GST rate")
    sgst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="State GST rate")
    igst_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Integrated GST rate")
    
    # Accounting
    tax_gl_account = models.CharField(max_length=50, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'business_entities'
        db_table = 'be_tax_class_enhanced'
        verbose_name = 'Tax Class (Enhanced)'
        verbose_name_plural = 'Tax Classes (Enhanced)'
        ordering = ['tax_rate', 'tax_name']
        unique_together = [['company', 'tax_code']]

    def __str__(self):
        return f"{self.tax_name} ({self.tax_rate}%)"


class CustomerGroup(models.Model):
    """
    Customer segmentation for pricing and terms
    D365 Equivalent: CustGroup
    """
    company = models.ForeignKey('Company', on_delete=models.PROTECT, related_name='customer_groups')
    group_code = models.CharField(max_length=20)
    group_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # Pricing
    default_price_list = models.ForeignKey('company.PriceList', on_delete=models.PROTECT, null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Default discount for this group")
    
    # Terms
    payment_terms = models.CharField(max_length=50, null=True, blank=True, help_text="e.g., Net 30, Net 45")
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'business_entities'
        db_table = 'be_customer_group'
        verbose_name = 'Customer Group'
        verbose_name_plural = 'Customer Groups'
        ordering = ['group_name']
        unique_together = [['company', 'group_code']]

    def __str__(self):
        return self.group_name


class Promotion(models.Model):
    """
    Promotional pricing and discounts
    D365 Equivalent: RetailDiscountTable
    """
    class PromotionType(models.TextChoices):
        PERCENTAGE = 'PERCENTAGE', 'Percentage Discount'
        FIXED_AMOUNT = 'FIXED_AMOUNT', 'Fixed Amount Off'
        BUY_X_GET_Y = 'BUY_X_GET_Y', 'Buy X Get Y'
        BUNDLE = 'BUNDLE', 'Bundle Discount'
        QUANTITY_BASED = 'QUANTITY_BASED', 'Quantity Based'

    company = models.ForeignKey('Company', on_delete=models.PROTECT, related_name='promotions')
    promotion_code = models.CharField(max_length=20)
    promotion_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    promotion_type = models.CharField(max_length=20, choices=PromotionType.choices)
    
    # Discount Value
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="For percentage discounts")
    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0, help_text="For fixed amount discounts")
    
    # Buy X Get Y
    buy_quantity = models.IntegerField(null=True, blank=True, help_text="Buy this many")
    get_quantity = models.IntegerField(null=True, blank=True, help_text="Get this many free/discounted")
    
    # Validity
    start_date = models.DateField()
    end_date = models.DateField()
    
    # Applicability
    applies_to_all_items = models.BooleanField(default=False)
    applies_to_categories = models.ManyToManyField('company.Category', blank=True)
    applies_to_items = models.ManyToManyField('company.ItemMaster', blank=True)
    
    # Conditions
    min_purchase_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    min_quantity = models.IntegerField(null=True, blank=True)
    
    # Limits
    max_uses_total = models.IntegerField(null=True, blank=True, help_text="Total times this can be used")
    max_uses_per_customer = models.IntegerField(null=True, blank=True)
    current_uses = models.IntegerField(default=0)
    
    # Channels
    is_pos_enabled = models.BooleanField(default=True)
    is_online_enabled = models.BooleanField(default=True)
    
    # Priority
    priority = models.IntegerField(default=0, help_text="Higher priority promotions apply first")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'business_entities'
        db_table = 'be_promotion'
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'
        ordering = ['-priority', 'promotion_name']
        unique_together = [['company', 'promotion_code']]

    def __str__(self):
        return f"{self.promotion_name} ({self.promotion_type})"


class LoyaltyProgram(models.Model):
    """
    Customer Loyalty Program configuration
    D365 Equivalent: RetailLoyaltySchemeTable
    """
    company = models.ForeignKey('Company', on_delete=models.PROTECT, related_name='loyalty_programs')
    program_code = models.CharField(max_length=20)
    program_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # Earning Rules
    points_per_currency = models.DecimalField(max_digits=5, decimal_places=2, help_text="Points earned per ₹100 spent")
    min_transaction_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Redemption Rules
    redemption_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="₹ value per point")
    min_points_for_redemption = models.IntegerField(default=100)
    max_redemption_percent = models.DecimalField(max_digits=5, decimal_places=2, default=100, help_text="Max % of transaction that can be paid with points")
    
    # Tiers
    has_tiers = models.BooleanField(default=False)
    tier_config = models.JSONField(null=True, blank=True, help_text="Tier thresholds and benefits")
    
    # Validity
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    points_expiry_months = models.IntegerField(null=True, blank=True, help_text="Points expire after X months")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'business_entities'
        db_table = 'be_loyalty_program'
        verbose_name = 'Loyalty Program'
        verbose_name_plural = 'Loyalty Programs'
        ordering = ['program_name']
        unique_together = [['company', 'program_code']]

    def __str__(self):
        return self.program_name


class CustomerLoyalty(models.Model):
    """
    Customer enrollment in loyalty program
    D365 Equivalent: RetailLoyaltyCardTable
    """
    class Tier(models.TextChoices):
        BRONZE = 'BRONZE', 'Bronze'
        SILVER = 'SILVER', 'Silver'
        GOLD = 'GOLD', 'Gold'
        PLATINUM = 'PLATINUM', 'Platinum'

    customer = models.OneToOneField('company.OperationalCustomer', on_delete=models.CASCADE, related_name='loyalty')
    program = models.ForeignKey(LoyaltyProgram, on_delete=models.PROTECT, related_name='enrollments')
    
    # Card Details
    loyalty_card_number = models.CharField(max_length=50, unique=True, db_index=True)
    
    # Points
    points_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    lifetime_points_earned = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    lifetime_points_redeemed = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Tier
    current_tier = models.CharField(max_length=20, choices=Tier.choices, default=Tier.BRONZE)
    tier_qualifying_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0, help_text="Amount spent for tier qualification")
    
    # Dates
    enrolled_date = models.DateField(default=timezone.now)
    last_transaction_date = models.DateField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'business_entities'
        db_table = 'be_customer_loyalty'
        verbose_name = 'Customer Loyalty'
        verbose_name_plural = 'Customer Loyalty'
        ordering = ['-points_balance']

    def __str__(self):
        return f"{self.customer.customer_name} - {self.loyalty_card_number} ({self.points_balance} pts)"




