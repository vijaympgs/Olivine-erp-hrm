# Employee Directory & Master Implementation Plan

**Date**: 2025-12-28 20:54 IST  
**Status**: 🚀 Ready to Execute  
**Estimated Time**: 2-3 hours

---

## 📋 IMPLEMENTATION CHECKLIST

### **Phase 1: Backend - HRM Domain** ⏳
- [ ] 1.1 Create `backend/domain/hrm/` directory structure
- [ ] 1.2 Create HRM models (Employee, Department, Position)
- [ ] 1.3 Create HRM serializers (Directory & Master)
- [ ] 1.4 Create HRM ViewSets (Directory & Master)
- [ ] 1.5 Create HRM URLs
- [ ] 1.6 Register HRM URLs in main API
- [ ] 1.7 Create migrations
- [ ] 1.8 Run migrations

### **Phase 2: Frontend - Employee Directory** ⏳
- [ ] 2.1 Create `frontend/src/modules/hrm/` directory
- [ ] 2.2 Create Employee types (`types.ts`)
- [ ] 2.3 Create Employee service (`employeeService.ts`)
- [ ] 2.4 Create EmployeeDirectoryPage component
- [ ] 2.5 Create Employee card component
- [ ] 2.6 Add route to router

### **Phase 3: Frontend - Employee Master** ⏳
- [ ] 3.1 Create EmployeeMasterPage component
- [ ] 3.2 Create Employee form component
- [ ] 3.3 Create Employee table component
- [ ] 3.4 Add permission guards
- [ ] 3.5 Add route to router

### **Phase 4: Testing & Validation** ⏳
- [ ] 4.1 Test Employee Directory (all users)
- [ ] 4.2 Test Employee Master (HR Admin only)
- [ ] 4.3 Test search and filters
- [ ] 4.4 Test CRUD operations
- [ ] 4.5 Test permissions

---

## 🚨 DECISION REQUIRED

**Question**: Should we create a NEW HRM domain or use the existing legacy Employee model?

### **Option 1: Create New HRM Domain** (RECOMMENDED)
**Pros**:
- ✅ Clean separation from user_management
- ✅ Follows BBP (1.1 Employee Management.md)
- ✅ Proper domain-driven design
- ✅ Can implement all BBP features
- ✅ Future-proof for HRM expansion

**Cons**:
- ⏱️ More setup time (create domain, models, migrations)
- 🔄 Need to migrate data from legacy Employee model

### **Option 2: Use Legacy Employee Model**
**Pros**:
- ⚡ Faster implementation (models already exist)
- 📊 Data already exists

**Cons**:
- ❌ Marked as "LEGACY_DEPRECATED" and "Read-Only"
- ❌ Doesn't follow BBP structure
- ❌ Limited fields (missing many BBP requirements)
- ❌ In wrong domain (user_management vs hrm)
- ❌ Not future-proof

---

## ✅ RECOMMENDATION: Option 1 (Create New HRM Domain)

**Rationale**:
1. The legacy Employee model is marked as deprecated and read-only
2. BBP defines comprehensive Employee structure
3. Proper domain separation (HRM vs User Management)
4. Enables future HRM features (Payroll, Performance, Learning)

---

## 🏗️ IMPLEMENTATION STRATEGY

### **Step 1: Create HRM Domain** (Backend)

```bash
backend/domain/hrm/
├── __init__.py
├── models.py              # Employee, Department, Position
├── serializers.py         # EmployeeDirectorySerializer, EmployeeMasterSerializer
├── views.py               # EmployeeDirectoryViewSet, EmployeeMasterViewSet
├── urls.py                # URL routing
├── apps.py                # App configuration
├── admin.py               # Django admin
└── migrations/
    └── __init__.py
```

### **Step 2: Create Frontend Structure**

```bash
frontend/src/modules/hrm/
├── types.ts               # TypeScript types
├── employeeService.ts     # API service
├── pages/
│   ├── EmployeeDirectoryPage.tsx
│   └── EmployeeMasterPage.tsx
└── components/
    ├── EmployeeCard.tsx
    ├── EmployeeForm.tsx
    └── EmployeeTable.tsx
```

---

## 📊 DATA MODEL (From BBP)

