#!/usr/bin/env python
"""Export ERP Menu Items to CSV to check toolbar strings"""

import os
import sys
import django
import csv

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')

django.setup()

from core.auth_access.backend.user_management.models import ERPMenuItem

def main():
    print('Exporting ERP Menu Items to CSV...')
    
    # Get all menu items
    all_items = ERPMenuItem.objects.all().order_by('module_name', 'menu_order')
    
    # Export to CSV
