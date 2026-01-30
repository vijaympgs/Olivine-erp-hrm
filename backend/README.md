# Retail ERP Backend

Django REST Framework backend for the Retail ERP Platform.

## 🚀 Setup

### Environment Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load demo data (optional)
python manage.py shell < scripts/seed_demo_data.py
```

### Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📁 Project Structure

```
backend/
├── domain/                 # Business logic modules
│   ├── admin/             # User management
│   ├── business_entities/ # Companies, locations
│   ├── finance/           # Financial operations
│   ├── inventory/         # Stock management
│   ├── master/            # Master data
│   ├── procurement/       # Purchase orders
│   └── reporting/         # Analytics
├── erp_core/              # Django project configuration
│   ├── settings/          # Environment-specific settings
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
├── common/                # Shared utilities
│   ├── audit.py          # Audit trail
│   ├── mixins.py         # Common model mixins
│   └── validators.py     # Custom validators
└── scripts/               # Management scripts
```

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/user/` - Current user info

### Business Entities
- `GET /api/companies/` - List companies
- `GET /api/locations/` - List locations

### Inventory
- `GET /api/items/` - List inventory items
- `POST /api/items/` - Create new item

### POS
- `POST /api/pos/transactions/` - Create transaction
- `GET /api/pos/sessions/` - List POS sessions

## 🧪 Testing

```bash
# Run tests
python manage.py test

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## 🔐 Environment Variables

Create a `.env` file in the backend directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

## 📊 Database Schema

The system uses Django's ORM with the following main models:
- User management (Django's built-in User model extended)
- Company and Location hierarchy
- Inventory items with attributes and variants
- POS transactions and sessions
- Purchase orders and procurement