# STANDARD USER CREDENTIALS - PERMANENT REFERENCE

**AUTHORITATIVE SOURCE - DO NOT MODIFY**

This file defines the standard user credentials that MUST be maintained across all environments.

---

## 🔒 STANDARD CREDENTIALS (PERMANENT)

| Username | Password     | Role                |
|----------|--------------|---------------------|
| admin    | admin123     | Administrator       |
| boadmin  | boadmin123   | Back Office Manager |
| bouser   | bouser123    | Back Office User    |
| posadmin | posadmin123  | POS Manager         |
| posuser  | posuser123   | POS User            |

---

## 📋 RULES

1. **These credentials are PERMANENT** - Do not change usernames or password pattern
2. **Pattern:** `<username>123` - Always maintain this pattern
3. **5 Users Only** - Exactly these 5 users, no more, no less
4. **Seeding:** Use `set_passwords.py` to restore these credentials if needed
5. **Testing:** These credentials are for development and testing
6. **Production:** In production, change passwords but maintain usernames and roles

---

## 🔄 RESTORATION

If credentials are lost or changed, run:

```bash
python set_passwords.py
```

This will restore all 5 users to the standard credentials above.

---

## ✅ VERIFICATION

To verify credentials are correct:

```bash
python manage.py shell -c "from django.contrib.auth.models import User; from domain.user_management.models import UserRole; [(print(f'{u.username:10} | {\"<password>\":12} | {UserRole.objects.filter(user=u, is_active=True).first().role.role_name if UserRole.objects.filter(user=u, is_active=True).exists() else \"No role\"}')) for u in User.objects.filter(is_active=True).order_by('username')]"
```

---

**Last Updated:** 2025-12-22  
**Status:** AUTHORITATIVE  
**Maintained By:** Platform Team
