from django.shortcuts import render, redirect

from .models import Blog, Post
from .forms import BlogForm

def index(request):
    """Home page for Blog"""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Show all blogs"""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Show a single blog and all posts"""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('-date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    """Create a new blog"""
    if request.method != 'POST':
        # No data submitted; create blank form
        form = BlogForm()
    else:
        # POST data submitted; process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
        
    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)
