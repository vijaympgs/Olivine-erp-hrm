#!/usr/bin/env python
"""
Seed Test Data Script
=====================

This script seeds the database with essential test data:
1. Locations for the company
2. User permissions for admin user
3. Other master data as needed

Usage:
    python backend/manage.py shell < backend/scripts/seed_test_data.py
    OR
    python backend/scripts/seed_test_data.py
"""

import os
import sys
import django

# Setup Django environment if running as standalone script
if __name__ == "__main__":
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings')
    django.setup()

from django.contrib.auth import get_user_model
from core.licensing.backend.business_entities.models import Company
from Retail.backend.domain.models import Location
from datetime import date

User = get_user_model()


def seed_locations():
    """Create test locations for the company"""
    print("\n" + "="*60)
    print("SEEDING LOCATIONS")
    print("="*60)
    
    # Get the company
    try:
        company = Company.objects.get(code='MINDRA')
        print(f"✓ Found company: {company.name} ({company.code})")
    except Company.DoesNotExist:
        print("✗ Company 'MINDRA' not found. Creating...")
        company = Company.objects.create(
            name='Mindra Retail Pvt Ltd',
            code='MINDRA',
            legal_entity_type='PVT_LTD',
            country='IN',
            default_currency='INR',
            timezone='Asia/Kolkata',
            status='ACTIVE'
        )
        print(f"✓ Created company: {company.name}")
    
    # Check if locations already exist
    existing_count = Location.objects.filter(company=company).count()
    if existing_count > 0:
        print(f"\n⚠ Found {existing_count} existing locations. Skipping creation.")
        for loc in Location.objects.filter(company=company)[:5]:
            print(f"  - {loc.location_code}: {loc.name}")
        return
    
    # Create test locations
    locations_data = [
        {
            'location_code': 'HQ-BLR',
            'name': 'Bangalore Head Office',
            'display_name': 'HQ Bangalore',
            'location_type': 'OFFICE',
            'address_line1': 'MG Road, Brigade Gateway',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'postal_code': '560001',
            'phone': '+91-80-12345678',
            'email': 'hq@mindra.com',
            'timezone': 'Asia/Kolkata',
            'is_active': True,
        },
        {
            'location_code': 'STORE-BLR-01',
            'name': 'Bangalore Store 1 - Koramangala',
            'display_name': 'Koramangala Store',
            'location_type': 'STORE',
            'channel_type': 'RETAIL',
            'address_line1': '80 Feet Road, Koramangala',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'postal_code': '560034',
            'phone': '+91-80-23456789',
            'email': 'koramangala@mindra.com',
            'timezone': 'Asia/Kolkata',
            'is_pos_enabled': True,
            'is_active': True,
            'opening_date': date(2024, 1, 15),
        },
        {
            'location_code': 'STORE-BLR-02',
            'name': 'Bangalore Store 2 - Indiranagar',
            'display_name': 'Indiranagar Store',
            'location_type': 'STORE',
            'channel_type': 'RETAIL',
            'address_line1': '100 Feet Road, Indiranagar',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'postal_code': '560038',
            'phone': '+91-80-34567890',
            'email': 'indiranagar@mindra.com',
            'timezone': 'Asia/Kolkata',
            'is_pos_enabled': True,
            'is_active': True,
            'opening_date': date(2024, 3, 1),
        },
        {
            'location_code': 'WH-BLR-01',
            'name': 'Bangalore Warehouse - Whitefield',
            'display_name': 'Whitefield Warehouse',
            'location_type': 'WAREHOUSE',
            'address_line1': 'ITPL Main Road, Whitefield',
            'city': 'Bangalore',
            'state': 'Karnataka',
            'country': 'India',
            'postal_code': '560066',
            'phone': '+91-80-45678901',
            'email': 'warehouse@mindra.com',
            'timezone': 'Asia/Kolkata',
            'is_dc': True,
            'is_active': True,
        },
        {
            'location_code': 'STORE-DEL-01',
            'name': 'Delhi Store 1 - Connaught Place',
            'display_name': 'CP Store',
            'location_type': 'STORE',
            'channel_type': 'RETAIL',
            'address_line1': 'Block A, Connaught Place',
            'city': 'New Delhi',
            'state': 'Delhi',
            'country': 'India',
            'postal_code': '110001',
            'phone': '+91-11-12345678',
            'email': 'cp@mindra.com',
            'timezone': 'Asia/Kolkata',
            'is_pos_enabled': True,
            'is_active': True,
            'opening_date': date(2024, 6, 1),
        },
    ]
    
    print(f"\nCreating {len(locations_data)} locations...")
    created_count = 0
    
    for loc_data in locations_data:
        try:
            location = Location.objects.create(company=company, **loc_data)
            print(f"  ✓ Created: {location.location_code} - {location.name}")
            created_count += 1
        except Exception as e:
            print(f"  ✗ Failed to create {loc_data['location_code']}: {str(e)}")
    
    print(f"\n✓ Successfully created {created_count} locations")


def seed_user_locations():
    """Link admin user to locations"""
    print("\n" + "="*60)
    print("SEEDING USER-LOCATION MAPPINGS")
    print("="*60)
    
    try:
        admin_user = User.objects.get(username='admin')
        print(f"✓ Found admin user: {admin_user.username}")
    except User.DoesNotExist:
        print("✗ Admin user not found. Please create admin user first.")
        return
    
    # Note: User-Location mapping might be handled differently in your app
    # This is a placeholder - adjust based on your actual model structure
    print("⚠ User-Location mapping model not implemented yet.")
    print("  This will be handled by the /api/auth/user-locations/ endpoint")


def verify_data():
    """Verify seeded data"""
    print("\n" + "="*60)
    print("VERIFICATION")
    print("="*60)
    
    # Check companies
    company_count = Company.objects.filter(status='ACTIVE').count()
    print(f"\n✓ Active Companies: {company_count}")
    
    # Check locations
    location_count = Location.objects.filter(is_active=True).count()
    print(f"✓ Active Locations: {location_count}")
    
    if location_count > 0:
        print("\nSample Locations:")
        for loc in Location.objects.filter(is_active=True)[:3]:
            print(f"  - {loc.location_code}: {loc.name} ({loc.location_type})")
    
    # Check users
    user_count = User.objects.count()
    print(f"\n✓ Total Users: {user_count}")
    
    admin_exists = User.objects.filter(username='admin').exists()
    print(f"✓ Admin User Exists: {admin_exists}")


def main():
    """Main seeding function"""
    print("\n" + "="*60)
    print("DATABASE SEEDING SCRIPT")
    print("="*60)
    print("This script will populate the database with test data")
    
    try:
        # Seed locations
        seed_locations()
        
        # Seed user-location mappings
        seed_user_locations()
        
        # Verify
        verify_data()
        
        print("\n" + "="*60)
        print("✓ SEEDING COMPLETED SUCCESSFULLY")
        print("="*60)
        
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
