from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('info_view')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('info_view')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('info_view')