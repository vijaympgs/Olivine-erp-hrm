import os

def fix_files():
    root_dir = r'c:\00mindra\olivine-platform\Retail\backend'
    replacements = [
        ("Company.objects.filter(is_active=True)", "Company.objects.filter(status='ACTIVE')"),
        ("Company.objects.filter(is_active=False)", "Company.objects.filter(status='INACTIVE')"),
    ]
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old, new in replacements:
                    new_content = new_content.replace(old, new)
                
                if new_content != content:
                    print(f"Fixing {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_files()
