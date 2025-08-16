from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, PostForm
from .models import Post


@login_required()
def profile(request):
    print(request.user)
    return render(request, 'blog/profile.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data = request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CustomUserCreationForm(data = request.POST)
            return render(
                request, 'blog/register.html', {
                    "form": form,
                }
            )
    else:
        form = CustomUserCreationForm()

        return render(
            request, 'blog/register.html', {
                "form": form,
            }
        )


def home(request):
    return HttpResponse('Home page')


# DJANGO BLOG CRUD
class PostListView(generic.ListView):
    model = Post


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Automatically called by UserPassesTest mixin"""
        post = self.get_object()
        return self.request.user == post.author  # Only author can edit


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    context_object_name = 'post'

    def test_func(self):
        """Automatically called by UserPassesTest mixin"""
        post = self.get_object()
        return self.request.user == post.author  # Only author can delete
