# Screen: Security Settings

**Sidebar Path**: System Administration > Security Settings  
**URL**: `/admin/security`  
**Component**: `SecuritySettingsPage.tsx`

---

## Purpose

Security Settings configures system-wide security policies:
- Password policies
- Session management
- Two-factor authentication (2FA)
- IP whitelisting/blacklisting
- Login attempt limits
- API security

---

## Preconditions

| Prerequisite | Required |
|--------------|----------|
| User has `admin.security.manage` permission | Yes |

---

## Scenarios

### SC-SEC-001: View Security Settings

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `/admin/security` | Page loads |
| 2 | Verify sections | Password, Session, 2FA, IP, API |

---

### SC-SEC-002: Configure Password Policy

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Password Policy section | Expand |
| 2 | Set minimum length | 8 |
| 3 | Require uppercase | ON |
| 4 | Require number | ON |
| 5 | Require special char | ON |
| 6 | Save | Policy saved |

---

### SC-SEC-003: Set Password Expiry

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Password section | Expand |
| 2 | Enable password expiry | Toggle ON |
| 3 | Set expiry days | 90 |
| 4 | Set warning days | 7 |
| 5 | Save | Settings saved |

---

### SC-SEC-004: Password History

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Enable password history | Toggle ON |
| 2 | Set history count | 5 |
| 3 | Save | Cannot reuse last 5 passwords |

---

### SC-SEC-005: Configure Session Timeout

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Session section | Expand |
| 2 | Set idle timeout | 30 minutes |
| 3 | Set absolute timeout | 8 hours |
| 4 | Save | Settings saved |

---

### SC-SEC-006: Configure Concurrent Sessions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Session section | Expand |
| 2 | Set max concurrent | 1 |
| 3 | Save | Only 1 session allowed |
| 4 | Test | Second login kicks first |

---

### SC-SEC-007: Enable Two-Factor Auth

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open 2FA section | Expand |
| 2 | Enable 2FA | Toggle ON |
| 3 | Select method | TOTP/SMS/Email |
| 4 | Save | 2FA enabled |

---

### SC-SEC-008: Configure 2FA for Roles

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | 2FA section | Settings |
| 2 | Enable "Require for admins" | Toggle ON |
| 3 | Save | Admins must use 2FA |

---

### SC-SEC-009: Set Login Attempt Limits

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Login section | Expand |
| 2 | Set max attempts | 5 |
| 3 | Set lockout duration | 15 minutes |
| 4 | Save | Policy active |

---

### SC-SEC-010: IP Whitelist

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open IP Access section | Expand |
| 2 | Enable whitelist | Toggle ON |
| 3 | Add IP | 192.168.1.0/24 |
| 4 | Save | Only whitelisted IPs |

---

### SC-SEC-011: IP Blacklist

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open IP Access section | Expand |
| 2 | Add to blacklist | 10.0.0.5 |
| 3 | Save | IP blocked |

---

### SC-SEC-012: API Security Settings

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open API section | Expand |
| 2 | Enable API key auth | Toggle ON |
| 3 | Set rate limit | 1000/hour |
| 4 | Save | API protected |

---

### SC-SEC-013: Generate API Key

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | API section | Expand |
| 2 | Click Generate Key | Key dialog |
| 3 | Set name | "Integration Key" |
| 4 | Set permissions | Select scopes |
| 5 | Generate | Key displayed once |

---

### SC-SEC-014: Revoke API Key

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | View API keys | List |
| 2 | Select key | Existing key |
| 3 | Click Revoke | Confirmation |
| 4 | Confirm | Key disabled |

---

### SC-SEC-015: Security Audit

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Security Audit" | Audit report |
| 2 | Verify sections | Weak passwords, inactive users, etc. |
| 3 | Recommendations | Actionable items |

---

**Scenario Count**: 15  
**Automation Ready**: Yes  
**Last Updated**: 2026-01-25
