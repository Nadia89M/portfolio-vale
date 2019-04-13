from django.shortcuts import get_object_or_404, render
from .models import Portfolio


def index(request):
    return render(request, 'portfolio/index.html', {})
