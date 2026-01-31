"""
Admin Mixins for Django Admin
"""
from django.contrib import admin


class TableNameDisplayMixin:
    """
    Mixin to display the database table name in Django admin list view
    """
    def table_name(self, obj):
        """
        Display the database table name for the model
        """
        return obj._meta.db_table
    table_name.short_description = 'Table Name'
    table_name.admin_order_field = 'id'
