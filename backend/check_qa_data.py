"""
Quick script to check and populate TestReadiness table
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings')
django.setup()

from qa_console.models import TestReadiness

# Check current count
count = TestReadiness.objects.count()
print(f"Current TestReadiness entries: {count}")

if count > 0:
    print("\nSample entries:")
    for entry in TestReadiness.objects.all()[:10]:
        print(f"  - {entry.menu_id}: {entry.menu_label} (UI: {entry.ui_status}, BBP: {'Yes' if entry.bbp_path else 'No'})")
else:
    print("\nNo entries found. The table is empty.")
    print("The frontend should populate this via the sync_entries endpoint.")




