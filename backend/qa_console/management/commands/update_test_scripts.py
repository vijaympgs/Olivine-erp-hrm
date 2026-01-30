# backend/qa_console/management/commands/update_test_scripts.py

from django.core.management.base import BaseCommand
from backend.qa_console.models import TestReadiness


class Command(BaseCommand):
    help = 'Update test script paths for components with existing test scripts'

    def handle(self, *args, **options):
        updates = [
            {
                'menu_id': 'requisitions',
                'script_path': 'retail/backend/procurement/pr/tests/test_4_1_purchase_requisition.py'
            },
            {
                'menu_id': 'rfqs',
                'script_path': 'retail/backend/procurement/rfq/tests/test_4_2_request_for_quotation.py'
            },
            {
                'menu_id': 'purchase-orders',
                'script_path': 'retail/backend/procurement/po/tests/test_4_3_purchase_order.py'
            },
            {
                'menu_id': 'asns',
                'script_path': 'retail/backend/procurement/asn/tests/test_4_5_advance_shipment_notice.py'
            },
            {
                'menu_id': 'receipts',
                'script_path': 'retail/backend/procurement/grn/tests/test_4_6_goods_receipts.py'
            },
            {
                'menu_id': 'bills',
                'script_path': 'retail/backend/procurement/invoice/tests/test_4_7_invoice_matching.py'
            },
            {
                'menu_id': 'purchase-returns',
                'script_path': 'retail/backend/procurement/returns/tests/test_4_8_purchase_returns.py'
            },
            {
                'menu_id': 'suppliers',
                'script_path': 'backend/domain/company/tests/test_vendors_master_data.py'
            },
            {
                'menu_id': 'payments',
                'script_path': 'retail/backend/procurement/payments/tests/test_payments_processing.py'
            },
            {
                'menu_id': 'compliance',
                'script_path': 'retail/backend/procurement/compliance/tests/test_compliance_management.py'
            },
            {
                'menu_id': 'procurement-config',
                'script_path': 'retail/backend/procurement/tests/test_configuration_management.py'
            },
            # Inventory Module (Comprehensive Mapping)
            # 1. Dashboard
            { 'menu_id': 'inventory-dashboard', 'script_path': 'retail/backend/inventory/tests/test_5_1_inventory_dashboard.py' },
            { 'menu_id': 'inventory-overview', 'script_path': 'retail/backend/inventory/tests/test_5_1_inventory_dashboard.py' },
            { 'menu_id': 'stock-by-location', 'script_path': 'retail/backend/inventory/tests/test_5_1_inventory_dashboard.py' },
            { 'menu_id': 'stock-valuation', 'script_path': 'retail/backend/inventory/tests/test_5_1_inventory_dashboard.py' },
            { 'menu_id': 'movement-trends', 'script_path': 'retail/backend/inventory/tests/test_5_1_inventory_dashboard.py' },
            { 'menu_id': 'stock-alerts', 'script_path': 'retail/backend/inventory/tests/test_5_1_inventory_dashboard.py' },

            # 2. Stock Management
            { 'menu_id': 'stock-management', 'script_path': 'retail/backend/inventory/tests/test_5_2_stock_management.py' },
            { 'menu_id': 'stock-all', 'script_path': 'retail/backend/inventory/tests/test_5_2_stock_management.py' },
            { 'menu_id': 'stock-location-view', 'script_path': 'retail/backend/inventory/tests/test_5_2_stock_management.py' },
            { 'menu_id': 'stock-category', 'script_path': 'retail/backend/inventory/tests/test_5_2_stock_management.py' },
            { 'menu_id': 'stock-batch', 'script_path': 'retail/backend/inventory/tests/test_5_2_stock_management.py' },
            { 'menu_id': 'low-stock-alerts', 'script_path': 'retail/backend/inventory/tests/test_5_2_stock_management.py' },
            { 'menu_id': 'overstock-alerts', 'script_path': 'retail/backend/inventory/tests/test_5_2_stock_management.py' },
            { 'menu_id': 'stock-aging', 'script_path': 'retail/backend/inventory/tests/test_5_2_stock_management.py' },

            # 3. Stock Movements
            { 'menu_id': 'stock-movements', 'script_path': 'retail/backend/inventory/tests/test_5_3_stock_movements.py' },
            { 'menu_id': 'movement-history', 'script_path': 'retail/backend/inventory/tests/test_5_3_stock_movements.py' },
            { 'menu_id': 'goods-receipt', 'script_path': 'retail/backend/inventory/tests/test_5_3_stock_movements.py' },
            { 'menu_id': 'goods-issue', 'script_path': 'retail/backend/inventory/tests/test_5_3_stock_movements.py' },
            { 'menu_id': 'internal-transfers', 'script_path': 'retail/backend/inventory/tests/test_5_3_stock_movements.py' },
            { 'menu_id': 'intercompany-transfers', 'script_path': 'retail/backend/inventory/tests/test_5_3_stock_movements.py' },
            { 'menu_id': 'movement-reports', 'script_path': 'retail/backend/inventory/tests/test_5_3_stock_movements.py' },

            # 4. Stock Adjustments
            { 'menu_id': 'stock-adjustments', 'script_path': 'retail/backend/inventory/tests/test_5_4_stock_adjustments.py' },
            { 'menu_id': 'adjustment-entry', 'script_path': 'retail/backend/inventory/tests/test_5_4_stock_adjustments.py' },
            { 'menu_id': 'adjustment-history', 'script_path': 'retail/backend/inventory/tests/test_5_4_stock_adjustments.py' },
            { 'menu_id': 'reason-codes', 'script_path': 'retail/backend/inventory/tests/test_5_4_stock_adjustments.py' },
            { 'menu_id': 'adjustment-approval', 'script_path': 'retail/backend/inventory/tests/test_5_4_stock_adjustments.py' },
            { 'menu_id': 'adjustment-reports', 'script_path': 'retail/backend/inventory/tests/test_5_4_stock_adjustments.py' },

            # 5. Physical Inventory
            { 'menu_id': 'physical-inventory', 'script_path': 'retail/backend/inventory/tests/test_5_5_physical_inventory.py' },
            { 'menu_id': 'cycle-schedule', 'script_path': 'retail/backend/inventory/tests/test_5_5_physical_inventory.py' },
            { 'menu_id': 'stock-take-exec', 'script_path': 'retail/backend/inventory/tests/test_5_5_physical_inventory.py' },
            { 'menu_id': 'variance-analysis', 'script_path': 'retail/backend/inventory/tests/test_5_5_physical_inventory.py' },
            { 'menu_id': 'count-approval', 'script_path': 'retail/backend/inventory/tests/test_5_5_physical_inventory.py' },
            { 'menu_id': 'reconciliation', 'script_path': 'retail/backend/inventory/tests/test_5_5_physical_inventory.py' },

            # 6. Inventory Valuation
            { 'menu_id': 'inventory-valuation', 'script_path': 'retail/backend/inventory/tests/test_5_6_inventory_valuation.py' },
            { 'menu_id': 'valuation-methods', 'script_path': 'retail/backend/inventory/tests/test_5_6_inventory_valuation.py' },
            { 'menu_id': 'cost-analysis', 'script_path': 'retail/backend/inventory/tests/test_5_6_inventory_valuation.py' },
            { 'menu_id': 'period-valuation', 'script_path': 'retail/backend/inventory/tests/test_5_6_inventory_valuation.py' },

            # 7. Replenishment (5.7)
            { 'menu_id': 'reorder-points', 'script_path': 'retail/backend/inventory/tests/test_5_7_replenishment.py' },
            { 'menu_id': 'safety-stock', 'script_path': 'retail/backend/inventory/tests/test_5_7_replenishment.py' },
            { 'menu_id': 'min-max', 'script_path': 'retail/backend/inventory/tests/test_5_7_replenishment.py' },
            { 'menu_id': 'reorder-policies', 'script_path': 'retail/backend/inventory/tests/test_5_7_replenishment.py' },
            { 'menu_id': 'demand-forecast', 'script_path': 'retail/backend/inventory/tests/test_5_7_replenishment.py' },
            { 'menu_id': 'replenish-suggest', 'script_path': 'retail/backend/inventory/tests/test_5_7_replenishment.py' },

            # 8. Item Tracking (5.8)
            { 'menu_id': 'batch-mgmt', 'script_path': 'retail/backend/inventory/tests/test_5_8_item_tracking.py' },
            { 'menu_id': 'serial-tracking', 'script_path': 'retail/backend/inventory/tests/test_5_8_item_tracking.py' },
            { 'menu_id': 'expiry-mgmt', 'script_path': 'retail/backend/inventory/tests/test_5_8_item_tracking.py' },
            { 'menu_id': 'batch-trace', 'script_path': 'retail/backend/inventory/tests/test_5_8_item_tracking.py' },
            { 'menu_id': 'recall-mgmt', 'script_path': 'retail/backend/inventory/tests/test_5_8_item_tracking.py' },

            # 9. Inventory Reports (5.9)
            { 'menu_id': 'stock-summary-report', 'script_path': 'retail/backend/inventory/tests/test_5_9_inventory_reports.py' },
            { 'menu_id': 'movement-report', 'script_path': 'retail/backend/inventory/tests/test_5_9_inventory_reports.py' },
            { 'menu_id': 'valuation-report', 'script_path': 'retail/backend/inventory/tests/test_5_9_inventory_reports.py' },
            { 'menu_id': 'aging-report', 'script_path': 'retail/backend/inventory/tests/test_5_9_inventory_reports.py' },
            { 'menu_id': 'abc-analysis', 'script_path': 'retail/backend/inventory/tests/test_5_9_inventory_reports.py' },
            { 'menu_id': 'velocity-analysis', 'script_path': 'retail/backend/inventory/tests/test_5_9_inventory_reports.py' },
            { 'menu_id': 'dead-stock', 'script_path': 'retail/backend/inventory/tests/test_5_9_inventory_reports.py' },

            # 10. Inventory Setup (5.10)
            { 'menu_id': 'inventory-setup', 'script_path': 'retail/backend/inventory/tests/test_5_10_inventory_setup.py' },
            { 'menu_id': 'revaluation', 'script_path': 'retail/backend/inventory/tests/test_5_10_inventory_setup.py' },

            # Sales Module (Comprehensive Mapping - 6.1 to 6.5)
            # 1. Sales Quotation (6.1)
            { 'menu_id': 'quotes', 'script_path': 'retail/backend/sales/tests/test_6_1_sales_quotation.py' },
            { 'menu_id': 'quote-list', 'script_path': 'retail/backend/sales/tests/test_6_1_sales_quotation.py' },
            { 'menu_id': 'quote-create', 'script_path': 'retail/backend/sales/tests/test_6_1_sales_quotation.py' },
            { 'menu_id': 'quote-approval', 'script_path': 'retail/backend/sales/tests/test_6_1_sales_quotation.py' },
            { 'menu_id': 'quote-revision', 'script_path': 'retail/backend/sales/tests/test_6_1_sales_quotation.py' },
            { 'menu_id': 'quote-conversion', 'script_path': 'retail/backend/sales/tests/test_6_1_sales_quotation.py' },

            # 2. Sales Order (6.2)
            { 'menu_id': 'orders', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-list', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-create', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-approval', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-fulfillment', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-allocation', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-picking', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-packing', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-shipping', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },
            { 'menu_id': 'order-delivery', 'script_path': 'retail/backend/sales/tests/test_6_2_sales_order.py' },

            # 3. Sales Invoice (6.3)
            { 'menu_id': 'invoices', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'invoice-list', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'invoice-create', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'invoice-approval', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'invoice-matching', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'payment-recording', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'payment-allocation', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'invoice-dunning', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'credit-notes', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },
            { 'menu_id': 'revenue-recognition', 'script_path': 'retail/backend/sales/tests/test_6_3_sales_invoice.py' },

            # 4. Sales Return / RMA (6.4)
            { 'menu_id': 'returns', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },
            { 'menu_id': 'rma-list', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },
            { 'menu_id': 'rma-create', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },
            { 'menu_id': 'rma-approval', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },
            { 'menu_id': 'return-receipt', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },
            { 'menu_id': 'return-inspection', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },
            { 'menu_id': 'refund-processing', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },
            { 'menu_id': 'exchange-orders', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },
            { 'menu_id': 'return-disposition', 'script_path': 'retail/backend/sales/tests/test_6_4_sales_return.py' },

            # 5. Sales Configuration (6.5)
            { 'menu_id': 'sales-config', 'script_path': 'retail/backend/sales/tests/test_6_5_sales_configuration.py' },
            { 'menu_id': 'sales-process-settings', 'script_path': 'retail/backend/sales/tests/test_6_5_sales_configuration.py' },
            { 'menu_id': 'sales-tolerance-settings', 'script_path': 'retail/backend/sales/tests/test_6_5_sales_configuration.py' },
            { 'menu_id': 'sales-approval-matrix', 'script_path': 'retail/backend/sales/tests/test_6_5_sales_configuration.py' },
            { 'menu_id': 'return-policy-config', 'script_path': 'retail/backend/sales/tests/test_6_5_sales_configuration.py' },
            { 'menu_id': 'pricing-config', 'script_path': 'retail/backend/sales/tests/test_6_5_sales_configuration.py' },
        ]

        updated_count = 0
        created_count = 0

        for update_data in updates:
            menu_id = update_data['menu_id']
            script_path = update_data['script_path']

            # Determine menu label
            label_map = {
                'requisitions': 'Requisitions',
                'rfqs': 'Requests for Quotation',
                'purchase-orders': 'Purchase Orders',
                'asns': 'ASNs',
                'receipts': 'Goods Receipts',
                'bills': 'Invoice Matching',
                'purchase-returns': 'Purchase Returns',
                'suppliers': 'Vendors',
                'payments': 'Payments',
                'compliance': 'Compliance',
                'procurement-config': 'Configuration',
                # Inventory
                'inventory-dashboard': 'Dashboard',
                'stock-management': 'Stock Management',
                'stock-movements': 'Stock Movements',
                'stock-adjustments': 'Stock Adjustments',
                'stock-take': 'Physical Inventory',
                'inventory-valuation': 'Valuation',
                # Sales
                'quotes': 'Sales Quotations',
                'quote-list': 'Quote List',
                'quote-create': 'Create Quote',
                'quote-approval': 'Quote Approval',
                'quote-revision': 'Quote Revision',
                'quote-conversion': 'Quote Conversion',
                'orders': 'Sales Orders',
                'order-list': 'Order List',
                'order-create': 'Create Order',
                'order-approval': 'Order Approval',
                'order-fulfillment': 'Order Fulfillment',
                'order-allocation': 'Inventory Allocation',
                'order-picking': 'Picking',
                'order-packing': 'Packing',
                'order-shipping': 'Shipping',
                'order-delivery': 'Delivery',
                'invoices': 'Sales Invoices',
                'invoice-list': 'Invoice List',
                'invoice-create': 'Create Invoice',
                'invoice-approval': 'Invoice Approval',
                'invoice-matching': 'Invoice Matching',
                'payment-recording': 'Payment Recording',
                'payment-allocation': 'Payment Allocation',
                'invoice-dunning': 'Dunning',
                'credit-notes': 'Credit Notes',
                'revenue-recognition': 'Revenue Recognition',
                'returns': 'Sales Returns (RMA)',
                'rma-list': 'RMA List',
                'rma-create': 'Create RMA',
                'rma-approval': 'RMA Approval',
                'return-receipt': 'Return Receipt',
                'return-inspection': 'Return Inspection',
                'refund-processing': 'Refund Processing',
                'exchange-orders': 'Exchange Orders',
                'return-disposition': 'Return Disposition',
                'sales-config': 'Sales Configuration',
                'sales-process-settings': 'Process Settings',
                'sales-tolerance-settings': 'Tolerance Settings',
                'sales-approval-matrix': 'Approval Matrix',
                'return-policy-config': 'Return Policy',
                'pricing-config': 'Pricing Configuration',
            }
            
            obj, created = TestReadiness.objects.update_or_create(
                menu_id=menu_id,
                defaults={
                    'script_path': script_path,
                    'app_id': 'retail',
                    'module_id': 'sales' if 'sales' in script_path else ('inventory' if 'inventory' in script_path else 'procurement'),
                    'menu_label': label_map.get(menu_id, menu_id),
                    'ui_status': 'Done' if 'sales' in script_path else 'Pending'
                }
            )

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created: {menu_id} → {script_path}')
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Updated: {menu_id} → {script_path}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n📊 Summary: {created_count} created, {updated_count} updated'
            )
        )




