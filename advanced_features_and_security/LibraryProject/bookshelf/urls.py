from django.urls import path
from .views import add_book, book_list, edit_book, delete_book

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('view/', book_list, name='book_list'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
]   