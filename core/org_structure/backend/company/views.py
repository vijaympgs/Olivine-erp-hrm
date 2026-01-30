from rest_framework import viewsets, status, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import (
    OperationalCompany,
    # Location,  # Retail-only model - removed
    # Attribute,  # Retail/FMS/CRM only - removed
    # AttributeValue,  # Retail/FMS/CRM only - removed
    # ProductAttributeTemplate,  # Retail/FMS/CRM only - removed
    # UnitOfMeasure,  # Retail/FMS/CRM only - removed
    # UOMConversion,  # Retail/FMS/CRM only - removed
    # Item,  # Retail/FMS/CRM only - removed
    # ItemMaster,  # Retail/FMS/CRM only - removed
    # ItemVariant,  # Retail/FMS/CRM only - removed
    # PriceList,  # Retail/FMS/CRM only - removed
    # OperationalCustomer as Customer,  # Retail/FMS/CRM only - removed
    # OperationalSupplier as Supplier,  # Retail/FMS/CRM only - removed
    # Category,  # Retail/FMS/CRM only - removed
    # Brand,  # Retail/FMS/CRM only - removed
)

from .serializers import (
    CompanySerializer,
    CompanyListSerializer,
    # LocationSerializer,  # Retail-only - removed
    # LocationListSerializer,  # Retail-only - removed
    # All other serializers removed - Retail/FMS/CRM only
)


class StandardResultsSetPagination(PageNumberPagination):
    """Standard pagination for all ViewSets"""
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Company ViewSet providing CRUD operations with filtering and search
    HRM-only: Minimal ViewSet for HRM module
    """
    permission_classes = [permissions.AllowAny]
    queryset = OperationalCompany.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'legal_entity_type']
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'code', 'created_at']
    ordering = ['name']

    def get_serializer_class(self):
        """Use different serializers for list vs detail views"""
        if self.action == 'list':
            return CompanyListSerializer
        return CompanySerializer

    def perform_create(self, serializer):
        """Custom create logic"""
        serializer.save()

    def perform_update(self, serializer):
        """Custom update logic with currency change confirmation"""
        # In a real implementation, you might want to track currency changes
        # and require additional confirmation for system-wide impacts
        serializer.save()

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only active companies"""
        active_companies = self.queryset.filter(status='ACTIVE')
        serializer = CompanyListSerializer(active_companies, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        """Safely deactivate a company with validation"""
        company = self.get_object()

        # Check if this is the last active company
        other_active = OperationalCompany.objects.filter(status='ACTIVE').exclude(id=company.id)
        if not other_active.exists():
            return Response(
                {'error': 'Cannot deactivate the last active company in the system.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        company.status = 'INACTIVE'
        company.save()

        serializer = self.get_serializer(company)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        """Activate a company"""
        company = self.get_object()
        company.status = 'ACTIVE'
        company.save()

        serializer = self.get_serializer(company)
        return Response(serializer.data)


# Note: LocationViewSet removed - Location is Retail-only model
# Note: All other ViewSets removed - Retail/FMS/CRM only
