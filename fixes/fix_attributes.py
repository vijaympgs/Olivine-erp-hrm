import os

def fix_company_attributes():
    root_dir = r'c:\00mindra\olivine-platform\Retail\backend'
    
    replacements = {
        ".company_name": ".name",
        "'company.company_name'": "'company.name'",
        "\"company.company_name\"": "\"company.name\"",
        "'source_company.company_name'": "'source_company.name'",
        "'destination_company.company_name'": "'destination_company.name'",
    }
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old, new in replacements.items():
                    new_content = new_content.replace(old, new)
                
                if new_content != content:
                    print(f"Fixing attributes in {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_company_attributes()
