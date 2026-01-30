
import os
import sys
import django
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def setup_django():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    backend_dir = os.path.join(project_root, 'backend')
    if backend_dir not in sys.path:
        sys.path.insert(0, backend_dir)
        
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
    django.setup()

def standardize_toolbars():
    from core.auth_access.backend.user_management.models import ERPMenuItem

    # 1. Define Standard Patterns
    # N=New, E=Edit, S=Save, C=Cancel, K=Clear
    # V=View, D=Delete, R=Refresh, X=Exit
    # Q=Search, F=Filter
    # P=Print, M=Email, Y=Download, I=Upload
    # Z=Auth, T=Submit, J=Reject, A=Amend, H=Hold, O=Void

    PATTERN_MASTER = "NESCKVDXRQFX"         # Standard Master (Core + Search/Filter/Exit)
    PATTERN_TRANSACTION = "NESCKVDXRQFZTJAHO" # Transaction (Master + Workflow) + P?
    PATTERN_REPORT = "RQFPYMX"              # Report (Refresh, Search, Filter, Print, Export, Email, Exit)
    PATTERN_LIST = "NRQFXY"                 # Simple List (New, Refresh, Search, Filter, Exit, Export)

    # 2. Categorize Menu Items
    
    # MASTERS (Setup, Configuration, Master Data)
    # Using 'MASTERS' submodule or specific IDs
    # Note: 'pos-terminal-configuration' is POS submodule but is a Master.
    masters_query = ERPMenuItem.objects.filter(
        module_name='RETAIL'
    ).filter(
        submodule__in=['MASTERS'] 
    ) | ERPMenuItem.objects.filter(
        menu_id__in=[
            'pos-terminal-configuration', 
            'customer-list', 'customer-groups', 'loyalty', 
            'suppliers', 'compliance', 
            'inventory-parameters', 'movement-types', 'approval-rules', 
            'reason-codes', 'valuation-methods', 'reorder-rules', 
            'procurement-config', 'sales-config',
            'batch-mgmt', 'serial-tracking', 'expiry-mgmt'
        ]
    )

    # TRANSACTIONS (Operations, Documents)
    # Filter by submodule or keywords
    transactions_query = ERPMenuItem.objects.filter(
        module_name='RETAIL'
    ).filter(
        menu_id__in=[
            'pos-checkout', 'pos-day-open', 'pos-session-open', 'pos-session-close', 'pos-day-close', 'pos-settlement',
            'quotes', 'orders', 'invoices', 'returns',
            'requisitions', 'rfqs', 'purchase-orders', 'asns', 'receipts', 'purchase-returns', 'bills', 'payments',
            'adjustment-entry', 'stock-take-exec', 'reconciliation', 'replenish-suggest'
        ]
    )

    # REPORTS (Analytics, View-only lists)
    reports_query = ERPMenuItem.objects.filter(
        module_name='RETAIL'
    ).filter(
        menu_id__icontains='report'
    ) | ERPMenuItem.objects.filter(
        menu_id__icontains='analysis'
    ) | ERPMenuItem.objects.filter(
        menu_id__in=[
            'stock-levels', 'stock-by-location', 'stock-valuation', 'movement-trends', 'stock-alerts',
            'dashboard', 'retail-dashboard', 'inventory-overview',
            'movement-history', 'goods-receipt', 'goods-issue', 'internal-transfers', 'intercompany-transfers',
            'adjustment-history'
        ]
    )

    # 3. Apply Updates
    
    def apply_pattern(queryset, pattern, label):
        count = 0
        for item in queryset:
            # Only update if it's currently generic or manually flagged as update-needed
            # Or forcibly update all to enforce governance. 
            # Given user request "Derive a pattern", let's enforce.
            if item.applicable_toolbar_config != pattern:
                item.applicable_toolbar_config = pattern
                item.save()
                count += 1
        logger.info(f"Updated {count} items to {label} pattern ({pattern})")

    # Apply Lists first (as default fallback, maybe?) - No, apply specific first.
    
    # We'll rely on the queries. Note that one item might match multiple (e.g. contains 'report').
    # We should exclude previously matched ones if we want priority.
    # transactions match specifically designated IDs.
    
    apply_pattern(transactions_query, PATTERN_TRANSACTION, "TRANSACTION")
    
    # Masters might overlap if ID is in list.
    apply_pattern(masters_query, PATTERN_MASTER, "MASTER")
    
    # Reports
    apply_pattern(reports_query, PATTERN_REPORT, "REPORT")

if __name__ == '__main__':
    setup_django()
    standardize_toolbars()




