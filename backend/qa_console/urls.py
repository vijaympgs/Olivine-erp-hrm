
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestReadinessViewSet

router = DefaultRouter()
router.register(r'readiness', TestReadinessViewSet)

urlpatterns = [
    path('', include(router.urls)),
]




