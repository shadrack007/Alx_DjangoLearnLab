from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget

from .models import Post, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True, help_text = "Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            "tags": TagWidget(),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long')

        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clear_content(self):
        comment_content = self.cleaned_data.get('content')

        if len(comment_content < 0):
            raise forms.ValidationError('Comment must be at least 1 character long')
        return comment_content
