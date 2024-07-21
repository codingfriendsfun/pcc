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

def blog(request, blog_id):
    """Show a single blog and all entries"""
    blog = Blog.objects.get(id=blog_id)
    entries = blog.entry_set.order_by('-date_added')
    context = {'blog': blog, 'entries': entries}
    return render(request, 'blogs/blog.html', context)
