from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user_app.models import Users

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        
        if username and phone_number and password:
            Users.objects.create(
                first_name=first_name,
                username=username,
                phone_number=phone_number,
                password=password
            )
            return redirect('login_page')
    return render(request, 'User/register.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_run_page') 

    if request.method == 'POST':
        username_input = request.POST.get('username', '').strip()
        password_input = request.POST.get('password', '')

        if username_input and password_input:
            user = authenticate(request, username=username_input, password=password_input)

            if user is not None:
                login(request, user)
                if not request.POST.get('remember'):
                    request.session.set_expiry(0)
                return redirect('home_run_page')
            else:
                messages.error(request, "Foydalanuvchi nomi yoki parol xato!")
        else:
            messages.error(request, "Barcha maydonlarni to'ldiring!")
    return render(request, 'User/login.html')
