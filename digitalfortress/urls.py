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
    path('hints/get', api.getHints, name='getHints'),
]