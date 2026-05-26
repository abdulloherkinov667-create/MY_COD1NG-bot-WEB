from django.shortcuts import render

def register_page(request):
    return render(request, 'User/register.html')

def login_page(request):
    return render(request, 'User/login.html')