"""
Toolbar Permissions API Views - v2.0 API-Driven System

Provides API endpoints for frontend to fetch filtered toolbar actions
based on ERPMenuItem settings, user roles, and UI modes.
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..models import ERPMenuItem, Role, RolePermission, UserRole
from django.contrib.auth.models import User
import json

# Action character to action ID mapping
ACTION_MAP = {
    'N': 'new',
    'E': 'edit',
    'R': 'refresh',
    'Q': 'search',
    'F': 'filter',
    'X': 'exit',
    'V': 'view',
    'D': 'delete',
    'I': 'import',
    'O': 'export',
    'L': 'clone',
    'B': 'notes',
    'U': 'attach',
    'G': 'help',
    'S': 'save',
    'C': 'cancel',
    'K': 'clear',
    'A': 'authorize',
    'T': 'submit',
    'J': 'reject',
    'W': 'amend',
    'P': 'print',
    'M': 'email',
    '1': 'first',
    '2': 'prev',
    '3': 'next',
    '4': 'last',
    'H': 'hold',
    'Z': 'void',
}

# Mode-specific action filters
MODE_ACTION_FILTERS = {
    'LIST': ['new', 'refresh', 'search', 'filter', 'view', 'import', 'export', 'clone', 'notes', 'attach', 'help', 'first', 'prev', 'next', 'last', 'print', 'email'],
    'VIEW': ['edit', 'refresh', 'search', 'filter', 'print', 'email', 'clone', 'notes', 'attach', 'help', 'first', 'prev', 'next', 'last'],
    'EDIT': ['save', 'cancel', 'refresh', 'search', 'filter', 'print', 'email', 'notes', 'attach', 'help'],
    'CREATE': ['save', 'cancel', 'refresh', 'search', 'filter', 'print', 'email', 'notes', 'attach', 'help'],
}

def parse_config_string(config_string):
    """Parse character string configuration to action IDs."""
    if not config_string:
        return []
    actions = []
    for char in config_string.upper():
        if char in ACTION_MAP:
            actions.append(ACTION_MAP[char])
    return actions

def filter_actions_by_mode(actions, mode):
    """Filter actions based on UI mode."""
    if mode in MODE_ACTION_FILTERS:
        return [action for action in actions if action in MODE_ACTION_FILTERS[mode]]
    return actions

def get_user_roles(user):
    """Get all roles assigned to a user."""
    if user.is_anonymous:
        return []
    user_roles = UserRole.objects.filter(user=user).select_related('role')
    return [ur.role for ur in user_roles]

def apply_role_permissions(menu_item, user, actions):
    """
    Apply user role permissions to filter toolbar actions.
    
    Args:
        menu_item: The ERPMenuItem object
        user: The authenticated user (or None)
        actions: List of action IDs to filter
    
    Returns:
        List of allowed action IDs after applying role permissions
    """
    if not user or user.is_anonymous:
        # No user - return all actions (or could return empty for security)
        return actions
    
    # Get user's roles
    user_roles = get_user_roles(user)
    
    if not user_roles:
        # User has no roles - return all actions for now (development mode)
        # In production, you might want to return empty list for security
        return actions
    
    # Check if user has any role permission for this menu item
    role_permissions = RolePermission.objects.filter(
        menu_item=menu_item,
        role__in=user_roles,
        can_access=True
    )
    
    if not role_permissions.exists():
        # No role permissions - return all actions for now (development mode)
        # In production, you might want to return empty list for security
        return actions
    
    # If any role permission exists, allow all actions
    # (In a real implementation, you might want to check specific action permissions)
    return actions

class ToolbarPermissionsView(APIView):
    """
    API endpoint to fetch filtered toolbar permissions based on view_id, mode, and user roles.
    No authentication required for development.
    """
    permission_classes = [AllowAny]
    
    def get(self, request):
        menu_id = request.GET.get('menu_id')
        mode = request.GET.get('mode', 'LIST')
        
        if not menu_id:
            return Response({
                'error': 'menu_id parameter is required',
                'allowed_actions': []
            }, status=400)
        
        if mode not in MODE_ACTION_FILTERS:
            return Response({
                'error': f'Invalid mode: {mode}. Valid modes: {list(MODE_ACTION_FILTERS.keys())}',
                'allowed_actions': []
            }, status=400)
        
        try:
            # Fetch the menu item
            menu_item = ERPMenuItem.objects.get(
                menu_id=menu_id,
                is_active=True
            )
            
            # Get mode-specific toolbar configuration
            mode_column_map = {
                'LIST': 'toolbar_list',
                'VIEW': 'toolbar_view',
                'EDIT': 'toolbar_edit',
                'CREATE': 'toolbar_create',
            }
            
            # Use mode-specific column if available, otherwise fall back to applicable_toolbar_config
            toolbar_config = getattr(menu_item, mode_column_map.get(mode, 'applicable_toolbar_config'), None)
            
            # If mode-specific config is empty, fall back to applicable_toolbar_config
            if not toolbar_config:
                toolbar_config = menu_item.applicable_toolbar_config
            
            # Parse configuration
            base_actions = parse_config_string(toolbar_config)
            
            # Filter by mode
            mode_filtered_actions = filter_actions_by_mode(base_actions, mode)
            
            # Apply user role permissions
            user = request.user if hasattr(request, 'user') and request.user else None
            final_actions = apply_role_permissions(menu_item, user, mode_filtered_actions)
            
            return Response({
                'allowed_actions': final_actions,
                'view_id': menu_item.menu_id,
                'menu_name': menu_item.menu_name,
                'mode': mode,
                'toolbar_config': menu_item.toolbar_config,
                'user_roles': [role.role_name for role in get_user_roles(user)] if user else []
            })
            
        except ERPMenuItem.DoesNotExist:
            return Response({
                'error': f'Menu item not found: {menu_id}',
                'allowed_actions': []
            }, status=404)
            
        except Exception as e:
            return Response({
                'error': 'Internal server error',
                'details': str(e),
                'allowed_actions': []
            }, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def list_toolbar_permissions(request):
    """
    API endpoint to list all available toolbar configurations with their permissions.
    """
    try:
        menu_items = ERPMenuItem.objects.filter(is_active=True).order_by('module_name', 'menu_name')
        
        configs = []
        for item in menu_items:
            # Get permissions for each mode
            mode_permissions = {}
            for mode in MODE_ACTION_FILTERS:
                base_actions = parse_config_string(item.toolbar_config)
                mode_filtered = filter_actions_by_mode(base_actions, mode)
                mode_permissions[mode] = mode_filtered
            
            configs.append({
                'menu_id': item.menu_id,
                'menu_name': item.menu_name,
                'toolbar_config': item.toolbar_config,
                'menu_type': item.view_type,
                'app': item.module_name,
                'module': item.module_name,
                'submodule': item.submodule,
                'mode_permissions': mode_permissions
            })
        
        return JsonResponse({
            'menu_items': configs,
            'count': len(configs),
            'available_modes': list(MODE_ACTION_FILTERS.keys())
        })
        
    except Exception as e:
        return JsonResponse({
            'error': 'Internal server error',
            'details': str(e)
        }, status=500)

@login_required
@require_http_methods(["GET"])
def get_user_toolbar_permissions(request):
    """
    API endpoint to get toolbar permissions for the authenticated user.
    
    Query Parameters:
        view_id: The menu_id to lookup
        mode: The UI mode (VIEW, VIEW_FORM, CREATE, EDIT)
    
    Returns:
        JsonResponse with user-specific allowed_actions
    """
    view_id = request.GET.get('view_id')
    mode = request.GET.get('mode', 'VIEW')
    
    if not view_id:
        return JsonResponse({
            'error': 'view_id parameter is required',
            'allowed_actions': []
        }, status=400)
    
    # Create a ToolbarPermissionsView instance and call its get method
    view = ToolbarPermissionsView()
    return view.get(request)
