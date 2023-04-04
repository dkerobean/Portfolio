from django.shortcuts import render
from .models import UserContact
from django.contrib import messages


def home(request):
    
    return render(request, 'main/home.html')


def contact(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
            
        UserContact.objects.create(name=name, email=email, message=message)
        
        messages.success(
            request, 'Your message has been sent. We will get back to you soon.')
    else:
        messages.error(
            request, 'An Error Occured, Try again ')
    
    
    return render(request, 'main/contact.html')


def about(request):
    
    return render(request, 'main/about.html')


def works(request):
    
    return render(request, 'main/works.html')