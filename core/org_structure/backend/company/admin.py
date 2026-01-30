"""
Company Admin Configuration for HRM-only mode

All Retail-specific models (items, suppliers, customers, brands, categories, etc.) 
have been removed as they are not required for HRM functionality.
"""

from django.contrib import admin

# No models registered for HRM-only mode
# All Retail-specific models (Category, Brand, TaxClass, ItemMaster, 
# OperationalSupplier, OperationalCustomer, Attribute, AttributeValue, 
# UnitOfMeasure, PriceList, ProductAttributeTemplate, ProductAttributeTemplateLine)
# are not needed for HRM functionality
