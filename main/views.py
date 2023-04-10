from django.shortcuts import render
from .models import UserContact
from django.contrib import messages
from .models import UserContact


def home(request):
    
    title = 'Home'
    
    context = {
        'title':title
    }
    
    return render(request, 'main/home.html', context)


def contact(request):
    
    title = 'Contact'
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
            
        UserContact.objects.create(name=name, email=email, message=message)
        
        messages.success(
            request, 'Your message has been sent. We will get back to you soon.')
        
    context = {
        'title':title
    }
     
    
    return render(request, 'main/contact.html', context)


def about(request):
    
    title = 'About'
    
    context = {
        'title':title
    }
    
    return render(request, 'main/about.html', context)


def works(request):
    
    title = 'Portfolio'
    
    context = {
        'title':title
    }
    
    return render(request, 'main/works.html', context)