from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

def error_html(request):
    return render(request, 'error.html')

@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint for Railway"""
    return JsonResponse({
        'status': 'healthy',
        'service': 'Boshliq'
    }, status=200)