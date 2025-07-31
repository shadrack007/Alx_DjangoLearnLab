from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'author']