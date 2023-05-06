
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def signup (request):

    if request.method == "GET":
        return render (request, 'login/signup.html')

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user:
            login or auth_login(request, user)
            messages.info(request,('welcome'))
            return redirect('home')
        
        
        else:
            messages.success(request, ("An Error Occured, Try Agian"))
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})

