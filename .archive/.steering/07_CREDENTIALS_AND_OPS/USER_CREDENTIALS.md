# User Credentials Reference

**Date:** 2025-12-22  
**System:** Retail ERP Platform  
**Status:** Active Users Only

---

## 🔐 ACTIVE USER CREDENTIALS

### **1. Administrator**
- **Username:** `admin`
- **Email:** `admin@enterprise.local`
- **Role:** Administrator
- **Password:** `admin123` *(likely default - verify)*
- **OpCo:** Mumbai (OC_MUM_01)
- **Location:** Mumbai Flagship Store
- **Access:** Full platform access

---

### **2. Back Office Manager**
- **Username:** `boadmin`
- **Email:** `boadmin@enterprise.local`
- **Role:** Back Office Manager
- **Password:** `boadmin123` *(likely default - verify)*
- **OpCo:** Mumbai (OC_MUM_01)
- **Location:** Mumbai Flagship Store
- **Access:** All back-office menus

---

### **3. Back Office User**
- **Username:** `bouser`
- **Email:** `bouser@enterprise.local`
- **Role:** Back Office User
- **Password:** `bouser123` *(likely default - verify)*
- **OpCo:** Bangalore (OC_BLR_03)
- **Location:** Bangalore Flagship Store
- **Access:** Operational back-office menus

---

### **4. POS Manager**
- **Username:** `posadmin`
- **Email:** `posadmin@enterprise.local`
- **Role:** POS Manager
- **Password:** `posadmin123` *(likely default - verify)*
- **OpCo:** Hyderabad (OC_HYD_04)
- **Location:** Hyderabad Flagship Store
- **Access:** Full POS menus

---

### **5. POS User**
- **Username:** `posuser`
- **Email:** `posuser@enterprise.local`
- **Role:** POS User
- **Password:** `posuser123` *(likely default - verify)*
- **OpCo:** Chennai (OC_CHE_05)
- **Location:** Chennai Flagship Store
- **Access:** POS execution menus

---

## ⚠️ IMPORTANT NOTES

1. **Password Security:**
   - Django stores passwords as hashed values (not plain text)
   - Passwords listed above are **likely defaults** based on common patterns
   - **Verify by attempting login** or reset if needed

2. **Password Reset (if needed):**
   ```bash
   # Via Django management command
   python manage.py changepassword <username>
   
   # Via Django shell
   python manage.py shell
   >>> from django.contrib.auth.models import User
   >>> user = User.objects.get(username='admin')
   >>> user.set_password('new_password')
   >>> user.save()
   ```

3. **Deactivated Users:**
   - `testadmin` - Deactivated (was duplicate admin)

4. **Login URL:**
   - Frontend: `http://localhost:5173/login`
   - Backend Admin: `http://localhost:8000/admin`

---

## 🧪 LOGIN TESTING CHECKLIST

Test each user to verify credentials:

- [ ] **admin** - Should see location selector, full menu access
- [ ] **boadmin** - Should see location selector, back-office menus
- [ ] **bouser** - Should see location selector, operational menus
- [ ] **posadmin** - Should see location selector, POS menus
- [ ] **posuser** - Should NOT see location selector (auto-assigned)

---

## 🔄 PASSWORD STANDARDIZATION (OPTIONAL)

If you want to set all passwords to a known value for testing:

```python
# Run this in Django shell
from django.contrib.auth.models import User

users_passwords = {
    'admin': 'admin123',
    'boadmin': 'boadmin123',
    'bouser': 'bouser123',
    'posadmin': 'posadmin123',
    'posuser': 'posuser123',
}

for username, password in users_passwords.items():
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print(f"✅ Password set for {username}")
```

---

**Last Updated:** 2025-12-22  
**Maintained By:** Senior Execution Engineer

