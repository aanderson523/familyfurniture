
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def user_logout(request):
    if request.method =='POST':
        logout(request)

        return redirect('login')
    return render(request, 'logout.html', {})