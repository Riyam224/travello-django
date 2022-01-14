from django import forms
from django.forms.models import ModelForm
from .models import *



class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
