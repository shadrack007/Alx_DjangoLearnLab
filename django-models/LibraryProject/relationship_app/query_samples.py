from .models import Book, Librarian, Library

# List all books in the library
books = Library.objects.get(name=library_name).books

# Query all books, by a specific author
author_books = Book.objects.filter(author__name='John Doe').all()

# Retrieve the librarian of a specific library
librarian = Librarian.objects.get(library__name='Central Library')