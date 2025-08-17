from django.db.models.fields import return_None
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, PostForm, CommentForm
from .models import Post, Comment


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #         pass the comment form
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
        return redirect(self.object.get_absolute_url())


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


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm()

    def form_valid(self, form):
        #         form.instance - unsaved Comment instance
        post = get_object_or_404(Post, pk = self.kwargs['post_id'])

        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        """redirect to post detail on success"""
        return self.object.post.get_absolute_url()
