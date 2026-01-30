from rest_framework import serializers
from .models import Company
from .master_data_models import CustomerGroup, LoyaltyProgram



class AddressSerializer(serializers.Serializer):
    line1 = serializers.CharField(required=False, allow_blank=True)
    line2 = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(required=False, allow_blank=True)
    postalCode = serializers.CharField(
        required=False, allow_blank=True
    )
    country = serializers.CharField(required=False, allow_blank=True)


class CompanySerializer(serializers.ModelSerializer):
    # nested, SPA-facing address object
    address = AddressSerializer(required=False)

    class Meta:
        model = Company
        fields = [
            "id",
            "code",
            "name",
            "legal_entity_type",
            "country",
            "default_currency",
            "timezone",
            "status",
            "address",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def to_representation(self, instance: Company):
        data = super().to_representation(instance)
        data["address"] = instance.address_dict
        return data

    def create(self, validated_data):
        address_data = validated_data.pop("address", {}) or {}

        company = Company.objects.create(
            **validated_data,
            address_line1=address_data.get("line1", ""),
            address_line2=address_data.get("line2", ""),
            city=address_data.get("city", ""),
            state=address_data.get("state", ""),
            postal_code=address_data.get("postalCode", ""),
            address_country=address_data.get("country", ""),
        )
        return company

    def update(self, instance: Company, validated_data):
        address_data = validated_data.pop("address", None)

        # Simple field updates
        for field, value in validated_data.items():
            setattr(instance, field, value)

        # Address mapping
        if address_data is not None:
            instance.address_line1 = address_data.get("line1", instance.address_line1)
            instance.address_line2 = address_data.get("line2", instance.address_line2)
            instance.city = address_data.get("city", instance.city)
            instance.state = address_data.get("state", instance.state)
            instance.postal_code = address_data.get("postalCode", instance.postal_code)
            instance.address_country = address_data.get(
                "country", instance.address_country
            )

        instance.save()
        return instance

    def validate(self, attrs):
        """
        Optional: enforce 'last active company' rule here later.
        For now, just pass through.
        """
        return super().validate(attrs)


# OperatingCompanySerializer REMOVED - OperatingCompany concept deleted


# ==============================================================================
# CUSTOMER GROUP & LOYALTY PROGRAM SERIALIZERS
# ==============================================================================

class CustomerGroupSerializer(serializers.ModelSerializer):
    """Serializer for CustomerGroup model"""
    company_name = serializers.CharField(source='company.name', read_only=True)
    
    class Meta:
        model = CustomerGroup
        fields = [
            'id',
            'company',
            'company_name',
            'group_code',
            'group_name',
            'description',
            'default_price_list',
            'discount_percent',
            'payment_terms',
            'credit_limit',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'company_name', 'created_at', 'updated_at']


class LoyaltyProgramSerializer(serializers.ModelSerializer):
    """Serializer for LoyaltyProgram model"""
    company_name = serializers.CharField(source='company.name', read_only=True)
    
    class Meta:
        model = LoyaltyProgram
        fields = [
            'id',
            'company',
            'company_name',
            'program_code',
            'program_name',
            'description',
            'points_per_currency',
            'min_transaction_amount',
            'redemption_rate',
            'min_points_for_redemption',
            'max_redemption_percent',
            'has_tiers',
            'tier_config',
            'start_date',
            'end_date',
            'points_expiry_months',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'company_name', 'created_at', 'updated_at']




