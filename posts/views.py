from django.shortcuts import render, redirect
from .models import Posts
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

def posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Posts.objects.get(slug=slug)
    return render(request, 'post_page.html', {'post': post})

@login_required(login_url='/users/login')
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'post_new.html', {'form': form})