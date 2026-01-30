from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from core.org-structure.backend.company.views import ItemVariantViewSet  # TODO: Fix import path
from .views import UnitOfMeasureViewSet

router = DefaultRouter()
# router.register(r'variants', ItemVariantViewSet, basename='variant')  # TODO: Fix import
router.register(r'uoms', UnitOfMeasureViewSet, basename='uom')

urlpatterns = [
    path('', include(router.urls)),
]




