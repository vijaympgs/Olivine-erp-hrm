import os
import sys
import django
from collections import Counter

if 'c:\\00mindra\\olivine-platform' not in sys.path:
    sys.path.append('c:\\00mindra\\olivine-platform')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.erp_core.settings')
django.setup()

from HRM.backend.hrm.models import EmployeeRecord

def check():
    print("Checking Employee Levels...")
    employees = EmployeeRecord.objects.all()
    print(f"Total: {employees.count()}")
    
    job_level_counts = Counter()
    hierarchy_level_counts = Counter()
    
    for e in employees:
        job_level_counts[e.job_level] += 1
        hierarchy_level_counts[e.hierarchy_level] += 1
        
    print("\nJob Level Distribution:")
    for level, count in sorted(job_level_counts.items(), key=lambda x: str(x[0])):
        print(f"  {level}: {count}")
        
    print("\nHierarchy Level Distribution:")
    for level, count in sorted(hierarchy_level_counts.items(), key=lambda x: str(x[0])):
        print(f"  {level}: {count}")

if __name__ == '__main__':
    check()
