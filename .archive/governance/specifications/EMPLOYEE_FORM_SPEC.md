---
title: "Employee Form - UI Specification Document"
description: "Complete specification for Employee form component using Section C layout"
date: "2025-12-19 19:02:35"
modified: "2025-12-19 19:02:35"
author: "Development Team"
version: "1.0.0"
category: "ui-specification"
tags: [employee, form, section-c, ui-spec, hr]
project: "Retail ERP Platform"
component: "EmployeeFormStandalone"
path: "frontend/src/ui/components/employee/EmployeeFormStandalone.tsx"
last_reviewed: "2025-12-19 19:02:35"
review_status: "approved"
---

# Employee Form - UI Specification Document

## 📋 **Document Overview**

**Component Name**: `EmployeeFormStandalone`  
**Module**: Human Resources (HR)  
**Layout Section**: Section C: Primary Workspace  
**Complexity Level**: Medium  
**Form Type**: Multi-tab standalone form with internal navigation  

---

## 🎯 **Purpose & Scope**

This specification defines the complete UI/UX standards for the Employee form component. The form is designed to operate entirely within **Section C: Primary Workspace** as a self-contained component with internal tab navigation, following the established UI Layout Terminology.

### **Key Objectives**
- ✅ Self-contained form within Section C (no external sidebar dependency)
- ✅ Compact, efficient layout optimized for data entry
- ✅ Horizontal tab navigation for different employee information sections
- ✅ No overlapping with other UI sections (A, B, D)
- ✅ Responsive and accessible design
- ✅ Consistent with Terminal form design patterns

---

## 🏗️ **Layout Architecture**

### **Section C Positioning**

The form uses **fixed positioning** to fit exactly within Section C:

```css
position: fixed;
left: 256px;    /* Account for Section A: Sidebar (256px width) */
top: 64px;      /* Account for Section B: Application Header (64px height) */
right: 0;       /* Extend to right edge */
bottom: 48px;   /* Account for Section D: Status Bar (48px height) */
```

### **Visual Layout Structure**

```
┌─────────────────────────────────────────────────────────────┐
│                    Section B: Application Header (64px)      │
├─────────────┬───────────────────────────────────────────────┤
│             │                                               │
│  Section A: │      Section C: Primary Workspace             │
│   Sidebar   │  ┌─────────────────────────────────────────┐  │
│   (256px)   │  │ Employee Header (Photo, Name, Status)   │  │
│             │  │ Height: 60px (py-3 = 12px * 2 + content) │  │
│             │  ├─────────────────────────────────────────┤  │
│             │  │ Tab Navigation (Horizontal)             │  │
│             │  │ Height: 44px (py-2 = 8px * 2 + content) │  │
│             │  ├─────────────────────────────────────────┤  │
│             │  │                                         │  │
│             │  │  Scrollable Form Content Area           │  │
│             │  │  (Flexible height)                      │  │
│             │  │                                         │  │
│             │  ├─────────────────────────────────────────┤  │
│             │  │ Action Buttons (Save | Cancel)          │  │
│             │  │ Height: 60px (py-3 = 12px * 2 + btns)   │  │
│             │  └─────────────────────────────────────────┘  │
├─────────────┴───────────────────────────────────────────────┤
│                    Section D: Status Bar (48px)             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 **Design System Specifications**

### **Typography**

```css
/* Font Family */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* Text Sizes */
- Headers (h2): text-base (16px), font-semibold
- Section Titles (h4): text-sm (14px), font-semibold
- Labels: text-xs (12px), font-medium
- Input Text: text-sm (14px)
- Helper Text: text-xs (12px)
- Tab Labels: text-xs (12px), font-medium
- Status Badge: text-xs (12px), font-semibold, uppercase
```

### **Color Palette**

```css
/* Background Colors */
--bg-white: #FFFFFF
--bg-gray-50: #F9FAFB
--bg-gray-100: #F3F4F6

/* Section-Specific Backgrounds */
--bg-gray-section: #F9FAFB      /* Personal, Documents */
--bg-blue-section: #EFF6FF       /* Employment */
--bg-purple-section: #F5F3FF     /* Organization */
--bg-green-section: #F0FDF4      /* Contact */
--bg-orange-section: #FFF7ED     /* Compliance */
--bg-yellow-section: #FEFCE8     /* Compensation */

/* Text Colors */
--text-primary: #111827          /* gray-900 */
--text-secondary: #6B7280        /* gray-500 */
--text-label: #374151            /* gray-700 */

/* Border Colors */
--border-default: #E5E7EB        /* gray-200 */
--border-input: #D1D5DB          /* gray-300 */
--border-error: #EF4444          /* red-500 */
--border-focus: #3B82F6          /* blue-500 */

