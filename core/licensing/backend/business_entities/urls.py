from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, CustomerGroupViewSet, LoyaltyProgramViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'customer-groups', CustomerGroupViewSet, basename='customer-group')
router.register(r'loyalty-programs', LoyaltyProgramViewSet, basename='loyalty-program')



urlpatterns = [
    path('', include(router.urls)),
]



