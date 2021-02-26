from django.shortcuts import render
from django.contrib.auth.models import User
from myapp.models import Page, Post, Song
# Create your views here.


def home(request):
    return render(request, 'home.html')


def user_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def page_view(request):
    pages = Page.objects.all()
    return render(request, 'pages.html', {'pages': pages})


def post_view(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def song_view(request):
    songs = Song.objects.all()
    return render(request, 'songs.html', {'songs': songs})
