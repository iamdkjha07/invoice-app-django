from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/htmls/dashboard.html', {'titles':'Dashboard - Invoice'})
    else:
        return redirect('loginPage')

def logOut(request):
    logout(request)
    return redirect('loginPage')