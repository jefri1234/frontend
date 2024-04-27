
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='login'),
]
