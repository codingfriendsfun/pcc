from django.shortcuts import render

from .models import Pizza

def index(request):
    """The home page for pizzas"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)
