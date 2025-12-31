# FMS BBP Development Implementation Guide

## **Single Line Prompt for Any BBP Development Implementation:**

```
Refer BBP_Template_Reference.md and implement [TARGET_FILE_PATH] with Django models, UI components, CRUD operations, and persistence
```

## **Development Implementation Instructions:**

### **Step 1: Read and Analyze BBP**
1. Read the target BBP file completely
2. Identify module type (Master/Transaction/Dashboard/Reports/Config)
3. Extract Django models from section 02.1.3 Core Models
4. Note UI/UX specifications from section 02.1.7
5. Review business rules from section 02.1.6
6. Check API specifications from section 02.1.9

### **Step 2: Django Models Implementation**
**Refer to BBP Section: 02.1.3 Core Models**
- Implement primary model with all fields
- Add supporting models as specified
- Include proper indexes and constraints
- Add audit fields (created_at, updated_at, etc.)
- Implement foreign key relationships
- Add Meta class with db_table and indexes

### **Step 3: Database Migration**
- Create Django migration files
- Run migrations to create database tables
- Test model relationships and constraints

### **Step 4: CRUD Operations Implementation**
**Refer to BBP Section: 02.1.9 API Specifications**
- Create Django views for CRUD operations
- Implement serializers for API responses
- Add URL routing for all endpoints
- Include pagination and filtering
- Add error handling and validation

### **Step 5: UI Components Development**

#### **5.1 Choose Implementation Approach**
**Option A: Full Material Design 3.0 Implementation**
- Follow BBP Section 02.1.7 UI/UX Specifications exactly
- Implement Material Design components with rounded corners and colors
- Use complete design system with animations and transitions

**Option B: HTML-Only Dynamics 365 Implementation**
- Use simple black/white/grey color scheme
- No rounded corners, sharp edges only
- Follow exact Dynamics 365 interface patterns
- Minimal styling, focus on functionality over aesthetics

#### **5.2 Layout Structure**
- **Master-detail layout** for list and detail views
- **Tabbed interface** for different data sections
- **Sidebar navigation** for module navigation

#### **5.3 Component Implementation (Material Design 3.0)**
**Refer to BBP Subsections:**
- **7.10 Component Standards** - Button, form, card specifications
- **7.11 Filter System Standards** - Search and filter components
- **7.12 Data Display Standards** - Table and list components

#### **5.4 Component Implementation (Dynamics 365 HTML)**
- **Header:** Fixed header with branding and user info
- **Navigation Pane:** Fixed left navigation with module menu
- **Command Bar:** Action buttons with simple styling
- **Data Grid:** Clean table layout with hover states
- **Forms:** Simple forms with basic validation
- **Tabs:** Functional tab switching without styling

#### **5.5 Design System Application**
**Material Design 3.0:**
- **7.6 Typography Standards** - Font families and sizes
- **7.7 Color Palette** - Primary, secondary, semantic colors
- **7.8 Spacing System** - 8px base unit spacing scale
- **7.9 Border & Shadow System** - Border radius and box shadows

