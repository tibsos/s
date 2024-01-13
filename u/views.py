from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Profile

def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('email')

        user = authenticate(username = username, password = password)
        login(request, user)

        return redirect('/')

    c = {}

    return render(request, 'login.html', c)

def register(request):

    if request.method == 'POST':

        print(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('email')

        email = request.POST.get('email')
        name = request.POST.get('name')
        category = request.POST.get('category')
        plan = request.POST.get('plan')

        user = User(username = username)
        user.set_password(password)
        user.save()

        profile = Profile(user = user, name = name, email = email, category = category, plan = plan) 
        profile.save()

        user = authenticate(username = username, password = password)
        login(request, user)


        return redirect('/')

    c = {}

    return render(request, 'register.html', c)


def check_username(request):

    username = request.POST.get('username')

    if User.objects.filter(username = username).exists(): return HttpResponse('Y')

    else: return HttpResponse('N')

def check_email(request):

    email = request.POST.get('email')

    if Profile.objects.filter(email = email).exists(): return HttpResponse('Y')

    else: return HttpResponse('N')
