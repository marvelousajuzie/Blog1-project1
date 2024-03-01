from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import admin
from .models import Blog
from django.utils import timezone


def index(request):
      blogs = Blog.objects.all()
      return render(request, 'index.html',{'blogs': blogs})

def createblog(request):
      if request.method == 'POST':
             title = request.POST['title']
             body = request.POST['words']
             blog = Blog.objects.create(title = title, body= body)
             blog.save();
             return redirect('/')
      else:
            return render(request, 'createblog.html')



def updateblog(request, pk):
        blog= Blog.objects.get(id = pk)
        if request.method == 'POST':
            blog.title = request.POST.get('title')
            blog.body = request.POST.get('body')

            blog.created_at = timezone.now()
            blog.save()
            return redirect('/')     
        else:
            return render(request, 'updateblog.html',{'blog': blog})    
        

def deleteblog(request, pk):
      blog= Blog.objects.get(id = pk)
      if request.method == 'POST':
           Blog.delete(blog)
           messages.info(request, "Deleted Sucessfully")
           return redirect('/')
      else:
        return render(request, 'deleteblog.html', {'blog': blog})


def post(request, pk):
    blogs = Blog.objects.get(id = pk)
    return render(request, 'post.html', {'blogs': blogs})


