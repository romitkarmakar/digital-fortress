from django.views import View
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from ..forms import UserRegisterForm, UserLoginForm, HintForm, RoundForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ..models import models
from django.forms import formset_factory

class RegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            user.save()
            return HttpResponse("Registered Successfully")

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})