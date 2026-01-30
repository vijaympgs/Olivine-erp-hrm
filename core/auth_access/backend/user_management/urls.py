from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet, LoginView,
    # User & Permission Management API Views
    UserListView, GetUserPermissionsView, RoleListView, GetRolePermissionsView,
    PermissionMatrixView, MenuItemListView, MenuItemHierarchyView,
    BulkPermissionUpdateView, UserRoleListView, BulkUserRoleUpdateView,
    # UserLocationListView, BulkUserLocationUpdateView,  # Removed - Location is Retail-only
    RoleTemplateView, ApplyRoleTemplateView,
    CurrentUserView, UpdateUserProfileView
)
from . import toolbar_views

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='auth-login'),
    
    # ============================================================================
    # USER & PERMISSION MANAGEMENT API ENDPOINTS
    # ============================================================================
    
    # User Management
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:user_id>/permissions/', GetUserPermissionsView.as_view(), name='get-user-permissions'),
    path('me/', CurrentUserView.as_view(), name='current-user'),
    path('profile/', UpdateUserProfileView.as_view(), name='update-user-profile'),
    
    # Role Management
    path('roles/', RoleListView.as_view(), name='role-list'),
    path('roles/<str:role_key>/permissions/', GetRolePermissionsView.as_view(), name='get-role-permissions'),
    
    # Permission Matrix
    path('permission-matrix/', PermissionMatrixView.as_view(), name='permission-matrix'),
    path('permission-matrix/bulk/', BulkPermissionUpdateView.as_view(), name='bulk-permission-update'),
    
    # Menu Items
    path('menu-items/', MenuItemListView.as_view(), name='menu-item-list'),
    path('menu-items/hierarchy/', MenuItemHierarchyView.as_view(), name='menu-item-hierarchy'),
    
    # User-Role Mapping
    path('user-roles/', UserRoleListView.as_view(), name='user-role-list'),
    path('user-roles/bulk/', BulkUserRoleUpdateView.as_view(), name='bulk-user-role-update'),
    
    # User-Location Mapping removed - Location is Retail-only
    
    # Role Templates
    path('role-templates/', RoleTemplateView.as_view(), name='role-templates'),
    path('apply-role-template/', ApplyRoleTemplateView.as_view(), name='apply-role-template'),
    
    # Toolbar Configuration API
    path('ui-config/<str:view_id>/', toolbar_views.get_ui_config, name='get-ui-config'),
    path('menu-items-list/', toolbar_views.list_menu_items, name='list-menu-items'),
    
    # NEW: Toolbar Permissions API (Character-based permission system)
    path('toolbar-permissions/', toolbar_views.get_toolbar_permissions, name='toolbar-permissions'),
]
