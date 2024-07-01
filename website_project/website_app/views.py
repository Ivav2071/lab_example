from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect,request
from django.contrib.auth.models import User
from django.db import models



from django.urls import reverse
from .forms import OrderForm


def index(request):
    return render(request, 'index.html')

def vacancy(request):
    return render(request,'vacancy.html')

def products(request):
    return render(request,'products.html')

def contact(request):
    return render(request,'contact.html')


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('products'))

def home(request):
    return render(request, 'home.html')

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # Логика обработки заказа (например, отправка уведомления)
            return redirect('order_success')  # Перенаправление на страницу успешного оформления заказа
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form})


def order_success(request):
    return render(request, 'order_success.html')

