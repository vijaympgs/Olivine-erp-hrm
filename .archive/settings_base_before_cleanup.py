import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    "erp_core.apps.RetailAdminConfig",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "django_filters",
    "drf_spectacular",
    # Local apps
    # NOTE: core.shared.backend.* are utility libraries, not Django apps - removed from INSTALLED_APPS
    "core.org_structure.backend.company",
    "core.auth_access.backend.user_management",
    "core.auth_access.backend.toolbar_control",
    "core.licensing.backend.business_entities.apps.BusinessEntitiesConfig",
    "core.licensing.backend.licensing.apps.LicensingConfig",
    # Common domain contracts (MUST be before retail apps that reference them)
    "common.domain",
    # Retail domain models (Location is Retail-exclusive)
    "Retail.backend.domain",
    # Application modules
    "FMS.backend.finance.apps.FinanceConfig",
    "Retail.backend.inventory.apps.InventoryConfig",
    "Retail.backend.master.item",
    "Retail.backend.master.supplier",
    # NOTE: core.shared.backend.uom and core.shared.backend.attributes are utility libraries - removed from INSTALLED_APPS
    # "core.org_structure.backend.location",  # REMOVED: Location moved to Retail.backend.domain
    "core.org_structure.backend.company_master",
    "Retail.backend.procurement.apps.ProcurementConfig",
    "backend.domain.reporting",
    "Retail.backend.pos",
    "HRM.backend.hrm.apps.HrmConfig",
    "Retail.backend.sales.apps.SalesConfig",
    "backend.qa_console",
    "CRM.backend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",  # Disabled for development
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "erp_core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "erp_core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # Allow access for development
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# API Documentation
SPECTACULAR_SETTINGS = {
    "TITLE": "Retail ERP API",
    "DESCRIPTION": "API for Retail ERP Platform",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-me-in-production")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://localhost:3002",
    "http://127.0.0.1:3002",
    "http://localhost:3003",
    "http://127.0.0.1:3003",
    "http://localhost:3004",
    "http://127.0.0.1:3004",
    "http://localhost:3005",
    "http://127.0.0.1:3005",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://localhost:3002",
    "http://127.0.0.1:3002",
    "http://localhost:3003",
    "http://127.0.0.1:3003",
    "http://localhost:3004",
    "http://127.0.0.1:3004",
    "http://localhost:3005",
    "http://127.0.0.1:3005",
]
CORS_ALLOW_ALL_ORIGINS = DEBUG
CORS_ALLOW_CREDENTIALS = True

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Static files
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Reload views/employee
# Reload trigger
# Reload trigger 2
# Reload trigger 3
