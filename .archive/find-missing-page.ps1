# Find the missing Inventory page
# Compare menu items vs actual pages

$menuItems = @(
    # Dashboard (5)
    "InventoryDashboard",
    "StockByLocation",
    "StockValuation",
    "MovementTrends",
    "AlertsNotifications",
    
    # Stock Management (7)
    "StockLevelList",
    "StockByLocation",  # duplicate
    "StockByCategory",
    "StockByBatchSerial",
    "LowStockAlerts",
    "OverstockAlerts",
    "StockAgingAnalysis",
    
    # Stock Movements (6)
    "StockMovementList",
    "GoodsReceiptView",
    "GoodsIssueView",
    "TransferList",
    "IntercompanyTransferList",
    "MovementReports",
    
    # Stock Adjustments (5)
    "AdjustmentForm",
    "AdjustmentList",
    "ReasonCodeList",
    "AdjustmentApprovalList",
    "AdjustmentReport",
    
    # Physical Inventory (8)
    "CycleCountingSchedule",
    "StockTakeList",
    "StockTakeForm",
    "StockTakeExecution",
    "VarianceAnalysis",
    "CountApproval",
    "Reconciliation",
    "StockTakeReports",
    
    # Valuation (4)
    "ValuationMethods",
    "ValuationReports",
    "CostAnalysis",
    "PeriodEndValuation",
    
    # Replenishment (4)
    "ReorderRules",
    "ReplenishmentWorksheet",
    "SafetyStockAnalysis",
    "MinMaxPlanning",
    
    # Batch & Serial (4)
    "BatchList",
    "SerialList",
    "ExpiryManagement",
    "BatchTraceability",
    
    # Reports (7)
    "StockSummaryReport",
    "MovementReports",  # duplicate
    "StockValuationReport",
    "StockAgingAnalysis",  # duplicate
    "ABCAnalysisReport",
    "VelocityAnalysisReport",
    "DeadStockReport",
    
    # Configuration (4)
    "InventorySettings",
    "MovementTypeList",
    "ValuationMethod",
    "ApprovalRules",
    
    # Merchandising (9)
    "ItemMasterSetup",
    "AttributeSetup",
    "AttributeValueSetup",
    "ProductAttributeTemplateSetup",
    "PriceListSetup",
    "UOMSetup",
    "UOMForm",
    "InventorySetup",
    "ReorderPolicyList"
)

$actualPages = Get-ChildItem -Path "frontend\apps\retail\inventory\pages" -Filter "*.tsx" | Select-Object -ExpandProperty Name

Write-Host "=== INVENTORY PAGE ANALYSIS ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Total Menu Items (with duplicates): $($menuItems.Count)"
Write-Host "Unique Menu Items: $(($menuItems | Sort-Object -Unique).Count)"
Write-Host "Actual Pages: $($actualPages.Count)"
Write-Host ""

# Find missing
$missing = @()
foreach ($item in ($menuItems | Sort-Object -Unique)) {
    $found = $false
    foreach ($page in $actualPages) {
        if ($page -like "*$item*") {
            $found = $true
            break
        }
    }
    if (-not $found) {
        $missing += $item
    }
}

if ($missing.Count -eq 0) {
    Write-Host "✅ All menu items have corresponding pages!" -ForegroundColor Green
} else {
    Write-Host "❌ Missing pages:" -ForegroundColor Red
    $missing | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
}
