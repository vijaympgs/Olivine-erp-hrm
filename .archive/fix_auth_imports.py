import os
import re

root_dirs = [
    r"c:\00mindra\olivine-erp-platform\apps",
    r"c:\00mindra\olivine-erp-platform\core"
]

for root_dir in root_dirs:
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith((".tsx", ".ts")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    original = content
                    # Fix auth imports
                    content = re.sub(r'from\s+["''](\.\./)+auth/', 'from "@auth/', content)
                    
                    if content != original:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"Fixed auth imports in {file}")
                except Exception as e:
                    pass




