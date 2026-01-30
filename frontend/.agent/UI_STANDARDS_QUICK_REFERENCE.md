# Quick Reference: Using Centralized UI Standards

## For Developers: How to Use the New System

### 1. Typography in Components

#### ❌ OLD WAY (Hardcoded):
```tsx
<h1 className="text-2xl font-bold text-gray-900">Page Title</h1>
<h2 className="text-lg font-semibold text-gray-800">Section Header</h2>
<label className="text-sm font-medium text-gray-700">Form Label</label>
<p className="text-xs text-gray-600">Body text</p>
```

#### ✅ NEW WAY (Centralized):
```tsx
<h1 style={{
  fontSize: 'var(--typography-l1-size)',
  fontWeight: 'var(--typography-l1-weight)',
  color: 'var(--typography-l1-color)',
  lineHeight: 'var(--typography-l1-line-height)',
  letterSpacing: 'var(--typography-l1-letter-spacing)'
}}>Page Title</h1>

<h2 style={{
  fontSize: 'var(--typography-l2-size)',
  fontWeight: 'var(--typography-l2-weight)',
  color: 'var(--typography-l2-color)'
}}>Section Header</h2>

<label style={{
  fontSize: 'var(--form-label-size)',
  fontWeight: 'var(--form-label-weight)',
  color: 'var(--form-label-color)'
}}>Form Label</label>

<p style={{
  fontSize: 'var(--typography-l4-size)',
  fontWeight: 'var(--typography-l4-weight)',
  color: 'var(--typography-l4-color)'
}}>Body text</p>
```

### 2. Modals

#### ❌ OLD WAY:
```tsx
<div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50">
  <div className="bg-white rounded-lg shadow-xl max-w-4xl p-6">
    Modal content
  </div>
</div>
```

#### ✅ NEW WAY:
```tsx
<div 
  className="fixed inset-0 flex items-center justify-center"
  style={{
    backgroundColor: 'var(--modal-backdrop)',
    backdropFilter: `blur(var(--modal-backdrop-blur))`,
    zIndex: 'var(--modal-z-index)'
  }}
>
  <div style={{
    backgroundColor: 'var(--modal-bg)',
    borderColor: 'var(--modal-border)',
    borderRadius: 'var(--modal-border-radius)',
    maxWidth: 'var(--modal-max-width)',
    padding: 'var(--modal-padding)',
    boxShadow: `var(--modal-shadow)`
  }}>
    Modal content
  </div>
</div>
```

### 3. Form Fields

#### ✅ STANDARD PATTERN:
```tsx
<div className="space-y-1">
  {/* Label - uses formLabel variables */}
  <label 
    htmlFor="field-id"
    style={{
      fontSize: 'var(--form-label-size)',
      fontWeight: 'var(--form-label-weight)',
      color: 'var(--form-label-color)'
    }}
  >
    Field Label
  </label>
  
  {/* Input - uses formInput variables */}
  <input
    id="field-id"
    type="text"
    style={{
      fontSize: 'var(--form-input-size)',
      fontWeight: 'var(--form-input-weight)',
      color: 'var(--form-input-color)'
    }}
    className="w-full px-3 py-2 border rounded"
  />
  
  {/* Helper text - uses formHelper variables */}
  <p style={{
    fontSize: 'var(--form-helper-size)',
    fontWeight: 'var(--form-helper-weight)',
    color: 'var(--form-helper-color)'
  }}>
    Helper text here
  </p>
  
  {/* Error message - uses formError variables */}
  {error && (
    <p style={{
      fontSize: 'var(--form-error-size)',
      fontWeight: 'var(--form-error-weight)',
      color: 'var(--form-error-color-text)'
    }}>
      {error}
    </p>
  )}
</div>
```

---

## CSS Variables Reference

### Typography Hierarchy

| Level | Purpose | Default Size | Default Weight | Variable Prefix |
|-------|---------|--------------|----------------|-----------------|
| L1 | Page Titles | 24px | 700 | `--typography-l1-*` |
| L2 | Section Headers | 18px | 600 | `--typography-l2-*` |
| L3 | Subsection Headers | 14px | 600 | `--typography-l3-*` |
| L4 | Form Labels & Body | 12px | 400 | `--typography-l4-*` |

### Form-Specific Typography

| Element | Purpose | Default Size | Default Weight | Variable Prefix |
|---------|---------|--------------|----------------|-----------------|
| Label | Field labels | 12px | 500 | `--form-label-*` |
| Input | Input field text | 14px | 400 | `--form-input-*` |
| Helper | Help text | 12px | 400 | `--form-helper-*` |
| Error | Error messages | 12px | 500 | `--form-error-*` |

