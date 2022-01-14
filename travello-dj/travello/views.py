from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from .models import Destination
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    dests = Destination.objects.all()
    context = {
        'dests': dests
    }
    return render(request , 'index.html' , context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    else:
        form = ContactForm()
            
            
    
    context = {
        'form': form
    }
    return render(request , 'contact.html' , context)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request , 'register.html' , context) 