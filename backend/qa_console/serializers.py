
from rest_framework import serializers
from .models import TestReadiness

class TestReadinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReadiness
        fields = '__all__'




