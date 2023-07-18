from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .form import UserForm

def index(request):
    return render(request, 'dashboard/index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user, '------------------------------- >')
            return redirect('index')

    return render(request, 'dashboard/login.html')


def register_user(request):
    form = UserForm()
    for f in form:
        if f.label == 'Password':
            f.label = 'Parol'
        elif f.label == 'Password confirmation':
            f.label = 'Parolni tasdiqlash'

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            return redirect('index')
        else:
            print('-----------------------------------------------------')
    return render(request, 'dashboard/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('index')
