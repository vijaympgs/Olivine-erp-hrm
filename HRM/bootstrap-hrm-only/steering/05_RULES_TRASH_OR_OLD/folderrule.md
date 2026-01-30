ROLE:
You are working inside an existing Django-based Retail ERP backend.

PROJECT STRUCTURE (AUTHORITATIVE):
- Django project root: backend/
- Django project module: erp_core
- Django settings package: erp_core/settings/

SETTINGS SOURCE OF TRUTH:
- ONLY this file defines global Django configuration:
  backend/erp_core/settings/base.py

ENVIRONMENT FILES:
- backend/erp_core/settings/dev.py
- backend/erp_core/settings/prod.py
These MUST ONLY import from base.py and override environment-specific values
(e.g. DEBUG, DATABASES, ALLOWED_HOSTS, logging).

ABSOLUTE SETTINGS RULES (DO NOT VIOLATE):
- DO NOT create new settings files.
- DO NOT modify or add Django settings in any domain module.
- DO NOT touch:
  backend/domain/**/settings.py
- DO NOT duplicate INSTALLED_APPS across multiple files.
- DO NOT move Django configuration out of base.py.

MANDATORY BEHAVIOR:
- Any change to:
  - INSTALLED_APPS
  - AUTH_USER_MODEL
  - MIDDLEWARE
  - DATABASES
  - REST_FRAMEWORK
  - AUTHENTICATION
  - TIME_ZONE / USE_TZ
  MUST be made ONLY in:
  backend/erp_core/settings/base.py

DOMAIN SETTINGS CLARIFICATION:
- Files such as:
  backend/domain/master/settings.py
  are DOMAIN-LEVEL configuration files.
- Django DOES NOT load these automatically.
- These files must NEVER be treated as Django project settings.

VERIFICATION STEP (MANDATORY):
- Before final output, explicitly verify that:
  - All Django configuration changes are located ONLY in base.py
  - dev.py and prod.py contain ONLY environment overrides
  - No domain/*/settings.py file was modified

FINAL CONFIRMATION (REQUIRED):
At the end, explicitly state:
✔ Django settings correctly applied in erp_core/settings/base.py
✔ No domain settings files were modified
✔ No duplicate or misplaced configuration exists

If you cannot comply with these rules, STOP immediately.
