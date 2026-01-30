"""
Employee Self-Service URL Configuration
Following BBP 1.3 Employee Self-Service specifications
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.employee_self_service import (
    EmployeeChangeRequestViewSet, ESSServiceCatalogViewSet, ESSServiceRequestViewSet,
    ESSDashboardViewSet, ESSAnalyticsViewSet
)

router = DefaultRouter()
router.register(r'change-requests', EmployeeChangeRequestViewSet, basename='change-requests')
router.register(r'services', ESSServiceCatalogViewSet, basename='services')
router.register(r'service-requests', ESSServiceRequestViewSet, basename='service-requests')
router.register(r'dashboard', ESSDashboardViewSet, basename='dashboard')
router.register(r'analytics', ESSAnalyticsViewSet, basename='analytics')

app_name = 'ess'
urlpatterns = [
    path('', include(router.urls),
]