### **Employee** (Core)
```python
class Employee(models.Model):
    # Identity
    id = UUIDField(primary_key=True)
    employee_code = CharField(unique=True, immutable=True)
    
    # Company & Organization
    company = ForeignKey(Company)
    department = ForeignKey(Department)
    position = ForeignKey(Position)
    manager = ForeignKey('self', null=True)
    primary_location = ForeignKey(Location)
    
    # Personal Info
    first_name = CharField()
    last_name = CharField()
    display_name = CharField()
    email = EmailField(unique=True)
    mobile_number = CharField()
    gender = CharField(choices=GENDER_CHOICES)
    date_of_birth = DateField()
    
    # Employment
    employment_type = CharField(choices=TYPE_CHOICES)  # permanent, contract, part-time
    employment_status = CharField(choices=STATUS_CHOICES)  # draft, onboarding, active, on_leave, resigned, terminated
    date_of_joining = DateField()
    confirmation_date = DateField(null=True)
    exit_date = DateField(null=True)
    
    # Audit
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    created_by = ForeignKey(User)
    updated_by = ForeignKey(User)
```

### **Department**
```python
class Department(models.Model):
    id = UUIDField(primary_key=True)
    company = ForeignKey(Company)
    code = CharField(unique per company)
    name = CharField()
    is_active = BooleanField()
```

### **Position**
```python
class Position(models.Model):
    id = UUIDField(primary_key=True)
    company = ForeignKey(Company)
    code = CharField()
    title = CharField()
    level = IntegerField()
    is_managerial = BooleanField()
```

---

## 🔐 PERMISSION STRATEGY

### **Employee Directory** (Public)
```python
# views.py
class EmployeeDirectoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]  # All authenticated users
    serializer_class = EmployeeDirectorySerializer
    
    def get_queryset(self):
        # Return only public employee information
        # Filter by user's company
        return Employee.objects.filter(
            company=self.request.user.company,
            employment_status='active'
        ).select_related('department', 'position', 'manager')
```

### **Employee Master** (Admin Only)
```python
# views.py
class EmployeeMasterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsHRAdmin]  # HR Admin only
    serializer_class = EmployeeMasterSerializer
    
    def get_queryset(self):
        # Return complete employee information
        return Employee.objects.filter(
            company=self.request.user.company
        ).select_related('department', 'position', 'manager', 'location')
```

---

## 🎨 UI/UX SPECIFICATIONS

### **Employee Directory Page**
```
Layout: Card Grid
Components:
- Search bar (top, prominent)
- Filter panel (department, location)
- Employee cards (photo, name, title, department, contact)
- Pagination

Features:
- Quick search
- Click to email
- Click to call
- View org chart
- Export to CSV
```

### **Employee Master Page**
```
Layout: Data Table + Form
Components:
- Action toolbar (Create, Import, Export)
- Data table (sortable, filterable)
- Employee form (modal, multi-tab)
- Bulk actions

Features:
- Create employee
- Edit employee
- View complete data
- Bulk import/export
- Audit log
```

---

## ⏱️ TIME ESTIMATES

| Phase | Task | Estimated Time |
|-------|------|----------------|
| **Phase 1** | Backend HRM Domain | 60 min |
| | - Create models | 20 min |
| | - Create serializers | 15 min |
| | - Create ViewSets | 15 min |
| | - Create URLs | 5 min |
| | - Migrations | 5 min |
| **Phase 2** | Employee Directory | 45 min |
| | - Types & Service | 10 min |
| | - Directory Page | 20 min |
| | - Employee Card | 10 min |
| | - Routing | 5 min |
| **Phase 3** | Employee Master | 45 min |
| | - Master Page | 20 min |
| | - Employee Form | 15 min |
| | - Table Component | 10 min |
| **Phase 4** | Testing | 30 min |
| **TOTAL** | | **3 hours** |

---

## 🚀 EXECUTION PLAN

### **Immediate Actions**:
1. ✅ Get approval for Option 1 (Create New HRM Domain)
2. ⏳ Create HRM domain structure
3. ⏳ Implement models following BBP
4. ⏳ Create serializers (Directory & Master)
5. ⏳ Create ViewSets with permissions
6. ⏳ Create frontend pages
7. ⏳ Test and validate

---

## ❓ QUESTIONS TO RESOLVE

1. **Data Migration**: Should we migrate data from legacy Employee model to new HRM Employee?
2. **Seed Data**: Should we create seed employees for testing?
3. **Photo Storage**: Where should employee photos be stored? (S3, local, etc.)
4. **Permissions**: Should we create a new "HR Admin" role or use existing roles?

---

**Status**: Awaiting approval to proceed with Option 1  
**Next Step**: Create HRM domain structure and models  
**Estimated Completion**: 3 hours from approval
