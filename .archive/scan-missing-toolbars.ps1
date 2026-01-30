# Scan for Retail pages MISSING the MasterToolbar
# Excludes: POS Billing, Dashboards, Reports

$directories = @(
    "frontend\apps\retail",
    "frontend\src\pages\sales",
    "frontend\src\pages\setup",
    "frontend\src\pages\merchandising"
)

$excludePatterns = @(
    "*Dashboard*",
    "*Report*",
    "*Analytics*",
    "PosPage.tsx",  # POS Billing
    "components"    # Skip component subfolders, focus on pages
)

$missingToolbar = @()

foreach ($dir in $directories) {
    if (Test-Path $dir) {
        $files = Get-ChildItem -Path $dir -Recurse -Filter "*.tsx" -File

        foreach ($file in $files) {
            # Check exclusions
            $skip = $false
            
            # Skip if path contains "components" directory
            if ($file.FullName -match "\\components\\") { $skip = $true }
            
            # Skip specific patterns
            foreach ($pattern in $excludePatterns) {
                if ($file.Name -like $pattern) { $skip = $true; break }
            }

            if (-not $skip) {
                $content = Get-Content $file.FullName -Raw
                # Check for MasterToolbar import or usage
                # We look for "MasterToolbar" or "MasterToolbarConfigDriven"
                if ($content -notmatch "MasterToolbar") {
                    $missingToolbar += $file.FullName
                }
            }
        }
    }
}

Write-Host "=== PAGES MISSING TOOLBAR ===" -ForegroundColor Cyan
if ($missingToolbar.Count -eq 0) {
    Write-Host "✅ All applicable pages have MasterToolbar!" -ForegroundColor Green
} else {
    $missingToolbar | ForEach-Object { 
        Write-Host "❌ $_" -ForegroundColor Red
        # Check if it's a real page or a helper component that slipped through
    }
}
