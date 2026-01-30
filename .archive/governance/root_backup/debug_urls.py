
import os
import sys
import django
from django.urls import reverse, get_resolver

# Setup Django environment
sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
try:
    django.setup()
except Exception as e:
    print(f"Django setup failed: {e}")
    sys.exit(1)

def print_urls():
    print("Checking Admin URL...")
    try:
        url = reverse('admin:index')
        print(f"✅ 'admin:index' resolves to: {url}")
    except Exception as e:
        print(f"❌ 'admin:index' FAILED to resolve: {e}")

    print(f"\nMEDIA_URL: '{settings.MEDIA_URL}'")
    print(f"STATIC_URL: '{settings.STATIC_URL}'")

    print("\nScanning urlpatterns:")
    resolver = get_resolver()
    for i, pattern in enumerate(resolver.url_patterns):
        print(f" [{i}] {pattern}")


    from django.conf import settings
    print(f"\nAPPEND_SLASH: {settings.APPEND_SLASH}")
    print(f"ROOT_URLCONF: {settings.ROOT_URLCONF}")
    print(f"MIDDLEWARE: {settings.MIDDLEWARE}")

if __name__ == "__main__":
    print_urls()



