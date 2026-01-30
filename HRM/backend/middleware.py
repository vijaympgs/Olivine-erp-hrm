"""
Custom middleware for HRM backend
"""
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser

class DisableAuthenticationForToolbarAPI(MiddlewareMixin):
    """
    Middleware to disable authentication for toolbar permissions API
    This allows the frontend to fetch toolbar configuration without authentication
    """
    def process_request(self, request):
        # Disable authentication for toolbar permissions API
        if request.path.startswith('/api/toolbar-permissions/'):
            request.user = AnonymousUser()
            request.auth = None
        return None
