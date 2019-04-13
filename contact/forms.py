from django import forms
from django.core import validators
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), 
                            validators=[validators.EmailValidator()])
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    contact_date = forms.DateTimeField(required=False, widget=forms.HiddenInput())
    class Meta():
        model = Contact
        fields = ('name','email','message') 