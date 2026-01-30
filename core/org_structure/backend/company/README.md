# Company Master Module

## Overview

The Company Master module implements the core company management functionality as specified in BBP 1.1. It provides CRUD operations for managing company entities that serve as the root master for configuration, reporting boundaries, and business hierarchies.

## Features

### Backend (Django)
- **Model**: Complete Company model with validation rules
- **API**: RESTful endpoints with filtering, search, and pagination
- **Admin**: Django admin interface for company management
- **Validation**: Business rule enforcement (unique codes, active company requirement)

### Frontend (React)
- **List View**: Searchable and filterable company listing
- **Modal Form**: Create/edit company with comprehensive form validation
- **Status Management**: Activate/deactivate companies with safety checks
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS

## API Endpoints

```
GET    /api/companies/           # List companies with filters
POST   /api/companies/           # Create new company
GET    /api/companies/{id}/      # Get company details
PUT    /api/companies/{id}/      # Update company
DELETE /api/companies/{id}/      # Delete company
POST   /api/companies/{id}/activate/    # Activate company
POST   /api/companies/{id}/deactivate/  # Deactivate company
GET    /api/companies/active/    # Get only active companies
```

## Data Model

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | UUID | Yes | Primary key |
| company_code | String(20) | Yes, Unique | Auto-generated from name |
| company_name | String(100) | Yes | Legal company name |
| legal_entity_type | Enum | Yes | SOLE_PROPRIETOR, PARTNERSHIP, LLP, PVT_LTD, FRANCHISE |
| address | JSON | No | Registered address details |
| default_currency | String(10) | Yes | ISO currency code (default: INR) |
| timezone | String(50) | Yes | Olson timezone (default: Asia/Kolkata) |
| status | Enum | Yes | ACTIVE, INACTIVE |

## Business Rules

1. **Unique Company Code**: Each company must have a unique code
2. **Active Company Requirement**: At least one active company must exist
3. **Auto-generation**: Company code is auto-generated from company name if not provided
4. **Currency Change Confirmation**: Changes to default currency require confirmation (affects system-wide behavior)

## Usage

### Backend Integration

1. Add to Django settings:
```python
INSTALLED_APPS = [
    # ... other apps
    'domain.company',
]
```

2. Include URLs:
```python
urlpatterns = [
    # ... other patterns
    path('', include('domain.company.urls')),
]
```

3. Run migrations:
```bash
python manage.py makemigrations company
python manage.py migrate
```

4. Load sample data:
```bash
python manage.py loaddata domain/company/fixtures/sample_companies.json
```

### Frontend Integration

1. Import and use the CompanySettings component:
```tsx
import { CompanySettings } from '../pages/CompanySettings';

// In your router
{ path: "setup/company", element: <CompanySettings /> }
```

2. The component includes:
   - Company listing with search and filters
   - Create/edit modal with form validation
   - Status management (activate/deactivate)
   - Error handling and loading states

## Testing

### Sample Data
The module includes sample companies for testing:
- Retail Corporation Ltd (PVT_LTD, Active)
- Fashion Hub Franchise (FRANCHISE, Active)  
- Tech Solutions LLP (LLP, Inactive)

### API Testing
```bash
# List companies
curl -X GET "http://localhost:8000/api/companies/"

# Create company
curl -X POST "http://localhost:8000/api/companies/" \
  -H "Content-Type: application/json" \
  -d '{"company_name": "Test Company", "legal_entity_type": "PVT_LTD"}'
```

## Navigation

The Company Settings page is accessible via:
- **Menu Path**: System Configuration → Company Settings
- **URL**: `/setup/company`
- **Menu ID**: `company` in the System Configuration section

## Dependencies

- **Backend**: Django, DRF, django-filters
- **Frontend**: React, TypeScript, Tailwind CSS, Lucide React icons
- **Used By**: All other modules that require company context

## Future Enhancements

- Multi-company user access controls
- Company-specific branding and themes
- Advanced address validation
- Integration with external business registries
- Audit trail for company changes