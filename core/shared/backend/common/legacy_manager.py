from django.db import models
from django.core.exceptions import ValidationError

class LegacyReadonlyQuerySet(models.QuerySet):
    def update(self, *args, **kwargs):
        raise ValidationError("Legacy model write operation (update) is blocked. Use Canonical model domain.business_entities / hr.")
    
    def delete(self, *args, **kwargs):
        raise ValidationError("Legacy model delete() is blocked.")
        
    def bulk_create(self, *args, **kwargs):
        raise ValidationError("Legacy model bulk_create() is blocked.")
        
    def bulk_update(self, *args, **kwargs):
        raise ValidationError("Legacy model bulk_update() is blocked.")

class LegacyReadonlyManager(models.Manager):
    def get_queryset(self):
        return LegacyReadonlyQuerySet(self.model, using=self._db)

    def create(self, **kwargs):
        raise ValidationError("Legacy model create() is blocked.")
        
    def bulk_create(self, *args, **kwargs):
        raise ValidationError("Legacy model bulk_create() is blocked.")
        
    def bulk_update(self, *args, **kwargs):
        raise ValidationError("Legacy model bulk_update() is blocked.")




