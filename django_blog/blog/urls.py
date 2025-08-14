from django.urls import path
from django.contrib.auth.views import LoginView

from .views import home, posts, register, profile

urlpatterns = [
    path('', home, name = "home"),
    path('profile/', profile, name = 'profile'),
    path('posts/', posts, name = 'posts'),
    path('login/', LoginView.as_view(template_name = "blog/login.html"), name = 'login'),
    path('register/', register, name = 'register'),
]
