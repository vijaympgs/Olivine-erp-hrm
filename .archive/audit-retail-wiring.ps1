# Retail Sidebar Wiring Audit Script
# Extract all Retail menu items and check router registration

Write-Host "=== RETAIL SIDEBAR WIRING AUDIT ===" -ForegroundColor Cyan
Write-Host ""

# Define Retail paths from menuConfig.ts (manually extracted)
$retailPaths = @(
    # Dashboard
    "/retail/dashboard",
    "/test-console",
    
    # Store Ops (7 items)
    "/pos/ui",
    "/operations/pos/day-open",
    "/operations/pos/session-open",
    "/operations/pos/session-close",
    "/operations/pos/day-close",
    "/operations/pos/settlement",
    "/pos/terminal",
    
    # Sales (5 items)
    "/sales/quotes",
    "/sales/orders",
    "/sales/invoices",
    "/sales/returns",
    "/sales/configuration",
    
    # Merchandising (9 items)
    "/inventory/item-master",
    "/inventory/attributes",
    "/inventory/attribute-values",
    "/inventory/attribute-templates",
    "/inventory/price-lists",
    "/setup/simple-masters",
    "/inventory/uoms",
    
    # Inventory Dashboard (5 items)
    "/inventory/dashboard",
    "/inventory/stock-by-location",
    "/inventory/stock-valuation",
    "/inventory/movement-trends",
    "/inventory/alerts",
    
    # Stock Management (7 items)
    "/inventory/levels",
    "/inventory/stock-by-category",
    "/inventory/stock-by-batch-serial",
    "/inventory/alerts/low-stock",
    "/inventory/alerts/overstock",
    "/inventory/aging-analysis",
    
    # Stock Movements (6 items)
    "/inventory/movements",
    "/inventory/goods-receipt-view",
    "/inventory/goods-issue-view",
    "/inventory/transfers",
    "/inventory/intercompany",
    "/inventory/movement-reports",
    
    # Stock Adjustments (5 items)
    "/inventory/adjustments/new",
    "/inventory/adjustments/history",
    "/inventory/adjustments/reason-codes",
    "/inventory/adjustments/approvals",
    "/inventory/adjustments/reports",
    
    # Physical Inventory (7 items)
    "/inventory/cycle-counting-schedule",
    "/inventory/stock-takes",
    "/inventory/stock-take-execution/new",
    "/inventory/variance-analysis/latest",
    "/inventory/count-approval",
    "/inventory/reconciliation/latest",
    "/inventory/stock-take-reports",
    
    # Inventory Valuation (4 items - note: some point to /inventory/levels)
    # Already counted above
    
    # Replenishment (4 items)
    "/inventory/replenishment/rules",
    "/inventory/replenishment/worksheet",
    "/inventory/replenishment/safety-stock",
    "/inventory/replenishment/min-max-planning",
    
    # Batch & Serial (4 items)
    "/inventory/batches",
    "/inventory/serials",
    # "/inventory/levels/low_stock" - already counted
    # "/inventory/movements" - already counted
    
    # Inventory Reports (7 items)
    "/inventory/reports/stock-summary",
    # "/inventory/movement-reports" - already counted
    "/inventory/reports/valuation-report",
    # "/inventory/aging-analysis" - already counted
    "/inventory/reports/abc-analysis",
    "/inventory/reports/velocity-analysis",
    "/inventory/reports/dead-stock",
    
    # Inventory Configuration (4 items)
    "/inventory/config/settings",
    "/inventory/config/movement-types",
    "/inventory/config/valuation-methods",
    "/inventory/config/approval-rules",
    
    # Procurement (11 items)
    "/partners/suppliers",
    "/procurement/compliance",
    "/procurement/requisitions",
    "/procurement/rfqs",
    "/procurement/orders",
    "/procurement/asns",
    "/procurement/receipts",
    "/procurement/returns",
    "/procurement/bills",
    "/procurement/payments",
    "/procurement/configuration",
    
    # Customers (3 items)
    "/partners/customers",
    "/customers/groups",
    "/customers/loyalty"
)

# Get unique paths
$uniqueRetailPaths = $retailPaths | Sort-Object -Unique

Write-Host "Total Retail Menu Items: $($uniqueRetailPaths.Count)" -ForegroundColor Yellow
Write-Host ""

# Read router.tsx
$routerContent = Get-Content "frontend\src\app\router.tsx" -Raw

# Check each path
$wired = @()
$unwired = @()

foreach ($path in $uniqueRetailPaths) {
    # Escape special regex characters
    $escapedPath = [regex]::Escape($path)
    
    # Check if path exists in router
    if ($routerContent -match "path:\s*[`"']$escapedPath[`"']") {
        $wired += $path
    } else {
        $unwired += $path
    }
}

# Display Results
Write-Host "=== WIRED PATHS ($($wired.Count)) ===" -ForegroundColor Green
$wired | ForEach-Object { Write-Host "  ✅ $_" -ForegroundColor Green }

Write-Host ""
Write-Host "=== UNWIRED PATHS ($($unwired.Count)) ===" -ForegroundColor Red
$unwired | ForEach-Object { Write-Host "  ❌ $_" -ForegroundColor Red }

Write-Host ""
Write-Host "=== SUMMARY ===" -ForegroundColor Cyan
Write-Host "Total Retail Items: $($uniqueRetailPaths.Count)"
Write-Host "Wired: $($wired.Count) ($([math]::Round(($wired.Count / $uniqueRetailPaths.Count) * 100, 1))%)" -ForegroundColor Green
Write-Host "Unwired: $($unwired.Count) ($([math]::Round(($unwired.Count / $uniqueRetailPaths.Count) * 100, 1))%)" -ForegroundColor Red
