import os

def fix_tests_v7():
    root_dir = r'c:\00mindra\olivine-platform\Retail\backend'
    
    user_fallback = """
        cls.user = get_user_model().objects.filter(is_active=True).first()
        if not cls.user:
            cls.user = get_user_model().objects.create_superuser(username='testadmin', email='admin@test.com', password='password')
"""

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and 'tests' in root:
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if we have setUpTestData
                if "def setUpTestData(cls):" in content:
                    # Look for the user assignment
                    if "cls.user = User.objects" in content or "cls.user = get_user_model().objects" in content:
                        # Replace with fallback version
                        # (This is a bit tricky with Regex, but let's try a simple approach)
                        import re
                        new_content = re.sub(r'cls\.user = (User|get_user_model\(\))\.objects\.filter\(is_active=True\)\.first\(\)', 
                                            r'cls.user = \1.objects.filter(is_active=True).first()\n        if not cls.user:\n            cls.user = \1.objects.create_superuser(username="testadmin", email="admin@test.com", password="password")', 
                                            content)
                        
                        if new_content != content:
                            print(f"Adding user fallback in {path}")
                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(new_content)

if __name__ == "__main__":
    fix_tests_v7()
