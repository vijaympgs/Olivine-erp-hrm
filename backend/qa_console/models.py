
from django.db import models

class TestReadiness(models.Model):
    STATUS_UI_CHOICES = [('Pending', 'Pending'), ('Done', 'Done'), ('N/A', 'N/A')]
    STATUS_DIT_CHOICES = [('Pending', 'Pending'), ('InProgress', 'In Progress'), ('Done', 'Done')]
    STATUS_UAT_CHOICES = [
        ('Not Started', 'Not Started'), 
        ('InProgress', 'In Progress'), 
        ('Complete', 'Complete')
    ]
    RESULT_CHOICES = [('Pass', 'Pass'), ('Fail', 'Fail')]

    # Hierarchy identifiers
    app_id = models.CharField(max_length=50) # e.g. "retail"
    module_id = models.CharField(max_length=50) # e.g. "pos"
    sub_module_id = models.CharField(max_length=50, blank=True, null=True) # e.g. "daily-ops"
    
    # The Suite/Screen identifier
    menu_id = models.CharField(max_length=100, unique=True, primary_key=True) # e.g. "pos-day-open"
    menu_label = models.CharField(max_length=100) # e.g. "Day Open"
    
    # Statuses
    ui_status = models.CharField(max_length=20, choices=STATUS_UI_CHOICES, default='Pending')
    dit_status = models.CharField(max_length=20, choices=STATUS_DIT_CHOICES, default='Pending')
    uat_status = models.CharField(max_length=20, choices=STATUS_UAT_CHOICES, default='Not Started')
    
    # Execution info
    script_path = models.CharField(max_length=255, blank=True, null=True)
    bbp_path = models.CharField(max_length=255, blank=True, null=True)  # Path to BBP document
    last_run_at = models.DateTimeField(null=True, blank=True)
    last_result = models.CharField(max_length=20, choices=RESULT_CHOICES, null=True, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'qa_console'

    def __str__(self):
        return f"{self.menu_label} ({self.menu_id})"




