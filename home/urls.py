from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('about/',views.watch,name='watches'),
    path('log',views.log,name='log'),
    
]
