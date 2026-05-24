from django.shortcuts import render

def error_html(request):
    return render(request, 'error.html')

def home_run_page(request):
    return render(request, 'home_page.html')