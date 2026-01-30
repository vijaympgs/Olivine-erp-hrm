# DJANGO COMMAND PERMANENT FIX

**Agent**: Hindra (HRM Domain Owner)  
**Date**: January 30, 2026  
**Purpose**: Permanent fix for Django manage.py command execution

---

## PROBLEM

When running Django commands with `cd backend && python manage.py check`, the system looks for:
```
d:\olvine-erp\manage.py
```

Instead of:
```
d:\olvine-erp\backend\manage.py
```

This causes the error:
```
python: can't open file 'd:\\olvine-erp\\manage.py': [Errno 2] No such file or directory
```

---

## PERMANENT FIX

**ALWAYS use the full path to manage.py:**

```bash
# ❌ WRONG - This will fail
cd backend && python manage.py check

# ✅ CORRECT - Use full path
python backend/manage.py check
```

---

## STANDARD DJANGO COMMANDS

### System Checks
```bash
python backend/manage.py check
python backend/manage.py check --deploy
```

### Database Migrations
```bash
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py showmigrations
python backend/manage.py sqlmigrate app_name migration_number
```

### Create Superuser
```bash
python backend/manage.py createsuperuser
```

### Shell
```bash
python backend/manage.py shell
```

### Collect Static Files
```bash
python backend/manage.py collectstatic
```

### Run Server
```bash
python backend/manage.py runserver
python backend/manage.py runserver 8000
python backend/manage.py runserver 0.0.0.0:8000
```

---

## IMPORTANT NOTES

1. **Never use `cd backend`** - The directory change doesn't persist in the command execution context
2. **Always use full path** - `python backend/manage.py [command]`
3. **Working directory is always `d:\olvine-erp`** - This is the current working directory
4. **manage.py is in `backend/` folder** - Always reference it as `backend/manage.py`

---

## EXAMPLES

### Check Django System
```bash
python backend/manage.py check
```

### Run Migrations
```bash
python backend/manage.py makemigrations
python backend/manage.py migrate
```

### Create Admin User
```bash
python backend/manage.py createsuperuser
```

### Start Development Server
```bash
python backend/manage.py runserver
```

---

## WHY THIS HAPPENS

The `cd` command in Windows doesn't persist the directory change when used in command chaining with `&&`. The working directory remains `d:\olvine-erp` for the entire command execution, so Python looks for `manage.py` in the root directory instead of the `backend/` directory.

By using the full path `backend/manage.py`, we explicitly tell Python where to find the file, regardless of the working directory.

---

## PERMANENT SOLUTION

**Memorize this pattern:**
```bash
python backend/manage.py [command]
```

Replace `[command]` with any Django management command:
- `check`
- `makemigrations`
- `migrate`
- `createsuperuser`
- `shell`
- `runserver`
- `collectstatic`
- etc.

---

**END OF DJANGO COMMAND PERMANENT FIX**

**Version**: 1.0  
**Last Updated**: January 30, 2026  
**Agent**: Hindra (HRM Domain Owner)
