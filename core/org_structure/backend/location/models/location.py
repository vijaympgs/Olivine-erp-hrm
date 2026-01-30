from django.db import models
import uuid
from core.licensing.backend.business_entities.models import Company

class Location(models.Model):
    class Type(models.TextChoices):
        STORE = 'STORE', 'Store'
        WAREHOUSE = 'WAREHOUSE', 'Warehouse'
        OFFICE = 'OFFICE', 'Office'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='locations')
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    location_type = models.CharField(max_length=20, choices=Type.choices)
    address = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'master_location'
        unique_together = ('company', 'code')
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['code']

    def __str__(self):
        return f"{self.name} ({self.code})"




