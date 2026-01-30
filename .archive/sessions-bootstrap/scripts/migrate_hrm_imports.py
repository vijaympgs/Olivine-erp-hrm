import os
import re

def migrate_hrm_code(root_dir):
    patterns = [
        # (pattern, replacement)
        # Fix string model references like 'HRM.backend.hrm.Model' -> 'hrm.Model'
        (re.compile(r"(['\"])HRM\.backend\.hrm\."), r"\1hrm."),
        # Ensure 'hrm' as app label is preserved in strings if needed, but usually it's just 'hrm'
        (re.compile(r"(['\"])hrm\b"), r"\1hrm"),
    ]

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('.py', '.tsx', '.ts', '.js', '.json')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    for pattern, replacement in patterns:
                        new_content = pattern.sub(replacement, new_content)
                    
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    migrate_hrm_code(r"c:\00mindra\olivine-platform\HRM")
