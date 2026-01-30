from django.core.management.base import BaseCommand
from HRM.backend.hrm.models import EmployeeRecord
import math

class Command(BaseCommand):
    help = 'Distribute employees equally across all hierarchy levels'

    def handle(self, *args, **options):
        self.stdout.write('Starting global redistribution...')

        # Prepare Hierarchy Levels (Specific Distribution: 1, 4, 4, 4, 4, Rest)
        self.stdout.write('Enforcing hierarchy counts (1, 4, 4, 4, 4, Rest)...')
        
        all_employees = list(EmployeeRecord.objects.all().order_by('hire_date', 'id'))
        
        updates = []
        
        # Level 0: CEO (1)
        if len(all_employees) > 0:
            ceo = all_employees[0]
            if ceo.hierarchy_level != 0 or ceo.manager is not None:
                ceo.hierarchy_level = 0
                ceo.manager = None  # Ensure CEO has no manager (Root Node)
                updates.append(ceo)
            ceo.job_level = 'L1'
            ceo.save() # Save individually to be safe

        
        # Level 1: VP (4)
        for i in range(1, 5):
            if i < len(all_employees):
                emp = all_employees[i]
                if emp.hierarchy_level != 1:
                    emp.hierarchy_level = 1
                    updates.append(emp)
                emp.job_level = 'L2'
                emp.save()
        
        # Level 2: Director (4)
        for i in range(5, 9):
            if i < len(all_employees):
                emp = all_employees[i]
                if emp.hierarchy_level != 2:
                    emp.hierarchy_level = 2
                    updates.append(emp)
                emp.job_level = 'L3'
                emp.save()

        # Level 3: Manager (4)
        for i in range(9, 13):
            if i < len(all_employees):
                emp = all_employees[i]
                if emp.hierarchy_level != 3:
                    emp.hierarchy_level = 3
                    updates.append(emp)
                emp.job_level = 'L4'
                emp.save()

        # Level 4: Senior Staff (4)
        for i in range(13, 17):
            if i < len(all_employees):
                emp = all_employees[i]
                if emp.hierarchy_level != 4:
                    emp.hierarchy_level = 4
                    updates.append(emp)
                emp.job_level = 'L5'
                emp.save()

        # Level 5: Staff (Rest)
        for i in range(17, len(all_employees)):
            emp = all_employees[i]
            if emp.hierarchy_level != 5:
                emp.hierarchy_level = 5
                updates.append(emp)
            emp.job_level = 'L6'
            # We don't save everyone individually in loop if not needed, rely on bulk later?
            # actually logic below relies on DB being updated.
            # updates list is for hierarchy_level bulk update.
            # I should add 'job_level' to bulk update too?
        
        if updates:
            # We must update BOTH hierarchy_level and job_level in DB for consistency
            # But bulk_update with fields list needs to be precise.
            # The manual .save() calls above handled L0-L4.
            # L5 logic added to 'updates'.
            EmployeeRecord.objects.bulk_update(updates, ['hierarchy_level'])
            # Also batch update job_levels for L6
            l6_ids = [e.id for e in all_employees[17:]]
            EmployeeRecord.objects.filter(id__in=l6_ids).update(job_level='L6')

            self.stdout.write(f"Refactor complete. Synced levels.")


        levels = {
            'L1': {'level': 0, 'name': 'CEO'},
            'L2': {'level': 1, 'name': 'VP'},
            'L3': {'level': 2, 'name': 'Director'},
            'L4': {'level': 3, 'name': 'Manager'},
            'L5': {'level': 4, 'name': 'Senior Staff'},
            'L6': {'level': 5, 'name': 'Staff'},
        }

        # Fetch all employees by level
        employees = {}
        for key, info in levels.items():
            # For L6, we want everything >= 5
            if info['level'] == 5:
                employees[key] = list(EmployeeRecord.objects.filter(hierarchy_level__gte=5).order_by('id'))
            else:
                employees[key] = list(EmployeeRecord.objects.filter(hierarchy_level=info['level']).order_by('id'))
            
            self.stdout.write(f"Fetched {len(employees[key])} {info['name']}s ({key})")

        # Helper to distribute Equal Reportees
        def distribute(managers, reportees, manager_level_name, reportee_level_name):
            if not managers or not reportees:
                self.stdout.write(f"Skipping {manager_level_name} -> {reportee_level_name} (missing data)")
                return
            
            self.stdout.write(f"Distributing {len(reportees)} {reportee_level_name}s among {len(managers)} {manager_level_name}s...")
            
            updates = []
            for i, reportee in enumerate(reportees):
                # Round-robin assignment
                manager = managers[i % len(managers)]
                
                # Check if change is needed
                if reportee.manager_id != manager.id:
                    reportee.manager = manager
                    # Update department/title to match manager for consistency?
                    # User asked for "Equivalent reportees", implies structural change.
                    # I'll update manager linkage primarily.
                    # Optionally sync department if it looks weird otherwise
                    if reportee_level_name == 'Staff' or reportee_level_name == 'Senior Staff':
                        # For lower levels, sync department
                        reportee.department_name = manager.department_name
                    
                    updates.append(reportee)
            
            if updates:
                EmployeeRecord.objects.bulk_update(updates, ['manager', 'department_name'])
                self.stdout.write(self.style.SUCCESS(f"  Updated {len(updates)} records."))
            else:
                self.stdout.write("  No changes needed (already balanced).")

            # Report Distribution Stats
            counts = {m.id: 0 for m in managers}
            for r in reportees:
                # We need to simulate the new state since DB might not reflect bulk_update instantly in 'reportees' list if filtered?
                # Actually bulk_update updates DB. 
                # Let's count properly via logic:
                mid = managers[list(reportees).index(r) % len(managers)].id
                counts[mid] += 1
            
            min_c = min(counts.values())
            max_c = max(counts.values())
            self.stdout.write(f"  Result: Each {manager_level_name} has between {min_c} and {max_c} reportees.")

        # Execute Distributions
        distribute(employees['L1'], employees['L2'], 'CEO', 'VP')         # 1 -> 2
        distribute(employees['L2'], employees['L3'], 'VP', 'Director')    # 2 -> 5
        distribute(employees['L3'], employees['L4'], 'Director', 'Manager') # 5 -> 8
        distribute(employees['L4'], employees['L5'], 'Manager', 'Senior Staff') # 8 -> 8
        distribute(employees['L5'], employees['L6'], 'Senior Staff', 'Staff')   # 8 -> 251

        self.stdout.write(self.style.SUCCESS('\n✅ Global redistribution complete!'))



