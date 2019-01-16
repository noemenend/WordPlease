from django.contrib import messages
from django.contrib.auth import authenticate, login as loginDjangoAuth
from django.shortcuts import render, redirect

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Wrong username or password')
        else:
            loginDjangoAuth(request, user)
            return redirect('home')
    return render(request, 'users/login.html')
