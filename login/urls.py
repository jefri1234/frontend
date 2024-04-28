
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='login'),
    path('notas/', views.notas.as_view(), name='notas'),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
