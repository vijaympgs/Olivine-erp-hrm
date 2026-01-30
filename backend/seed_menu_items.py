"""
Seed ERP Menu Items with Toolbar Configuration
Run: python manage.py shell < seed_menu_items.py
"""
from core.auth_access.backend.user_management.models import ERPMenuItem

# All enabled config
ALL_ENABLED = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"

# Sample menu items for Retail module
MENU_ITEMS = [
    # Inventory
    {'menu_id': 'STOCK_LEVELS', 'menu_name': 'Stock Levels', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/levels'},
    {'menu_id': 'STOCK_BY_LOCATION', 'menu_name': 'Stock by Location', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'DASHBOARD', 'route_path': '/inventory/stock-by-location'},
    {'menu_id': 'STOCK_VALUATION', 'menu_name': 'Stock Valuation', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'DASHBOARD', 'route_path': '/inventory/stock-valuation'},
    {'menu_id': 'MOVEMENT_TRENDS', 'menu_name': 'Movement Trends', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'DASHBOARD', 'route_path': '/inventory/movement-trends'},
    {'menu_id': 'ALERTS_NOTIFICATIONS', 'menu_name': 'Alerts & Notifications', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/alerts'},
    {'menu_id': 'STOCK_BY_CATEGORY', 'menu_name': 'Stock by Category', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/stock-by-category'},
    {'menu_id': 'STOCK_BY_BATCH_SERIAL', 'menu_name': 'Stock by Batch/Serial', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/stock-by-batch-serial'},
    {'menu_id': 'LOW_STOCK_ALERTS', 'menu_name': 'Low Stock Alerts', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/alerts/low-stock'},
    {'menu_id': 'OVERSTOCK_ALERTS', 'menu_name': 'Overstock Alerts', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/alerts/overstock'},
    {'menu_id': 'STOCK_AGING', 'menu_name': 'Stock Aging Analysis', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/aging-analysis'},
    {'menu_id': 'GOODS_RECEIPT_VIEW', 'menu_name': 'Goods Receipt View', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/goods-receipt-view'},
    {'menu_id': 'GOODS_ISSUE_VIEW', 'menu_name': 'Goods Issue View', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/goods-issue-view'},
    {'menu_id': 'MOVEMENT_REPORTS', 'menu_name': 'Movement Reports', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/movement-reports'},
    
    # Physical Inventory (Phase 2)
    {'menu_id': 'CYCLE_COUNTING_SCHEDULE', 'menu_name': 'Cycle Counting Schedule', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/cycle-counting-schedule'},
    {'menu_id': 'STOCK_TAKE_LIST', 'menu_name': 'Stock Take List', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/stock-takes'},
    {'menu_id': 'STOCK_TAKE_EXECUTION', 'menu_name': 'Stock Take Execution', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'TRANSACTION', 'route_path': '/inventory/stock-take-execution'},
    {'menu_id': 'VARIANCE_ANALYSIS', 'menu_name': 'Variance Analysis', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'DASHBOARD', 'route_path': '/inventory/variance-analysis'},
    {'menu_id': 'COUNT_APPROVAL', 'menu_name': 'Count Approval', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/count-approval'},
    {'menu_id': 'RECONCILIATION', 'menu_name': 'Reconciliation', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'TRANSACTION', 'route_path': '/inventory/reconciliation'},
    {'menu_id': 'STOCK_TAKE_REPORTS', 'menu_name': 'Stock Take Reports', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/stock-take-reports'},

    # Replenishment Planning (Phase 3)
    {'menu_id': 'REORDER_RULES', 'menu_name': 'Reorder Rules', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/replenishment/rules'},
    {'menu_id': 'REPLENISHMENT_WORKSHEET', 'menu_name': 'Replenishment Worksheet', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'TRANSACTION', 'route_path': '/inventory/replenishment/worksheet'},
    {'menu_id': 'SAFETY_STOCK_ANALYSIS', 'menu_name': 'Safety Stock Analysis', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'DASHBOARD', 'route_path': '/inventory/replenishment/safety-stock'},
    {'menu_id': 'MIN_MAX_PLANNING', 'menu_name': 'Min/Max Planning', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'DASHBOARD', 'route_path': '/inventory/replenishment/min-max-planning'},

    # Batch & Serial Tracking (Phase 4)
    {'menu_id': 'BATCH_MANAGEMENT', 'menu_name': 'Batch Management', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/batches'},
    {'menu_id': 'SERIAL_TRACKING', 'menu_name': 'Serial Number Tracking', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/serials'},

    # Inventory Reports (Phase 5)
    {'menu_id': 'STOCK_SUMMARY_REPORT', 'menu_name': 'Stock Summary Report', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/reports/stock-summary'},
    {'menu_id': 'STOCK_VALUATION_REPORT', 'menu_name': 'Stock Valuation Report', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/reports/valuation-report'},
    {'menu_id': 'ABC_ANALYSIS', 'menu_name': 'ABC Analysis', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/reports/abc-analysis'},
    {'menu_id': 'VELOCITY_ANALYSIS', 'menu_name': 'Velocity Analysis', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/reports/velocity-analysis'},
    {'menu_id': 'DEAD_STOCK_REPORT', 'menu_name': 'Dead Stock Report', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/reports/dead-stock'},

    # Stock Adjustments (Phase 6)
    {'menu_id': 'ADJUSTMENT_ENTRY', 'menu_name': 'Stock Adjustment Entry', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'TRANSACTION', 'route_path': '/inventory/adjustments/new'},
    {'menu_id': 'ADJUSTMENT_HISTORY', 'menu_name': 'Adjustment History', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/adjustments/history'},
    {'menu_id': 'REASON_CODES', 'menu_name': 'Reason Code Management', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/adjustments/reason-codes'},
    {'menu_id': 'ADJUSTMENT_APPROVAL', 'menu_name': 'Approval Workflow', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/adjustments/approvals'},
    {'menu_id': 'ADJUSTMENT_REPORTS', 'menu_name': 'Adjustment Reports', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'REPORT', 'route_path': '/inventory/adjustments/reports'},

    # Inventory Configuration (Phase 7)
    {'menu_id': 'INV_PARAMETERS', 'menu_name': 'General Parameters', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'FORM', 'route_path': '/inventory/config/settings'},
    {'menu_id': 'MOVEMENT_TYPES', 'menu_name': 'Movement Types', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/config/movement-types'},
    {'menu_id': 'VALUATION_METHODS', 'menu_name': 'Valuation Methods', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/config/valuation-methods'},
    {'menu_id': 'APPROVAL_RULES', 'menu_name': 'Approval Rules', 'module_name': 'RETAIL', 'submodule': 'INVENTORY', 'view_type': 'LIST', 'route_path': '/inventory/config/approval-rules'},

    # Sales
    {'menu_id': 'SALES_QUOTES', 'menu_name': 'Sales Quotes', 'module_name': 'RETAIL', 'submodule': 'SALES', 'view_type': 'TRANSACTION', 'route_path': '/sales/quotes'},
    {'menu_id': 'SALES_ORDERS', 'menu_name': 'Sales Orders', 'module_name': 'RETAIL', 'submodule': 'SALES', 'view_type': 'TRANSACTION', 'route_path': '/sales/orders'},
    {'menu_id': 'SALES_INVOICES', 'menu_name': 'Sales Invoices', 'module_name': 'RETAIL', 'submodule': 'SALES', 'view_type': 'TRANSACTION', 'route_path': '/sales/invoices'},
    {'menu_id': 'SALES_RETURNS', 'menu_name': 'Sales Returns', 'module_name': 'RETAIL', 'submodule': 'SALES', 'view_type': 'TRANSACTION', 'route_path': '/sales/returns'},
    {'menu_id': 'SALES_CONFIG', 'menu_name': 'Sales Configuration', 'module_name': 'RETAIL', 'submodule': 'SALES', 'view_type': 'FORM', 'route_path': '/sales/configuration'},
    
    # Procurement
    {'menu_id': 'PURCHASE_REQUISITIONS', 'menu_name': 'Purchase Requisitions', 'module_name': 'RETAIL', 'submodule': 'PROCUREMENT', 'view_type': 'TRANSACTION', 'route_path': '/procurement/requisitions'},
    {'menu_id': 'PURCHASE_ORDERS', 'menu_name': 'Purchase Orders', 'module_name': 'RETAIL', 'submodule': 'PROCUREMENT', 'view_type': 'TRANSACTION', 'route_path': '/procurement/orders'},
    {'menu_id': 'GOODS_RECEIPTS', 'menu_name': 'Goods Receipts', 'module_name': 'RETAIL', 'submodule': 'PROCUREMENT', 'view_type': 'TRANSACTION', 'route_path': '/procurement/receipts'},
    
    # Masters
    {'menu_id': 'ITEM_MASTER', 'menu_name': 'Item Master', 'module_name': 'RETAIL', 'submodule': 'MASTERS', 'view_type': 'MASTER', 'route_path': '/inventory/item-master'},
    {'menu_id': 'CUSTOMER_MASTER', 'menu_name': 'Customer Master', 'module_name': 'RETAIL', 'submodule': 'MASTERS', 'view_type': 'MASTER', 'route_path': '/partners/customers'},
    {'menu_id': 'SUPPLIER_MASTER', 'menu_name': 'Supplier Master', 'module_name': 'RETAIL', 'submodule': 'MASTERS', 'view_type': 'MASTER', 'route_path': '/partners/suppliers'},
]

print("Seeding ERP Menu Items...")
created_count = 0
updated_count = 0

for item_data in MENU_ITEMS:
    menu_item, created = ERPMenuItem.objects.update_or_create(
        menu_id=item_data['menu_id'],
        defaults={
            'menu_name': item_data['menu_name'],
            'module_name': item_data['module_name'],
            'submodule': item_data.get('submodule'),
            'view_type': item_data.get('view_type', 'LIST'),
            'route_path': item_data.get('route_path'),
            'toolbar_config': ALL_ENABLED,
            'is_active': True,
            'is_system_menu': True,
            'menu_order': created_count + updated_count
        }
    )
    
    if created:
        created_count += 1
        print(f"✅ Created: {item_data['menu_name']}")
    else:
        updated_count += 1
        print(f"🔄 Updated: {item_data['menu_name']}")

print(f"\n✅ Seed complete: {created_count} created, {updated_count} updated")
print(f"Total menu items: {ERPMenuItem.objects.count()}")




