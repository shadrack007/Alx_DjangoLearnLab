from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

from .models import Book
from .forms import BookForm

# Create your views here.
@permission_required('bookshelf.can_add_books', raise_exception=True)
def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            return render(request, 'bookshelf/form_example.html', {
                'form': form,
            })
    else:
        return render(request, 'bookshelf/form_example.html', {'form': form})
  

@permission_required('bookshelf.can_view_books', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_edit_books', raise_exception=True)
def edit_book(request, book_id):
    return HttpResponse(f"Book {book_id} edited successfully.")

@permission_required('bookshelf.can_delete_books', raise_exception=True)
def delete_book(request, book_id):
    return HttpResponse(f"Book {book_id} deleted successfully.")
