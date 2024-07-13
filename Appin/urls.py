from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import models
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('generic/', views.generic, name = 'generic'),
    path('elements/', views.elements, name = 'elements'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.login, name = 'signup')
] 

