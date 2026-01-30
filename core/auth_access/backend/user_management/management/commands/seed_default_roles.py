"""
Management command to seed default roles for the permission system
"""
from django.core.management.base import BaseCommand
from core.auth_access.backend.user_management.models import Role


class Command(BaseCommand):
    help = 'Seeds default roles for the retail permission system'

    def handle(self, *args, **options):
        self.stdout.write('Seeding default roles...')

        # Define FIXED system roles based on the ROLE-USER separation model
        # RULES:
        # - Roles are seeded and protected
        # - Roles must NOT be created/edited/deleted via UI
        # - is_system_role=True means the role is protected
        default_roles = [
            {
                'role_key': 'admin',
                'role_name': 'Administrator',
                'description': 'Full access to all modules and admin features',
                'is_system_role': True  # Protected - cannot be deleted/edited via UI
            },
            {
                'role_key': 'backofficemanager',
                'role_name': 'Back Office Manager',
                'description': 'Back office operations, approvals (Procurement, Inventory, Pricing, etc.)',
                'is_system_role': True  # Protected
            },
            {
                'role_key': 'backofficeuser',
                'role_name': 'Back Office User',
                'description': 'Back office screens (read/write as permitted), no approvals',
                'is_system_role': True  # Protected
            },
            {
                'role_key': 'posmanager',
                'role_name': 'POS Manager',
                'description': 'POS configuration, day open/close, reconciliation, terminal management',
                'is_system_role': True  # Protected
            },
            {
                'role_key': 'posuser',
                'role_name': 'POS User',
                'description': 'POS billing, on-the-fly customer/item creation (as configured), no admin access',
                'is_system_role': True  # Protected
            },
            # Legacy roles - kept for backward compatibility but not protected
            {
                'role_key': 'manager',
                'role_name': 'Manager',
                'description': 'General management role with elevated permissions (legacy)',
                'is_system_role': False
            },
            {
                'role_key': 'staff',
                'role_name': 'Staff',
                'description': 'Standard staff role with basic permissions (legacy)',
                'is_system_role': False
            }
        ]

        created_count = 0
        updated_count = 0

        for role_data in default_roles:
            role, created = Role.objects.update_or_create(
                role_key=role_data['role_key'],
                defaults={
                    'role_name': role_data['role_name'],
                    'description': role_data['description'],
                    'is_system_role': role_data['is_system_role'],
                    'is_active': True
                }
            )

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Created role: {role.role_name}")
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Updated role: {role.role_name}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nRole seeding complete! Created: {created_count}, Updated: {updated_count}'
            )
        )




