# Screen: File Search Explorer

**Sidebar Path**: System Administration > File Search Explorer  
**URL**: `/admin/file-explorer`  
**Component**: `FileSearchExplorerPage.tsx`

---

## Purpose

File Search Explorer provides system-wide search and management for:
- Document search across modules
- File attachment management
- Report archive browsing
- Template management
- Import/Export file history

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `admin.files.view` permission | Yes |
| Index service running | For search |

---

## Scenarios

### SC-FSE-001: Open File Explorer

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/admin/file-explorer` | Page loads |
| 2 | Verify panels | Folder tree + File list + Preview |
| 3 | Verify search bar | Global search available |

---

### SC-FSE-002: Browse Folder Structure

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | View folder tree | Hierarchical view |
| 2 | Expand "Reports" | Sub-folders visible |
| 3 | Click folder | Contents shown in file list |

---

### SC-FSE-003: Search Files by Name

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enter search term | "invoice" |
| 2 | Press Enter | Results filtered |
| 3 | Verify results | Files containing "invoice" |

---

### SC-FSE-004: Search with Filters

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click Advanced | Filter panel |
| 2 | Select file type | PDF |
| 3 | Set date range | Last 30 days |
| 4 | Search | Filtered results |

---

### SC-FSE-005: Preview File

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select file | PDF or image |
| 2 | Preview panel | Content displayed |
| 3 | For PDF | Paginated preview |

---

### SC-FSE-006: Download File

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select file | Any file |
| 2 | Click Download | File downloads |
| 3 | Verify | File intact |

---

### SC-FSE-007: Download Multiple Files

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select multiple | Ctrl+click |
| 2 | Click Download | ZIP download |
| 3 | Verify | All files in ZIP |

---

### SC-FSE-008: Upload File

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to folder | Target location |
| 2 | Click Upload | File dialog |
| 3 | Select file | Local file |
| 4 | Upload | File appears in list |

---

### SC-FSE-009: Delete File

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select file | Deletable file |
| 2 | Click Delete | Confirmation |
| 3 | Confirm | File removed |

---

### SC-FSE-010: Cannot Delete System Files

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select system file | Protected file |
| 2 | Delete button | Disabled |
| 3 | Or attempt | Error: Protected |

---

### SC-FSE-011: Create Folder

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select parent folder | Location |
| 2 | Click "New Folder" | Name dialog |
| 3 | Enter name | "Archives" |
| 4 | Create | Folder appears |

---

### SC-FSE-012: Rename File

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select file | User file |
| 2 | Click Rename | In-place edit |
| 3 | Enter new name | New name |
| 4 | Save | File renamed |

---

### SC-FSE-013: Move File

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select file | Source file |
| 2 | Drag to folder | OR use Move |
| 3 | Drop | File in new location |

---

### SC-FSE-014: Copy File

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Select file | Source file |
| 2 | Click Copy | Copy action |
| 3 | Navigate to target | Destination folder |
| 4 | Paste | File copied |

---

### SC-FSE-015: View File Properties

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Right-click file | Context menu |
| 2 | Click Properties | Properties dialog |
| 3 | Verify | Name, size, type, created, modified |

---

### SC-FSE-016: Search by File Content

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enable content search | Toggle |
| 2 | Search term | Text inside file |
| 3 | Results | Files containing text |

---

**Scenario Count**: 16  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
