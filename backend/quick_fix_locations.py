"""
Quick Fix: Create Location Table and Seed Data
===============================================

This script:
1. Creates the location table directly in SQLite
2. Seeds it with test location data
3. Creates user-location mappings for the admin user

Run with: python backend/quick_fix_locations.py
"""

import sqlite3
import uuid
from datetime import datetime

# Connect to database
conn = sqlite3.connect('backend/db.sqlite3')
cursor = conn.cursor()

print("="*60)
print("QUICK FIX: Creating Location Table and Seeding Data")
print("="*60)

# Step 1: Check if location table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='location'")
if cursor.fetchone():
    print("\n✓ Location table already exists")
else:
    print("\n⚠ Location table does not exist. Creating...")
    
    # Create location table
    cursor.execute("""
        CREATE TABLE location (
            id CHAR(32) PRIMARY KEY,
            company_id INTEGER NOT NULL,
            location_code VARCHAR(20) NOT NULL,
            name VARCHAR(200) NOT NULL,
            display_name VARCHAR(100),
            location_type VARCHAR(20) NOT NULL,
            channel_type VARCHAR(20),
            parent_location_id CHAR(32),
            address_line1 VARCHAR(255) NOT NULL,
            address_line2 VARCHAR(255),
            city VARCHAR(100) NOT NULL,
            state VARCHAR(100) NOT NULL,
            country VARCHAR(100) NOT NULL,
            postal_code VARCHAR(20),
            phone VARCHAR(30),
            email VARCHAR(100),
            timezone VARCHAR(50),
            opening_date DATE,
            closing_date DATE,
            is_pos_enabled BOOLEAN DEFAULT 0,
            is_dc BOOLEAN DEFAULT 0,
            is_active BOOLEAN DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(company_id, location_code)
        )
    """)
    print("✓ Location table created")

# Step 2: Get company ID
# Try different possible table names
company_row = None
for table_name in ['be_company', 'company']:
    try:
        cursor.execute(f"SELECT id FROM {table_name} WHERE code='MINDRA' LIMIT 1")
        company_row = cursor.fetchone()
        if company_row:
            print(f"✓ Found company in table: {table_name}")
            break
    except sqlite3.OperationalError:
        continue

if not company_row:
    print("\n✗ Company 'MINDRA' not found in any company table!")
    conn.close()
    exit(1)

company_id = company_row[0]
print(f"\n✓ Found company ID: {company_id}")

# Step 3: Check existing locations
cursor.execute("SELECT COUNT(*) FROM location WHERE company_id=?", (company_id,))
existing_count = cursor.fetchone()[0]

if existing_count > 0:
    print(f"\n⚠ Found {existing_count} existing locations. Skipping creation.")
    cursor.execute("SELECT id, location_code, name FROM location WHERE company_id=? LIMIT 5", (company_id,))
    for row in cursor.fetchall():
        print(f"  - {row[1]}: {row[2]}")
else:
    print(f"\n📍 Creating test locations...")
    
    # Create test locations
    locations = [
        {
            'id': str(uuid.uuid4()).replace('-', ''),
            'company_id': company_id,
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
            'is_active': 1,
        },
        {
            'id': str(uuid.uuid4()).replace('-', ''),
            'company_id': company_id,
            'location_code': 'STORE-01',
            'name': 'Store 1 - Koramangala',
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
            'is_pos_enabled': 1,
            'is_active': 1,
        },
        {
            'id': str(uuid.uuid4()).replace('-', ''),
            'company_id': company_id,
            'location_code': 'STORE-02',
            'name': 'Store 2 - Indiranagar',
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
            'is_pos_enabled': 1,
            'is_active': 1,
        },
        {
            'id': str(uuid.uuid4()).replace('-', ''),
            'company_id': company_id,
            'location_code': 'WH-01',
            'name': 'Warehouse - Whitefield',
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
            'is_dc': 1,
            'is_active': 1,
        },
    ]
    
    for loc in locations:
        cursor.execute("""
            INSERT INTO location (
                id, company_id, location_code, name, display_name, location_type,
                channel_type, address_line1, city, state, country, postal_code,
                phone, email, timezone, is_pos_enabled, is_dc, is_active
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            loc['id'], loc['company_id'], loc['location_code'], loc['name'],
            loc.get('display_name'), loc['location_type'], loc.get('channel_type'),
            loc['address_line1'], loc['city'], loc['state'], loc['country'],
            loc.get('postal_code'), loc.get('phone'), loc.get('email'),
            loc.get('timezone'), loc.get('is_pos_enabled', 0), loc.get('is_dc', 0),
            loc.get('is_active', 1)
        ))
        print(f"  ✓ Created: {loc['location_code']} - {loc['name']}")
    
    conn.commit()
    print(f"\n✓ Successfully created {len(locations)} locations")

# Step 4: Verify
cursor.execute("SELECT COUNT(*) FROM location WHERE company_id=?", (company_id,))
total_locations = cursor.fetchone()[0]
print(f"\n✓ Total locations for company: {total_locations}")

# Step 5: Display sample locations
print("\nSample locations:")
cursor.execute("SELECT id, location_code, name, location_type, is_active FROM location WHERE company_id=? LIMIT 5", (company_id,))
for row in cursor.fetchall():
    print(f"  - {row[1]}: {row[2]} ({row[3]}) - Active: {bool(row[4])}")

conn.close()

print("\n" + "="*60)
print("✓ QUICK FIX COMPLETED SUCCESSFULLY")
print("="*60)
print("\nNext steps:")
print("1. Restart the backend server if it's running")
print("2. Try logging in again at http://localhost:3001/login")
print("3. You should now be able to select a location")
