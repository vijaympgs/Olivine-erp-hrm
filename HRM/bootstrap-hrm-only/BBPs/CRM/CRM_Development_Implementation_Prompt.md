# CRM BBP Development Implementation Guide

## **Single Line Prompt for Any BBP Development Implementation:**

```
Refer CRM_Template_Reference.md and implement [TARGET_FILE_PATH] with Django models, UI components, CRUD operations, and persistence
```

## **Development Implementation Instructions (ENHANCED)**

### **Step 1: Read and Analyze BBP**
1. Read the target BBP file completely
2. Identify module type (Master/Transaction/Dashboard/Reports/Config)
3. Extract Django models from section 3 (Core Models)
4. Note UI/UX specifications from section 7 (UI/UX Specifications)
5. Review business rules from section 6 (Business Rules & Validations)
6. Check API specifications from section 9 (API Specifications)
7. Understand integration points from section 8 (Integration Points)

### **Step 2: Django Models Implementation**
**Refer to BBP Section: 3 - Core Models (Django)**
- Implement primary model with all fields as specified
- Add supporting models as specified in section 4 (Reference Models)
- Include proper indexes and constraints from Meta class
- Add audit fields (created_at, updated_at, created_by_user_id, company_id)
- Implement foreign key relationships as defined in section 5
- Follow Django naming conventions and best practices
- Include UUID primary keys for all models
- Add proper field validation and constraints

### **Step 3: Database Migration**
- Create Django migration files using `python manage.py makemigrations`
- Run migrations to create database tables
- Test model relationships and constraints
- Verify data integrity and foreign key constraints
- Add initial data if required

### **Step 4: CRUD Operations Implementation**
**Refer to BBP Section: 9 - API Specifications**
- Create Django views for CRUD operations (Create, Read, Update, Delete)
- Implement serializers for API responses following Django REST Framework
- Add URL routing for all endpoints as specified in BBP
- Include pagination and filtering capabilities
- Add comprehensive error handling and validation
- Implement business rules from BBP section 6
- Add search and filtering functionality

### **Step 5: UI Components Development**

#### **5.1 Choose Implementation Approach**
**Recommended Approach: HTML-Only Dynamics 365 Implementation**
- Use simple black/white/grey color scheme
- No rounded corners, sharp edges only (border-radius: 0px)
- Follow exact Dynamics 365 interface patterns
- Minimal styling, focus on functionality over aesthetics
- Consistent with FMS/HRM implementation patterns

**Alternative Approaches:**
- **Full Material Design 3.0:** Complete design system with animations
- **Hybrid Implementation:** Configurable UI approach per module

#### **5.2 Layout Structure**
- **Fixed Header:** Company branding, user info, navigation
- **Navigation Pane:** Fixed left navigation with module menu
- **Command Bar:** Action buttons with simple styling
- **Content Area:** Main content area with data grid and forms
- **Responsive Design:** Mobile and tablet compatibility

#### **5.3 Component Implementation (Dynamics 365 HTML)**
**Core Components:**
- **Header:** Fixed header with branding and user info
- **Navigation:** Fixed left navigation with module menu items
- **Command Bar:** Action buttons (New, Edit, Delete, Save, Cancel)
- **Data Grid:** Clean table layout with hover states
- **Forms:** Simple forms with basic validation
- **Tabs:** Functional tab switching without styling
- **Filters:** Search and filter components
- **Status Indicators:** Visual status displays