**Dynamics 365 HTML:**
- **Typography:** Segoe UI font family
- **Colors:** Black (#000000), White (#ffffff), Grey (#f8f8f8, #d6d6d6)
- **Spacing:** Simple padding and margins
- **Borders:** 1px solid borders, no radius
- **Shadows:** Minimal or no shadows

### **Step 6: Sidebar Implementation**
**Refer to BBP Section: 02.1.7.1 User Interface Requirements**
- Create responsive sidebar navigation
- Include module-specific menu items
- Add collapsible sections for sub-modules
- Implement active state indicators
- Add search functionality in sidebar

### **Step 7: Form Implementation**
**Refer to BBP Section: 02.1.6 Business Rules & Validations**
- Create forms based on Django model fields
- Implement client-side validation
- Add server-side validation from BBP rules
- Include error handling and display
- Add form submission handling

### **Step 8: Data Persistence**
**Refer to BBP Section: 02.1.10 Security Requirements**
- Implement secure data storage
- Add data encryption for sensitive fields
- Include audit trail functionality
- Implement user authentication and authorization
- Add data backup and recovery

### **Step 9: Testing Implementation**
**Refer to BBP Section: 02.1.12 Testing Requirements**
- Create unit tests for models and views
- Implement integration tests for API endpoints
- Add user acceptance tests for UI workflows
- Test business rules and validations
- Performance testing for large datasets

### **Step 10: Deployment Configuration**
**Refer to BBP Section: 02.1.13 Deployment Specifications**
- Configure Django settings for production
- Set up database connections
- Configure static file serving
- Add logging and monitoring
- Implement security headers and HTTPS

## **Key BBP Sections to Reference:**

### **For Django Models:**
- **Section 02.1.3:** Core Models (Django)
- **Section 02.1.4:** Reference Models (Django)
- **Section 02.1.5:** Foreign Key Relationships

### **For UI Components:**
- **Section 02.1.7.1:** User Interface Requirements
- **Section 02.1.7.2:** User Experience Design
- **Section 02.1.7.6:** Typography Standards
- **Section 02.1.7.7:** Color Palette
- **Section 02.1.7.8:** Spacing System
- **Section 02.1.7.10:** Component Standards
- **Section 02.1.7.11:** Filter System Standards
- **Section 02.1.7.12:** Data Display Standards

### **For Business Logic:**
- **Section 02.1.6:** Business Rules & Validations
- **Section 02.1.10:** Security Requirements
- **Section 02.1.11:** Performance Considerations

### **For Integration:**
- **Section 02.1.8:** Integration Points
- **Section 02.1.9:** API Specifications

## **Implementation Checklist:**

### **Django Backend:**
- [ ] Models implemented with all fields and relationships
- [ ] Migrations created and applied
- [ ] CRUD views implemented
- [ ] Serializers created
- [ ] URL routing configured
- [ ] Business rules implemented
- [ ] Security measures added
- [ ] API endpoints tested

### **Frontend UI:**
- [ ] Layout structure implemented
- [ ] Sidebar navigation created
- [ ] Components built to specifications
- [ ] Design system applied
- [ ] Forms implemented with validation
- [ ] Responsive design implemented
- [ ] Accessibility features added
- [ ] User experience flows tested

### **Data & Persistence:**
- [ ] Database schema created
- [ ] Data validation implemented
- [ ] Audit trail added
- [ ] Security encryption applied
- [ ] Backup procedures implemented
- [ ] Performance optimization applied

### **Testing & Quality:**
- [ ] Unit tests written
- [ ] Integration tests created
- [ ] User acceptance tests performed
- [ ] Performance tests conducted
- [ ] Security tests implemented
- [ ] Cross-browser compatibility tested

---

## **Implementation Prompt Examples:**

### **Material Design 3.0 Implementation:**
```
Refer FMS_Template_Reference.md and implement FMS\01.Finance Setup & Configuration\1.1 Chart of Accounts.md with Django models, UI components, CRUD operations, and persistence
```

### **Dynamics 365 HTML-Only Implementation:**
```
Refer FMS_Template_Reference.md and implement FMS\01.Finance Setup & Configuration\1.1 Chart of Accounts.md with HTML only, following Dynamics 365 UI patterns, simple black/white/grey colors, no rounded corners, command bar, navigation pane, and content area structure
```

### **Custom Implementation with Specific Framework:**
```
Refer FMS_Template_Reference.md and implement [TARGET_FILE_PATH] with Django models, UI components, CRUD operations, and persistence using [FRAMEWORK]
```

## **Dynamics 365 HTML Implementation Details:**

### **File Structure:**
- Create HTML file in module directory: `FMS/01.Finance Setup & Configuration/chart_of_accounts.html`
- Use semantic HTML5 structure
- Separate CSS in `<style>` tags for simplicity
- Add JavaScript for interactivity

### **Essential Dynamics 365 Components:**
```html
<!-- Header -->
<div class="d365-header">
    <div class="d365-logo">Module Name</div>
    <div class="d365-user-info">User Info</div>
</div>

<!-- Navigation Pane -->
<div class="d365-nav-pane">
    <div class="d365-nav-item active">Current Module</div>
    <div class="d365-nav-item">Other Modules</div>
</div>

<!-- Command Bar -->
<div class="d365-command-bar">
    <button class="d365-button d365-button-primary">+ New</button>
    <button class="d365-button">Edit</button>
    <button class="d365-button">Delete</button>
</div>

<!-- Content Area -->
<div class="d365-content">
    <!-- Search, Filters, Data Grid -->
</div>
```

### **CSS Styling Guidelines:**
```css
/* Core Colors */
.d365-header { background-color: #ffffff; }
.d365-nav-pane { background-color: #f8f8f8; }
.d365-command-bar { background-color: #ffffff; }
.d365-content { background-color: #ffffff; }

/* No Rounded Corners */
* { border-radius: 0px; }
.d365-button { border-radius: 0px; }
.d365-form-input { border-radius: 0px; }

/* Borders Only */
.d365-header { border-bottom: 1px solid #d6d6d6; }
.d365-nav-pane { border-right: 1px solid #d6d6d6; }
.d365-button { border: 1px solid #d6d6d6; }
.d365-form-input { border: 1px solid #d6d6d6; }

/* Typography */
body { font-family: 'Segoe UI', sans-serif; }
.d365-logo { font-weight: 600; }
.d365-grid-header { font-weight: 600; }

/* Fixed Positioning */
.d365-header { position: fixed; top: 0; height: 50px; }
.d365-nav-pane { position: fixed; left: 0; top: 50px; }
.d365-command-bar { position: fixed; top: 50px; left: 250px; }
.d365-content { margin-left: +++++++ REPLACE

---

**VERSION:** 1.0  
**LAST UPDATED:** December 29, 2025  
**COMPATIBLE:** All BBP Template Reference versions
