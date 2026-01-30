import os

def fix_tests_v3():
    root_dir = r'c:\00mindra\olivine-platform\Retail\backend'
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and 'tests' in root:
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                new_lines = []
                changed = False
                for i, line in enumerate(lines):
                    if "Company.objects.filter(status='ACTIVE').first()" in line:
                        indent = line[:line.find("cls.") if "cls." in line else line.find("self.")]
                        prefix = "cls" if "cls." in line else "self"
                        new_lines.append(line)
                        new_lines.append(f"{indent}if not {prefix}.company:\n")
                        new_lines.append(f"{indent}    {prefix}.company = Company(company_name='Test Company', company_code='TEST', status='ACTIVE')\n")
                        new_lines.append(f"{indent}    {prefix}.company._permit_legacy_creation = True\n")
                        new_lines.append(f"{indent}    {prefix}.company.save()\n")
                        changed = True
                    elif "if not cls.company:" in line and "raise ValueError" in lines[i+1] if i+1 < len(lines) else False:
                        # Skip adding this line if we already added creation logic
                        continue
                    elif "raise ValueError(\"Missing active Company\")" in line:
                        continue
                    else:
                        new_lines.append(line)
                
                if changed:
                    print(f"Fixing {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)

if __name__ == "__main__":
    fix_tests_v3()
