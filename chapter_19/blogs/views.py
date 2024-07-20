from django.shortcuts import render

def index(request):
    """Home page for Blog"""
    return render(request, 'blogs/index.html')
