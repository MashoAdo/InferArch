from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from arch.forms import ContactForm

def home(request):
    return render(request, 'arch/base.html')

def about(request):
    return render(request, 'arch/about.html', {'title':'About'})

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'arch/success.html')
    return render(request, 'arch/contact.html', {'form': form})

