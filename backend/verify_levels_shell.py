from HRM.backend.hrm.models import EmployeeRecord
from collections import Counter

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
