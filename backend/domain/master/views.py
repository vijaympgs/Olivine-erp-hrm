from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from core.org_structure.backend.company.models import UnitOfMeasure
from .serializers import UnitOfMeasureSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


from rest_framework.decorators import action

class UnitOfMeasureViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Unit of Measure (UOM) management
    
    Provides CRUD operations for UOMs with filtering by:
    - company_id
    - uom_type
    - include_inactive (boolean)
    - search (code or name)
    """
    serializer_class = UnitOfMeasureSerializer
    permission_classes = [AllowAny]  # TODO: Add proper authentication
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['company', 'uom_type', 'is_active']
    search_fields = ['uom_code', 'uom_name']
    ordering_fields = ['uom_code', 'uom_name', 'created_at']
    ordering = ['uom_code']
    
    def get_queryset(self):
        """
        Filter queryset based on query parameters
        """
        queryset = UnitOfMeasure.objects.select_related('company').all()
        
        # Filter by company
        company_id = self.request.query_params.get('company_id', None)
        if company_id:
            queryset = queryset.filter(company_id=company_id)
        
        # Filter by active status
        include_inactive = self.request.query_params.get('include_inactive', 'false').lower() == 'true'
        if not include_inactive:
            queryset = queryset.filter(is_active=True)
        
        return queryset

    def _get_uom_usage(self, instance):
        """
        Check if UOM is referred by any Item, Variant or Conversion
        """
        return (
            instance.items_as_stock_uom.exists() or
            instance.variants_as_stock_uom.exists() or
            instance.variants_as_sales_uom.exists() or
            instance.variants_as_purchase_uom.exists() or
            instance.conversions_from.exists() or
            instance.conversions_to.exists()
        )

    @action(detail=True, methods=['get'])
    def check_usage(self, request, pk=None):
        """
        Check if the UOM is in use and return the result.
        Used by UI to decide whether to show deactivation modal.
        """
        instance = self.get_object()
        in_use = self._get_uom_usage(instance)
        return Response({"in_use": in_use})

    def destroy(self, request, *args, **kwargs):
        """
        Custom destroy: Deactivate UOM instead of hard delete
        Checks business rules before deactivation.
        """
        instance = self.get_object()
        
        if self._get_uom_usage(instance):
            return Response(
                {"error": "This UOM is currently in use by existing items or conversions and cannot be deactivated."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)




