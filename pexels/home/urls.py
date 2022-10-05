from django.contrib import admin
from django.urls import path
from . import views
from .views import FileView

urlpatterns = [
    path('', views.homePage, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('feedback', views.feedback, name='feedback'),
    path('explore', views.explore, name='explore'),
    path('signout', views.signout, name='signout'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('upload', views.upload, name='upload'),
    path('/api/upload',FileView.as_view(), name='FileView'),  
]