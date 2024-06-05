from django.shortcuts import render


def index(request):
    """The home page for Learning Log."""

    return render(request, 'learning_logs/index.html')

def base(request):
    """Base template."""

    return  render(request, 'learning)logs/base.html')
