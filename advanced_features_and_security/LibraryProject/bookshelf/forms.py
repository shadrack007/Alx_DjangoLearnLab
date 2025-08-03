from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'publication_year': 'Year of Publication',
        }