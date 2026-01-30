# Cleanup Redundant Seed Files
# Purpose: Remove redundant seed files, keep only essential ones
# Date: 2026-01-09 20:40 IST

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "CLEANING UP REDUNDANT SEED FILES" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Files to DELETE (redundant)
$filesToDelete = @(
    "seed\seed_all_menu_items.py",
    "seed\seed_customers.py",
    "seed\seed_data.py",
    "seed\seed_default_roles.py",
    "seed\seed_default_users.py",
    "seed\seed_finance.py",
    "seed\seed_masters.py",
    "seed\seed_menu_items_backend.py",
    "seed\seed_retail_menu_items.py"
)

# Files to KEEP
$filesToKeep = @(
    "seed\seed_complete_database.py",
    "seed\seed_enterprise_masters.py",
    "seed\seed_toolbar_controls.py"
)

Write-Host "Files to KEEP:" -ForegroundColor Green
foreach ($file in $filesToKeep) {
    if (Test-Path $file) {
        Write-Host "  ✓ $file" -ForegroundColor Green
    }
    else {
        Write-Host "  ⚠ $file (not found)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Files to DELETE:" -ForegroundColor Yellow
$deletedCount = 0
foreach ($file in $filesToDelete) {
    if (Test-Path $file) {
        Remove-Item $file -Force
        Write-Host "  ✓ Deleted: $file" -ForegroundColor Red
        $deletedCount++
    }
    else {
        Write-Host "  - Not found: $file" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "CLEANUP COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  - Files deleted: $deletedCount" -ForegroundColor White
Write-Host "  - Files remaining: $($filesToKeep.Count)" -ForegroundColor White

Write-Host ""
Write-Host "Remaining seed files:" -ForegroundColor Cyan
Write-Host "  1. seed_complete_database.py    - Main seed (RECOMMENDED)" -ForegroundColor White
Write-Host "  2. seed_enterprise_masters.py   - Alternative (200 items)" -ForegroundColor White
Write-Host "  3. seed_toolbar_controls.py     - Toolbar configs only" -ForegroundColor White

Write-Host ""
Write-Host "To seed database, run:" -ForegroundColor Cyan
Write-Host "  python seed\seed_complete_database.py" -ForegroundColor White
Write-Host ""
