from django.urls import path, include
from .views import list_books, LibraryDetailView, register   
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_details'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('auth/register', register, name='register')
]