#### **5.4 Design System Application**
**Dynamics 365 HTML Standards:**
- **Typography:** Segoe UI font family
- **Colors:** Black (#000000), White (#ffffff), Grey (#f8f8f8, #d6d6d6)
- **Spacing:** Simple padding and margins (4px, 8px, 16px, 24px)
- **Borders:** 1px solid borders, no radius (border-radius: 0px)
- **Shadows:** Minimal or no shadows
- **Backgrounds:** White for main content, light grey for sidebars

#### **5.5 File Structure**
```
CRM/[Module Directory]/
├── [module_name].html          # Main HTML file
├── models.py                  # Django models
├── views.py                   # Django views
├── urls.py                    # Django URLs
├── serializers.py             # Django serializers
└── forms.py                   # Django forms (if needed)
```

### **Step 6: HTML Implementation Structure**
**Essential HTML Template:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Module Name] - CRM System</title>
    <style>
        /* Dynamics 365 CSS Styles */
        body { font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; background-color: #f8f8f8; }
        .header { position: fixed; top: 0; left: 0; right: 0; height: 50px; background-color: #ffffff; border-bottom: 1px solid #d6d6d6; z-index: 1000; }
        .nav-pane { position: fixed; top: 50px; left: 0; width: 250px; bottom: 0; background-color: #f8f8f8; border-right: 1px solid #d6d6d6; overflow-y: auto; }
        .command-bar { position: fixed; top: 50px; left: 250px; right: 0; height: 40px; background-color: #ffffff; border-bottom: 1px solid #d6d6d6; z-index: 999; }
        .content { margin-left: 250px; margin-top: 90px; padding: 20px; background-color: #ffffff; min-height: calc(100vh - 90px); }
        .button { padding: 8px 16px; border: 1px solid #d6d6d6; background-color: #ffffff; cursor: pointer; border-radius: 0px; }
        .button:hover { background-color: #f8f8f8; }
        .button-primary { background-color: #0078d4; color: #ffffff; border-color: #0078d4; }
        .button-primary:hover { background-color: #106ebe; }
        .data-grid { width: 100%; border-collapse: collapse; }
        .data-grid th { background-color: #f8f8f8; padding: 12px; text-align: left; border-bottom: 1px solid #d6d6d6; font-weight: 600; }
        .data-grid td { padding: 12px; border-bottom: 1px solid #d6d6d6; }
        .data-grid tr:hover { background-color: #f8f8f8; }
        .form-input { width: 100%; padding: 8px; border: 1px solid #d6d6d6; border-radius: 0px; }
        .form-input:focus { outline: 1px solid #0078d4; }
        .tab { display: inline-block; padding: 10px 20px; border: 1px solid #d6d6d6; border-bottom: none; cursor: pointer; background-color: #ffffff; }
        .tab.active { border-bottom: 1px solid #ffffff; background-color: #ffffff; }
        .tab-content { border: 1px solid #d6d6d6; padding: 20px; }
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <div style="float: left; padding: 15px 20px; font-weight: 600;">CRM System</div>
        <div style="float: right; padding: 15px 20px;">User Info</div>
    </div>

    <!-- Navigation Pane -->
    <div class="nav-pane">
        <div class="nav-item active">[Current Module]</div>
        <div class="nav-item">Other Modules</div>
    </div>

    <!-- Command Bar -->
    <div class="command-bar">
        <button class="button button-primary" onclick="showAddForm()">+ New</button>
        <button class="button" onclick="editSelected()">Edit</button>
        <button class="button" onclick="deleteSelected()">Delete</button>
    </div>

    <!-- Content Area -->
    <div class="content">
        <!-- Main content will be loaded here -->
    </div>

    <script>
        // JavaScript functionality
        // CRUD operations, form handling, etc.
    </script>
</body>
</html>
```

### **Step 7: Django Backend Implementation**
**Models Implementation:**
```python
# models.py
from django.db import models
import uuid

class [ModelName](models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.UUIDField()
    created_by_user_id = models.UUIDField()
    
    # Fields from BBP section 3
    [field_name] = models.[FieldType]([options])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = '[table_name]'
        indexes = [
            models.Index(fields=['field1', 'field2'], name='idx_[name]'),
        ]
```

**Views Implementation:**
```python
# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import [ModelName]
import json

def [model_name]_list(request):
    if request.method == 'GET':
        objects = [ModelName].objects.filter(company_id=get_company_id(request))
        data = [{'id': str(obj.id), 'name': obj.name} for obj in objects]
        return JsonResponse({'data': data})

@csrf_exempt
def [model_name]_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Create object with validation
        return JsonResponse({'success': True})
```

### **Step 8: JavaScript Interactivity**
**CRUD Operations:**
```javascript
// Data loading
function loadData() {
    fetch('/api/[model_name]/list/')
        .then(response => response.json())
        .then(data => {
            renderDataGrid(data.data);
        });
}

// Form submission
function saveForm() {
    const formData = new FormData(document.getElementById('[form_id]'));
    fetch('/api/[model_name]/create/', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData))
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loadData();
            hideForm();
        }
    });
}

// Search and filtering
function filterData() {
    const searchTerm = document.getElementById('search').value;
    // Implement filtering logic
}
```

### **Step 9: Business Rules Implementation**
**Refer to BBP Section: 6 - Business Rules & Validations**
- Implement validation logic in Django models (clean() methods)
- Add client-side validation in JavaScript
- Implement business rule checks in views
- Add proper error handling and user feedback
- Include audit trail functionality

### **Step 10: Security Implementation**
**Refer to BBP Section: 10 - Security Requirements**
- Implement authentication and authorization
- Add CSRF protection
- Include data validation and sanitization
- Implement role-based access control
- Add audit logging for all operations

### **Step 11: Testing Implementation**
**Refer to BBP Section: 12 - Testing Requirements**
- Create unit tests for models and views
- Implement integration tests for API endpoints
- Add user acceptance tests for UI workflows
- Test business rules and validations
- Perform security testing

### **Step 12: Deployment Configuration**
**Refer to BBP Section: 13 - Deployment Specifications**
- Configure Django settings for production
- Set up database connections
- Configure static file serving
- Add logging and monitoring
- Implement security headers and HTTPS

## **Key BBP Sections to Reference:**

### **For Django Models:**
- **Section 3:** Core Models (Django)
- **Section 4:** Reference Models (Django)
- **Section 5:** Foreign Key Relationships

### **For UI Components:**
- **Section 7.1:** User Interface Requirements
- **Section 7.2:** User Experience Design
- **Section 7.6:** Typography Standards
- **Section 7.7:** Color Palette
- **Section 7.8:** Spacing System
- **Section 7.10:** Component Standards
- **Section 7.11:** Filter System Standards
- **Section 7.12:** Data Display Standards

### **For Business Logic:**
- **Section 6:** Business Rules & Validations
- **Section 10:** Security Requirements
- **Section 11:** Performance Considerations

### **For Integration:**
- **Section 8:** Integration Points
- **Section 9:** API Specifications

## **Implementation Checklist:**

### **Django Backend:**
- [ ] Models implemented with all fields and relationships from BBP section 3
- [ ] Migrations created and applied successfully
- [ ] CRUD views implemented with proper error handling
- [ ] Serializers created for API responses
- [ ] URL routing configured as per BBP section 9
- [ ] Business rules implemented from BBP section 6
- [ ] Security measures added (authentication, authorization)
- [ ] API endpoints tested and documented
- [ ] Database optimization with proper indexes
- [ ] Data validation implemented

### **Frontend UI (Dynamics 365 HTML):**
- [ ] Layout structure matches Dynamics 365 patterns exactly
- [ ] Fixed header with branding and navigation implemented
- [ ] Fixed navigation pane with module menu created
- [ ] Command bar with action buttons implemented
- [ ] Data grid with search and filters created
- [ ] Forms with validation implemented
- [ ] Responsive design for mobile/tablet/desktop
- [ ] Status indicators and validation messages added
- [ ] JavaScript interactivity for all CRUD operations
- [ ] Accessibility features (ARIA labels, keyboard navigation)
- [ ] Error handling and user feedback implemented
- [ ] Data export and import capabilities added

### **Data & Persistence:**
- [ ] Database schema created from BBP models
- [ ] Data validation implemented from BBP rules
- [ ] Audit trail added for all operations
- [ ] Security encryption applied for sensitive data
- [ ] Backup procedures implemented
- [ ] Performance optimization applied

### **Testing & Quality:**
- [ ] Unit tests written for models and views
- [ ] Integration tests created for API endpoints
- [ ] User acceptance tests performed for UI workflows
- [ ] Performance tests conducted with large datasets
- [ ] Security tests implemented and passed
- [ ] Cross-browser compatibility tested
- [ ] Accessibility compliance verified (WCAG 2.1 AA)

## **Implementation Prompts (ENHANCED)**

### **For Master/Transaction Modules (Complete Template):**
```
Refer CRM_Template_Reference.md and implement [TARGET_FILE_PATH] with Django models, UI components, CRUD operations, and persistence

Implementation Requirements:
1. Read the BBP file completely to understand all requirements
2. Implement all Django models from BBP section 3 with proper relationships
3. Create HTML file following Dynamics 365 UI patterns
4. Use simple black/white/grey color scheme with no rounded corners
5. Include fixed header, navigation pane, command bar, and content area
6. Implement all business rules from BBP section 6
7. Create CRUD operations with JavaScript
8. Follow UI/UX specifications from BBP section 7
9. Add security requirements from BBP section 10
10. Include testing requirements from BBP section 12

Technical Requirements:
- Use semantic HTML5 structure
- Include CSS in <style> tags for simplicity
- Add JavaScript for interactivity and CRUD operations
- Implement Django models as specified in BBP
- Create responsive design for mobile and desktop
- Include accessibility features (ARIA labels, keyboard navigation)
- Add error handling and validation
- Implement search and filtering capabilities
- Include data export functionality

File Structure:
- HTML file in module directory: [module_name].html
- Django files: models.py, views.py, urls.py, serializers.py
- Inline CSS and JavaScript in HTML file

Quality Standards:
- Follow Dynamics 365 UI patterns exactly
- Implement all BBP requirements completely
- Ensure responsive design works on all devices
- Include comprehensive error handling
- Test all CRUD operations
- Validate business rules implementation
```

### **For Dashboard/Report Modules (Simplified Template):**
```
Refer CRM_Template_Reference.md and implement [TARGET_FILE_PATH] with Django models, UI components, CRUD operations, and persistence

Implementation Requirements:
1. Read the BBP file completely to understand all requirements
2. Implement simplified Django models for data storage
3. Create HTML file following Dynamics 365 UI patterns
4. Use simple black/white/grey color scheme with no rounded corners
5. Focus on data visualization and reporting functionality
6. Implement data aggregation and calculations
7. Create export capabilities (PDF, Excel, CSV)
8. Follow simplified UI/UX specifications from BBP section 7
9. Include scheduling and automation features
10. Add data refresh and real-time updates

Technical Requirements:
- Use semantic HTML5 structure
- Include CSS in <style> tags for simplicity
- Add JavaScript for data visualization and interactivity
- Implement Django models for data storage
- Create responsive design for mobile and desktop
- Include accessibility features (ARIA labels, keyboard navigation)
- Add data export functionality
- Implement chart and graph libraries
- Include real-time data updates

File Structure:
- HTML file in module directory: [module_name].html
- Django files: models.py, views.py, urls.py
- Inline CSS and JavaScript in HTML file

Quality Standards:
- Follow Dynamics 365 UI patterns exactly
- Implement all BBP requirements completely
- Ensure responsive design works on all devices
- Include comprehensive error handling
- Test all data visualization features
- Validate export functionality
```

### **For Configuration Modules (Focused Template):**
```
Refer CRM_Template_Reference.md and implement [TARGET_FILE_PATH] with Django models, UI components, CRUD operations, and persistence

Implementation Requirements:
1. Read the BBP file completely to understand all requirements
2. Implement Django models from BBP section 3
3. Create HTML file following Dynamics 365 UI patterns
4. Use simple black/white/grey color scheme with no rounded corners
5. Focus on configuration logic and user experience
6. Implement setup procedures and validation requirements
7. Create configuration dependency management
8. Follow UI/UX specifications from BBP section 7
9. Include rollback and recovery procedures
10. Add configuration testing and validation

Technical Requirements:
- Use semantic HTML5 structure
- Include CSS in <style> tags for simplicity
- Add JavaScript for configuration management
- Implement Django models for configuration storage
- Create responsive design for mobile and desktop
- Include accessibility features (ARIA labels, keyboard navigation)
- Add configuration validation and testing
- Implement setup wizards and procedures

File Structure:
- HTML file in module directory: [module_name].html
- Django files: models.py, views.py, urls.py
- Inline CSS and JavaScript in HTML file

Quality Standards:
- Follow Dynamics 365 UI patterns exactly
- Implement all BBP requirements completely
- Ensure responsive design works on all devices
- Include comprehensive error handling
- Test all configuration functionality
- Validate setup procedures
```

---

## **Dynamics 365 HTML Implementation Details (ENHANCED)**

### **Essential CSS Framework:**
```css
/* Core Dynamics 365 Styles */
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: 'Segoe UI', 'Segoe UI Web', 'Segoe UI Symbol', 'Roboto', 'Helvetica Neue', 'Arial', sans-serif;
    font-size: 14px;
    line-height: 1.4;
    color: #000000;
    background-color: #f8f8f8;
}

/* Layout Containers */
.header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 50px;
    background-color: #ffffff;
    border-bottom: 1px solid #d6d6d6;
    z-index: 1000;
    display: flex;
    align-items: center;
    padding: 0 20px;
}

.nav-pane {
    position: fixed;
    top: 50px;
    left: 0;
    width: 250px;
    bottom: 0;
    background-color: #f8f8f8;
    border-right: 1px solid #d6d6d6;
    overflow-y: auto;
    z-index: 999;
}

.command-bar {
    position: fixed;
    top: 50px;
    left: 250px;
    right: 0;
    height: 40px;
    background-color: #ffffff;
    border-bottom: 1px solid #d6d6d6;
    z-index: 998;
    display: flex;
    align-items: center;
    padding: 0 20px;
}

.content {
    margin-left: 250px;
    margin-top: 90px;
    padding: 20px;
    background-color: #ffffff;
    min-height: calc(100vh - 90px);
}

/* Buttons */
.button {
    padding: 8px 16px;
    border: 1px solid #d6d6d6;
    background-color: #ffffff;
    color: #000000;
    cursor: pointer;
    border-radius: 0px;
    font-size: 14px;
    font-family: inherit;
    text-decoration: none;
    display: inline-block;
    vertical-align: middle;
}

.button:hover {
    background-color: #f8f8f8;
}

.button:active {
    background-color: #e1e1e1;
}

.button-primary {
    background-color: #0078d4;
    color: #ffffff;
    border-color: #0078d4;
}

.button-primary:hover {
    background-color: #106ebe;
}

.button-primary:active {
    background-color: #0078d4;
}

/* Forms */
.form-input {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #d6d6d6;
    border-radius: 0px;
    font-size: 14px;
    font-family: inherit;
    background-color: #ffffff;
}

.form-input:focus {
    outline: 1px solid #0078d4;
    border-color: #0078d4;
}

.form-select {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #d6d6d6;
    border-radius: 0px;
    font-size: 14px;
    font-family: inherit;
    background-color: #ffffff;
}

.form-textarea {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #d6d6d6;
    border-radius: 0px;
    font-size: 14px;
    font-family: inherit;
    background-color: #ffffff;
    resize: vertical;
    min-height: 80px;
}

/* Data Grid */
.data-grid {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
}

.data-grid th {
    background-color: #f8f8f8;
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #d6d6d6;
    font-weight: 600;
    color: #000000;
    white-space: nowrap;
}

.data-grid td {
    padding: 12px;
    border-bottom: 1px solid #d6d6d6;
    color: #000000;
    vertical-align: top;
}

.data-grid tr:hover {
    background-color: #f8f8f8;
}

.data-grid tr.selected {
    background-color: #e3f2fd;
}

/* Tabs */
.tab {
    display: inline-block;
    padding: 10px 20px;
    border: 1px solid #d6d6d6;
    border-bottom: 1px solid #ffffff;
    cursor: pointer;
    background-color: #ffffff;
    color: #000000;
    text-decoration: none;
    font-size: 14px;
    font-family: inherit;
}

.tab:hover {
    background-color: #f8f8f8;
}

.tab.active {
    border-bottom: 1px solid #ffffff;
    background-color: #ffffff;
    color: #0078d4;
}

.tab-content {
    border: 1px solid #d6d6d6;
    padding: 20px;
    background-color: #ffffff;
}

/* Status Indicators */
.status-success {
    color: #107c10;
    font-weight: 600;
}

.status-warning {
    color: #ff8c00;
    font-weight: 600;
}

.status-error {
    color: #d83b01;
    font-weight: 600;
}

/* Utility Classes */
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-left { text-align: left; }
.mb-20 { margin-bottom: 20px; }
.mt-20 { margin-top: 20px; }
.hidden { display: none; }
.visible { display: block; }
```

---

**VERSION:** 2.0  
**LAST UPDATED:** December 31, 2025  
**ENHANCEMENTS:** HRM/FMS implementation learnings, Dynamics 365 patterns, improved workflow  
**COMPATIBLE:** All CRM BBP Template Reference versions
