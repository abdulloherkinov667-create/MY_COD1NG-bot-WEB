from django.shortcuts import render

def register_page(request):
    return render(request, 'User/register.html')