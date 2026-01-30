# 🔐 LOGIN CREDENTIALS - DEV/TESTING MODE

**System:** Retail ERP Platform  
**Date:** 2025-12-22  
**Status:** ✅ VERIFIED & STANDARDIZED  
**Mode:** 🔓 DEVELOPMENT/TESTING (Passwords Visible)

---

## 📋 ACTIVE USER CREDENTIALS (5 Users)

### **1. Administrator** 👑
```o
Username: admin
Password: admin123
Email:    admin@enterprise.local
Role:     Administrator
Company:  MINDRA / RRI (can select either)
Location: Mumbai Flagship Store
```
**Access:** Full platform access, Location selector visible

---

### **2. Back Office Manager** 📊
```
Username: boadmin
Password: boadmin123
Email:    boadmin@enterprise.local
Role:     Back Office Manager
Company:  MINDRA / RRI
Location: Mumbai Flagship Store
```
**Access:** All back-office menus, Location selector visible

---

### **3. Back Office User** 📝
```
Username: bouser
Password: bouser123
Email:    bouser@enterprise.local
Role:     Back Office User
Company:  MINDRA / RRI
Location: Bangalore Flagship Store
```
**Access:** Operational back-office menus, Location selector visible

---

### **4. POS Manager** 🏪
```
Username: posadmin
Password: posadmin123
Email:    posadmin@enterprise.local
Role:     POS Manager
Company:  MINDRA / RRI
Location: Hyderabad Flagship Store
```
**Access:** Full POS menus, Location selector visible

---

### **5. POS User** 💳
```
Username: posuser
Password: posuser123
Email:    posuser@enterprise.local
Role:     POS User
Company:  MINDRA / RRI
Location: Chennai Flagship Store
```
**Access:** POS execution menus, Location selector **HIDDEN** (auto-assigned)

---

## 🏢 AVAILABLE COMPANIES AT LOGIN

| Code | Company Name | Legal Entity Type |
|------|-------------|-------------------|
| **MINDRA** | Mindra Retail Pvt Ltd | Private Limited |
| **RRI** | Refined Retail Inc | Private Limited |

---

## 🌐 LOGIN URLS

- **Frontend:** `http://localhost:5173/login`
- **Backend Admin:** `http://localhost:8000/admin`

---

## ✅ PASSWORD PATTERN

All passwords follow the pattern: `<username>123`

| Username | Password |
|----------|----------|
| admin | admin123 |
| boadmin | boadmin123 |
| bouser | bouser123 |
| posadmin | posadmin123 |
| posuser | posuser123 |

---

## 🧪 QUICK TEST CREDENTIALS

**Recommended test user:** 

```
Username: admin
Password: admin123
Company:  MINDRA (or RRI)
```

**Login Flow:**
1. Navigate to `http://localhost:5173/login`
2. Select Company: **MINDRA** or **RRI**
3. Enter username: `admin`
4. Enter password: `admin123`
5. Click "Authenticate Session"
6. **Expected:** Location selection modal appears
7. Select "Mumbai Flagship Store"
8. **Expected:** Navigate to dashboard

---

## 📊 USER DISTRIBUTION BY COMPANY

**Note:** All users can log in to either MINDRA or RRI.  
Location assignments are per Operating Company (internal).

---

## 🔄 PASSWORD RESET (If Needed)

```bash
# Run the password standardization script
python set_passwords.py

# Or manually via Django shell
python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(username='admin')
>>> user.set_password('admin123')
>>> user.save()
```

---

## ⚠️ SECURITY WARNING

**🔓 DEVELOPMENT MODE ONLY**

These credentials are for **development and testing only**.  
**DO NOT use these passwords in production!**

For production:
- Use strong, unique passwords
- Enable 2FA/MFA
- Implement password policies
- Rotate credentials regularly

---

**Last Updated:** 2025-12-22 22:29 IST  
**Passwords Verified:** ✅ All 5 users  
**Login Ready:** ✅ Yes  
**Mode:** 🔓 DEV/TESTING



