# Nexus ERP Typography System

## 🎨 Distinctive Font Stack

Our ERP platform uses a carefully curated font combination that feels professional, human, and distinctly non-AI generated:

### **Primary Fonts**

**DM Sans** - Primary UI Font
- **Why**: Geometric yet humanist, with distinctive character
- **Usage**: Body text, forms, navigation, general UI
- **Personality**: Professional, approachable, modern
- **Features**: Variable font with optical sizing, excellent readability

**Crimson Pro** - Display Font  
- **Why**: Elegant serif with strong personality for headings
- **Usage**: Page titles, section headers, branding
- **Personality**: Sophisticated, editorial, trustworthy
- **Features**: High contrast, excellent for large sizes

**Fira Code** - Monospace Font
- **Why**: Distinctive coding font with programming ligatures
- **Usage**: Data tables, codes, technical content
- **Personality**: Technical, precise, developer-friendly
- **Features**: Programming ligatures, tabular numbers

## 🎯 Typography Classes

### **Semantic Classes**

```css
.erp-title        /* Page and section titles */
.erp-subtitle     /* Descriptive text under titles */
.erp-body         /* General body text */
.erp-data         /* Data and numbers */
.erp-label        /* Form labels and UI labels */
.erp-number       /* Financial and numeric data */
.erp-button       /* Button text */
.erp-form-input   /* Form input text */
.erp-table-header /* Table column headers */
.erp-sidebar-text /* Sidebar navigation text */
```

### **Font Features**

Our fonts use advanced OpenType features:

- **Kerning**: Improved letter spacing
- **Ligatures**: Natural letter combinations
- **Tabular Numbers**: Aligned numeric data
- **Small Caps**: Professional labels
- **Optical Sizing**: Size-specific optimizations

## 🏢 Enterprise Character

### **What Makes It Distinctive**

1. **DM Sans Geometric Warmth**: Unlike cold geometric fonts, DM Sans has humanist touches
2. **Crimson Pro Editorial Feel**: Gives the ERP a sophisticated, publication-quality appearance
3. **Fira Code Technical Precision**: Shows attention to developer/technical user needs
4. **Advanced Typography**: OpenType features show professional attention to detail

### **Avoiding AI-Generated Feel**

- **No Generic Sans**: Avoided overused fonts like Inter, Roboto
- **Serif for Hierarchy**: Crimson Pro adds editorial sophistication
- **Distinctive Monospace**: Fira Code has character vs generic monospace
- **Thoughtful Features**: Small caps, ligatures, tabular nums show human curation

## 📊 Usage Guidelines

### **Hierarchy**

```
H1: Crimson Pro, 2xl, medium weight
H2: Crimson Pro, xl, medium weight  
H3: Crimson Pro, lg, medium weight
H4: DM Sans, base, semibold weight
Body: DM Sans, sm, normal weight
Labels: DM Sans, xs, medium weight + small caps
Data: Fira Code, sm, normal weight + tabular nums
```

### **Contexts**

- **Marketing/Branding**: Crimson Pro for elegance
- **UI/Forms**: DM Sans for clarity and approachability  
- **Data/Technical**: Fira Code for precision
- **Navigation**: DM Sans with subtle text shadows

## 🎨 Visual Identity

This typography system creates a unique identity:

- **Professional but Approachable**: DM Sans warmth
- **Sophisticated**: Crimson Pro editorial quality
- **Technical Competence**: Fira Code precision
- **Attention to Detail**: Advanced OpenType features

The combination feels distinctly human-curated, avoiding the generic look of AI-generated interfaces while maintaining enterprise professionalism.

## 🔧 Implementation

Fonts are loaded via Google Fonts with display=swap for performance:

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,200..900;1,200..900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300..700&display=swap');
```

All fonts include variable weight support for precise typography control.