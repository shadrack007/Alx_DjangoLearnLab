from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name = 'user_register'),
    path('login/', obtain_auth_token, name = 'login'),
    path('profile/', views.UserProfileView.as_view(), name = 'user_Profile'),
]
