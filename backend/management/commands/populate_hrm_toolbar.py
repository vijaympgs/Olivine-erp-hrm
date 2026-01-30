"""
Django management command to populate toolbar columns for HRM_EMPLOYEE_MASTER
"""
from django.core.management.base import BaseCommand
from core.auth_access.backend.user_management.models import ERPMenuItem

class Command(BaseCommand):
    help = 'Populate toolbar columns for HRM_EMPLOYEE_MASTER menu item'

    def handle(self, *args, **options):
        try:
            menu_item = ERPMenuItem.objects.get(menu_id='HRM_EMPLOYEE_MASTER')
            
            # Set mode-specific toolbar configurations
            menu_item.toolbar_list = 'NRQFVIOX'  # New, Refresh, Query, Filter, View, Import, Export, Exit
            menu_item.toolbar_view = 'X'  # Exit only
            menu_item.toolbar_edit = 'SCX'  # Save, Cancel, Exit
            menu_item.toolbar_create = 'SCX'  # Save, Cancel, Exit
            
            menu_item.save()
            
            self.stdout.write(self.style.SUCCESS('✅ Successfully populated toolbar columns for HRM_EMPLOYEE_MASTER:'))
            self.stdout.write(f'   toolbar_list: {menu_item.toolbar_list}')
            self.stdout.write(f'   toolbar_view: {menu_item.toolbar_view}')
            self.stdout.write(f'   toolbar_edit: {menu_item.toolbar_edit}')
            self.stdout.write(f'   toolbar_create: {menu_item.toolbar_create}')
            
        except ERPMenuItem.DoesNotExist:
            self.stdout.write(self.style.ERROR('❌ Error: HRM_EMPLOYEE_MASTER menu item not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error: {e}'))
