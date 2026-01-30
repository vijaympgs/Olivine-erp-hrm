# Screen: Backup & Recovery

**Sidebar Path**: System Administration > Backup & Recovery  
**URL**: `/admin/backup`  
**Component**: `BackupRecoveryPage.tsx`

---

## Purpose

Backup & Recovery manages system data protection:
- Manual and scheduled backups
- Backup history and management
- Point-in-time recovery
- Data export/import
- Disaster recovery procedures

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `admin.backup.manage` permission | Yes |
| Backup storage configured | System config |

---

## Scenarios

### SC-BACKUP-001: View Backup Dashboard

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/admin/backup` | Dashboard loads |
| 2 | Verify sections | Recent backups, Schedule, Storage |
| 3 | Verify status | Last backup info, next scheduled |

---

### SC-BACKUP-002: Create Manual Backup

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Backup Now" | Backup dialog |
| 2 | Select type | Full/Incremental |
| 3 | Enter description | "Pre-upgrade backup" |
| 4 | Start | Progress indicator |
| 5 | Complete | Backup in list |

---

### SC-BACKUP-003: Schedule Automatic Backup

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Schedule | Schedule settings |
| 2 | Set frequency | Daily |
| 3 | Set time | 02:00 AM |
| 4 | Set retention | 30 days |
| 5 | Save | Schedule active |

---

### SC-BACKUP-004: View Backup History

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click History tab | Backup list |
| 2 | Verify columns | Date, Type, Size, Status |
| 3 | Verify details | Expandable rows |

---

### SC-BACKUP-005: Download Backup

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select backup | From list |
| 2 | Click Download | File download |
| 3 | Verify | Encrypted backup file |

---

### SC-BACKUP-006: Delete Old Backup

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select old backup | Past retention |
| 2 | Click Delete | Confirmation |
| 3 | Confirm | Backup removed |

---

### SC-BACKUP-007: Restore from Backup

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select backup | Valid backup |
| 2 | Click Restore | Restore wizard |
| 3 | Select target | Full/Selective |
| 4 | Confirm | Restore initiated |
| 5 | Complete | Data restored |

**⚠️ CAUTION**: This replaces current data

---

### SC-BACKUP-008: Selective Restore

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select backup | Valid backup |
| 2 | Click Restore | Wizard |
| 3 | Select "Selective" | Options |
| 4 | Choose modules | e.g., Item Master only |
| 5 | Restore | Only selected data |

---

### SC-BACKUP-009: Point-in-Time Recovery

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Point-in-Time" | Recovery wizard |
| 2 | Select date/time | Specific moment |
| 3 | Preview | Affected records |
| 4 | Recover | Data restored to point |

---

### SC-BACKUP-010: Verify Backup Integrity

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select backup | Any backup |
| 2 | Click Verify | Integrity check |
| 3 | Results | Checksum verified |

---

### SC-BACKUP-011: Export Data

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Export | Export wizard |
| 2 | Select data | Modules/tables |
| 3 | Select format | CSV/JSON/SQL |
| 4 | Export | File downloaded |

---

### SC-BACKUP-012: Import Data

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Import | Import wizard |
| 2 | Upload file | Valid format |
| 3 | Map fields | If needed |
| 4 | Validate | Pre-import check |
| 5 | Import | Data imported |

---

### SC-BACKUP-013: Storage Configuration

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Settings | Storage config |
| 2 | Configure location | Local/S3/Azure |
| 3 | Set credentials | If cloud |
| 4 | Test connection | Success |
| 5 | Save | Storage configured |

---

### SC-BACKUP-014: Backup Notifications

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Notifications | Settings |
| 2 | Enable email alerts | Toggle ON |
| 3 | Set recipients | Admin emails |
| 4 | Alert on | Success/Failure |
| 5 | Save | Notifications active |

---

### SC-BACKUP-015: View Storage Usage

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | View Storage panel | Dashboard |
| 2 | Verify | Used/Available space |
| 3 | Trend | Growth over time |

---

**Scenario Count**: 15  
**Automation Ready**: Partial (some require manual verification)  
**Last Updated**: 2026-01-25
