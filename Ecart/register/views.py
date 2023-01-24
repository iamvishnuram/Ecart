from django.shortcuts import render,redirect
from .forms import SignUp
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth, messages


def signup(request):
    if request.method == 'POST':
        forms = SignUp(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            return redirect('/store')   
    else:
        forms = SignUp()
    return render(request, 'registration/signup.html', {'forms': forms})

