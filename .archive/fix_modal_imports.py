import os
import re

root_dirs = [
    r"c:\00mindra\olivine-erp-platform\apps",
    r"c:\00mindra\olivine-erp-platform\core"
]

modal_names = [
    'UOMModal', 'AttributeModal', 'AttributeValueModal', 'CompanyModal',
    'CustomerModal', 'ItemModal', 'ItemModalWithVariants', 'LocationModal',
    'PriceListModal', 'ProductAttributeTemplateModal', 'SupplierModal'
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
                    # Fix modal imports - replace relative paths to @core/ui-canon/frontend/components
                    for modal in modal_names:
                        pattern = rf'from\s+["''](\.\./)+components/{modal}["'']'
                        replacement = f'from "@core/ui-canon/frontend/components/{modal}"'
                        content = re.sub(pattern, replacement, content)
                    
                    if content != original:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"Fixed modal imports in {file}")
                except Exception as e:
                    pass




