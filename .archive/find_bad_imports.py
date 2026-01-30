import os
import re

root_dir = r"c:\00mindra\olivine-erp-platform\frontend\src\pages"
pattern = r'from\s+["'']\.\./components/'

files_to_fix = []

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".tsx"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    if re.search(pattern, content):
                        files_to_fix.append(filepath)
            except:
                pass

for f in files_to_fix:
    print(f)




