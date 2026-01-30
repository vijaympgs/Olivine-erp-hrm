from django.contrib import admin

class TableNameDisplayMixin:
    """
    Mixin to display the database table name in the admin change list view.
    This mixin adds a 'table_name' context variable to the changelist_view.
    """
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        # Get the database table name from the model's _meta
        table_name = self.model._meta.db_table
        extra_context['table_name'] = table_name
        return super().changelist_view(request, extra_context)
