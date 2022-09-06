from django.contrib import admin
from django.urls import path
from . import views

# importing views from views..py
from .views import homePage
  
urlpatterns = [
    path('home', views.homePage, name='home'),
    path('login', views.login, name='login'),
]