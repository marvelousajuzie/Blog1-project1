from django.shortcuts import render
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


def post(request, pk):
    blogs = Blog.objects.get(id = pk)
    return render(request, 'post.html', {'blogs': blogs})