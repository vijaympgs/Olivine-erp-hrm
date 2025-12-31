# FMS BBP Template Reference Guide

## **Template Structure for Business Blueprint Creation**

---

## **1. MODULE IDENTIFICATION**

**Module Name:** [MODULE_NAME]
**Module Number:** [X.Y]
**Module Type:** [Master/Transaction/Dashboard/Reports/Config/Rule/Setup]
**Target File:** [DIRECTORY_PATH]/X.Y [MODULE_NAME].md
**Created Date:** [DATE]
**Version:** [VERSION]
**Author:** [AUTHOR_NAME]

---

## **2. PURPOSE**

### **2.1 Business Purpose**
[Brief description of the module's business purpose and strategic value]

### **2.2 Business Scope**
[Detailed scope of functionality, including what's in and what's out]

### **2.3 Key Stakeholders**
[List of primary users and their needs]

---

## **3. CORE MODELS (DJANGO)**

### **3.1 Primary Model: [ModelName]**

```python
class [ModelName](models.Model):
    """
    [Model description and purpose]
    """
    
    # Primary Key
    id = models.UUIDField(primary_key=True, default=uuid.uuid, editable=False)
    
    # Foreign Keys
    company_id = models.UUIDField()
    created_by_user_id = models.UUIDField()
    
    # Core Fields
    [field_name] = models.[FieldType](max_length=[length], [options])
    
    # Audit Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = '[table_name]'
        verbose_name = '[Verbose Name]'
        verbose_name_plural = '[Verbose Name Plural]'
        indexes = [
            models.Index(fields=['field1', 'field2'], name='idx_[name]'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['field1', 'field2'], name='uk_[name]'),
        ]
```

### **3.2 Supporting Models**

[List additional models with same structure as above]

---

## **4. REFERENCE MODELS (DJANGO)**

### **4.1 [ReferenceModelName]**

```python
class [ReferenceModelName](models.Model):
    """
    [Reference model description]
    """
    
    # Fields and relationships
    [field definitions]
    
    class Meta:
        db_table = '[table_name]'
        verbose_name = '[Verbose Name]'
```

---

## **5. FOREIGN KEY RELATIONSHIPS**

### **5.1 Primary Relationships**
- **[ModelName]** → **[RelatedModelName]**: [Relationship description]
- **[ModelName]** → **[RelatedModelName]**: [Relationship description]

### **5.2 Many-to-Many Relationships**
- **[ModelName]** ↔ **[RelatedModelName]**: [Relationship description]

---

## **6. BUSINESS RULES & VALIDATIONS**

### **6.1 Data Integrity Rules**
- [Rule 1 description]
- [Rule 2 description]
- [Rule 3 description]

### **6.2 Validation Logic**
```python
def clean_[field_name](self):
    """
    Custom validation for [field_name]
    """
    # Validation logic here
    pass
```

### **6.3 Business Constraints**
- [Constraint 1 description]
- [Constraint 2 description]

---

## **7. UI/UX SPECIFICATIONS**

### **7.1 User Interface Requirements**
- **Layout:** [Layout description]
- **Navigation:** [Navigation structure]
- **Responsiveness:** [Mobile/tablet/desktop requirements]

### **7.2 User Experience Design**
- **User Flow:** [Step-by-step user journey]
- **Error Handling:** [Error message standards]
- **Loading States:** [Loading indicator requirements]

### **7.3 Accessibility Standards**
- **WCAG Compliance:** [Accessibility level target]
- **Keyboard Navigation:** [Keyboard support requirements]
- **Screen Reader Support:** [Screen reader compatibility]

### **7.4 Visual Design System**
- **Color Scheme:** [Color palette and usage]
- **Typography:** [Font families and sizes]
- **Iconography:** [Icon library and standards]

### **7.5 Design Language Standards**
- **Design System:** [Material Design/Ant Design/Custom system]
- **Component Library:** [Component library name and version]
- **Design Tokens:** [Design token system for consistency]

### **7.6 Typography Standards**
- **Primary Font Family:** [Font name, fallbacks]
- **Secondary Font Family:** [Font name for headings/special text]
- **Font Sizes:**
  - **H1:** [Size]px / [Weight] / [Line-height]
  - **H2:** [Size]px / [Weight] / [Line-height]
  - **H3:** [Size]px / [Weight] / [Line-height]
  - **H4:** [Size]px / [Weight] / [Line-height]
  - **H5:** [Size]px / [Weight] / [Line-height]
  - **H6:** [Size]px / [Weight] / [Line-height]
  - **Body Large:** [Size]px / [Weight] / [Line-height]
  - **Body Medium:** [Size]px / [Weight] / [Line-height]
  - **Body Small:** [Size]px / [Weight] / [Line-height]
  - **Caption:** [Size]px / [Weight] / [Line-height]
- **Font Weights:** [Light/Regular/Medium/Semibold/Bold]
- **Text Colors:** [Primary/Secondary/Tertiary/Disabled/Error/Success/Warning]

### **7.7 Color Palette**
- **Primary Colors:**
  - **Primary 50:** #[Hex] (Lightest)
  - **Primary 100:** #[Hex]
  - **Primary 200:** #[Hex]
  - **Primary 300:** #[Hex]
  - **Primary 400:** #[Hex]
  - **Primary 500:** #[Hex] (Main)
  - **Primary 600:** #[Hex]
  - **Primary 700:** #[Hex]
  - **Primary 800:** #[Hex]
  - **Primary 900:** #[Hex] (Darkest)
- **Secondary Colors:** [Color definitions and hex codes]
- **Neutral Colors:** [Gray scale from 50 to 900]
- **Semantic Colors:**
  - **Success:** [Green palette]
  - **Warning:** [Amber/Yellow palette]
  - **Error:** [Red palette]
  - **Info:** [Blue palette]

### **7.8 Spacing System**
- **Base Unit:** [4px/8px base spacing unit]
- **Spacing Scale:**
  - **XS:** [Size]px (4px if base is 4px)
  - **SM:** [Size]px (8px if base is 4px)
  - **MD:** [Size]px (16px if base is 4px)
  - **LG:** [Size]px (24px if base is 4px)
  - **XL:** [Size]px (32px if base is 4px)
  - **2XL:** [Size]px (48px if base is 4px)
  - **3XL:** [Size]px (64px if base is 4px)

### **7.9 Border & Shadow System**
- **Border Radius:**
  - **None:** 0px
  - **SM:** 2px
  - **MD:** 4px
  - **LG:** 8px
  - **XL:** 12px
  - **Full:** 50%
- **Border Width:** [0px/1px/2px standards]
- **Box Shadows:**
  - **SM:** [Shadow definition]
  - **MD:** [Shadow definition]
  - **LG:** [Shadow definition]
  - **XL:** [Shadow definition]

### **7.10 Component Standards**
- **Buttons:**
  - **Primary Button:** [Size, padding, border-radius, colors]
  - **Secondary Button:** [Size, padding, border-radius, colors]
  - **Outline Button:** [Size, padding, border-radius, colors]
  - **Text Button:** [Size, padding, colors]
  - **Icon Button:** [Size, padding, colors]
  - **Floating Action Button:** [Size, shape, position]
- **Form Controls:**
  - **Text Input:** [Height, padding, border, focus states]
  - **Select Dropdown:** [Height, padding, border, arrow style]
  - **Checkbox:** [Size, checkmark style, colors]
  - **Radio Button:** [Size, dot style, colors]
  - **Toggle Switch:** [Size, thumb style, colors]
  - **Date Picker:** [Calendar style, input format]
  - **Time Picker:** [Clock style, input format]
- **Cards:**
  - **Default Card:** [Padding, shadow, border-radius]
  - **Elevated Card:** [Padding, shadow, border-radius]
  - **Outlined Card:** [Padding, border, border-radius]
- **Tables:**
  - **Header Row:** [Height, background, text style]
  - **Data Row:** [Height, border, hover state]
  - **Pagination:** [Size, style, active state]

### **7.11 Filter System Standards**
- **Filter Layout:** [Sidebar/Top bar/Accordion style]
- **Filter Components:**
  - **Search Input:** [Width, placeholder, icon]
  - **Date Range Picker:** [Format, preset options]
  - **Multi-select Dropdown:** [Chip display, max items]
  - **Single Select Dropdown:** [Width, search capability]
  - **Checkbox Group:** [Layout, max visible items]
  - **Radio Group:** [Layout, orientation]
  - **Range Slider:** [Min/max values, step]
  - **Number Input:** [Min/max, step, validation]
- **Filter Actions:**
  - **Apply Button:** [Position, style]
  - **Clear Button:** [Position, style]
  - **Reset Button:** [Position, style]
  - **Save Filter:** [Functionality, naming]
- **Filter States:**
  - **Active Filters:** [Chip display, remove action]
  - **Filter Count:** [Badge display, position]
  - **Loading State:** [Spinner, disabled state]

### **7.12 Data Display Standards**
- **Tables:**
  - **Column Headers:** [Alignment, sorting icons, resize]
  - **Row Height:** [Compact/Standard/Comfortable]
  - **Cell Padding:** [Horizontal/Vertical spacing]
  - **Alternating Rows:** [Background color, opacity]
  - **Hover State:** [Background color, transition]
  - **Selection State:** [Background color, checkbox]
- **Lists:**
  - **List Item Height:** [Standard height]
  - **List Item Padding:** [Horizontal/Vertical spacing]
  - **Divider Lines:** [Thickness, color, opacity]
  - **Avatar Size:** [Small/Medium/Large dimensions]
- **Cards/Grid:**
  - **Card Spacing:** [Gap between cards]
  - **Card Aspect Ratio:** [Standard proportions]
  - **Image Placeholder:** [Size, background, icon]
  - **Text Overflow:** [Ellipsis handling, line clamp]

### **7.13 Interactive Elements**
- **Hover States:** [Color transitions, timing]
- **Focus States:** [Outline style, color, offset]
- **Active States:** [Color changes, transform effects]
- **Disabled States:** [Opacity, cursor, colors]
- **Loading States:** [Spinner styles, skeleton screens]
- **Empty States:** [Illustrations, messages, actions]

### **7.14 Responsive Design Standards**
- **Breakpoints:**
  - **Mobile:** <[Size]px
  - **Tablet:** [Size]px - [Size]px
  - **Desktop:** >[Size]px
  - **Large Desktop:** >[Size]px
- **Container Max Widths:** [Mobile/Tablet/Desktop values]
- **Grid Systems:** [Column counts, gutters per breakpoint]
- **Typography Scaling:** [Font size adjustments per breakpoint]
- **Component Adaptations:** [Layout changes per breakpoint]

### **7.15 Animation & Transitions**
- **Transition Duration:** [Fast/Medium/Slow values]
- **Easing Functions:** [Ease-in/ease-out/ease-in-out standards]
- **Micro-interactions:** [Button hover, form field focus, etc.]
- **Page Transitions:** [Fade/slide/scale effects]
- **Loading Animations:** [Spinner styles, skeleton screen timing]

---

## **8. INTEGRATION POINTS**

### **8.1 External Systems**
- **[System Name]:** [Integration description and API endpoints]
- **[System Name]:** [Integration description and API endpoints]

### **8.2 Internal APIs**
- **[API Name]:** [API endpoint and purpose]
- **[API Name]:** [API endpoint and purpose]

---

## **9. API SPECIFICATIONS**

### **9.1 REST Endpoints**

#### **GET /api/[resource]/**
- **Purpose:** [Endpoint purpose]
- **Authentication:** [Auth requirements]
- **Parameters:** [Query parameters]
- **Response:** [Response format]

#### **POST /api/[resource]/**
- **Purpose:** [Endpoint purpose]
- **Authentication:** [Auth requirements]
- **Request Body:** [Request format]
- **Response:** [Response format]

### **9.2 Data Formats**
- **Request Format:** [JSON/XML/CSV requirements]
- **Response Format:** [JSON/XML/CSV requirements]
- **Error Format:** [Error response structure]

---

## **10. SECURITY REQUIREMENTS**

### **10.1 Authentication**
- **Method:** [JWT/OAuth2/Session-based]
- **Authorization:** [Role-based access control]
- **Session Management:** [Session handling requirements]

### **10.2 Data Protection**
- **Encryption:** [Data encryption standards]
- **Masking:** [Sensitive data masking rules]
- **Backup:** [Data backup procedures]

### **10.3 Access Control**
- **Permissions:** [Permission matrix]
- **Roles:** [Role definitions]
- **Audit Trail:** [Audit logging requirements]

---

## **11. PERFORMANCE CONSIDERATIONS**

### **11.1 Database Optimization**
- **Indexing Strategy:** [Index design for performance]
- **Query Optimization:** [Query performance requirements]
- **Connection Pooling:** [Database connection management]

### **11.2 Caching Strategy**
- **Cache Layers:** [Redis/Memory/database caching]
- **Cache Invalidation:** [Cache refresh policies]
- **Performance Metrics:** [KPIs and monitoring]

---

## **12. TESTING REQUIREMENTS**

### **12.1 Unit Tests**
- **Coverage Target:** [Percentage coverage requirement]
- **Test Framework:** [pytest/unittest/other]
- **Test Data:** [Test data management]

### **12.2 Integration Tests**
- **API Testing:** [API endpoint testing]
- **Database Testing:** [Database integration testing]
- **Third-party Testing:** [External system testing]

### **12.3 User Acceptance Tests**
- **UAT Scenarios:** [Test case definitions]
- **User Stories:** [User story mapping]
- **Acceptance Criteria:** [Definition of done]

---

## **13. DEPLOYMENT SPECIFICATIONS**

### **13.1 Environment Requirements**
- **Development:** [Dev environment setup]
- **Staging:** [Staging environment setup]
- **Production:** [Production environment setup]

### **13.2 Configuration Management**
- **Settings:** [Configuration parameters]
- **Environment Variables:** [Environment-specific settings]
- **Secrets Management:** [Secret handling procedures]

### **13.3 Monitoring & Logging**
- **Application Logs:** [Logging levels and formats]
- **Performance Metrics:** [Monitoring setup]
- **Error Tracking:** [Error capture and alerting]

---

## **14. MAINTENANCE & SUPPORT**

### **14.1 Regular Maintenance**
- **Database Maintenance:** [Maintenance schedules]
- **Performance Tuning:** [Optimization procedures]
- **Security Updates:** [Security patching]

### **14.2 Support Procedures**
- **Issue Tracking:** [Ticket system integration]
- **Knowledge Base:** [Documentation maintenance]
- **User Training:** [Training programs]

---

## **15. VERSION CONTROL**

### **15.1 Version History**
- **v1.0.0:** [Initial release description]
- **v1.1.0:** [Update description]
- **v1.2.0:** [Current version description]

### **15.2 Change Management**
- **Release Process:** [Release procedures]
- **Rollback Procedures:** [Rollback capabilities]
- **Migration Scripts:** [Data migration handling]

---

## **16. COMPLIANCE & AUDIT**

### **16.1 Regulatory Compliance**
- **GDPR:** [Data protection compliance]
- **SOX:** [Financial compliance requirements]
- **HIPAA:** [Healthcare compliance if applicable]

### **16.2 Audit Requirements**
- **Audit Trail:** [Audit logging implementation]
- **Compliance Reporting:** [Compliance report generation]
- **Documentation:** [Audit documentation maintenance]

---

**END OF BBP TEMPLATE**

---

## **COMPLEXITY-BASED TEMPLATE USAGE INSTRUCTIONS**

### **Complexity Classification:**
- **MST-S:** Master - Simple (Basic configuration, 2-3 models, minimal validation)
- **MST-M:** Master - Medium (Standard configuration, 4-6 models, moderate complexity)
- **MST-C:** Master - Complex (Advanced configuration, 7+ models, high complexity)
- **TXN-S:** Transaction - Simple (Basic transactions, 2-3 models, simple workflow)
- **TXN-M:** Transaction - Medium (Standard transactions, 4-6 models, moderate workflow)
- **TXN-C:** Transaction - Complex (Advanced transactions, 7+ models, complex workflow)

### **Template Sections by Complexity:**

#### **For MST-S/TXN-S (Simple):**
1. **All 16 sections** - Use complete template
2. **Sections 3-6:** Minimal models and basic business rules
3. **Sections 8-16:** Mark non-applicable sections as "Not Applicable"
4. **Focus:** Core functionality with minimal complexity

#### **For MST-M/TXN-M (Medium):**
1. **All 16 sections** - Use complete template
2. **Sections 3-6:** Standard models and business rules
3. **Sections 8-16:** Detailed specifications for all sections
4. **Focus:** Comprehensive functionality with moderate complexity

#### **For MST-C/TXN-C (Complex):**
1. **All 16 sections** - Use complete template
2. **Sections 3-6:** Advanced models with complex relationships
3. **Sections 8-16:** Comprehensive specifications with advanced features
4. **Focus:** Enterprise-grade functionality with high complexity

### **For Dashboard Modules (_D):**
1. **Simplified template (4 sections only):**
   - Purpose
   - Type: Dashboard
   - Functional Capture
   - UI/UX Spec
2. **Focus:** Metrics, KPIs, and data visualization
3. **NO Django models, business rules, or technical sections**

### **For Report Modules (_R):**
1. **Simplified template (4 sections only):**
   - Purpose
   - Type: Reports
   - Functional Capture
   - UI/UX Spec
2. **Focus:** Data points, reporting requirements, and export capabilities
3. **NO Django models, business rules, or technical sections**

### **For Config/Setup/Workflow Modules (_C/_S/_W):**
1. **Focused template (6 sections):**
   - Purpose
   - Type: Config/Rule/Setup
   - Core Models (Django)
   - Business Rules/Validations
   - UI/UX Spec
   - Sections 8-16: Simplified or marked as "Not Applicable"
2. **Focus:** Configuration logic and user experience

### **Complexity-Specific Guidelines:**

#### **MST-S (Simple Masters):**
- **Models:** 2-3 Django models with basic fields
- **Business Rules:** Simple validation rules
- **Integrations:** Minimal external integrations
- **UI/UX:** Standard components, basic layouts
- **Testing:** Basic unit and integration tests

#### **MST-M (Medium Masters):**
- **Models:** 4-6 Django models with relationships
- **Business Rules:** Moderate validation and business logic
- **Integrations:** Standard external system integrations
- **UI/UX:** Custom components, moderate complexity
- **Testing:** Comprehensive testing including UAT

#### **MST-C (Complex Masters):**
- **Models:** 7+ Django models with complex relationships
- **Business Rules:** Advanced validation and complex business logic
- **Integrations:** Multiple external systems, advanced APIs
- **UI/UX:** Highly customized, advanced interactions
- **Testing:** Enterprise-grade testing with performance testing

#### **TXN-S (Simple Transactions):**
- **Models:** 2-3 Django models for transaction processing
- **Workflow:** Basic transaction flow
- **Approvals:** Simple or no approval workflow
- **Reporting:** Basic transaction reports

#### **TXN-M (Medium Transactions):**
- **Models:** 4-6 Django models with transaction relationships
- **Workflow:** Standard transaction flow with approvals
- **Approvals:** Multi-level approval workflows
- **Reporting:** Standard transaction and management reports

#### **TXN-C (Complex Transactions):**
- **Models:** 7+ Django models with complex relationships
- **Workflow:** Advanced transaction flows with conditional logic
- **Approvals:** Complex approval hierarchies and business rules
- **Reporting:** Advanced analytics and compliance reports

### **General Guidelines:**
- Always include company_id for multi-tenant support
- Add audit fields (created_by_user_id, created_at, updated_at)
- Follow Django naming conventions
- Include proper indexing strategy based on complexity
- Document all business rules clearly
- Specify security requirements based on data sensitivity
- Define testing procedures appropriate to complexity level
- Include deployment specifications with scalability considerations
- Mark non-applicable sections clearly in complex modules

---

**TEMPLATE VERSION:** 2.0
**LAST UPDATED:** December 29, 2025
**COMPATIBLE:** Django 4.0+
