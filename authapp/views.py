# authapp/views.py
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('shop:product_list'))  # Cambia a 'shop:product_list'
    else:
        form = UserCreationForm()
    return render(request, 'authapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('shop:product_list'))  # Cambia a 'shop:product_list'
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Cambia 'login' por la URL de tu vista de login
