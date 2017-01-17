from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import User

from accounts.forms import LoginForm, RegisterForm


def log_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(password=password, username=username)
            if auth_user:
                login(request, auth_user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()

        return render(request, 'login.html', {'form': form})


@login_required(login_url='/accounts/login')
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            auth_user = authenticate(password=password, username=username)
            if auth_user:
                login(request, auth_user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})