from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .models import Library
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

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