/* Status Colors */
--status-active-bg: #D1FAE5      /* green-100 */
--status-active-text: #065F46    /* green-800 */
--status-inactive-bg: #E5E7EB    /* gray-300 */
--status-inactive-text: #4B5563  /* gray-600 */

/* Button Colors */
--btn-primary-bg: #2563EB        /* blue-600 */
--btn-primary-hover: #1D4ED8     /* blue-700 */
--btn-secondary-bg: #FFFFFF
--btn-secondary-border: #D1D5DB  /* gray-300 */
--btn-secondary-text: #374151    /* gray-700 */
```

### **Spacing System**

```css
/* Padding Values */
--padding-xs: 4px    /* p-1 */
--padding-sm: 8px    /* p-2 */
--padding-md: 12px   /* p-3 */
--padding-lg: 16px   /* p-4 */
--padding-xl: 24px   /* p-6 */

/* Gap Values */
--gap-xs: 4px        /* gap-1 */
--gap-sm: 8px        /* gap-2 */
--gap-md: 12px       /* gap-3 */
--gap-lg: 16px       /* gap-4 */

/* Margin Values */
--margin-xs: 2px     /* mt-0.5 */
--margin-sm: 4px     /* mt-1 */
--margin-md: 8px     /* mt-2 */
--margin-lg: 12px    /* mt-3 */
```

### **Border Radius**

```css
--radius-sm: 4px     /* rounded */
--radius-md: 6px     /* rounded-md */
--radius-lg: 8px     /* rounded-lg */
--radius-full: 9999px /* rounded-full */
```

---

## 📐 **Component Structure**

### **1. Employee Header Section**

**Purpose**: Display employee identity and status  
**Height**: 60px (fixed)  
**Background**: bg-gray-50  
**Border**: border-b  

```tsx
<div className="flex-shrink-0 border-b bg-gray-50 px-4 py-3">
  <div className="flex items-center space-x-3">
    {/* Photo: 48px × 48px (h-12 w-12) */}
    {/* Name: text-base, font-semibold */}
    {/* Employee Code: text-xs, font-mono */}
    {/* Status Badge: text-xs, font-semibold, uppercase */}
  </div>
</div>
```

**Elements**:
- **Photo**: 48px × 48px, rounded-full, border-2, border-gray-300
- **Name**: text-base (16px), font-semibold, text-gray-900
- **Employee Code**: text-xs (12px), font-mono, text-gray-500
- **Status Badge**: px-2 py-1, rounded-full, text-xs, font-semibold, uppercase

### **2. Tab Navigation Section**

**Purpose**: Navigate between employee information sections  
**Height**: 44px (fixed)  
**Background**: bg-white  
**Border**: border-b  

```tsx
<div className="flex-shrink-0 border-b bg-white">
  <nav className="flex space-x-1 px-4" aria-label="Tabs">
    {/* Tab buttons: px-3 py-2, text-xs, font-medium */}
  </nav>
</div>
```

**Tab States**:
- **Active**: border-b-2, border-blue-500, text-blue-600
- **Inactive**: border-transparent, text-gray-500
- **Hover**: text-gray-700, border-gray-300

**Tab List** (8 tabs):
1. Summary
2. Personal
3. Employment
4. Organization
5. Contact
6. Compliance
7. Compensation
8. Documents

### **3. Scrollable Content Area**

**Purpose**: Display form fields for the active tab  
**Height**: Flexible (fills available space)  
**Overflow**: overflow-y-auto  

```tsx
<form onSubmit={handleSubmit} className="flex-1 overflow-y-auto">
  <div className="p-4 space-y-4">
    {/* Tab-specific content */}
  </div>
</form>
```

**Content Padding**: p-4 (16px all sides)  
**Section Spacing**: space-y-4 (16px between sections)  

### **4. Action Buttons Section**

**Purpose**: Form submission and cancellation  
**Height**: 60px (fixed)  
**Background**: bg-gray-50  
**Border**: border-t  

```tsx
<div className="flex-shrink-0 border-t bg-gray-50 px-4 py-3">
  <div className="flex justify-between items-center">
    <div className="text-xs text-gray-500">Employee Information</div>
    <div className="flex space-x-3">
      {/* Cancel button */}
      {/* Save button */}
    </div>
  </div>
</div>
```

---

## 🔘 **Button Specifications**

### **Primary Button (Save)**

```css
/* Styling */
padding: 6px 24px;              /* px-6 py-1.5 */
font-size: 14px;                /* text-sm */
color: #FFFFFF;
background-color: #2563EB;      /* bg-blue-600 */
border-radius: 4px;             /* rounded */
font-weight: 500;               /* font-medium */

