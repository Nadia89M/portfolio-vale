from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from contact.forms import ContactForm

def index(request):
    return render(request, 'pages/index.html', {})

def about(request):
    return render(request, 'pages/about.html', {})

def thanks(request):
    return render(request, 'pages/thanks.html', {})

def services(request):
    return render(request, 'pages/services.html', {})

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        #     Send email
            send_mail(
              'Contact Inquiry',
              'There has been an inquiry. Sign into the admin panel for more info.',
              'nadia.mohamed89@gmail.com',
              ['nadia.mohamed89@gmail.com'],
            )
            return thanks(request)
    return render(request, 'pages/contact.html', {'form': form})
