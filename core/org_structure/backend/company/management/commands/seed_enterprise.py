"""
OLIVINE ERP - ENTERPRISE MASTER DATA SEED
Django Management Command
Purpose: Seed minimal master data for toolbar testing
Date: 2026-01-09 21:05 IST

GOVERNANCE COMPLIANCE:
- Uses ONLY registered AppConfigs via apps.get_model()
- Zero dependency on Python import paths (prevents structure leakage)
- Cleanly separates 'business_entities' (Licensing) vs 'company' (Operating)
- Uses 'retail_domain' for Location
- Uses Canonical Models (ItemMaster, OperationalSupplier, OperationalCustomer)
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from django.apps import apps
from django.contrib.auth.models import User
from datetime import date

class Command(BaseCommand):
    help = 'Seeds enterprise master data for toolbar testing'

    @transaction.atomic
    def handle(self, *args, **options):
        # ---------------------------------------------------------
        # LOAD MODELS VIA REGISTRY (Governance Compliant)
        # ---------------------------------------------------------
        LicensingCompany = apps.get_model('business_entities', 'Company')
        OperatingCompany = apps.get_model('company', 'Company') # For reference
        Location = apps.get_model('retail_domain', 'Location')
        
        # Masters
        Category = apps.get_model('company', 'Category')
        Brand = apps.get_model('company', 'Brand')
        UnitOfMeasure = apps.get_model('company', 'UnitOfMeasure')
        
        # Canonical Operational Models
        ItemMaster = apps.get_model('company', 'ItemMaster')
        ItemVariant = apps.get_model('company', 'ItemVariant')
        ProductAttributeTemplate = apps.get_model('company', 'ProductAttributeTemplate')
        
        # Partners
        OperationalCustomer = apps.get_model('company', 'OperationalCustomer')
        OperationalSupplier = apps.get_model('company', 'OperationalSupplier')
        
        # User Mgmt
        Role = apps.get_model('user_management', 'Role')
        UserRole = apps.get_model('user_management', 'UserRole')
        ERPMenuItem = apps.get_model('user_management', 'ERPMenuItem')
        
        # HR
        Employee = apps.get_model('hr', 'Employee')

        # License
        LicenseConfiguration = apps.get_model('licensing', 'LicenseConfiguration')

        self.stdout.write("\n" + "="*100)
        self.stdout.write(self.style.SUCCESS(" " * 30 + "OLIVINE ERP - ENTERPRISE DATA SEED"))
        self.stdout.write("="*100 + "\n")
        
        # PHASE 0: LICENSE SETUP
        # Must exist before Company creation due to business_entities.models.clean() validation
        self.stdout.write(self.style.WARNING("[0/8] Setting up License Configuration..."))
        self.stdout.write("-" * 100)
        
        license_config, created = LicenseConfiguration.objects.get_or_create(
            is_active=True,
            defaults={
                'license_key': 'ENTERPRISE-SEED-KEY',
                'licensee_name': 'Mindra Retail',
                'max_companies': 10,  # Allow enough companies for the seed
                'max_locations_per_company': 10,
                'max_total_locations': 50,
                'valid_from': date.today(),
                'valid_until': date(2099, 12, 31)
            }
        )
        if not created:
            # Ensure limits are sufficient if it already exists
            license_config.max_companies = max(license_config.max_companies, 10)
            license_config.max_locations_per_company = max(license_config.max_locations_per_company, 10)
            license_config.max_total_locations = max(license_config.max_total_locations, 50)
            license_config.save()
            
        self.stdout.write(f"  ✓ License Active: {license_config.license_key}")
        
        # PHASE 1: USERS & ROLES
        self.stdout.write(self.style.WARNING("[1/8] Creating Users & Roles..."))
        self.stdout.write("-" * 100)
        
        # Create Roles
        roles_data = [
            {'role_key': 'admin', 'role_name': 'System Administrator', 'description': 'Full system access'},
            {'role_key': 'backofficemanager', 'role_name': 'Back Office Manager', 'description': 'Back office management'},
            {'role_key': 'backofficeuser', 'role_name': 'Back Office User', 'description': 'Back office operations'},
            {'role_key': 'posmanager', 'role_name': 'POS Manager', 'description': 'Store management'},
            {'role_key': 'posuser', 'role_name': 'POS User', 'description': 'Cashier operations'},
        ]
        
        for role_data in roles_data:
            Role.objects.get_or_create(role_key=role_data['role_key'], defaults=role_data)
        
        # Create Users
        users_data = [
            ('admin', 'admin123', 'System', 'Administrator', 'EMP001', 'admin', True, True),
            ('boadmin', 'boadmin123', 'Back Office', 'Manager', 'EMP002', 'backofficemanager', False, True),
            ('bouser', 'bouser123', 'Back Office', 'User', 'EMP003', 'backofficeuser', False, False),
            ('posadmin', 'posadmin123', 'POS', 'Manager', 'EMP004', 'posmanager', False, True),
            ('posuser', 'posuser123', 'POS', 'User', 'EMP005', 'posuser', False, False),
        ]
        
        for username, pwd, fn, ln, emp_code, role_key, is_super, is_staff in users_data:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': fn, 'last_name': ln,
                    'email': f'{username}@mindra.com',
                    'is_superuser': is_super, 'is_staff': is_staff, 'is_active': True
                }
            )
            if created:
                user.set_password(pwd)
                user.save()
            
            emp, _ = Employee.objects.get_or_create(
                employee_code=emp_code,
                defaults={
                    'user': user, 'first_name': fn, 'last_name': ln,
                    'email': f'{username}@mindra.com',
                    'designation': f'{fn} {ln}', 'status': 'active'
                }
            )
            
            role = Role.objects.get(role_key=role_key)
            UserRole.objects.get_or_create(user=user, role=role, defaults={'is_active': True})
            self.stdout.write(f"  ✓ User: {username:12} | Role: {role.role_name:25} | Employee: {emp_code}")
        
        self.stdout.write(f"\n  Total: {User.objects.count()} users, {Role.objects.count()} roles\n")
        
        # PHASE 2: LICENSING COMPANY (Legal Entity)
        self.stdout.write(self.style.WARNING("[2/8] Creating Licensing Company (Legal Entity)..."))
        self.stdout.write("-" * 100)
        
        licensing_company, _ = LicensingCompany.objects.get_or_create(
            code='MINDRA',
            defaults={
                'name': 'Mindra Retail Pvt Ltd',
                'legal_entity_type': 'PRIVATE_LTD',
                'city': 'Bangalore',
                'state': 'Karnataka',
                'country': 'IN',
                'postal_code': '560001',
                'default_currency': 'INR',
                'timezone': 'Asia/Kolkata',
                'status': 'ACTIVE',
            }
        )
        self.stdout.write(f"  ✓ Licensing Company: {licensing_company.name}\n")
        
        # PHASE 3: LOCATIONS (Linked to Licensing Company)
        self.stdout.write(self.style.WARNING("[3/8] Creating Locations..."))
        self.stdout.write("-" * 100)
        
        locations_data = [
            ('HQ', 'Head Office', 'HEAD_OFFICE', False, False),
            ('WH-BLR', 'Bangalore Warehouse', 'WAREHOUSE', False, True),
            ('STR-MG', 'MG Road Store', 'STORE', True, False),
            ('STR-IND', 'Indiranagar Store', 'STORE', True, False),
            ('ONLINE', 'Online Store', 'VIRTUAL', False, False),
        ]
        
        for code, name, loc_type, pos_enabled, is_dc in locations_data:
            loc, _ = Location.objects.get_or_create(
                company=licensing_company,
                location_code=code,
                defaults={
                    'name': name,
                    'location_type': loc_type,
                    'is_pos_enabled': pos_enabled,
                    'is_dc': is_dc,
                    'city': 'Bangalore',
                    'state': 'Karnataka',
                    'country': 'India',
                }
            )
            self.stdout.write(f"  ✓ Location: {name}")
        
        self.stdout.write(f"\n  Total: {Location.objects.count()} locations\n")
        
        # PHASE 4: MASTER DATA (UOMs, Categories, Brands)
        # Note: These link to Licensing Company in legacy mode
        self.stdout.write(self.style.WARNING("[4/8] Creating Master Data..."))
        self.stdout.write("-" * 100)
        
        # UOMs
        uoms_data = [
            ('PCS', 'Pieces', 'STOCK', False),
            ('KG', 'Kilogram', 'STOCK', True),
            ('GM', 'Gram', 'STOCK', True),
            ('MTR', 'Meter', 'STOCK', True),
            ('LTR', 'Liter', 'STOCK', True),
            ('BOX', 'Box', 'SALES', False),
            ('PACK', 'Pack', 'SALES', False),
            ('PAIR', 'Pair', 'SALES', False),
        ]
        
        for code, name, uom_type, decimal in uoms_data:
            UnitOfMeasure.objects.get_or_create(
                company=licensing_company,
                uom_code=code,
                defaults={
                    'uom_name': name,
                    'uom_type': uom_type,
                    'decimal_allowed': decimal,
                    'is_core_uom': True
                }
            )
        self.stdout.write(f"  ✓ UOMs: {UnitOfMeasure.objects.count()} units created")
        
        # Categories
        categories = ['Electronics', 'Fashion', 'Grocery', 'Home', 'Pharmacy']
        for cat_name in categories:
            Category.objects.get_or_create(name=cat_name)
        self.stdout.write(f"  ✓ Categories: {Category.objects.count()} categories created")
        
        # Brands
        branding_data = ['Nike', 'Adidas', 'Samsung', 'Apple', 'Sony', 'LG', 'Nestle', 'ITC', 'HUL', 'Amul']
        for brand_name in branding_data:
            Brand.objects.get_or_create(name=brand_name)
        self.stdout.write(f"  ✓ Brands: {Brand.objects.count()} brands created\n")
        
        # PHASE 5: TEMPLATES & SETUP
        self.stdout.write(self.style.WARNING("[5/8] Creating Attribute Template..."))
        
        template, _ = ProductAttributeTemplate.objects.get_or_create(
            company=licensing_company,
            template_code='DEFAULT',
            defaults={
                'template_name': 'Default Template',
                'template_mode': 'SIMPLE',
                'is_core_template': True
            }
        )
        self.stdout.write(f"  ✓ Template: {template.template_name}")

        # PHASE 6: ITEMS (200)
        self.stdout.write(self.style.WARNING("\n[6/8] Creating Items (200)..."))
        self.stdout.write("-" * 100)
        
        stock_uoms = list(UnitOfMeasure.objects.filter(uom_type='STOCK'))
        if not stock_uoms:
            stock_uoms = list(UnitOfMeasure.objects.all())
        
        all_categories = list(Category.objects.all())
        all_brands = list(Brand.objects.all())
        
        items_count = 0
        for i in range(1, 201):
            if ItemMaster.objects.filter(item_code=f"ITEM-{i:04d}").exists():
                items_count += 1
                continue
                
            uom = stock_uoms[i % len(stock_uoms)]
            cat = all_categories[i % len(all_categories)] if all_categories else None
            brand = all_brands[i % len(all_brands)] if all_brands else None
            
            item, created = ItemMaster.objects.get_or_create(
                company=licensing_company,
                item_code=f"ITEM-{i:04d}",
                defaults={
                    'item_name': f"Standard Item {i:04d}",
                    'item_type': 'STOCKED',
                    'stock_uom': uom,
                    'attribute_template': template,
                    'status': 'ACTIVE',
                    'category': cat,
                    'brand': brand
                }
            )
            
            # Create Default Variant
            ItemVariant.objects.get_or_create(
                item=item,
                sku_code=f"SKU-{i:04d}-DEF",
                defaults={
                    'variant_name': f"{item.item_name} (Default)",
                    'sales_uom': uom,
                    'stock_uom': uom,
                    'is_default_variant': True
                    # Note: ItemVariant has no company field, it links to ItemMaster
                }
            )
            
            items_count += 1
            if i % 50 == 0:
                self.stdout.write(f"  ... {i} items processed")
                
        self.stdout.write(f"  ✓ Total Items: {items_count}")
        
        # PHASE 7: BUSINESS PARTNERS
        self.stdout.write(self.style.WARNING("\n[7/8] Creating Business Partners..."))
        self.stdout.write("-" * 100)
        
        for i in range(1, 51):
             OperationalCustomer.objects.get_or_create(
                 company=licensing_company,
                 customer_code=f"CUST-{i:03d}",
                 defaults={
                     'customer_name': f"Customer {i:03d}", 
                     'customer_type': 'INDIVIDUAL', 
                     'status': 'ACTIVE'
                 }
             )
             OperationalSupplier.objects.get_or_create(
                 company=licensing_company,
                 supplier_code=f"SUPP-{i:03d}",
                 defaults={
                     'supplier_name': f"Supplier {i:03d}", 
                     'status': 'ACTIVE'
                 }
             )
        self.stdout.write(f"  ✓ Customers: {OperationalCustomer.objects.count()}")
        self.stdout.write(f"  ✓ Suppliers: {OperationalSupplier.objects.count()}")

        # PHASE 8: MENU ITEMS (Toolbar Configs)
        self.stdout.write(self.style.WARNING("\n[8/8] Creating Menu Items & Toolbar Configs..."))
        self.stdout.write("-" * 100)
        
        menu_items_data = [
            ('INVENTORY_UOM_SETUP', 'UOM Setup', 'RETAIL', 'MASTER', 'NESCKVDXRQF', '/inventory/uoms'),
            ('ITEM_MASTER', 'Item Master', 'RETAIL', 'MASTER', 'NESCKVDXRQFIO', '/inventory/items'),
            ('PURCHASE_ORDERS', 'Purchase Orders', 'RETAIL', 'TRANSACTION', 'NESCKZTJAVPMRDX1234QF', '/procurement/purchase-orders'),
        ]
        
        for menu_id, menu_name, module, view_type, config, route in menu_items_data:
            ERPMenuItem.objects.get_or_create(
                menu_id=menu_id,
                defaults={
                    'menu_name': menu_name,
                    'module_name': module,
                    'view_type': view_type,
                    'applicable_toolbar_config': config,
                    'route_path': route,
                    'is_active': True
                }
            )
            self.stdout.write(f"  ✓ {menu_id:25} | {config}")
        
        self.stdout.write(f"\n  Total: {ERPMenuItem.objects.count()} menu items\n")
        
        # SUMMARY
        self.stdout.write("\n" + "="*100)
        self.stdout.write(self.style.SUCCESS(" " * 35 + "DATABASE SEED COMPLETE!"))
        self.stdout.write("="*100 + "\n")
        
        self.stdout.write("📊 FINAL STATISTICS:")
        self.stdout.write("-" * 100)
        self.stdout.write(f"  Users:              {User.objects.count():>5}")
        self.stdout.write(f"  Roles:              {Role.objects.count():>5}")
        self.stdout.write(f"  Companies:          {LicensingCompany.objects.count():>5}")
        self.stdout.write(f"  Locations:          {Location.objects.count():>5}")
        self.stdout.write(f"  Items:              {ItemMaster.objects.count():>5}")
        self.stdout.write(f"  Customers:          {OperationalCustomer.objects.count():>5}")
        self.stdout.write(f"  Suppliers:          {OperationalSupplier.objects.count():>5}")
        self.stdout.write(f"  Menu Items:         {ERPMenuItem.objects.count():>5}")
        self.stdout.write("-" * 100)
        
        self.stdout.write("\n🔐 LOGIN CREDENTIALS:")
        self.stdout.write("="*100)
        self.stdout.write(f"{'Username':<15} | {'Password':<15} | {'Role':<30}")
        self.stdout.write("-" * 100)
        self.stdout.write(f"{'admin':<15} | {'admin123':<15} | {'System Administrator':<30}")
        self.stdout.write(f"{'boadmin':<15} | {'boadmin123':<15} | {'Back Office Manager':<30}")
        self.stdout.write(f"{'posadmin':<15} | {'posadmin123':<15} | {'POS Manager':<30}")
        self.stdout.write("="*100 + "\n")
        
        self.stdout.write(self.style.SUCCESS("✅ ENTERPRISE DATA SEED COMPLETED SUCCESSFULLY!"))
        self.stdout.write("="*100 + "\n")




