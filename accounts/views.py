from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import *
from django.contrib.auth import login as user_login

# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})
