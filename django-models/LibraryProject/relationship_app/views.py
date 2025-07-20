from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

from .models import Book
from .forms import BookForm
from .models import Library
from .permission_test import is_admin, is_librarian, is_member

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/register.html', {
            'form': form
        })
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {
            'form': form
        })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('list_books')
        return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    


    
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request,'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        # process form
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list_books')
        else:
            return render(request, 'relationship_app/book_form.html', {
            "form": form,
            'action': 'Add Book'
        })
    else:
        form = BookForm()
        return render(request, 'relationship_app/book_form.html', {
            "form": form,
            'action': 'Add Book'
        })

@permission_required('relationship_app.can_change_app')
def change_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('list_books')

        else:
            form = BookForm(instance=book)
            return render(request, 'relationship_app/book_form.html', {
            "form": form,
            "action": "Update Book"
            })
    else:
        form = BookForm(instance=book)
        return render(request, 'relationship_app/book_form.html', {
            "form": form,
            "action": "Update Book"
        })


@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})