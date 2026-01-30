from rest_framework import serializers
from core.org_structure.backend.company.models import UnitOfMeasure


class UnitOfMeasureSerializer(serializers.ModelSerializer):
    """Serializer for Unit of Measure"""
    company_name = serializers.CharField(source='company.company_name', read_only=True)
    
    class Meta:
        model = UnitOfMeasure
        fields = [
            'id', 'company', 'company_name', 'uom_code', 'uom_name', 
            'uom_type', 'decimal_allowed', 'rounding_precision',
            'is_core_uom', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'company_name']
    
    def validate_uom_code(self, value):
        """Ensure UOM code is uppercase"""
        return value.upper() if value else value




