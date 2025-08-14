from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from .forms import CustomUserCreationForm


# Create your views here.
def home(request):
    return HttpResponse('home page')


def posts(request):
    return HttpResponse('posts pages')


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
