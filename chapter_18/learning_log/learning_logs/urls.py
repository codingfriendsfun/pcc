"""Defines URL patterns for templates"""

from django.urls import path
from . import views


app_name = 'templates'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]
