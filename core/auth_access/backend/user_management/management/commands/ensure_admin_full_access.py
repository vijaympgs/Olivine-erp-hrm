from django.core.management.base import BaseCommand
from core.auth_access.backend.user_management.models import Role, ERPMenuItem, RolePermission
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Ensures the admin role has full character-based permissions for all menu items.'

    def handle(self, *args, **options):
        self.stdout.write('Checking admin role permissions integrity...')

        # 1. Identify Admin Role
        # Look for role_key='admin' or role_name contains 'Admin'
        admin_role = Role.objects.filter(role_key='admin').first()
        if not admin_role:
            admin_role = Role.objects.filter(role_name__icontains='Admin').first()

        if not admin_role:
            self.stdout.write(self.style.ERROR('Admin role not found! Please seed roles first.'))
            return

        self.stdout.write(f'Using admin role: {admin_role.role_name} (key: {admin_role.role_key})')

        # 2. Iterate through all ERPMenuItems
        menu_items = ERPMenuItem.objects.all()
        processed_count = 0
        updated_count = 0
        created_count = 0

        for item in menu_items:
            # Full permissions = all 1s for the length of the applicable toolbar
            toolbar_string = item.applicable_toolbar_config or ""
            if not toolbar_string:
                continue
                
            full_mask = '1' * len(toolbar_string)
            
            # Use update_or_create to ensure record exists and has full mask
            role_perm, created = RolePermission.objects.update_or_create(
                role=admin_role,
                menu_item=item,
                defaults={
                    'toolbar_string': toolbar_string,
                    'toolbar_permissions': full_mask,
                    'can_access': True,
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': True,
                }
            )
            
            processed_count += 1
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Success: Processed {processed_count} menu items for Admin.'
        ))
        self.stdout.write(f'Created: {created_count}, Updated: {updated_count}')

        # 3. Optional: Ensure the 'admin' user is actually assigned to this role
        admin_user = User.objects.filter(username='admin').first()
        if admin_user:
            from core.auth_access.backend.user_management.models import UserRole
            user_role, created = UserRole.objects.get_or_create(
                user=admin_user,
                role=admin_role,
                defaults={'is_active': True}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Assigned user 'admin' to role '{admin_role.role_name}'"))




