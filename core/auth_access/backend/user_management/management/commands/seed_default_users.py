"""
Management command to seed default users for testing the permission system
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.auth_access.backend.user_management.models import Role, UserRole
from hr.models import Employee


class Command(BaseCommand):
    help = 'Seeds default test users with assigned roles and Employee records'

    def handle(self, *args, **options):
        self.stdout.write('Seeding default users...')

        # Define users with their role assignments
        users_to_create = [
            {
                'username': 'admin',
                'email': 'admin@enterprise.local',
                'password': 'admin123',
                'first_name': 'System',
                'last_name': 'Administrator',
                'role_key': 'admin',
                'is_superuser': True,
                'is_staff': True,
                'employee_code': 'EMP001',
                'designation': 'System Administrator',
                'department': 'IT',
            },
            {
                'username': 'boadmin',
                'email': 'boadmin@enterprise.local',
                'password': 'boadmin123',
                'first_name': 'Back Office',
                'last_name': 'Manager',
                'role_key': 'backofficemanager',
                'is_superuser': False,
                'is_staff': True,
                'employee_code': 'EMP002',
                'designation': 'Back Office Manager',
                'department': 'Operations',
            },
            {
                'username': 'bouser',
                'email': 'bouser@enterprise.local',
                'password': 'bouser123',
                'first_name': 'Back Office',
                'last_name': 'User',
                'role_key': 'backofficeuser',
                'is_superuser': False,
                'is_staff': False,
                'employee_code': 'EMP003',
                'designation': 'Back Office Executive',
                'department': 'Operations',
            },
            {
                'username': 'posadmin',
                'email': 'posadmin@enterprise.local',
                'password': 'posadmin123',
                'first_name': 'POS',
                'last_name': 'Manager',
                'role_key': 'posmanager',
                'is_superuser': False,
                'is_staff': True,
                'employee_code': 'EMP004',
                'designation': 'Store Manager',
                'department': 'Retail',
            },
            {
                'username': 'posuser',
                'email': 'posuser@enterprise.local',
                'password': 'posuser123',
                'first_name': 'POS',
                'last_name': 'User',
                'role_key': 'posuser',
                'is_superuser': False,
                'is_staff': False,
                'employee_code': 'EMP005',
                'designation': 'Cashier',
                'department': 'Retail',
            },
        ]

        created_count = 0
        updated_count = 0

        for user_data in users_to_create:
            role_key = user_data.pop('role_key')
            password = user_data.pop('password')
            employee_code = user_data.pop('employee_code')
            designation = user_data.pop('designation')
            department = user_data.pop('department')
            
            # Get or create user
            user, user_created = User.objects.update_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'is_superuser': user_data['is_superuser'],
                    'is_staff': user_data['is_staff'],
                    'is_active': True,
                }
            )
            
            # Set password
            user.set_password(password)
            user.save()
            
            # Get or create Employee linked to User
            employee, emp_created = Employee.objects.update_or_create(
                employee_code=employee_code,
                defaults={
                    'user': user,
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'email': user_data['email'],
                    'designation': designation,
                    'department': department,
                    'status': 'active',
                }
            )
            
            # Assign role
            try:
                role = Role.objects.get(role_key=role_key)
                UserRole.objects.update_or_create(
                    user=user,
                    role=role,
                    defaults={
                        'is_active': True,
                    }
                )
                role_name = role.role_name
            except Role.DoesNotExist:
                role_name = f'{role_key} (Role not found - run seed_default_roles first)'
            
            if user_created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Created user: {user.username} -> {role_name} (Employee: {employee_code})")
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Updated user: {user.username} -> {role_name} (Employee: {employee_code})")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nUser seeding complete! Created: {created_count}, Updated: {updated_count}'
            )
        )
        
        self.stdout.write('\n--- User Credentials (Access ID = Username) ---')
        self.stdout.write('Employee Code | Access ID  | Password     | Role')
        self.stdout.write('-' * 60)
        self.stdout.write('EMP001       | admin      | admin123     | Administrator')
        self.stdout.write('EMP002       | boadmin    | boadmin123   | Back Office Manager')
        self.stdout.write('EMP003       | bouser     | bouser123    | Back Office User')
        self.stdout.write('EMP004       | posadmin   | posadmin123  | POS Manager')
        self.stdout.write('EMP005       | posuser    | posuser123   | POS User')





