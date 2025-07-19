from .models import Book, Librarian, Library, Author

# List all books in the library
books = Library.objects.get(name=library_name).books.all()

# Query all books, by a specific author
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# Retrieve the librarian of a specific library
librarian = Librarian.objects.get(library=library_name)