import os
from django.core.wsgi import get_wsgi_application
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')

application = get_wsgi_application()




