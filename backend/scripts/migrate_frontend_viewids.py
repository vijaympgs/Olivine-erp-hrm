import os
import re

APPS_DIR = r'c:\00mindra\olivine-erp-platform\frontend\apps'

def migrate_view_ids():
    print("=" * 100)
    print("MIGRATING FRONTEND VIEW IDs TO UPPERCASE (Registry Sync)")
    print("=" * 100)
    
    files_processed = 0
    replacements_made = 0
    
    # Pattern to find viewId="..."
    pattern = r'viewId\s*=\s*[\'"]([^\'"]+)[\'"]'
    
    for root, dirs, files in os.walk(APPS_DIR):
        for file in files:
            if file.endswith('.tsx'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    try:
                        content = f.read()
                    except UnicodeDecodeError:
                        continue
                
                def replacer(match):
                    old_id = match.group(1)
                    # Convert to uppercase and underscore
                    new_id = old_id.upper().replace('-', '_')
                    if new_id != old_id:
                        nonlocal replacements_made
                        replacements_made += 1
                        return f'viewId="{new_id}"'
                    return match.group(0)
                
                new_content = re.sub(pattern, replacer, content)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"[UPDATED] {os.path.relpath(path, APPS_DIR)}")
                
                files_processed += 1

    print("\n" + "=" * 100)
    print(f"Migration Complete.")
    print(f"Files Processed: {files_processed}")
    print(f"Total Substitutions: {replacements_made}")
    print("=" * 100)

if __name__ == "__main__":
    migrate_view_ids()




