from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('myhtml', views.MyAppFunction, name='home-page'),
    path('myhtml/<int:number>/', views.MyAppFunction2),
]