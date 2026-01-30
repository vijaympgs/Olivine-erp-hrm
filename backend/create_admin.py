#!/usr/bin/env python
"""
Script to create a Django superuser
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'domain.master.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser
username = 'admin'
email = 'admin@example.com'
password = 'admin123'

if User.objects.filter(username=username).exists():
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print(f'✅ Password reset for user: {username}')
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'✅ Superuser created successfully!')

print(f'\n📋 Login Credentials:')
print(f'   Username: {username}')
print(f'   Password: {password}')
print(f'\n🔗 Admin URL: http://localhost:8000/admin/')




