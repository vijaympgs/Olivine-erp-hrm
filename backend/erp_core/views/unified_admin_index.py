"""
Unified Admin Index View for Olivine Platform
Provides a landing page with navigation to 5 consolidated business modules.
"""

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def unified_admin_index(request):
    """
    Unified admin index view grouped into 5 consolidated cards.
    Each card represents a full business module using real routing labels.
    """
    modules = [
        {
            'category': 'Enterprise Control Center',
            'items': [
                {
                    'name': '👥 HUMAN RESOURCES (HRM)',
                    'url': '/admin/hrm/', 
                    'description': 'Personnel, Payroll, Attendance & Recruitment',
                    'icon': 'users',
                    'color': '#3B82F6',
                    'sub_modules': [
                        {'name': 'Employees', 'url': '/admin/hrm/hrm/employeerecord/'},
                        {'name': 'Payroll', 'url': '/admin/hrm/hrm/payrollrun/'},
                        {'name': 'Attendance', 'url': '/admin/hrm/hrm/timeentry/'},
                        {'name': 'Shifts', 'url': '/admin/hrm/hrm/shift/'},
                        {'name': 'Job Postings', 'url': '/admin/hrm/hrm/jobposting/'},
                        {'name': 'Offer Letters', 'url': '/admin/hrm/hrm/offerletter/'},
                    ]
                },
                {
                    'name': '🛡️ PLATFORM ADMINISTRATION',
                    'url': '/admin/',
                    'description': 'Infrastructure, Security & Master Data',
                    'icon': 'shield',
                    'color': '#1E293B',
                    'sub_modules': [
                        {'name': 'Company', 'url': '/admin/business_entities/company/'},
                        {'name': 'Users', 'url': '/admin/auth/user/'},
                        {'name': 'Roles', 'url': '/admin/user_management/role/'},
                        {'name': 'ERP Menu Items', 'url': '/admin/toolbar_control/toolbaritemproxy/'},
                        {'name': 'Master Toolbars', 'url': '/admin/toolbar_control/toolbarcontrolproxy/'},
                        {'name': 'Role Toolbar Permissions', 'url': '/admin/toolbar_control/roletoolbarpermissionproxy/'},
                        {'name': 'User Toolbar Permissions', 'url': '/admin/toolbar_control/usertoolbarpermissionproxy/'},
                    ]
                },
            ]
        },
    ]
    
    context = {
        'modules': modules,
        'title': 'Olivine ERP Unified Control Center',
        'user': request.user,
    }
    
    return render(request, 'admin/unified_admin_index.html', context)
