from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import login

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_details'),
    path('auth/login/',LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('auth/logout/', LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('auth/register/', views.register, name='register')
]