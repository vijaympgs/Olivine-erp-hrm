from django.contrib import admin
from .models import FeatureFlag

@admin.register(FeatureFlag)
class FeatureFlagAdmin(admin.ModelAdmin):
    list_display = ("key", "is_global_enabled", "is_active")
    search_fields = ("key",)
    filter_horizontal = ("companies",)



