from django.shortcuts import render

from .models import Blog

def index(request):
    """Home page for Blog"""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Show all blogs"""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)
