from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('profile/', views.profile, name = 'profile'),
    path('login/', LoginView.as_view(template_name = "blog/login.html"), name = 'login'),
    path('register/', views.register, name = 'register'),
    path('', views.home, name = 'home'),
    #     post
    path('posts/', views.PostListView.as_view(), name = 'post_list'),
    path('posts/new/', views.PostCreateView.as_view(), name = 'post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name = 'post_details'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name = 'post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'post_delete'),
]
