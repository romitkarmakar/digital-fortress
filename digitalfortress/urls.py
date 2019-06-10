from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.userRegister, name='register'),
    path('login', views.userLogin, name='login'),
    path('logout', views.userLogout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('round', views.round, name='round'),
    path('getHints', api.getHints, name='getHints'),
    path('getRound', api.getRound, name='getRound'),
    path('checkHint', api.checkHint, name='checkHint'),
    path('getLocations', api.getLocations, name='getLocations'),
    path('checkRound', api.checkRound, name='checkRound'),
]