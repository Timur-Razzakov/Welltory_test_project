import datetime as dt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
# from account.forms import UserLoginForm, UserRegistrationForm, ContactForm, UserUpdateForm
from .forms import UserRegistrationForm ,UserLoginForm
from main.models import Error

User = get_user_model()

"""Функция для авторизации"""


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'account/login.html', {'form': form})


"""Функция выхода"""


def logout_view(request):
    logout(request)
    return redirect('home')


""" Функция для создание нового пользователя """


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)  # instans) commit=False-->исп для полного соединения с базой
        new_user.set_password(form.cleaned_data['password'])  # ЗАШИФРОВЫВАЕТ пароль
        new_user.save()
        messages.success(request, 'Пользователь добавлен в систему.')
        return render(request, 'account/registered.html',
                      {'new_user': new_user})
    return render(request, 'account/registration.html', {'form': form})


"""Функция для удаления пользователя"""


def delete_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            qs = User.objects.get(pk=user.pk)
            qs.delete()
            messages.error(request, 'Пользователь удалён :(')
    return redirect('home')
