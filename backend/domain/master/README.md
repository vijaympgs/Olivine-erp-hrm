# Master Data Layer — Domain Index

This directory contains foundational master modules required across the Retail ERP.

Modules:
- Company
- Location
- Supplier
- Customer
- Item & Variants
- Attributes & Attribute Groups
- Units of Measure

Principles:
- All masters are multi-company aware.
- Status lifecycle: Active / Inactive / Archived (future).
- Strict validation rules apply before referencing in transactions.
- All master modules expose:
  - CRUD APIs
  - Search endpoints
  - Audit trail
  - Reference integrity enforcement

Dependencies:
- Core authentication, RBAC, and workflow engine.
