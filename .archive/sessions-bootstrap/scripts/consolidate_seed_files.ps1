# Consolidate Seed Files Script
# Purpose: Copy all seed files to seed/ folder for easy access
# Date: 2026-01-09 20:36 IST

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "CONSOLIDATING SEED FILES" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Create seed folder if it doesn't exist
if (-not (Test-Path "seed")) {
    New-Item -ItemType Directory -Path "seed" | Out-Null
    Write-Host "Created seed/ folder" -ForegroundColor Green
}

# Copy seed files from various locations
$seedFiles = @(
    # From core/auth_access
    @{
        Source = "core\auth_access\backend\user_management\management\commands\seed_default_roles.py"
        Dest = "seed\seed_default_roles.py"
    },
    @{
        Source = "core\auth_access\backend\user_management\management\commands\seed_default_users.py"
        Dest = "seed\seed_default_users.py"
    },
    @{
        Source = "core\auth_access\backend\user_management\management\commands\seed_retail_menu_items.py"
        Dest = "seed\seed_retail_menu_items.py"
    },
    @{
        Source = "core\auth_access\backend\user_management\management\commands\seed_all_menu_items.py"
        Dest = "seed\seed_all_menu_items.py"
    },
    
    # From core/org_structure
    @{
        Source = "core\org_structure\backend\company\management\commands\seed_data.py"
        Dest = "seed\seed_data.py"
    },
    @{
        Source = "core\org_structure\backend\company\management\commands\seed_masters.py"
        Dest = "seed\seed_masters.py"
    },
    
    # From backend
    @{
        Source = "backend\seed_menu_items.py"
        Dest = "seed\seed_menu_items_backend.py"
    },
    @{
        Source = "backend\scripts\seed_toolbar_controls.py"
        Dest = "seed\seed_toolbar_controls.py"
    },
    
    # From apps
    @{
        Source = "apps\crm\backend\customer\management\commands\seed_customers.py"
        Dest = "seed\seed_customers.py"
    },
    @{
        Source = "apps\fms\backend\finance\management\commands\seed_finance.py"
        Dest = "seed\seed_finance.py"
    }
)

$copiedCount = 0
$skippedCount = 0

foreach ($file in $seedFiles) {
    if (Test-Path $file.Source) {
        Copy-Item -Path $file.Source -Destination $file.Dest -Force
        Write-Host "Copied: $($file.Dest)" -ForegroundColor Green
        $copiedCount++
    }
    else {
        Write-Host "Skipped (not found): $($file.Source)" -ForegroundColor Yellow
        $skippedCount++
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "CONSOLIDATION COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  - Files copied: $copiedCount" -ForegroundColor White
Write-Host "  - Files skipped: $skippedCount" -ForegroundColor White
Write-Host "  - Target folder: seed/" -ForegroundColor White

Write-Host ""
Write-Host "All seed files are now in the seed/ folder!" -ForegroundColor Green
Write-Host ""
