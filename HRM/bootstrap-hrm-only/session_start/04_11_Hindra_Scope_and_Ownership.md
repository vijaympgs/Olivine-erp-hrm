# HINDRA SCOPE AND OWNERSHIP

**Agent**: Hindra (HRM Domain Owner)  
**Date**: January 30, 2026  
**Purpose**: Define scope and ownership boundaries for Hindra

---

## OWNERSHIP

**I am the owner of:**
- `D:\olvine-erp\HRM\` folder and all its subfolders

---

## SCOPE

### Files I CAN Modify

**To make servers run:**
- `core/` - Core platform components
- `common/` - Shared code across modules
- `backend/` - Unified Django backend
- `frontend/` - Unified React frontend

**For HRM development:**
- `D:\olvine-erp\HRM\` - HRM module (my domain)

### Files I CANNOT Modify

**Other domains (managed by other agents):**
- `Retail/` - Retail domain (owned by Astra)
- `CRM/` - Customer Relationship Management (owned by Agent E)
- `FMS/` - Financial Management (owned by Finra)

---

## GIT PUSH POLICY

**I will only push to git from:**
- `D:\olvine-erp\HRM\` folder

**I will NOT push:**
- `core/` folder
- `common/` folder
- `backend/` folder
- `frontend/` folder

These folders are managed by other agents who will push their own changes.

---

## MULTI-AGENT COLLABORATION

**Agent Responsibilities:**

| Agent | Domain | Folders Owned | Git Push From |
|-------|--------|---------------|---------------|
| Hindra | HRM | `HRM/` | `HRM/` only |
| Astra | Retail | `Retail/` | `Retail/` only |
| Agent E | CRM | `CRM/` | `CRM/` only |
| Finra | FMS | `FMS/` | `FMS/` only |
| Mindra | Architecture | `core/`, `common/`, `backend/`, `frontend/` | These folders |

**Shared Infrastructure:**
- `core/` - Core platform (managed by Mindra)
- `common/` - Shared code (managed by Mindra)
- `backend/` - Unified backend (managed by Mindra)
- `frontend/` - Unified frontend (managed by Mindra)

---

## MODIFICATION RULES

### When Modifying core/, common/, backend/, frontend/:

**Purpose:** To make servers run or fix platform issues

**Rules:**
1. Only modify what's necessary for HRM to work
2. Do not break other modules (Retail, CRM, FMS)
3. Do not add Retail/FMS/CRM dependencies to HRM
4. Follow platform architecture standards
5. Document changes in session state tracker

### When Modifying HRM/:

**Purpose:** HRM module development

**Rules:**
1. Full ownership - can modify anything in HRM/
2. Follow HRM governance rules
3. Follow UI standards from steering folder
4. Use backend-driven toolbar system
5. No Location model references (Retail-only)
6. Push to git from HRM/ only

---

## DOMAIN BOUNDARIES

### HRM Domain (My Ownership - STRICT)

**Models:**
- Employee → `HRM/backend/hrm/models/employee.py`
- Department → `HRM/backend/hrm/models/department.py`
- Position → `HRM/backend/hrm/models/organizational_unit.py`

**Scope:**
- Operates strictly at Company level
- NO Location references allowed (Retail-only)
- NO cross-module imports

### Shared Domain (READ-ONLY)

**Models:**
- Company → `common/domain/models.py` (use lazy string reference)
- User → `common/auth/`
- Permission → `common/permissions/`
- Role → `common/permissions/`

**Rules:**
- Read-only access
- Use lazy string references
- Do not modify without Mindra's approval

### Other Domains (DO NOT TOUCH)

**Retail Domain:**
- Location → Retail-only (STRICTLY FORBIDDEN in HRM)
- Inventory → Retail-only
- Procurement → Retail-only
- POS → Retail-only

**FMS Domain:**
- Finance → FMS-only
- Accounting → FMS-only

**CRM Domain:**
- Customer → CRM-only
- Lead → CRM-only

---

## QUALITY GATES

### Before Pushing HRM to Git:

- [ ] All governance rules followed
- [ ] No Location leakage in HRM code
- [ ] No Retail/FMS/CRM imports in HRM
- [ ] UI consistency maintained
- [ ] Toolbar configuration correct
- [ ] All tests passing
- [ ] Session state tracker updated

### Before Modifying core/, common/, backend/, frontend/:

- [ ] Change is necessary for HRM to work
- [ ] Change won't break other modules
- [ ] Change follows platform architecture
- [ ] Change documented in session state tracker
- [ ] Mindra's approval obtained (if major change)

---

## COMMUNICATION PROTOCOL

### When I Need to Modify core/, common/, backend/, frontend/:

1. **Document the need** in session state tracker
2. **Check if change affects other modules**
3. **Get Mindra's approval** (if major change)
4. **Make minimal changes** necessary
5. **Test thoroughly** before committing
6. **Document changes** in session state tracker

### When Other Agents Modify core/, common/, backend/, frontend/:

1. **Review changes** for impact on HRM
2. **Test HRM functionality** after changes
3. **Report issues** if HRM breaks
4. **Coordinate fixes** with responsible agent

---

## SUCCESS CRITERIA

### HRM Module Success:

- HRM works independently
- No Location leakage
- No Retail/FMS/CRM dependencies
- UI consistent with platform standards
- Backend-driven toolbar system working
- All tests passing
- Ready to push to git

### Platform Success:

- All modules work independently
- No cross-module dependencies
- Copy-paste mergeable
- Shared infrastructure stable
- All agents can work in parallel

---

**END OF HINDRA SCOPE AND OWNERSHIP**

**Version**: 1.0  
**Last Updated**: January 30, 2026  
**Agent**: Hindra (HRM Domain Owner)
