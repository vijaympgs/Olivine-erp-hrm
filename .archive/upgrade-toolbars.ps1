# Upgrade pages to ConfigDriven Toolbar

$updates = @{
    "frontend\src\pages\admin\LayoutSettingsPage.tsx" = "layout-settings";
    "frontend\src\pages\SupplierSetup.tsx" = "suppliers";
    "frontend\src\pages\CustomerSetup.tsx" = "customer-list";
    "frontend\src\pages\LocationSetup.tsx" = "location-setup";
    "frontend\src\pages\CompanySettings.tsx" = "company-settings";
    "frontend\apps\retail\pos\terminal\TerminalPage.tsx" = "pos-terminal-configuration";
    "frontend\apps\retail\inventory\pages\AttributeValueSetup.tsx" = "attribute-values";
    "frontend\apps\retail\inventory\pages\ItemMasterSetup.tsx" = "item-master";
    "frontend\apps\retail\inventory\pages\ProductAttributeTemplateSetup.tsx" = "attribute-templates";
    "frontend\apps\retail\inventory\pages\ReorderPolicyListPage.tsx" = "reorder-rules";
    "frontend\apps\retail\inventory\pages\PriceListSetup.tsx" = "price-lists-master";
    "frontend\apps\retail\inventory\pages\AttributeSetup.tsx" = "attributes";
}

$root = "c:\00mindra\olivine-erp-platform"

foreach ($fileRel in $updates.Keys) {
    $file = Join-Path $root $fileRel
    $viewId = $updates[$fileRel]
    
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        
        # 1. Update Import
        $newImport = 'import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";'
        $content = $content -replace 'import \{ MasterToolbar(?:, MasterMode)? \} from ".*MasterToolbar";', $newImport
        
        # 2. Update Tag (Inject viewId if not present)
        # We assume standard formatting like <MasterToolbar \n
        if ($content -notmatch 'viewId=') {
            $content = $content -replace '<MasterToolbar', "<MasterToolbar`r`n                viewId=`"$viewId`""
        }
        
        Set-Content -Path $file -Value $content -Encoding UTF8
        Write-Host "Updated $fileRel with viewId=$viewId" -ForegroundColor Green
    } else {
        Write-Host "File not found: $fileRel" -ForegroundColor Yellow
    }
}
