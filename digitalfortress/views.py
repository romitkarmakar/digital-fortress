from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, UserLoginForm, HintForm, RoundForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models
from django.forms import formset_factory


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'index.html')


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

    return render(request, 'register.html', {'form': form})

@login_required
def userLogout(request):
    logout(request)
    return redirect('index')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def round(request):
    return render(request, 'round.html', {})


@login_required
def leaderboard(request):
    people = []
    profiles = models.Profile.objects.order_by('-score').all()

    for i in profiles:
        muser = User.objects.get(id=i.user_id)
        people.append({
            'username': muser.username,
            'score': i.score
        })
    return render(request, 'leaderboard.html', {'people': people})
