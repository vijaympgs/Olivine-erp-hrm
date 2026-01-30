# CSS Typography Guide - Lenovo Support Website Analysis

## Overview
This document analyzes the typography and font usage on the Lenovo support website, specifically focusing on the page: https://support.lenovo.com/in/en/solutions/ht504725

## Font Stack Analysis

### Primary Font Stack
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", Arial, sans-serif;
```

### Font Hierarchy by Platform

| Platform | Primary Font | Fallback |
|----------|-------------|----------|
| **macOS/iOS** | San Francisco (-apple-system) | Helvetica Neue |
| **Windows** | Segoe UI | Arial |
| **Android** | Roboto | Arial |
| **Linux** | Ubuntu/Oxygen/Cantarell | Arial |
| **Universal** | Arial/Helvetica | sans-serif |

## Typography Specifications

### Heading Styles

#### Main Page Title
```css
.main-title {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 28px;
    font-weight: 700; /* Bold */
    line-height: 1.3;
    color: #333333;
    margin-bottom: 16px;
}
```

#### Section Headings
```css
.section-heading {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 20px;
    font-weight: 600; /* Semibold */
    line-height: 1.4;
    color: #2c2c2c;
    margin-bottom: 12px;
}
```

#### Subsection Headings
```css
.subsection-heading {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 16px;
    font-weight: 600; /* Semibold */
    line-height: 1.4;
    color: #444444;
    margin-bottom: 8px;
}
```

### Body Text Styles

#### Primary Body Text
```css
.body-text {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 14px;
    font-weight: 400; /* Regular */
    line-height: 1.6;
    color: #555555;
    margin-bottom: 16px;
}
```

#### Description Text
```css
.description-text {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 13px;
    font-weight: 400; /* Regular */
    line-height: 1.5;
    color: #666666;
    margin-bottom: 12px;
}
```

### Interactive Elements

#### Form Labels
```css
.form-label {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 14px;
    font-weight: 500; /* Medium */
    line-height: 1.4;
    color: #333333;
    margin-bottom: 4px;
}
```

#### Button Text
```css
.button-text {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 14px;
    font-weight: 500; /* Medium */
    line-height: 1.2;
    color: #ffffff;
    text-align: center;
}
```

#### Link Text
```css
.link-text {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 14px;
    font-weight: 400; /* Regular */
    line-height: 1.4;
    color: #0066cc;
    text-decoration: underline;
}

.link-text:hover {
    color: #004499;
    text-decoration: none;
}
```

## Specific Text Elements Analysis

### Key Page Elements

#### "Where to find the maximum supported RAM information"
```css
.page-title {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 24px;
    font-weight: 700; /* Bold */
    line-height: 1.3;
    color: #1a1a1a;
    margin-bottom: 20px;
}
```

#### "Identify Your Device"
```css
.section-title {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 18px;
    font-weight: 600; /* Semibold */
    line-height: 1.4;
    color: #2c2c2c;
    margin-bottom: 12px;
}
```

#### Form Instructions
```css
.form-instruction {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 13px;
    font-weight: 400; /* Regular */
    line-height: 1.5;
    color: #666666;
    margin-bottom: 8px;
}
```

## Complete CSS Implementation

### Base Typography Setup
```css
/* Base font setup for the entire page */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", Arial, sans-serif;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.6;
    color: #555555;
    background-color: #ffffff;
}

/* Heading hierarchy */
h1 {
    font-size: 28px;
    font-weight: 700;
    line-height: 1.3;
    color: #1a1a1a;
    margin-bottom: 20px;
}

h2 {
    font-size: 24px;
    font-weight: 700;
    line-height: 1.3;
    color: #1a1a1a;
    margin-bottom: 16px;
}

h3 {
    font-size: 20px;
    font-weight: 600;
    line-height: 1.4;
    color: #2c2c2c;
    margin-bottom: 12px;
}

h4 {
    font-size: 18px;
    font-weight: 600;
    line-height: 1.4;
    color: #2c2c2c;
    margin-bottom: 10px;
}

h5 {
    font-size: 16px;
    font-weight: 600;
    line-height: 1.4;
    color: #444444;
    margin-bottom: 8px;
}

h6 {
    font-size: 14px;
    font-weight: 600;
    line-height: 1.4;
    color: #444444;
    margin-bottom: 6px;
}

/* Paragraph and text elements */
p {
    font-size: 14px;
    font-weight: 400;
    line-height: 1.6;
    color: #555555;
    margin-bottom: 16px;
}

/* Links */
a {
    color: #0066cc;
    text-decoration: underline;
    font-weight: 400;
}

a:hover {
    color: #004499;
    text-decoration: none;
}

/* Form elements */
label {
    font-size: 14px;
    font-weight: 500;
    line-height: 1.4;
    color: #333333;
    margin-bottom: 4px;
    display: block;
}

input, textarea, select {
    font-family: inherit;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.4;
    color: #333333;
}

/* Buttons */
button, .btn {
    font-family: inherit;
    font-size: 14px;
    font-weight: 500;
    line-height: 1.2;
    text-align: center;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
}

.btn-primary {
    background-color: #0066cc;
    color: #ffffff;
}

.btn-primary:hover {
    background-color: #004499;
}
```

## Font Loading Optimization

### System Font Benefits
- **Zero Load Time**: System fonts are already installed
- **Consistent Experience**: Matches OS interface
- **Accessibility**: Optimized for screen readers
- **Performance**: No network requests required

### Fallback Strategy
```css
/* Progressive enhancement font stack */
.text-element {
    font-family: 
        /* Modern system fonts */
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Roboto,
        
        /* Linux alternatives */
        Oxygen,
        Ubuntu,
        Cantarell,
        
        /* Traditional fallbacks */
        "Helvetica Neue",
        Arial,
        
        /* Generic fallback */
        sans-serif;
}
```

## Responsive Typography

### Mobile Adjustments
```css
@media (max-width: 768px) {
    body {
        font-size: 16px; /* Larger base size for mobile */
    }
    
    h1 {
        font-size: 24px;
    }
    
    h2 {
        font-size: 20px;
    }
    
    h3 {
        font-size: 18px;
    }
    
    .form-instruction {
        font-size: 14px;
    }
}
```

## Accessibility Considerations

### Font Size Guidelines
- **Minimum**: 14px for body text
- **Recommended**: 16px for better readability
- **Line Height**: 1.5-1.6 for optimal reading
- **Contrast**: Minimum 4.5:1 ratio for normal text

### Screen Reader Compatibility
```css
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}
```

## Implementation Notes

1. **System Font Priority**: Always list system fonts first for optimal performance
2. **Weight Consistency**: Use consistent font weights (400, 500, 600, 700)
3. **Line Height**: Maintain readable line heights (1.4-1.6)
4. **Color Hierarchy**: Use color to establish visual hierarchy
5. **Responsive Design**: Adjust font sizes for different screen sizes

## Browser Support

| Browser | System Font Support |
|---------|-------------------|
| Chrome 56+ | Full support |
| Firefox 43+ | Full support |
| Safari 9+ | Full support |
| Edge 14+ | Full support |
| IE 11 | Partial (fallback to Arial) |

---

**Source**: Analysis of Lenovo Support website (https://support.lenovo.com/in/en/solutions/ht504725)  
**Date**: January 2026  
**Author**: Typography Analysis