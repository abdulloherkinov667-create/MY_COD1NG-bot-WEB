from django.shortcuts import render

def error_html(request):
    return render(request, 'error.html')