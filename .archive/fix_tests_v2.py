import os
import re

def fix_tests_company_creation():
    root_dir = r'c:\00mindra\olivine-platform\Retail\backend'
    
    # Pattern to find cls.company assignment and following check
    pattern = re.compile(r"cls\.company\s*=\s*Company\.objects\.filter\(status='ACTIVE'\)\.first\(\)\s*if\s+not\s+cls\.company:\s*raise\s+ValueError\(\"Missing active Company\"\)", re.DOTALL)
    
    # Also handle variants of the check
    pattern_alt = re.compile(r"cls\.company\s*=\s*Company\.objects\.filter\(status='ACTIVE'\)\.first\(\)\s*if\s+not\s+cls\.company:\s+raise\s+ValueError\(\".*?\"\)", re.DOTALL)

    replacement = """cls.company = Company.objects.filter(status='ACTIVE').first()
        if not cls.company:
            cls.company = Company(company_name="Test Company", company_code="TEST", status='ACTIVE')
            cls.company._permit_legacy_creation = True
            cls.company.save()"""

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and 'tests' in root:
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                # Try specific replacements first
                new_content = re.sub(r"cls\.company\s*=\s*Company\.objects\.filter\(status='ACTIVE'\)\.first\(\)\s*if\s*not\s*cls\.company:\s*raise\s*ValueError\(.*?\)", replacement, new_content, flags=re.DOTALL)
                new_content = re.sub(r"self\.company\s*=\s*Company\.objects\.filter\(status='ACTIVE'\)\.first\(\)\s*if\s*not\s*self\.company:\s*raise\s*ValueError\(.*?\)", replacement.replace('cls.', 'self.'), new_content, flags=re.DOTALL)

                if new_content != content:
                    print(f"Fixing company creation in {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_tests_company_creation()
