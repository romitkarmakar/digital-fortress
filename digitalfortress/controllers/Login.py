from django.views import View
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from ..forms import UserRegisterForm, UserLoginForm, HintForm, RoundForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ..models import models
from django.forms import formset_factory

class LoginView(View):
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                print(request.GET)
                login(request, user=user)
                return redirect('dashboard')
            else:
                return HttpResponse("Authentication Failed")

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})