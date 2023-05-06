from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from shop.views import shop
from inventory import models

# Create your views here.
def selection(request):
    if selection.method =="POST":
        return redirect ('shop')

def items(request):
    return render(request, 'selection/instock.html')
