from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)

            login(request, user)

            return redirect('dashboard')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {'username': request.user.username})
    else:
        return redirect('login')
