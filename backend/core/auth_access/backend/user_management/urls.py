from django.urls import path
from .toolbar_views import ToolbarPermissionsView, get_toolbar_permissions

app_name = 'user_management'

urlpatterns = [
    path('toolbar-permissions/', ToolbarPermissionsView.as_view(), name='toolbar-permissions'),
    path('get-toolbar-permissions/', get_toolbar_permissions, name='get-toolbar-permissions'),
]
