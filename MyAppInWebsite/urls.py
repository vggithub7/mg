from django.contrib import admin
from django.urls import path
from . import views
from .views import HomePageView, CreatePostView # new

urlpatterns = [
    path('myhtml', views.MyAppFunction, name='home-page'),
    path('myhtml/<int:number>/', views.MyAppFunction2),
    path('images/', HomePageView.as_view(), name='home'),
    path('images/post/', CreatePostView.as_view(), name='add_post'), 
]