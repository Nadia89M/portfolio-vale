from django.shortcuts import get_object_or_404, render
from .models import Portfolio


def index(request):
    items = Portfolio.objects.order_by('-published_date')
    context = {
        'items' : items
    }
    return render(request, 'portfolio/index.html', context)

def project(request, portfolio_id):
    project = get_object_or_404(Portfolio, pk=portfolio_id)
    context = {
        'project' : project
    }
    return render(request, 'portfolio/project.html', context)
