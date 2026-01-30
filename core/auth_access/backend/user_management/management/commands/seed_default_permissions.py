"""
Management command to seed default permissions for roles
"""
from django.core.management.base import BaseCommand
from core.auth_access.backend.user_management.models import Role, MenuItemType, RolePermission


class Command(BaseCommand):
    help = 'Seeds default permissions for roles in the retail permission system'

    def handle(self, *args, **options):
        self.stdout.write('Seeding default permissions...')

        # Define permission templates for each role
        permission_templates = {
            'administrator': {
                'description': 'Full access to all retail menu items',
                'permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': True
                }
            },
            'pos_manager': {
                'description': 'POS management with store operations oversight',
                'permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': False  # Limited delete access
                }
            },
            'pos_user': {
                'description': 'Basic POS operations',
                'permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': False,
                    'can_delete': False
                }
            },
            'back_office_manager': {
                'description': 'Back office management access',
                'permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': True
                }
            },
            'back_office_user': {
                'description': 'Standard back office access',
                'permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': False
                }
            },
            'manager': {
                'description': 'General management access',
                'permissions': {
                    'can_view': True,
                    'can_create': True,
                    'can_edit': True,
                    'can_delete': False
                }
            },
            'staff': {
                'description': 'Basic staff access',
                'permissions': {
                    'can_view': True,
                    'can_create': False,
                    'can_edit': False,
                    'can_delete': False
                }
            }
        }

        # Special permission overrides for specific menu items and roles
        special_permissions = {
            'pos_user': {
                # POS users should have limited access to certain areas
                'user-permissions': {
                    'can_view': False,
                    'can_create': False,
                    'can_edit': False,
                    'can_delete': False
                },
                'organization-setup': {
                    'can_view': False,
                    'can_create': False,
                    'can_edit': False,
                    'can_delete': False
                }
            },
            'staff': {
                # Staff should have very limited access
                'user-permissions': {
                    'can_view': False,
                    'can_create': False,
                    'can_edit': False,
                    'can_delete': False
                },
                'organization-setup': {
                    'can_view': False,
                    'can_create': False,
                    'can_edit': False,
                    'can_delete': False
                },
                'procurement': {
                    'can_view': False,
                    'can_create': False,
                    'can_edit': False,
                    'can_delete': False
                }
            }
        }

        created_count = 0
        updated_count = 0

        # Get all roles and menu items
        roles = Role.objects.all()
        menu_items = MenuItemType.objects.filter(module_name='retail')

        for role in roles:
            if role.role_key not in permission_templates:
                self.stdout.write(
                    self.style.WARNING(f"No permission template found for role: {role.role_key}")
                )
                continue

            template = permission_templates[role.role_key]
            default_permissions = template['permissions']

            for menu_item in menu_items:
                # Check for special permissions override
                permissions = default_permissions.copy()
                if (role.role_key in special_permissions and 
                    menu_item.menu_id in special_permissions[role.role_key]):
                    permissions.update(special_permissions[role.role_key][menu_item.menu_id])

                role_permission, created = RolePermission.objects.update_or_create(
                    role=role,
                    menu_item=menu_item,
                    defaults=permissions
                )

                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'\nPermission seeding complete! Created: {created_count}, Updated: {updated_count}'
            )
        )

        # Display summary
        self.stdout.write('\nPermission Summary:')
        for role in roles:
            if role.role_key in permission_templates:
                count = RolePermission.objects.filter(role=role).count()
                self.stdout.write(f"  {role.role_name}: {count} permissions")




