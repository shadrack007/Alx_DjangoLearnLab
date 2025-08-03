from django.urls import path
from .views import add_book, view_books, edit_book, delete_book

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('view/', view_books, name='view_books'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
]   