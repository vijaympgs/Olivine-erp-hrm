from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from erp_core.views.unified_admin_index import unified_admin_index
from core.auth_access.backend.user_management.toolbar_views import get_toolbar_permissions
from erp_core.file_search_views import SearchRootsView, FileSearchView, FileContentView, FileOpenView
from erp_core.visual_extractor_views import VisualExtractionView

# Import HRM Admin Sites for unified console
from HRM.backend.hrm.admin_sites import (
    employee_management_site, organization_management_site, performance_management_site,
    learning_development_site, compensation_payroll_site, recruitment_screening_site,
    time_attendance_site, badges_recognition_site, tax_compliance_site, toolbar_configuration_site
)

urlpatterns = [
    path('', RedirectView.as_view(url='/platform/', permanent=False), name='index'),
    path('platform/', unified_admin_index, name='platform_index'),
    path('admin/', admin.site.urls),
    
    # HRM Admin Sites (Unified into single backend)
    path('admin/hrm-employees/', employee_management_site.urls),
    path('admin/hrm-organization/', organization_management_site.urls),
    path('admin/hrm-performance/', performance_management_site.urls),
    path('admin/hrm-learning/', learning_development_site.urls),
    path('admin/hrm-compensation/', compensation_payroll_site.urls),
    path('admin/hrm-recruitment/', recruitment_screening_site.urls),
    path('admin/hrm-attendance/', time_attendance_site.urls),
    path('admin/hrm-badges/', badges_recognition_site.urls),
    path('admin/hrm-tax/', tax_compliance_site.urls),
    path('admin/hrm-toolbar/', toolbar_configuration_site.urls),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # API Routes
    path('api/auth/', include('core.auth_access.backend.user_management.urls')),
    path('api/business/', include('core.licensing.backend.business_entities.urls')),
    
    # Master Data
    path('api/', include('backend.domain.master.urls')),  # Includes /api/uoms/
    
    path('api/hrm/', include('HRM.backend.hrm.urls')),  # HRM API
    path('api/reports/', include('backend.domain.reporting.urls')),
    path('api/user_management/', include('core.auth_access.backend.user_management.urls')),
    path('api/qa/', include('backend.qa_console.urls')),
    # Added direct toolbar-permissions endpoint for HRM modules
    # (Removed duplicate endpoints; using included URLs with proper authentication)
    # File Search API
    path('api/file-search/roots/', SearchRootsView.as_view(), name='file-search-roots'),
    path('api/file-search/search/', FileSearchView.as_view(), name='file-search'),
    path('api/file-search/file/', FileContentView.as_view(), name='file-content'),
    path('api/file-search/open/', FileOpenView.as_view(), name='file-open'),
    
    # System Tools API
    path('api/system-tools/extract-text/', VisualExtractionView.as_view(), name='extract-text'),
    
    path('', include('core.org_structure.backend.company.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
