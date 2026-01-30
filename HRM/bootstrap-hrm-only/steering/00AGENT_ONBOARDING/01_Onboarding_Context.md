# ONBOARDING FOR AGENTS: STEP 1 - Context & Status

## 👋 WELCOME: Olivine Retail ERP Platform
You are working on the **Olivine Retail ERP Platform**, a multi-tenant, enterprise-grade retail management system designed for scale.

**Primary Goals:**
1.  **Strict Architecture**: Clean separation between "Canonical Masters" (Global Definitions) and "Operational Data" (Transactions/Per-Company).
2.  **No "OperatingCompany" Model**: We use a `Company` model for operations. "Business Entity" is strictly for licensing/admin only.
3.  **Enterprise UI**: A VB.NET inspired, keyboard-heavy, high-density UI using React + Tailwind + Vite.
4.  **Backend Integrity**: Django DRF with strict service layers and domain separation.

---

## 📅 CURRENT STATUS (From NEXT_SESSION.md)
**Project Date**: 2025-12-26
**Context**: Procurement Module - RFQ Flow Implementation & Testing

### 🎯 IMMEDIATE OBJECTIVE
Functionalize the **Request for Quotation (RFQ)** module. The UI (`RFQFormPage.tsx`) exists, but backend persistence and full lifecycle (Draft -> Published -> Expired) need verification.

### 📋 ACTIVE TASK LIST
1.  **RFQ Backend Verification**
    *   Check `backend/domain/procurement/models.py` defines `RFQ` and `RFQLine`.
    *   Check `backend/domain/procurement/views.py` has `RFQViewSet`.
    *   Check `urls.py` registers the endpoint.
2.  **Allowed Interactions (Frontend)**
    *   Wire the **SAVE** button in `RFQFormPage.tsx` to `POST /api/v1/procurement/rfq/`.
    *   Implement "Publish" action.
3.  **Testing**
    *   Create a new RFQ via the UI.
    *   Verify product lookups work within the RFQ lines (already implemented, needs verification).
    *   Verify Supplier lookup works.
    *   Verify data persists to database.

---

## 🛠️ TECH STACK
- **Frontend**: React 18, TypeScript, Tailwind CSS, Lucide Icons, Vite.
- **Backend**: Python 3.10+, Django 4+, Django REST Framework (DRF).
- **Database**: PostgreSQL (Production), SQLite (Dev).
- **Architecture**: Modular Monolith (Domains: Procurement, Inventory, Sales, Finance, HR).

## ⚠️ CRITICAL "DO NOTs"
1.  **Do NOT edit `01practice-v2`**: This is a read-only reference codebase.
2.  **Do NOT create "OperatingCompany" models**: We removed this abstraction. Use `Company`.
3.  **Do NOT mix Business Entity and Company**: 
    - `BusinessEntity` = Admin/Billing only.
    - `Company` = Actual tenant where users log in and work.
