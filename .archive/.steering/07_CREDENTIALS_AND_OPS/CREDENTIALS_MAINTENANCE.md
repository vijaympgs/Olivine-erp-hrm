# Standard Credentials - Maintenance Guide

**Date:** 2025-12-22  
**Status:** AUTHORITATIVE & PERMANENT

---

## 🔒 PERMANENT CREDENTIALS

These credentials are **PERMANENT** and must be maintained across all environments:

```
Username   | Password     | Role
--------------------------------------------------
admin      | admin123     | Administrator
boadmin    | boadmin123   | Back Office Manager
bouser     | bouser123    | Back Office User
posadmin   | posadmin123  | POS Manager
posuser    | posuser123   | POS User
```

---

## 📋 MAINTENANCE RULES

1. **DO NOT MODIFY** - These credentials are authoritative
2. **Pattern:** `<username>123` - Always maintain this pattern
3. **Count:** Exactly 5 users, no more, no less
4. **Restoration:** Use `set_passwords.py` if credentials are lost
5. **Reference:** See `STANDARD_CREDENTIALS.md` for full details

---

## 🔄 HOW TO RESTORE CREDENTIALS

If credentials are changed or lost, run:

```bash
python set_passwords.py
```

This will:
- Reset all 5 users to standard passwords
- Verify all users exist
- Confirm credentials are correct

---

## ✅ VERIFICATION

To verify credentials are correct:

```bash
# Quick verification
python set_passwords.py

# Expected output:
# ✅ admin        → Password set to: admin123
# ✅ boadmin      → Password set to: boadmin123
# ✅ bouser       → Password set to: bouser123
# ✅ posadmin     → Password set to: posadmin123
# ✅ posuser      → Password set to: posuser123
# ✅ ALL STANDARD CREDENTIALS VERIFIED
```

---

## 📁 RELATED DOCUMENTATION

1. **STANDARD_CREDENTIALS.md** - Authoritative reference
2. **LOGIN_CREDENTIALS.md** - Full login guide with companies
3. **QUICK_LOGIN_REFERENCE.txt** - ASCII quick reference card
4. **README.md** - Quick credentials table at top
5. **set_passwords.py** - Password restoration script

---

## 🏢 COMPANIES

Users can log in to either company:
- **MINDRA** - Mindra Retail Pvt Ltd
- **RRI** - Refined Retail Inc

---

## ⚠️ IMPORTANT NOTES

### For Development/Testing:
- ✅ Use these credentials as-is
- ✅ Pattern is simple for easy testing
- ✅ All passwords are documented

### For Production:
- ⚠️ Change passwords to strong, unique values
- ⚠️ Maintain usernames and roles
- ⚠️ Implement 2FA/MFA
- ⚠️ Use password rotation policies

---

## 🔧 TROUBLESHOOTING

### Problem: User can't log in
**Solution:** Run `python set_passwords.py` to reset credentials

### Problem: Wrong number of users
**Solution:** Run `python normalize_users_roles.py` to restore 5 users

### Problem: Credentials changed accidentally
**Solution:** Run `python set_passwords.py` - credentials are restored from code

---

**Maintained By:** Platform Team  
**Last Verified:** 2025-12-22  
**Status:** ✅ ACTIVE & VERIFIED
