# Screen: Layout Settings

**Sidebar Path**: System Administration > Layout Settings  
**URL**: `/admin/layout-settings`  
**Component**: `LayoutSettingsPage.tsx`

---

## Purpose

Layout Settings controls global UI configuration including:
- Theme and appearance
- Sidebar behavior
- Dashboard widgets
- **Test Console Module Visibility** (NEW)
- Localization preferences
- Print templates

---

## Feature: Test Console Module Visibility

### Configuration Options

| Module | Setting Key | Default | Description |
|--------|-------------|---------|-------------|
| **Retail** | `testConsole.modules.retail` | **ON** | Show Retail in Test Console |
| **HRM** | `testConsole.modules.hrm` | OFF | Show HRM in Test Console |
| **CRM** | `testConsole.modules.crm` | OFF | Show CRM in Test Console |
| **FMS** | `testConsole.modules.fms` | OFF | Show FMS in Test Console |
| **Meet** | `testConsole.modules.meet` | OFF | Show Meet in Test Console |

### UI Wireframe

```
┌─────────────────────────────────────────────────────────────────────┐
│ Layout Settings                                    [Save] [Cancel]   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ▼ Theme & Appearance                                                │
│    • Theme Mode: [System ▼] [Light] [Dark]                          │
│    • Primary Color: [#1976d2] ●                                      │
│    • Font Size: [Medium ▼]                                           │
│                                                                      │
│  ▼ Sidebar Configuration                                             │
│    • Sidebar Mode: [Expanded ▼] [Compact] [Icons Only]              │
│    • Show Subtitles: [ON ●─────]                                    │
│    • Pin Sidebar: [ON ●─────]                                       │
│                                                                      │
│  ▼ Test Console Module Visibility                                    │
│    ┌─────────────────────────────────────────────────────────────┐  │
│    │                                                              │  │
│    │  Control which modules appear in the Test Console Explorer  │  │
│    │  ℹ️ System Administration is always visible                  │  │
│    │                                                              │  │
│    │  ☑ Retail                              [ON] ●────────       │  │
│    │    📦 Merchandising, Inventory, POS, Procurement, Sales     │  │
│    │                                                              │  │
│    │  ☐ HRM                                 [OFF] ────────●      │  │
│    │    👥 Employees, Payroll, Attendance, Leave                 │  │
│    │                                                              │  │
│    │  ☐ CRM                                 [OFF] ────────●      │  │
│    │    🎯 Leads, Opportunities, Campaigns, Tickets              │  │
│    │                                                              │  │
│    │  ☐ FMS                                 [OFF] ────────●      │  │
│    │    💰 General Ledger, AP/AR, Banking, Reports               │  │
│    │                                                              │  │
│    │  ☐ Meet                                [OFF] ────────●      │  │
│    │    📅 Meetings, Calendar, Video Calls                       │  │
│    │                                                              │  │
│    └─────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ▼ Dashboard Widgets                                                 │
│    • Show Quick Stats: [ON ●─────]                                  │
│    • Show Recent Activity: [ON ●─────]                              │
│    • Widget Order: [Drag to reorder]                                │
│                                                                      │
│  ▼ Localization                                                      │
│    • Language: [English ▼]                                           │
│    • Date Format: [DD-MM-YYYY ▼]                                     │
│    • Time Format: [12-hour ▼]                                        │
│    • Currency Display: [Symbol ▼]                                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `admin.layout.edit` permission | Yes |

---

## Scenarios

### SC-LAYOUT-001: View Layout Settings

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/admin/layout-settings` | Page loads |
| 2 | Verify sections | All sections visible |

---

### SC-LAYOUT-002: Change Theme Mode

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Theme section | Expand |
| 2 | Select "Dark" | Theme switches |
| 3 | Save | Setting persisted |
| 4 | Reload | Dark theme active |

---

### SC-LAYOUT-003: Configure Sidebar Mode

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Sidebar section | Expand |
| 2 | Select "Compact" | UI updates |
| 3 | Save | Setting persisted |

---

### SC-LAYOUT-004: Enable Test Console Module

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Test Console section | Expand |
| 2 | Toggle HRM to ON | Toggle switches |
| 3 | Save | Settings saved |
| 4 | Navigate to Test Console | `/test-console` |
| 5 | Verify | HRM visible in explorer |

---

### SC-LAYOUT-005: Disable Test Console Module

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Test Console section | Expand |
| 2 | Toggle Retail to OFF | Toggle switches |
| 3 | Save | Settings saved |
| 4 | Navigate to Test Console | Explorer loads |
| 5 | Verify | Retail NOT in tree |

---

### SC-LAYOUT-006: Default Module State

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Fresh installation | Default state |
| 2 | Check Test Console | Only Retail active |
| 3 | Verify | HRM, CRM, FMS, Meet = OFF |

---

### SC-LAYOUT-007: System Admin Always Visible

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Disable all modules | All OFF |
| 2 | Check Test Console | System Admin visible |
| 3 | Verify | Cannot toggle System Admin |

---

### SC-LAYOUT-008: Configure Dashboard Widgets

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Dashboard section | Expand |
| 2 | Toggle widgets | ON/OFF |
| 3 | Drag to reorder | Order changes |
| 4 | Save | Layout saved |
| 5 | View Dashboard | Widgets per config |

---

### SC-LAYOUT-009: Change Date Format

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Localization | Expand |
| 2 | Select DD/MM/YYYY | Format selected |
| 3 | Save | Setting saved |
| 4 | Verify | Dates in new format |

---

### SC-LAYOUT-010: Change Language

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Localization | Expand |
| 2 | Select language | If available |
| 3 | Save | Setting saved |
| 4 | Reload | UI in new language |

---

### SC-LAYOUT-011: Reset to Defaults

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Reset to Defaults" | Confirmation |
| 2 | Confirm | All settings reset |
| 3 | Verify | Default values restored |

---

### SC-LAYOUT-012: Cancel Without Saving

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Make changes | Various settings |
| 2 | Click Cancel | Confirmation |
| 3 | Confirm | Changes discarded |
| 4 | Reopen | Original values |

---

### SC-LAYOUT-013: Persist Across Sessions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Set configuration | Various settings |
| 2 | Save and logout | Session ends |
| 3 | Login again | New session |
| 4 | Verify | Settings preserved |

---

### SC-LAYOUT-014: Per-User Settings

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Login as User A | Configure theme |
| 2 | Login as User B | Different theme |
| 3 | Verify | Each user has own settings |

---

## API Specification

### Endpoints

```
GET  /api/admin/layout-settings/
POST /api/admin/layout-settings/
```

### Payload Structure

```json
{
  "theme": {
    "mode": "system",
    "primaryColor": "#1976d2",
    "fontSize": "medium"
  },
  "sidebar": {
    "mode": "expanded",
    "showSubtitles": true,
    "pinned": true
  },
  "testConsole": {
    "modules": {
      "retail": true,
      "hrm": false,
      "crm": false,
      "fms": false,
      "meet": false
    }
  },
  "dashboard": {
    "quickStats": true,
    "recentActivity": true,
    "widgetOrder": ["stats", "activity", "alerts"]
  },
  "localization": {
    "language": "en",
    "dateFormat": "DD-MM-YYYY",
    "timeFormat": "12h",
    "currencyDisplay": "symbol"
  }
}
```

---

**Scenario Count**: 14  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
