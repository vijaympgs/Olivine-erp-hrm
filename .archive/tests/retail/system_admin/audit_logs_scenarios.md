# Screen: Audit Logs

**Sidebar Path**: System Administration > Audit Logs  
**URL**: `/admin/audit-logs`  
**Component**: `AuditLogsPage.tsx`

---

## Purpose

Audit Logs provides complete system activity tracking:
- User login/logout events
- Data modification history
- Permission changes
- Security events
- System configuration changes
- API access logs

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `admin.audit.view` permission | Yes |
| Audit logging enabled | System config |

---

## Scenarios

### SC-AUDIT-001: View Audit Log List

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/admin/audit-logs` | Log list loads |
| 2 | Verify columns | Timestamp, User, Action, Entity, IP |
| 3 | Verify sorting | Default: newest first |

---

### SC-AUDIT-002: Filter by Date Range

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click date filter | Date picker |
| 2 | Set From | 7 days ago |
| 3 | Set To | Today |
| 4 | Apply | Filtered results |

---

### SC-AUDIT-003: Filter by User

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click User filter | User picker |
| 2 | Select user | Specific user |
| 3 | Apply | Only that user's logs |

---

### SC-AUDIT-004: Filter by Action Type

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Action filter | Dropdown |
| 2 | Select "LOGIN" | Login events |
| 3 | Select "CREATE" | Create events |
| 4 | Select "DELETE" | Delete events |

---

### SC-AUDIT-005: Filter by Entity/Module

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Entity filter | Dropdown |
| 2 | Select "Item Master" | Item changes only |
| 3 | Select "Purchase Order" | PO changes only |

---

### SC-AUDIT-006: View Log Details

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click log entry | Row selected |
| 2 | Details panel | Expanded view |
| 3 | Verify content | Before/After values, full metadata |

---

### SC-AUDIT-007: View Before/After Changes

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select UPDATE event | Modification log |
| 2 | View details | Diff view |
| 3 | Verify | Old value vs New value |

---

### SC-AUDIT-008: Search Logs

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter search term | "SKU-001" |
| 2 | Search | Logs mentioning term |

---

### SC-AUDIT-009: Export Audit Logs

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Set filters | Specific range/user |
| 2 | Click Export | Export dialog |
| 3 | Select CSV | Format |
| 4 | Download | Filtered logs exported |

---

### SC-AUDIT-010: View Login History

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Filter Action = "LOGIN" | Login events |
| 2 | Verify content | User, Time, IP, Status |
| 3 | Include failures | Failed login attempts |

---

### SC-AUDIT-011: View Failed Logins

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Filter Action = "LOGIN_FAILED" | Failed attempts |
| 2 | Verify | Username, IP, Reason |

---

### SC-AUDIT-012: Track Sensitive Data Access

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Filter Entity = "Salary" or "PII" | Sensitive access |
| 2 | Verify | Who viewed what, when |

---

### SC-AUDIT-013: Real-time Log Streaming

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enable Live View | Toggle |
| 2 | Perform action | In another tab |
| 3 | Verify | Entry appears without refresh |

---

### SC-AUDIT-014: Pagination

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify page controls | Page numbers, arrows |
| 2 | Set page size | 50/100/500 |
| 3 | Navigate | Pages load correctly |

---

### SC-AUDIT-015: Retention Policy Display

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | View retention info | Settings area |
| 2 | Verify | "Logs retained for X days" |

---

**Scenario Count**: 15  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
