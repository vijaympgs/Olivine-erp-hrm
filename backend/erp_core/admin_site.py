from django.contrib import admin
from django.apps import apps

class RetailAdminSite(admin.AdminSite):
    site_header = "Olivine Platform - Unified Administration"
    site_title = "Olivine ERP Portal"
    index_title = "All Modules"

    def get_app_list(self, request, app_label=None):
        """
        Custom grouping into exactly 5 top labels.
        Uses real app labels for routing to prevent 404s.
        """
        # Load all apps regardless of the filter to ensure we can pull 
        # models from different apps into the same group.
        all_apps = super().get_app_list(request, None)
        
        # 1. Map all models
        model_dict = {}
        for app in all_apps:
            for model in app['models']:
                key = f"{app['app_label']}.{model['object_name']}"
                model_dict[key] = model

        # 2. Define the 5 Primary Business Modules with REAL app labels for routing
        custom_groups = [
            {
                'name': '🛒 RETAIL',
                'app_label': 'pos', # Primary routing label
                'models': [
                    'pos.Terminal', 'pos.DayOpen', 'pos.PosSession', 'pos.POSTransaction',
                    'pos.POSTransactionLine', 'pos.POSTransactionPayment', 'pos.POSReconciliation',
                    'inventory.StockLevel', 'inventory.StockMovement', 'inventory.StockAdjustment',
                    'inventory.StockTransfer', 'inventory.StockTake', 'inventory.ValuationMethod',
                    'inventory.InventoryParameter', 'inventory.ApprovalRule',
                    'sales.SalesQuote', 'sales.SalesOrder', 'sales.SalesInvoice',
                    'sales.SalesReturnNote', 'sales.SalesConfig',
                    'procurement.PurchaseRequisition', 'procurement.RequestForQuotation',
                    'procurement.RFQVendor', 'procurement.PurchaseOrder',
                    'procurement.GoodsReceipt', 'procurement.ProcurementConfig',
                ]
            },
            {
                'name': '👥 HUMAN RESOURCES (HRM)',
                'app_label': 'hrm',
                'models': [
                    'hrm.EmployeeRecord', 'hrm.EmployeeProfile', 'hrm.EmployeeAddress',
                    'hrm.EmployeeSkill', 'hrm.EmployeeDocument', 'hrm.SkillCategory',
                    'hrm.Department', 'hrm.OrganizationalUnit', 'hrm.Position', 'hrm.EmployeePosition',
                    'hrm.SalaryStructure', 'hrm.PayGrade', 'hrm.PayrollRun',
                    'hrm.PayrollCalculation', 'hrm.EarningCode',
                    'hrm.TimeEntry', 'hrm.Shift', 'hrm.AttendancePolicy', 'hrm.Timesheet',
                    'hrm.JobPosting', 'hrm.JobApplication', 'hrm.ApplicationCandidate', 'hrm.OfferLetter',
                    'hrm.RatingScale', 'hrm.ReviewCycle', 'hrm.CalibrationSession',
                ]
            },
            {
                'name': '💵 FINANCE (FMS)',
                'app_label': 'finance',
                'models': [
                    'finance.AccountGroup', 'finance.AccountLedger',
                    'finance.JournalEntry', 'finance.JournalItem',
                    'business_entities.PaymentMethod', 'business_entities.TaxClassEnhanced',
                ]
            },
            {
                'name': '🤝 Customer Relations (CRM)',
                'app_label': 'crm',
                'models': [
                    'crm.Customer', 'crm.Lead', 'crm.Contact',
                    'business_entities.CustomerGroup', 'business_entities.Promotion',
                    'business_entities.LoyaltyProgram', 'business_entities.CustomerLoyalty',
                ]
            },
            {
                'name': '🛡️ PLATFORM ADMINISTRATION',
                'app_label': 'company',
                'models': [
                    'auth.User', 'auth.Group', 'user_management.Role',
                    'user_management.UserRole', 'authtoken.TokenProxy',
                    'business_entities.Company', 'retail_domain.Location',
                    'licensing.LicenseConfiguration', 'user_management.UserLocationMapping',
                    'company.ItemMaster', 'company.Category', 'company.Brand',
                    'company.UnitOfMeasure', 'company.OperationalSupplier',
                    'company.OperationalCustomer', 'company.TaxClass',
                ]
            },
        ]

        # 3. Filter groups if app_label is provided (for app-specific index pages)
        if app_label:
            custom_groups = [g for g in custom_groups if g['app_label'] == app_label]

        # 4. Build virtual apps
        new_app_list = []
        moved_models = set()

        for group in custom_groups:
            group_models = []
            for key in group['models']:
                if key in model_dict:
                    group_models.append(model_dict[key])
                    moved_models.add(key)
            
            if group_models:
                new_app_list.append({
                    'name': group['name'],
                    'app_label': group['app_label'],
                    'app_url': f"/admin/{group['app_label']}/",
                    'has_module_perms': True,
                    'models': group_models
                })

        # 5. Handle any models that didn't fit into the 5 primary groups
        # (Only if we're looking at the main dashboard or if those models belong to the filtered app)
        if not app_label:
             for app in all_apps:
                remaining = [m for m in app['models'] if f"{app['app_label']}.{m['object_name']}" not in moved_models]
                if remaining:
                    item = app.copy()
                    item['models'] = remaining
                    new_app_list.append(item)

        return new_app_list
