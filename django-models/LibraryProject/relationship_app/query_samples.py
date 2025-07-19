from .models import Book, Librarian

# List all books in the library
books = Book.objects.all()

# Query all books, by a specific author
author_books = Book.objects.filter(author__name='John Doe')

# Retrieve the librarian of a specific library
librarian = Librarian.objects.get(library__name='Central Library')