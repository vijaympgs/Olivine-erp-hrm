from rest_framework import serializers

from .models import OperationalCompany as Company


class CompanySerializer(serializers.ModelSerializer):
    """
    Company serializer for CRUD operations
    HRM-only: Minimal serializer for HRM module
    """
    company_code = serializers.CharField(source='code')
    company_name = serializers.CharField(source='name')
    
    class Meta:
        model = Company
        fields = [
            'id',
            'company_code',
            'company_name', 
            'legal_entity_type',
            'address',
            'default_currency',
            'timezone',
            'status',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_company_code(self, value):
        """Validate company code uniqueness"""
        if value:
            # Check if code already exists (excluding current instance during update)
            queryset = Company.objects.filter(code=value)
            if self.instance:
                queryset = queryset.exclude(id=self.instance.id)
            
            if queryset.exists():
                raise serializers.ValidationError("Company code must be unique.")
        
        return value
    
    def validate(self, attrs):
        """Cross-field validation"""
        # If trying to set status to INACTIVE, ensure at least one active company remains
        if attrs.get('status') == 'INACTIVE':
            active_companies = Company.objects.filter(status='ACTIVE')
            if self.instance:
                active_companies = active_companies.exclude(id=self.instance.id)
            
            if not active_companies.exists():
                raise serializers.ValidationError({
                    'status': 'At least one active company must exist in the system.'
                })
        
        return attrs


class CompanyListSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for list views
    HRM-only: Minimal list serializer for HRM module
    """
    company_code = serializers.CharField(source='code')
    company_name = serializers.CharField(source='name')
    
    class Meta:
        model = Company
        fields = [
            'id',
            'company_code',
            'company_name',
            'legal_entity_type', 
            'default_currency',
            'status'
        ]


# Note: LocationSerializer removed - Location is Retail-only model
# Note: All other serializers (Attribute, Item, PriceList, etc.) removed - Retail/FMS/CRM only
