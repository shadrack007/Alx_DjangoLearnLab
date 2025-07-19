from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Author, Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'templates/list_books.html', {'books': books})

class LibraryDetailsView(DetailView):
    model = Library
    template_name = 'templates/library_details.html'
    context_object_name = 'library'

