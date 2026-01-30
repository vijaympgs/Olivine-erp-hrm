from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet,
    # LocationViewSet,  # Retail-only - removed
    # AttributeViewSet,  # Retail/FMS/CRM only - removed
    # AttributeValueViewSet,  # Retail/FMS/CRM only - removed
    # ProductAttributeTemplateViewSet,  # Retail/FMS/CRM only - removed
    # UnitOfMeasureViewSet,  # Retail/FMS/CRM only - removed
    # UOMConversionViewSet,  # Retail/FMS/CRM only - removed
    # ItemViewSet,  # Retail/FMS/CRM only - removed
    # ItemVariantViewSet,  # Retail/FMS/CRM only - removed
    # PriceListViewSet,  # Retail/FMS/CRM only - removed
    # CustomerViewSet,  # Retail/FMS/CRM only - removed
    # SupplierViewSet,  # Retail/FMS/CRM only - removed
    # CategoryViewSet,  # Retail/FMS/CRM only - removed
    # BrandViewSet,  # Retail/FMS/CRM only - removed
)

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
# All other ViewSet registrations removed - Retail/FMS/CRM only

urlpatterns = [
    path('api/', include(router.urls)),
]