### Modal Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `--modal-max-width` | Maximum modal width | 90vw |
| `--modal-bg` | Background color | #FFFFFF |
| `--modal-border` | Border color | #E5E7EB |
| `--modal-border-radius` | Corner rounding | 8px |
| `--modal-backdrop` | Backdrop color | rgba(0,0,0,0.5) |
| `--modal-backdrop-blur` | Backdrop blur | 4px |
| `--modal-shadow` | Shadow intensity | xl |
| `--modal-padding` | Internal padding | 24px |
| `--modal-z-index` | Stacking order | 50 |

---

## Creating Utility Classes (Optional)

Add to `globals.css` or component-specific CSS:

```css
/* Typography Utilities */
.typography-l1 {
  font-size: var(--typography-l1-size);
  font-weight: var(--typography-l1-weight);
  color: var(--typography-l1-color);
  line-height: var(--typography-l1-line-height);
  letter-spacing: var(--typography-l1-letter-spacing);
}

.typography-l2 {
  font-size: var(--typography-l2-size);
  font-weight: var(--typography-l2-weight);
  color: var(--typography-l2-color);
  line-height: var(--typography-l2-line-height);
  letter-spacing: var(--typography-l2-letter-spacing);
}

.typography-l3 {
  font-size: var(--typography-l3-size);
  font-weight: var(--typography-l3-weight);
  color: var(--typography-l3-color);
  line-height: var(--typography-l3-line-height);
  letter-spacing: var(--typography-l3-letter-spacing);
}

.typography-l4 {
  font-size: var(--typography-l4-size);
  font-weight: var(--typography-l4-weight);
  color: var(--typography-l4-color);
  line-height: var(--typography-l4-line-height);
  letter-spacing: var(--typography-l4-letter-spacing);
}

/* Form Utilities */
.form-label {
  font-size: var(--form-label-size);
  font-weight: var(--form-label-weight);
  color: var(--form-label-color);
}

.form-input {
  font-size: var(--form-input-size);
  font-weight: var(--form-input-weight);
  color: var(--form-input-color);
}

.form-helper {
  font-size: var(--form-helper-size);
  font-weight: var(--form-helper-weight);
  color: var(--form-helper-color);
}

.form-error {
  font-size: var(--form-error-size);
  font-weight: var(--form-error-weight);
  color: var(--form-error-color-text);
}
```

Then use like:
```tsx
<h1 className="typography-l1">Page Title</h1>
<label className="form-label">Field Label</label>
<p className="typography-l4">Body text</p>
```

---

## Running UI Audit

### Method 1: Test Console (Recommended)
1. Navigate to `/test-console`
2. Select module from sidebar (e.g., "Retail")
3. Click "CSV" button in header
4. Report downloads automatically

### Method 2: Browser Console
```javascript
// Import and run
import('@utils/uiAudit').then(m => {
  // Download full report
  m.downloadUIAuditReport('Retail');
  
  // Or get statistics
  const audit = m.generateUIAudit('Retail');
  const stats = m.getAuditSummary(audit);
  console.log('Completion:', stats.completionPercentage + '%');
  console.log('Total Items:', stats.total);
  console.log('Missing:', stats.missing);
});
```

### Method 3: Programmatic
```typescript
import { 
  generateUIAudit, 
  getAuditSummary, 
  downloadUIAuditReport 
} from '@utils/uiAudit';

// In component
const handleAudit = () => {
  const auditData = generateUIAudit('Retail');
  const summary = getAuditSummary(auditData);
  
  console.log(`Total: ${summary.total}`);
  console.log(`Complete: ${summary.complete}`);
  console.log(`Missing: ${summary.missing}`);
  console.log(`Completion: ${summary.completionPercentage}%`);
  
  // Download CSV
  downloadUIAuditReport('Retail');
};
```

---

## Best Practices

### ✅ DO:
- Use CSS variables for all typography in forms and modals
- Keep modals within 90vw max-width
- Use L4 typography for all form content (except page titles)
- Run UI audit before claiming a module is "complete"
- Update Layout Settings to control global standards

### ❌ DON'T:
- Hardcode font sizes in modal or form components
- Use arbitrary Tailwind text sizes (text-sm, text-lg, etc.) in forms
- Create modals wider than viewport
- Skip the audit - it helps identify gaps

---

## Troubleshooting

### Variables not applying?
1. Check if `layoutManager.applyConfig()` has been called
2. Verify CSS variables exist: Open DevTools > Elements > :root > Computed
3. Ensure no `!important` overrides in component styles

### Modal too wide?
- Check `max-width` is using `var(--modal-max-width)`
- Default is 90vw, adjustable in Layout Settings

### Typography looks wrong?
- Verify you're using correct variable (L1/L2/L3/L4)
- Check if component has inline styles overriding
- Use browser DevTools to inspect computed values

---

*Last Updated: 2026-01-05*
