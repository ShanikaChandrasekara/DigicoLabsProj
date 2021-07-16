from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash,
)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import Group, User

from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm, OrderPlacementForm
from .models import OrderPlacement

def hi(request):
    return render(request, 'dashboard.html')

def hello(requset):
    return render(requset, 'MyApp/Scaffold/assets/css/style.css')

def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'register.html', context)


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('login')

        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'LRHWebApp/login.html')

    context = {}
    return render(request, 'login.html')



def orderplacement(request):
    print("Hello")
    print(request.method)
    if request.method == 'POST':
        form = OrderPlacementForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("I'm in inner if")
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            email = request.POST.get('email', '')
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            retype_password = request.POST.get('retype_password', '')


            print("I'm working 1")

            order_placement = OrderPlacement(first_name=first_name, last_name=last_name,
                                                      email=email,
                                                      username=username, password=password,
                                                      retype_password=retype_password
                                                      )

            print("I'm working 2")

            order_placement.save()
            print("I'm working 3")


        else:
            print("I'm working in else")




    else:
        print("I'm working in outer else")
        form = OrderPlacementForm()

    print("I'm working still")
    return render(request, 'orderPlacementPage.html', {'form': form})
    print("I'm working at the end")


