from django.contrib import admin

class TableNameDisplayMixin:
    """
    Mixin to display the database table name in the admin change list view.
    This mixin adds a 'table_name' column to the list_display.
    """
    
    def get_list_display(self, request):
        """
        Add table_name to list_display if not already present
        """
        list_display = super().get_list_display(request)
        
        # Convert tuple to list if needed
        if isinstance(list_display, tuple):
            list_display = list(list_display)
        
        # Add table_name at the beginning if not already present
        if 'table_name' not in list_display:
            list_display.insert(0, 'table_name')
        
        return tuple(list_display)
    
    def table_name(self, obj):
        """
        Display the database table name for the model
        """
        return obj._meta.db_table
    table_name.short_description = 'Table Name'
    table_name.admin_order_field = 'id'
