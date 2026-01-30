OLIVINE TYPOGRAPHY RULES (AUTHORITATIVE)

1. FONT FAMILY
- Primary font: Inter
- Fallbacks:
  'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
- Only ONE font family is allowed across the application.
- No per-component or per-module font overrides.

2. FONT WEIGHTS (STRICT)
- Regular: 400
- Medium: 500
- Semibold: 600
- Do NOT use 300, 700, or higher.
- Bold text must be rare and intentional.

3. FONT SIZES (ERP-OPTIMIZED SCALE)
- Page Title: 20–22px (600)
- Section Title: 14–15px (600)
- Body Text: 13–14px (400)
- Form Label: 12–13px (500)
- Helper / Subtitle Text: 12px (400)
- Table Text: 13px (400)

4. LINE HEIGHTS
- Titles: 1.2
- Body & Labels: 1.4
- Helper / Subtitle Text: 1.5
- Line-height must never be below 1.4 for body text.

5. SIDEBAR TYPOGRAPHY
- Section Header:
  - 12px, 600, line-height 1.4
- Menu Item Label:
  - 13–14px, 500, line-height 1.4
- Menu Item Subtitle:
  - 12px, 400, line-height 1.5
- Label and subtitle MUST be aligned on the same left text axis.
- Label and subtitle MUST live in the same text container.
- Subtitle must start directly under the label text, not under icons.

6. FORMS (EMPLOYEE, MASTER FORMS)
- Section Title:
  - 14–15px, 600
- Field Label:
  - 12–13px, 500
- Input Text:
  - 13–14px, 400
- Helper / Error Text:
  - 12px, 400
- Inputs must NOT be bold.
- Helper text must NOT be smaller than 12px.

7. TABLES & NUMERIC DATA
- Table Header:
  - 12px, 600
- Table Cell Text:
  - 13px, 400
- Numeric columns must use tabular numerals.
- Enable:
  font-feature-settings: "tnum";
- Tables must feel visually quieter than forms.

8. SPACING & RHYTHM
- Maintain consistent vertical spacing between:
  - Label → Input
  - Label → Subtitle
- No arbitrary spacing per component.
- Typography rhythm must be consistent across modules.

9. ACCESSIBILITY & TONE
- Avoid overly light gray text for subtitles.
- No italics for helper text.
- Typography must remain readable for long working hours.

10. NON-NEGOTIABLE RULE
- Typography is token-driven, not component-driven.
- Any deviation must update the typography tokens first.


/* =========================================================
   OLIVINE TYPOGRAPHY DESIGN TOKENS (AUTHORITATIVE)
   ========================================================= */

/* ---------- CSS VARIABLES (GLOBAL) ---------- */
:root {
  /* Font Family */
  --font-family-primary: 'Inter', system-ui, -apple-system,
    BlinkMacSystemFont, 'Segoe UI', sans-serif;

  /* Font Weights */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;

  /* Font Sizes */
  --font-size-page-title: 20px;
  --font-size-section-title: 14px;
  --font-size-body: 13px;
  --font-size-label: 12px;
  --font-size-helper: 12px;
  --font-size-table: 13px;

  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-normal: 1.4;
  --line-height-relaxed: 1.5;

  /* Letter Spacing */
  --letter-spacing-normal: 0;
}

/* ---------- GLOBAL BASE ---------- */
body {
  font-family: var(--font-family-primary);
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
}

/* ---------- SIDEBAR ---------- */
.sidebar-section-title {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-normal);
}

.sidebar-item-label {
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-normal);
}

.sidebar-item-subtitle {
  font-size: var(--font-size-helper);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-relaxed);
}

/* ---------- FORMS ---------- */
.form-section-title {
  font-size: var(--font-size-section-title);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-tight);
}

.form-label {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-normal);
}

.form-input,
.form-select,
.form-textarea {
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
}

.form-helper-text,
.form-error-text {
  font-size: var(--font-size-helper);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-relaxed);
}

/* ---------- TABLES ---------- */
.table-header {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-normal);
}

.table-cell {
  font-size: var(--font-size-table);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
  font-feature-settings: "tnum";
}

/* =========================================================
   TYPESCRIPT TOKENS (for React / MUI / Design System)
   ========================================================= */

export const typographyTokens = {
  fontFamily: {
    primary:
      "'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
  },

  fontWeight: {
    regular: 400,
    medium: 500,
    semibold: 600,
  },

  fontSize: {
    pageTitle: "20px",
    sectionTitle: "14px",
    body: "13px",
    label: "12px",
    helper: "12px",
    table: "13px",
  },

  lineHeight: {
    tight: 1.2,
    normal: 1.4,
    relaxed: 1.5,
  },

  numeric: {
    fontFeatureSettings: "tnum",
  },
};

/* =========================================================
   NON-NEGOTIABLE RULE
   =========================================================
   - Components must consume these tokens.
   - No hardcoded font sizes, weights, or families.
   - Any typography change must update tokens first.
   ========================================================= */
