from django.core.management.base import BaseCommand
from core.org_structure.backend.company.models import ItemMaster
from django.utils.crypto import get_random_string
from django.utils.timezone import now

class Command(BaseCommand):
    help = 'Create 30 dummy ItemMaster records if less than 30 exist'

    def handle(self, *args, **kwargs):
        count = ItemMaster.objects.count()
        print(f'Current ItemMaster count: {count}')
        if count >= 30:
            self.stdout.write('At least 30 ItemMaster records already exist. Exiting.')
            return

        for i in range(30 - count):
            sku = f'DUMMY-{get_random_string(5).upper()}'
            name = f'Dummy Product {i + 1}'
            item = ItemMaster(
                company_id=1,  # Update with valid Company ID
                item_code=sku,
                item_name=name,
                short_name=name[:15],
                item_type='STOCKED',
                attribute_template_id=None,  # Optional
                category_id=None,  # Optional
                brand_id=None,  # Optional
                stock_uom_id=1,  # Update with valid UOM ID
                status='Active',
                created_at=now(),
                updated_at=now()
            )
            item.save()
            self.stdout.write(f'Created {name} with SKU {sku}')

        self.stdout.write('Dummy ItemMaster creation complete.')




