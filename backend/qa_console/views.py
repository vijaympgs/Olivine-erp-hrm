
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TestReadiness
from .serializers import TestReadinessSerializer
import os
import glob

class TestReadinessViewSet(viewsets.ModelViewSet):
    queryset = TestReadiness.objects.all()
    serializer_class = TestReadinessSerializer
    lookup_field = 'menu_id'

    @action(detail=False, methods=['post'])
    def sync_entries(self, request):
        """
        Bulk upsert entries passed from the frontend (which holds the menuConfig source of truth).
        """
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Expected a list of entries"}, status=status.HTTP_400_BAD_REQUEST)
        
        created_count = 0
        updated_count = 0
        
        for item in data:
            menu_id = item.get('menu_id')
            if not menu_id:
                continue
                
            obj, created = TestReadiness.objects.update_or_create(
                menu_id=menu_id,
                defaults={
                    'app_id': item.get('app_id', ''),
                    'module_id': item.get('module_id', ''),
                    'sub_module_id': item.get('sub_module_id', None),
                    'menu_label': item.get('menu_label', ''),
                    # We don't overwrite statuses if they exist, only if creating?
                    # Actually update_or_create overwrites defaults.
                    # We want to preserve statuses if they exist.
                }
            )
            if created:
                created_count += 1
            else:
                updated_count += 1
                
        return Response({
            "message": "Sync complete",
            "created": created_count,
            "updated": updated_count
        })

    @action(detail=False, methods=['post'])
    def refresh_scripts(self, request):
        """
        Scan filesystem for test scripts and BBP documents, update database with paths.
        """
        try:
            # Define base paths
            backend_base = os.path.join(os.path.dirname(__file__), '..')
            project_root = os.path.join(backend_base, '..')
            bbp_base = os.path.join(project_root, '.steering', '00AGENT_ONBOARDING', '02_Business_Blueprints')
            
            # Mapping of component directories to menu_ids (for test scripts)
            component_map = {
                'pr': 'requisitions',
                'rfq': 'rfqs',
                'po': 'purchase-orders',
                'asn': 'asns',
                'grn': 'receipts',
                'invoice': 'bills',
                'returns': 'purchase-returns',
                'payments': 'payments',
                'compliance': 'compliance',
            }
            
            updated_count = 0
            found_scripts = []
            found_bbps = []
            
            # Scan for test scripts
            test_base_path = os.path.join(backend_base, 'domain', 'procurement')
            for component_dir, menu_id in component_map.items():
                test_dir = os.path.join(test_base_path, component_dir, 'tests')
                if os.path.exists(test_dir):
                    pattern = os.path.join(test_dir, 'test_4_*.py')
                    scripts = glob.glob(pattern)
                    
                    if scripts:
                        script_path = scripts[0]
                        rel_path = os.path.relpath(script_path, backend_base)
                        rel_path = rel_path.replace('\\', '/')
                        rel_path = f'backend/{rel_path}'
                        
                        try:
                            obj = TestReadiness.objects.get(menu_id=menu_id)
                            obj.script_path = rel_path
                            obj.save()
                            updated_count += 1
                            found_scripts.append({
                                'menu_id': menu_id,
                                'script_path': rel_path
                            })
                        except TestReadiness.DoesNotExist:
                            pass
            
            # Scan for BBP documents
            if os.path.exists(bbp_base):
                # Scan all subdirectories for BBP markdown files
                for root, dirs, files in os.walk(bbp_base):
                    for file in files:
                        if file.endswith('.md') and 'bbp' in file.lower():
                            bbp_full_path = os.path.join(root, file)
                            bbp_rel_path = os.path.relpath(bbp_full_path, project_root)
                            bbp_rel_path = bbp_rel_path.replace('\\', '/')
                            
                            # Try to match BBP to menu items based on filename or content
                            # For now, store the path for manual mapping or future enhancement
                            found_bbps.append({
                                'file': file,
                                'path': bbp_rel_path
                            })
            
            # Update all entries with BBP availability (simplified approach)
            # For Procurement module, map to procurement BBP
            procurement_bbp = '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/4.Procurement/4.1_pr_bbp.md'
            if os.path.exists(os.path.join(project_root, procurement_bbp)):
                TestReadiness.objects.filter(module_id='procurement').update(bbp_path=procurement_bbp)
            
            # For Inventory module - Specific BBP Mapping
            inventory_mapping = {
                # 5.1 Dashboard
                'inventory-overview': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.1_Inventory_Dashboard/5.1.1_Inventory_Overview_bbp.md',
                'stock-by-location': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.1_Inventory_Dashboard/5.1.2_Stock_by_Location_bbp.md',
                'stock-valuation': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.1_Inventory_Dashboard/5.1.3_Stock_Valuation_bbp.md',
                'movement-trends': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.1_Inventory_Dashboard/5.1.4_Movement_Trends_bbp.md',
                'stock-alerts': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.1_Inventory_Dashboard/5.1.5_Alerts_Notifications_bbp.md',
                
                # 5.2 Stock Mgmt
                'stock-all': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.2_Stock_Management/5.2.1_Stock_on_Hand_bbp.md',
                'stock-location-view': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.2_Stock_Management/5.2.2_Stock_by_Location_bbp.md',
                'stock-category': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.2_Stock_Management/5.2.3_Stock_by_Category_bbp.md',
                'stock-batch': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.2_Stock_Management/5.2.4_Stock_by_Batch_Serial_bbp.md',
                'low-stock-alerts': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.2_Stock_Management/5.2.5_Low_Stock_Alerts_bbp.md',
                'overstock-alerts': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.2_Stock_Management/5.2.6_Overstock_Alerts_bbp.md',
                'stock-aging': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.2_Stock_Management/5.2.7_Stock_Aging_Analysis_bbp.md',

                # 5.3 Movements
                'movement-history': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.3_Stock_Movements/5.3.1_Movement_History_bbp.md',
                'goods-receipt': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.3_Stock_Movements/5.3.2_Goods_Receipt_bbp.md',
                'goods-issue': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.3_Stock_Movements/5.3.3_Goods_Issue_bbp.md',
                'internal-transfers': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.3_Stock_Movements/5.3.4_Internal_Transfers_bbp.md',
                'intercompany-transfers': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.3_Stock_Movements/5.3.5_Intercompany_Transfers_bbp.md',
                'movement-reports': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/5.3_Stock_Movements/5.3.6_Movement_Reports_bbp.md',
            }

            # Apply specific mappings
            for menu_id, bbp_rel_path in inventory_mapping.items():
                 full_path = os.path.join(project_root, bbp_rel_path)
                 if os.path.exists(full_path):
                     TestReadiness.objects.filter(menu_id=menu_id).update(bbp_path=bbp_rel_path)

            # Fallback: Apply tracker to all other inventory items
            inventory_tracker = '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/BBP_TRACKER_INVENTORY.md'
            if os.path.exists(os.path.join(project_root, inventory_tracker)):
                 TestReadiness.objects.filter(module_id='inventory', bbp_path__isnull=True).update(bbp_path=inventory_tracker)
                 TestReadiness.objects.filter(module_id='inventory', bbp_path='').update(bbp_path=inventory_tracker)
            
            # Sales module - Specific BBP Mapping (6.1-6.5)
            sales_mapping = {
                # 6.1 Sales Quotation
                'quotes': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.1_sales_quote.md',
                'quote-list': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.1_sales_quote.md',
                'quote-create': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.1_sales_quote.md',
                'quote-approval': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.1_sales_quote.md',
                'quote-revision': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.1_sales_quote.md',
                'quote-conversion': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.1_sales_quote.md',
                
                # 6.2 Sales Order
                'orders': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-list': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-create': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-approval': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-fulfillment': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-allocation': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-picking': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-packing': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-shipping': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                'order-delivery': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.2_sales_order.md',
                
                # 6.3 Sales Invoice
                'invoices': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'invoice-list': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'invoice-create': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'invoice-approval': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'invoice-matching': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'payment-recording': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'payment-allocation': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'invoice-dunning': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'credit-notes': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                'revenue-recognition': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.3_sales_invoice.md',
                
                # 6.4 Sales Return (RMA)
                'returns': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                'rma-list': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                'rma-create': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                'rma-approval': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                'return-receipt': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                'return-inspection': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                'refund-processing': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                'exchange-orders': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                'return-disposition': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.4_sales_return.md',
                
                # 6.5 Sales Configuration
                'sales-config': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.5_sales_config.md',
                'sales-process-settings': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.5_sales_config.md',
                'sales-tolerance-settings': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.5_sales_config.md',
                'sales-approval-matrix': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.5_sales_config.md',
                'return-policy-config': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.5_sales_config.md',
                'pricing-config': '.steering/00AGENT_ONBOARDING/02_Business_Blueprints/6.Sales/6.5_sales_config.md',
            }

            # Apply Sales BBP mappings
            for menu_id, bbp_rel_path in sales_mapping.items():
                 full_path = os.path.join(project_root, bbp_rel_path)
                 if os.path.exists(full_path):
                     TestReadiness.objects.filter(menu_id=menu_id).update(bbp_path=bbp_rel_path)
            
            return Response({
                "message": "Scripts and BBPs refreshed successfully",
                "updated_count": updated_count,
                "found_scripts": len(found_scripts),
                "found_bbps": len(found_bbps),
                "scripts": found_scripts[:10],  # Limit response size
                "bbps": found_bbps[:10]
            })
        
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"Error in refresh_scripts: {error_details}")  # Log to console
            return Response({
                "error": "Failed to refresh scripts",
                "message": str(e),
                "details": error_details
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





