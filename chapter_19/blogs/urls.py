"""Defines URL patterns for blogs"""

from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all blogs
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for a blog 
    path('blogs/<int:blog_id>/', views.blog, name='blog')
]
