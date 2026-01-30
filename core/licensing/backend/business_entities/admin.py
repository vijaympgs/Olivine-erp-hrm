from django.contrib import admin
from .models import Company
from .master_data_models import (
    PaymentMethod, TaxClassEnhanced, CustomerGroup,
    Promotion, LoyaltyProgram, CustomerLoyalty
)

# ==============================================================================
# ARCHITECTURAL LOCK ENFORCEMENT
# ==============================================================================
# ⚠️ ALL OPERATIONAL MODELS HAVE BEEN MOVED TO domain.company
#
# This admin file now contains ONLY:
# 1. Company (for licensing/tenancy)
# 2. Master data models (PaymentMethod, TaxClass, etc.)
#
# For operational models (ItemMaster, Supplier, Customer, Location, etc.):
# See: backend/domain/company/admin.py
#
# RULE: business_entities = LICENSING METADATA ONLY
# RULE: domain.company = OPERATIONAL MASTERS ONLY
# ==============================================================================

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    🏢 COMPANY (LICENSING METADATA)
    
    Represents a legal/business entity for licensing purposes.
    This is the ONLY operational model allowed in business_entities.
    
    ⚠️ Platform Admin Only
    """
    list_display = ('code', 'name', 'legal_entity_type', 'default_currency', 'status', 'governance_indicator')
    search_fields = ('code', 'name')
    list_filter = ('status', 'legal_entity_type')
    
    fieldsets = (
        ('🏢 Company Identification', {
            'fields': ('code', 'name', 'legal_entity_type'),
            'description': 'Legal business entity for licensing'
        }),
        ('Business Details', {
            'fields': ('default_currency', 'timezone', 'country', 'status')
        }),
        ('Address', {
            'fields': ('address_line1', 'address_line2', 'city', 'state', 'postal_code', 'address_country'),
            'classes': ('collapse',)
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def governance_indicator(self, obj):
        return "🔒 Platform Only"
    governance_indicator.short_description = "Access Level"
    
    def has_module_permission(self, request):
        return request.user.is_superuser  # Platform admin only


# ==============================================================================
# MASTER DATA MODELS (Extensions)
# ==============================================================================

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('payment_name', 'payment_type', 'company', 'is_active')
    list_filter = ('company', 'is_active')


@admin.register(TaxClassEnhanced)
class TaxClassEnhancedAdmin(admin.ModelAdmin):
    list_display = ('tax_name', 'tax_code', 'tax_rate', 'is_active')


@admin.register(CustomerGroup)
class CustomerGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'company', 'discount_percent')


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('promotion_name', 'company', 'start_date', 'end_date', 'is_active')


@admin.register(LoyaltyProgram)
class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'company', 'is_active')


@admin.register(CustomerLoyalty)
class CustomerLoyaltyAdmin(admin.ModelAdmin):
    list_display = ('customer', 'program', 'points_balance')




