from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html', {})

def about(request):
    return render(request, 'pages/about.html', {})

def thanks(request):
    return render(request, 'pages/thanks.html', {})

def services(request):
    return render(request, 'pages/services.html', {})

def contact(request):
    return render(request, 'pages/services.html', {})