/* Hover State */
background-color: #1D4ED8;      /* hover:bg-blue-700 */

/* Focus State */
outline: none;
box-shadow: 0 0 0 1px #3B82F6; /* focus:ring-1 focus:ring-blue-500 */

/* Disabled State */
opacity: 0.5;                   /* disabled:opacity-50 */
cursor: not-allowed;            /* disabled:cursor-not-allowed */
```

### **Secondary Button (Cancel)**

```css
/* Styling */
padding: 6px 16px;              /* px-4 py-1.5 */
font-size: 14px;                /* text-sm */
color: #374151;                 /* text-gray-700 */
background-color: #FFFFFF;      /* bg-white */
border: 1px solid #D1D5DB;      /* border border-gray-300 */
border-radius: 4px;             /* rounded */

/* Hover State */
background-color: #F9FAFB;      /* hover:bg-gray-50 */

/* Focus State */
outline: none;
box-shadow: 0 0 0 1px #3B82F6; /* focus:ring-1 focus:ring-blue-500 */
```

### **Button Placement**

- **Position**: Bottom-right of the form
- **Order**: Cancel (left) → Save (right)
- **Spacing**: space-x-3 (12px gap)
- **Alignment**: Right-aligned within the action bar

---

## 📝 **Form Field Specifications**

### **Input Field Layout**

**Grid System**: 3-column grid (grid-cols-3)  
**Gap**: gap-3 (12px)  

```tsx
<div className="grid grid-cols-3 gap-3">
  <div>
    <label className="block text-xs font-medium text-gray-700 mb-1">
      Field Label *
    </label>
    <input
      className="w-full rounded border px-2 py-1.5 text-sm border-gray-300"
      type="text"
    />
  </div>
</div>
```

### **Input Field Styling**

```css
/* Default State */
width: 100%;                    /* w-full */
padding: 6px 8px;               /* px-2 py-1.5 */
font-size: 14px;                /* text-sm */
border: 1px solid #D1D5DB;      /* border border-gray-300 */
border-radius: 4px;             /* rounded */

/* Focus State */
outline: none;
border-color: #3B82F6;          /* focus:border-blue-500 */
box-shadow: 0 0 0 1px #3B82F6; /* focus:ring-1 focus:ring-blue-500 */

/* Error State */
border-color: #EF4444;          /* border-red-500 */
background-color: #FEF2F2;      /* bg-red-50 (optional) */

/* Disabled/Read-only State */
background-color: #F3F4F6;      /* bg-gray-100 */
cursor: not-allowed;            /* cursor-not-allowed */
```

### **Label Styling**

```css
display: block;
font-size: 12px;                /* text-xs */
font-weight: 500;               /* font-medium */
color: #374151;                 /* text-gray-700 */
margin-bottom: 4px;             /* mb-1 */
```

### **Error Message Styling**

```css
font-size: 12px;                /* text-xs */
color: #DC2626;                 /* text-red-600 */
margin-top: 2px;                /* mt-0.5 */
```

---

## 📑 **Tab Content Specifications**

### **Summary Tab**

**Purpose**: Read-only overview of all employee information  
**Layout**: Multiple colored sections with 3-column grid  

**Section Structure**:
```tsx
<div className="bg-{color}-50 p-3 rounded-lg">
  <h4 className="text-sm font-semibold text-gray-900 mb-3">Section Title</h4>
  <div className="grid grid-cols-3 gap-3 text-xs">
    <div>
      <span className="font-medium text-gray-600">Label:</span>
      <p className="text-gray-900 mt-0.5">Value</p>
    </div>
  </div>
