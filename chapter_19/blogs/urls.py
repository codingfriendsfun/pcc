"""Defines URL patterns for blogs"""

from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all blog entries
    path('blogs/', views.blogs, name='blogs')
]
