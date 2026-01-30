import os

def fix_tests_v4():
    root_dir = r'c:\00mindra\olivine-platform\Retail\backend'
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and 'tests' in root:
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace the legacy creation logic added by v3 (if any)
                if "_permit_legacy_creation" in content:
                    print(f"Updating company creation in {path}")
                    # Remove the v3 block
                    content = content.replace("company_name='Test Company', company_code='TEST'", "name='Test Company', code='TEST', legal_entity_type='PVT_LTD', country='IN', default_currency='INR', timezone='Asia/Kolkata'")
                    content = content.replace(".company._permit_legacy_creation = True", "")
                
                # Also ensure it's status='ACTIVE' (which we already replaced)
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    fix_tests_v4()
