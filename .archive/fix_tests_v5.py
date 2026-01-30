import os

def fix_tests_v5():
    root_dir = r'c:\00mindra\olivine-platform\Retail\backend'
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and 'tests' in root:
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Fix the stray 'cls' or 'self' introduced by v3/v4 error
                new_content = content.replace("\n            cls\n            cls.company.save()", "\n            cls.company.save()")
                new_content = new_content.replace("\n            self\n            self.company.save()", "\n            self.company.save()")
                
                # 2. Double check and fix any remaining company_name/company_code
                # (Should be handled by v4, but let's be safe)
                new_content = new_content.replace("company_name=", "name=")
                new_content = new_content.replace("company_code=", "code=")
                
                if new_content != content:
                    print(f"Fixing v5 in {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_tests_v5()
