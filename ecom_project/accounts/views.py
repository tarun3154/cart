from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import *




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('product_list')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def Userlogout(request):
    logout(request)
    return redirect('login')


def registration(request):
    userform = UserForm()

    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():  
            password = userform.cleaned_data.get('password')
            user = userform.save(commit=False)
            user.set_password(password)
            
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')

    return render(request, 'accounts/registration.html', {'user_form': userform})
