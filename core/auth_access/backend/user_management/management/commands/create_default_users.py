from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

class Command(BaseCommand):
    help = 'Creates default EnterpriseGPT users (admin, boadmin, bouser, posadmin, posuser).'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # User Definitions
        users_config = [
            {
                'username': 'admin',
                'role': 'admin', 
                'description': 'System Administrator',
                'is_staff': True,
                'is_superuser': True
            },
            {
                'username': 'boadmin',
                'role': 'backofficemanager',
                'description': 'Back Office Manager',
                'is_staff': True,
                'is_superuser': False
            },
            {
                'username': 'bouser',
                'role': 'backofficeuser',
                'description': 'Back Office User',
                'is_staff': False,
                'is_superuser': False
            },
            {
                'username': 'posadmin',
                'role': 'posmanager',
                'description': 'POS Manager',
                'is_staff': True,
                'is_superuser': False
            },
            {
                'username': 'posuser',
                'role': 'posuser',
                'description': 'POS User',
                'is_staff': False,
                'is_superuser': False
            },
        ]

        created_count = 0
        updated_count = 0

        self.stdout.write("Initializing EnterpriseGPT Users...")

        with transaction.atomic():
            for config in users_config:
                username = config['username']
                email = f"{username}@enterprisegpt.local"
                password = username  # Password matches username rule
                
                try:
                    user, created = User.objects.get_or_create(username=username)
                    
                    # Update Fields
                    user.email = email
                    user.is_staff = config['is_staff']
                    user.is_superuser = config['is_superuser']
                    user.set_password(password)
                    
                    # Try setting role/description if fields exist (Custom User Model Support)
                    if hasattr(user, 'role'):
                        user.role = config['role']
                    
                    if hasattr(user, 'description'):
                        user.description = config['description']
                        
                    user.save()

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Created: {username}"))
                        created_count += 1
                    else:
                        self.stdout.write(self.style.WARNING(f"Updated: {username}"))
                        updated_count += 1
                        
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing {username}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS(f"Completed: {created_count} created, {updated_count} updated."))




