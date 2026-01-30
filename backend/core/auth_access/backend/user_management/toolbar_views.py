from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ToolbarPermissionsView(APIView):
    """
    Get toolbar permissions for a specific menu and mode
    Allows access for development without authentication
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def get(self, request):
        menu_id = request.GET.get('menu_id')
        mode = request.GET.get('mode', 'VIEW')
        
        # Specific permissions for HRM_EMPLOYEE_SELF_SERVICE
        if menu_id == 'HRM_EMPLOYEE_SELF_SERVICE':
            if mode == 'VIEW':
                permissions = {
                    'menu_id': menu_id,
                    'mode': mode,
                    'allowed_actions': ['new', 'edit', 'view', 'delete', 'refresh', 'search', 'filter', 'export', 'print', 'exit', 'authorize', 'submit', 'reject', 'amend', 'import', 'first', 'prev', 'next', 'last', 'help', 'notes', 'attach'],
                    'toolbar_string': 'NEVDXRQFZTJAPMI1234O',  # Full listing mode functionality
                    'permission_mask': '11111111111111111111',
                    'new': True,
                    'edit': True,
                    'view': True,
                    'delete': True,
                    'refresh': True,
                    'search': True,
                    'filter': True,
                    'export': True,
                    'print': True,
                    'exit': True,
                    'authorize': True,
                    'submit': True,
                    'reject': True,
                    'amend': True,
                    'import': True,
                    'first': True,
                    'prev': True,
                    'next': True,
                    'last': True,
                    'help': True,
                    'notes': True,
                    'attach': True
                }
            elif mode in ['CREATE', 'EDIT']:
                permissions = {
                    'menu_id': menu_id,
                    'mode': mode,
                    'allowed_actions': ['save', 'cancel', 'clear', 'exit', 'help', 'notes', 'attach'],
                    'toolbar_string': 'SCKX?BG',  # Form mode functionality
                    'permission_mask': '1111111',
                    'save': True,
                    'cancel': True,
                    'clear': True,
                    'exit': True,
                    'help': True,
                    'notes': True,
                    'attach': True
                }
            else:
                permissions = {
                    'menu_id': menu_id,
                    'mode': mode,
                    'allowed_actions': ['exit'],
                    'toolbar_string': 'X',  # Minimal mode
                    'permission_mask': '1',
                    'exit': True
                }
        # Specific permissions for FILE_SEARCH_EXPLORER
        elif menu_id == 'FILE_SEARCH_EXPLORER':
            if mode == 'Explorer':
                permissions = {
                    'menu_id': menu_id,
                    'mode': mode,
                    'allowed_actions': ['search', 'refresh', 'exit'],
                    'toolbar_string': 'SRE',  # Search, Refresh, Exit
                    'permission_mask': '111',
                    'search': True,
                    'refresh': True,
                    'exit': True
                }
            else:
                permissions = {
                    'menu_id': menu_id,
                    'mode': mode,
                    'allowed_actions': ['exit'],
                    'toolbar_string': 'X',  # Minimal mode
                    'permission_mask': '1',
                    'exit': True
                }
        else:
            # For development, return default permissions for other menus
            permissions = {
                'menu_id': menu_id,
                'mode': mode,
                'allowed_actions': ['view', 'create', 'edit', 'delete', 'export', 'import', 'print', 'refresh', 'search', 'filter', 'new', 'save', 'cancel', 'exit'],
                'toolbar_string': 'VCEDXIPRSFNEX',  # View, Create, Edit, Delete, Export, Import, Print, Refresh, Search, Filter, New, Save, Cancel, Exit
                'permission_mask': '1111111111111',
                'can_view': True,
                'can_create': True,
                'can_edit': True,
                'can_delete': True,
                'can_export': True,
                'can_import': True,
                'can_print': True,
                'can_refresh': True,
                'can_filter': True,
                'can_search': True,
                'can_download': True,
                'can_upload': True,
                'can_new': True,
                'can_save': True,
                'can_cancel': True,
                'can_exit': True
            }
        
        return Response(permissions)


# Keep the function-based view for backward compatibility
@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_toolbar_permissions(request):
    """
    Get toolbar permissions for a specific menu and mode
    Allows access for development without authentication
    """
    menu_id = request.GET.get('menu_id')
    mode = request.GET.get('mode', 'VIEW')
    
    # Specific permissions for HRM_EMPLOYEE_SELF_SERVICE
    if menu_id == 'HRM_EMPLOYEE_SELF_SERVICE':
        if mode == 'VIEW':
            permissions = {
                'menu_id': menu_id,
                'mode': mode,
                'allowed_actions': ['new', 'edit', 'view', 'delete', 'refresh', 'search', 'filter', 'export', 'print', 'exit', 'authorize', 'submit', 'reject', 'amend', 'import', 'first', 'prev', 'next', 'last', 'help', 'notes', 'attach'],
                'toolbar_string': 'NEVDXRQFZTJAPMI1234O',  # Full listing mode functionality
                'permission_mask': '11111111111111111111',
                'new': True,
                'edit': True,
                'view': True,
                'delete': True,
                'refresh': True,
                'search': True,
                'filter': True,
                'export': True,
                'print': True,
                'exit': True,
                'authorize': True,
                'submit': True,
                'reject': True,
                'amend': True,
                'import': True,
                'first': True,
                'prev': True,
                'next': True,
                'last': True,
                'help': True,
                'notes': True,
                'attach': True
            }
        elif mode in ['CREATE', 'EDIT']:
            permissions = {
                'menu_id': menu_id,
                'mode': mode,
                'allowed_actions': ['save', 'cancel', 'clear', 'exit', 'help', 'notes', 'attach'],
                'toolbar_string': 'SCKX?BG',  # Form mode functionality
                'permission_mask': '1111111',
                'save': True,
                'cancel': True,
                'clear': True,
                'exit': True,
                'help': True,
                'notes': True,
                'attach': True
            }
        else:
            permissions = {
                'menu_id': menu_id,
                'mode': mode,
                'allowed_actions': ['exit'],
                'toolbar_string': 'X',  # Minimal mode
                'permission_mask': '1',
                'exit': True
            }
    # Specific permissions for FILE_SEARCH_EXPLORER
    elif menu_id == 'FILE_SEARCH_EXPLORER':
        if mode == 'Explorer':
            permissions = {
                'menu_id': menu_id,
                'mode': mode,
                'allowed_actions': ['search', 'refresh', 'exit'],
                'toolbar_string': 'SRE',  # Search, Refresh, Exit
                'permission_mask': '111',
                'search': True,
                'refresh': True,
                'exit': True
            }
        else:
            permissions = {
                'menu_id': menu_id,
                'mode': mode,
                'allowed_actions': ['exit'],
                'toolbar_string': 'X',  # Minimal mode
                'permission_mask': '1',
                'exit': True
            }
    else:
        # For development, return default permissions for other menus
        permissions = {
            'menu_id': menu_id,
            'mode': mode,
            'allowed_actions': ['view', 'create', 'edit', 'delete', 'export', 'import', 'print', 'refresh', 'search', 'filter', 'new', 'save', 'cancel', 'exit'],
            'toolbar_string': 'VCEDXIPRSFNEX',  # View, Create, Edit, Delete, Export, Import, Print, Refresh, Search, Filter, New, Save, Cancel, Exit
            'permission_mask': '1111111111111',
            'can_view': True,
            'can_create': True,
            'can_edit': True,
            'can_delete': True,
            'can_export': True,
            'can_import': True,
            'can_print': True,
            'can_refresh': True,
            'can_filter': True,
            'can_search': True,
            'can_download': True,
            'can_upload': True,
            'can_new': True,
            'can_save': True,
            'can_cancel': True,
            'can_exit': True
        }
    
    return Response(permissions)
