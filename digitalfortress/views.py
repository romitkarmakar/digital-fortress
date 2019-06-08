from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterForm, UserLoginForm, HintForm, RoundForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models
from django.forms import formset_factory

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponse("Index page")
    else:
        return HttpResponse("Please Login")

def userRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            user.save()
            return HttpResponse("Registered Successfully")
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form' : form})

def userLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user=user)
                return HttpResponse("Login Successfully")
            else:
                return HttpResponse("Authentication Failed")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form' : form})

@login_required
def userLogout(request):
    logout(request)
    return HttpResponse("Successfully Logged out")

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def round(request):
    hints = models.Hint.objects.all()
    print(hints[0].id)
    round = models.Round.objects.get()
    return render(request, 'round.html', {'hints' : hints, 'round': round})

@login_required
def leaderboard(request):
    return render(request, 'leaderboard.html')