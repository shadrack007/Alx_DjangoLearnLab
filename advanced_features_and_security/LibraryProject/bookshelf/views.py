from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

from .models import Book

# Create your views here.
@permission_required('bookshelf.can_add_books', raise_exception=True)
def add_book(request):
    return HttpResponse("Book added successfully.")

@permission_required('bookshelf.can_view_books', raise_exception=True)
def view_books(request):
    return HttpResponse("Here are the books.")

@permission_required('bookshelf.can_edit_books', raise_exception=True)
def edit_book(request, book_id):
    return HttpResponse(f"Book {book_id} edited successfully.")

@permission_required('bookshelf.can_delete_books', raise_exception=True)
def delete_book(request, book_id):
    return HttpResponse(f"Book {book_id} deleted successfully.")
