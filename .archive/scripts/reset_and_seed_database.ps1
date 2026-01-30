# OLIVINE ERP - Complete Database Reset & Seed
# Purpose: Reset database and load enterprise-grade data
# Owner: Astra (Full-Stack ERP Developer)
# Date: 2026-01-09 20:42 IST

Write-Host ""
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host (" " * 30 + "OLIVINE ERP - DATABASE RESET & SEED") -ForegroundColor Cyan
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host ""

# Step 1: Backup
Write-Host "[1/4] Backing up existing database..." -ForegroundColor Yellow
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
if (Test-Path "backend\db.sqlite3") {
    Copy-Item "backend\db.sqlite3" "backend\db.sqlite3.backup_$timestamp"
    Write-Host "  Backup created: db.sqlite3.backup_$timestamp" -ForegroundColor Green
}
else {
    Write-Host "  No existing database found" -ForegroundColor Yellow
}
Write-Host ""

# Step 2: Delete database
Write-Host "[2/4] Deleting existing database..." -ForegroundColor Yellow
if (Test-Path "backend\db.sqlite3") {
    Remove-Item "backend\db.sqlite3" -Force
    Write-Host "  Database deleted" -ForegroundColor Green
}
Write-Host ""

# Step 3: Run migrations
Write-Host "[3/4] Running migrations..." -ForegroundColor Yellow
python backend\manage.py migrate
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Migration failed! Exiting..." -ForegroundColor Red
    exit 1
}
Write-Host "  Migrations completed" -ForegroundColor Green
Write-Host ""

# Step 4: Seed enterprise data
Write-Host "[4/4] Seeding enterprise data..." -ForegroundColor Yellow
Write-Host "  This will create:" -ForegroundColor Cyan
Write-Host "    - 5 Companies" -ForegroundColor White
Write-Host "    - 25 Locations (5 per company)" -ForegroundColor White
Write-Host "    - 10 UOMs" -ForegroundColor White
Write-Host "    - 12+ Categories" -ForegroundColor White
Write-Host "    - 20 Brands" -ForegroundColor White
Write-Host "    - 20 Attributes with 100+ values" -ForegroundColor White
Write-Host "    - 200 Items with variants" -ForegroundColor White
Write-Host "    - 50 Customers" -ForegroundColor White
Write-Host "    - 50 Suppliers" -ForegroundColor White
Write-Host "    - 5 Test users with roles" -ForegroundColor White
Write-Host "    - Complete menu items & toolbar configs" -ForegroundColor White
Write-Host ""

python backend\manage.py seed_enterprise
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Seeding failed! Check errors above." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host (" " * 40 + "SETUP COMPLETE!") -ForegroundColor Green
Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host ""

Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "  1. Start Django server:  python backend\manage.py runserver" -ForegroundColor White
Write-Host "  2. Start frontend:       cd frontend && npm run dev" -ForegroundColor White
Write-Host "  3. Login at:             http://localhost:8000/admin/" -ForegroundColor White
Write-Host "  4. Test UOM page:        http://localhost:3000/inventory/uoms" -ForegroundColor White
Write-Host "  5. Test PO page:         http://localhost:3000/procurement/purchase-orders" -ForegroundColor White
Write-Host ""

Write-Host "Login Credentials:" -ForegroundColor Cyan
Write-Host "  admin / admin123        (System Administrator)" -ForegroundColor White
Write-Host "  boadmin / boadmin123    (Back Office Manager)" -ForegroundColor White
Write-Host "  posadmin / posadmin123  (POS Manager)" -ForegroundColor White
Write-Host ""

Write-Host "=" * 100 -ForegroundColor Cyan
Write-Host ""
