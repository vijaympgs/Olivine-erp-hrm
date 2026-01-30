# Clean Up All Seed Files - Keep Only ONE
# Purpose: Remove all redundant seed files, keep only the comprehensive one
# Date: 2026-01-09 20:47 IST

Write-Host ""
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host (" " * 35 + "SEED FILES CLEANUP") -ForegroundColor Cyan
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host ""

Write-Host "Philosophy: One seed to grow better!" -ForegroundColor Green
Write-Host ""

# The ONE seed to keep
$theSeed = "seed\seed_complete_database.py"

# All other seeds to DELETE
$seedsToDelete = @(
    "seed\seed_all_menu_items.py",
    "seed\seed_customers.py",
    "seed\seed_data.py",
    "seed\seed_default_roles.py",
    "seed\seed_default_users.py",
    "seed\seed_enterprise_masters.py",
    "seed\seed_finance.py",
    "seed\seed_masters.py",
    "seed\seed_menu_items_backend.py",
    "seed\seed_retail_menu_items.py",
    "seed\seed_toolbar_controls.py"
)

Write-Host "THE ONE SEED TO KEEP:" -ForegroundColor Green
Write-Host "  $theSeed" -ForegroundColor Green
Write-Host "    - 5 Companies, 25 Locations" -ForegroundColor White
Write-Host "    - 200 Items, 50 Customers, 50 Suppliers" -ForegroundColor White
Write-Host "    - Complete master data and toolbar configs" -ForegroundColor White
Write-Host ""

Write-Host "DELETING ALL OTHER SEEDS:" -ForegroundColor Yellow
$deletedCount = 0
foreach ($file in $seedsToDelete) {
    if (Test-Path $file) {
        Remove-Item $file -Force
        Write-Host "  Deleted: $file" -ForegroundColor Red
        $deletedCount++
    }
    else {
        Write-Host "  Not found: $file" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host (" " * 40 + "CLEANUP COMPLETE!") -ForegroundColor Green
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host ""

Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Files deleted:  $deletedCount" -ForegroundColor White
Write-Host "  Files kept:     1" -ForegroundColor White
Write-Host ""

Write-Host "The ONE seed file:" -ForegroundColor Cyan
Write-Host "  $theSeed" -ForegroundColor Green
Write-Host ""

Write-Host "To seed your database:" -ForegroundColor Cyan
Write-Host "  .\scripts\reset_and_seed_database.ps1" -ForegroundColor White
Write-Host ""

Write-Host "One seed to rule them all!" -ForegroundColor Green
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host ""
