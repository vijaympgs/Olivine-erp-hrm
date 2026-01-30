# Add to erp_core/urls.py
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

# urlpatterns += [ path("health/", health) ]



