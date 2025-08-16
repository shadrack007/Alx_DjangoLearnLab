from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('profile/', views.profile, name = 'profile'),
    path('login/', LoginView.as_view(template_name = "blog/login.html"), name = 'login'),
    path('register/', views.register, name = 'register'),
    path('', views.home, name = 'home'),
    #     post
    path('post/', views.PostListView.as_view(), name = 'post_list'),
    path('post/new/', views.PostCreateView.as_view(), name = 'post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post_details'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'post_delete'),
]
