"""
Business Entities Views
"""
from rest_framework import viewsets, status, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


from .models import Company
from .master_data_models import CustomerGroup, LoyaltyProgram
from .serializers import CompanySerializer, CustomerGroupSerializer, LoyaltyProgramSerializer


# OperatingCompanyViewSet REMOVED - OperatingCompany concept deleted

class CompanyViewSet(viewsets.ModelViewSet):
    """
    Company ViewSet for business_entities.Company
    This is the authoritative source for companies used in login
    """
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'legal_entity_type']
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'code', 'created_at']
    ordering = ['name']
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only active companies"""
        active_companies = self.queryset.filter(status='ACTIVE')
        serializer = self.get_serializer(active_companies, many=True)
        return Response(serializer.data)


class CustomerGroupViewSet(viewsets.ModelViewSet):
    """
    CustomerGroup ViewSet for simple customer segmentation
    Used in Code Masters UI
    """
    permission_classes = [permissions.AllowAny]
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['company', 'is_active']
    search_fields = ['group_code', 'group_name']
    ordering_fields = ['group_name', 'created_at']
    ordering = ['group_name']
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        """Activate a customer group"""
        group = self.get_object()
        group.is_active = True
        group.save()
        serializer = self.get_serializer(group)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        """Deactivate a customer group"""
        group = self.get_object()
        group.is_active = False
        group.save()
        serializer = self.get_serializer(group)
        return Response(serializer.data)


class LoyaltyProgramViewSet(viewsets.ModelViewSet):
    """
    LoyaltyProgram ViewSet for simple loyalty program management
    Used in Code Masters UI
    """
    permission_classes = [permissions.AllowAny]
    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['company', 'is_active']
    search_fields = ['program_code', 'program_name']
    ordering_fields = ['program_name', 'created_at']
    ordering = ['program_name']
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        """Activate a loyalty program"""
        program = self.get_object()
        program.is_active = True
        program.save()
        serializer = self.get_serializer(program)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        """Deactivate a loyalty program"""
        program = self.get_object()
        program.is_active = False
        program.save()
        serializer = self.get_serializer(program)
        return Response(serializer.data)





