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
    path('auth/register/', views.register, name='register'),
    path('librarian/', views.librarian_view, name='librarian'),
    path('admin/', views.admin_view, name='admin'),
    path('member/', views.member_view, name='member'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.change_book, name='change_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]