</div>
```

**Sections**:
1. Personal Information (bg-gray-50)
2. Employment Details (bg-blue-50)
3. Organization & Reporting (bg-purple-50)
4. Contact Information (bg-green-50)
5. Statutory / Compliance (bg-orange-50)
6. Compensation (bg-yellow-50)

### **Personal Tab**

**Fields** (3-column grid):
- First Name * (required)
- Last Name * (required)
- Employee Code (read-only)
- Date of Birth (date input)
- Gender (select dropdown)
- Marital Status (select dropdown)
- Photo (file input, col-span-3)

**Background**: bg-gray-50  
**Padding**: p-3  
**Border Radius**: rounded-lg  

### **Employment Tab**

**Fields** (3-column grid):
- Date of Joining * (required, date input)
- Employment Type (select dropdown)
- Designation (text input)
- Department (text input)

**Background**: bg-blue-50  

### **Organization Tab**

**Fields** (3-column grid):
- Business Unit (text input)
- Location (text input)
- Reporting Manager (text input with placeholder "Manager ID")

**Background**: bg-purple-50  

### **Contact Tab**

**Fields**:
- Email * (required, email input, 1 column)
- Mobile Number (text input, 1 column)
- Address (textarea, col-span-3, rows={2})

**Background**: bg-green-50  

### **Compliance Tab**

**Fields** (3-column grid):
- PAN (text input)
- Aadhaar (text input)
- PF Number (text input)
- ESI Number (text input)

**Background**: bg-orange-50  

### **Compensation Tab**

**Fields** (3-column grid):
- CTC (number input, read-only)
- Pay Grade (text input, read-only)

**Background**: bg-yellow-50  

### **Documents Tab**

**Content**: Placeholder for document upload feature  
**Background**: bg-gray-50  

---

## 🔄 **State Management**

### **Component State**

```typescript
const [activeTab, setActiveTab] = useState('summary');
const [formData, setFormData] = useState<EmployeeFormData>({...});
const [formErrors, setFormErrors] = useState<FormErrors>({});
```

### **Form Data Interface**

```typescript
interface EmployeeFormData {
  employee_code: string;
  first_name: string;
  last_name: string;
  date_of_birth?: string;
  gender?: 'M' | 'F' | 'O';
  marital_status?: 'single' | 'married' | 'divorced' | 'widowed';
  date_of_joining?: string;
  employment_type?: 'full_time' | 'part_time' | 'contract' | 'intern';
  designation?: string;
  department?: string;
  business_unit?: string;
  location?: string;
  reporting_manager?: number | null;
  email: string;
  mobile_number?: string;
  address?: string;
  pan?: string;
  aadhaar?: string;
  pf_number?: string;
  esi_number?: string;
  ctc?: number;
  pay_grade?: string;
  status: 'active' | 'inactive';
  photo?: File | string | null;
}
```

---

## ✅ **Validation Rules**

### **Required Fields**
- ✅ Employee Code
- ✅ First Name
- ✅ Last Name
- ✅ Email
- ✅ Date of Joining

### **Field Validation**

```typescript
// Email validation
/^[\w-.]+@[\w-]+\.[a-z]{2,}$/i

// Mobile number validation
/^\+?[\d\s-]{7,15}$/

// Required field validation
if (!value.trim()) {
  errors.field = 'Field is required';
}
```

---

## 📱 **Responsive Behavior**

### **Desktop (≥1024px)**
- Full 3-column grid layout
- All sections visible
- Optimal spacing

### **Tablet (768px - 1023px)**
- 2-column grid layout
- Adjusted spacing
- Maintained readability

### **Mobile (<768px)**
- Single column layout
- Stacked form fields
- Touch-optimized inputs

---

## ♿ **Accessibility Standards**

### **ARIA Labels**
```tsx
<nav aria-label="Tabs">
<form role="form">
<button aria-label="Save employee information">
```

### **Keyboard Navigation**
- Tab key: Navigate between fields
- Enter: Submit form
- Escape: Cancel/close

### **Focus Management**
- Visible focus indicators
- Logical tab order
- Focus trap within modal

---

## 🎯 **Usage Guidelines**

### **When to Use This Pattern**
- ✅ Complex forms with multiple sections
- ✅ Forms requiring organized data entry
- ✅ Self-contained forms in Section C
- ✅ Forms with 6+ logical groupings

### **When NOT to Use**
- ❌ Simple forms with <5 fields
- ❌ Forms requiring external sidebar navigation
- ❌ Forms needing multi-step wizards

---

## 📚 **Related Components**

- **TerminalForm**: Similar Section C layout pattern
- **EmployeeRootLayout**: Alternative layout with sidebar (deprecated for this use case)
- **EmployeeLifecycleNav**: External sidebar navigation (not used in standalone form)

---

## 🔗 **References**

- **UI Layout Terminology**: `docs/steering/UI_LAYOUT_TERMINOLOGY.md`
- **Component Library**: `docs/steering/COMPONENT_LIBRARY.md`
- **State Patterns**: `docs/steering/STATE_PATTERNS.md`
- **Terminal Form Reference**: `frontend/src/modules/pos/terminal/TerminalForm.tsx`

---

## 📝 **Implementation Checklist**

- [x] Fixed positioning for Section C
- [x] Compact header with employee info
- [x] Horizontal tab navigation
- [x] Scrollable content area
- [x] Fixed action buttons
- [x] 3-column grid layout
- [x] Color-coded sections
- [x] Form validation
- [x] Error handling
- [x] Responsive design
- [x] Accessibility compliance

---

## 🔄 **Version History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-12-19 | Development Team | Initial specification |

---

**Document Status**: ✅ Approved  
**Last Updated**: 2025-12-19 19:02:35  
**Next Review**: 2026-01-19
