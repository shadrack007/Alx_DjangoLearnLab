from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.template.defaultfilters import title
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from taggit.models import Tag

from .forms import CustomUserCreationForm, PostForm, CommentForm
from .models import Post, Comment


@login_required()
def profile(request):
    print(request.user)
    return render(request, 'blog/profile.html')


# USER REGISTRATION
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


# POST SEARCH
def post_search(request):
    query = request.GET.get('q')

    search_results = []

    if query:
        search_results = Post.objects.filter(
            Q(title__icontains = query) |
            Q(content__icontains = query) |
            Q(tags__name__icontains = query)
        ).distinct()

    context = {
        "search_results": search_results,
        "query": query,
    }

    return render(request, 'blog/post_search.html', context)


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


class PostByTagListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug = self.kwargs.get("tag_slug"))
        posts = Post.objects.filter(tags__name__iexact = self.tag.name)
        print(self.tag)
        print(posts)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


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
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        #         form.instance - unsaved Comment instance
        post = get_object_or_404(Post, pk = self.kwargs['pk'])

        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        """redirect to post detail on success"""
        return self.object.post.get_absolute_url()
