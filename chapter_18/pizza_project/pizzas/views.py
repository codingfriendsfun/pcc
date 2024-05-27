from django.shortcuts import render

def index(request):
    """The home page for pizzas"""
    return render(request, 'pizzas/index.html')
