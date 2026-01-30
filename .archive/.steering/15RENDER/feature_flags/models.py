from django.db import models
from domain.company.models import Company

class FeatureFlag(models.Model):
    key = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_global_enabled = models.BooleanField(default=False)
    companies = models.ManyToManyField(Company, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.key



