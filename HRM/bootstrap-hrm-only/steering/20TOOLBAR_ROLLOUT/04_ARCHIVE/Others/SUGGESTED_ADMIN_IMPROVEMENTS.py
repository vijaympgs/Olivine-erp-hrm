# Improved Django Admin for ERPMenuItem (Toolbar Configuration)
# Add this to: backend/core/auth_access/backend/user_management/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import ERPMenuItem

class ERPMenuItemAdmin(admin.ModelAdmin):
    list_display = [
        'menu_id',
        'menu_name',
        'module_name',
        'view_type',
        'applicable_toolbar_config',
        'button_count',  # NEW
        'config_type',   # NEW
        'route_path',    # NEW
        'is_active',
    ]
    
    list_filter = [
        'module_name',
        'view_type',
        'is_active',
    ]
    
    search_fields = [
        'menu_id',
        'menu_name',
        'route_path',
        'applicable_toolbar_config',
    ]
    
    list_editable = [
        'applicable_toolbar_config',
        'is_active',
    ]
    
    readonly_fields = [
        'button_count',
        'config_type',
        'config_breakdown',
    ]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('menu_id', 'menu_name', 'module_name', 'view_type')
        }),
        ('Routing', {
            'fields': ('route_path', 'parent_menu')
        }),
        ('Toolbar Configuration', {
            'fields': (
                'applicable_toolbar_config',
                'button_count',
                'config_type',
                'config_breakdown',
            ),
            'description': 'Configure which toolbar buttons appear for this screen'
        }),
        ('Status', {
            'fields': ('is_active', 'menu_order')
        }),
    )
    
    # NEW: Custom column to show button count
    def button_count(self, obj):
        if obj.applicable_toolbar_config:
            return len(obj.applicable_toolbar_config)
        return 0
    button_count.short_description = 'Buttons'
    
    # NEW: Custom column to show config type
    def config_type(self, obj):
        config = obj.applicable_toolbar_config or ''
        
        # Determine config type based on pattern
        if config == 'NESCKVDXRQF':
            return format_html('<span style="color: blue;">📋 Masters (Simple)</span>')
        elif config == 'NESCKVDXRQFIO':
            return format_html('<span style="color: green;">📦 Masters (Advanced)</span>')
        elif config == 'NESCKZTJAVPMRDX1234QF':
            return format_html('<span style="color: purple;">📄 Transactions</span>')
        elif config == 'VRXPYQFG':
            return format_html('<span style="color: orange;">📊 Reports</span>')
        elif config == 'NRQFX':
            return format_html('<span style="color: gray;">📑 List View</span>')
        elif config == 'ESCKXR':
            return format_html('<span style="color: teal;">⚙️ Configuration</span>')
        else:
            return format_html('<span style="color: red;">❓ Custom</span>')
    config_type.short_description = 'Config Type'
    
    # NEW: Custom readonly field to show config breakdown
    def config_breakdown(self, obj):
        if not obj.applicable_toolbar_config:
            return "No configuration set"
        
        config = obj.applicable_toolbar_config
        
        # Character mapping
        ACTION_MAP = {
            'N': 'New (F2)',
            'E': 'Edit (F3)',
            'S': 'Save (F8)',
            'C': 'Cancel (Esc)',
            'K': 'Clear (F5)',
            'V': 'View (F7)',
            'D': 'Delete (F4)',
            'X': 'Exit (Esc)',
            'R': 'Refresh (F9)',
            'Q': 'Search (Ctrl+F)',
            'F': 'Filter (Alt+F)',
            'I': 'Import (Ctrl+I)',
            'O': 'Export (Ctrl+E)',
            'Y': 'Export (Ctrl+E)',
            'Z': 'Authorize (F10)',
            'T': 'Submit (Alt+S)',
            'J': 'Reject (Alt+R)',
            'A': 'Amend (Alt+A)',
            'H': 'Hold (Alt+H)',
            'W': 'Void (Alt+V)',
            'P': 'Print (Ctrl+P)',
            'M': 'Email (Ctrl+M)',
            'L': 'Clone (Ctrl+Shift+C)',
            '1': 'First (Home)',
            '2': 'Prev (PgUp)',
            '3': 'Next (PgDn)',
            '4': 'Last (End)',
            'B': 'Notes (Alt+N)',
            'G': 'Attach (Alt+U)',
            '?': 'Help (F1)',
        }
        
        breakdown = []
        for char in config:
            action = ACTION_MAP.get(char, f'Unknown ({char})')
            breakdown.append(f'<li><code>{char}</code> = {action}</li>')
        
        html = f'''
        <div style="background: #f5f5f5; padding: 10px; border-radius: 5px;">
            <strong>Configuration: {config}</strong> ({len(config)} buttons)
            <ul style="margin: 10px 0; padding-left: 20px;">
                {''.join(breakdown)}
            </ul>
        </div>
        '''
        return format_html(html)
    config_breakdown.short_description = 'Configuration Breakdown'

# Register the admin
admin.site.register(ERPMenuItem, ERPMenuItemAdmin)



