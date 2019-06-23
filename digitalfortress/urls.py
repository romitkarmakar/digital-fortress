from django.urls import path
from . import views
from . import api
from digitalfortress.controllers.Login import LoginView
from digitalfortress.controllers.Register import RegisterView

urlpatterns = [
    path('', views.index, name='index'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
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