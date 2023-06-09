from django.shortcuts import render
from .models import UserContact
from django.contrib import messages
from .models import UserContact, ContactDetails, Review, Socials, Projects


def home(request):
    
    contact_details = ContactDetails.objects.all()
    reviews = Review.objects.all()
    social_links = Socials.objects.all()
    projects = Projects.objects.all()
    
    title = 'Home'
    
    context = {
        'title':title, 
        'contact_details':contact_details, 
        'reviews':reviews, 
        'social_links':social_links, 
        'projects':projects
    }
    
    
    return render(request, 'main/home.html', context)


def contact(request):
    
    contact_details = ContactDetails.objects.all()
    social_links = Socials.objects.all()
    
    title = 'Contact'
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
            
        UserContact.objects.create(name=name, email=email, message=message)
        
        messages.success(
            request, 'Your message has been sent. We will get back to you soon.')
        
    context = {
        'title':title,
        'contact_details': contact_details, 
        'social_links': social_links,
    }
     
    
    return render(request, 'main/contact.html', context)


def about(request):
    
    contact_details = ContactDetails.objects.all()
    reviews = Review.objects.all()
    social_links = Socials.objects.all()
    
    title = 'About'
    
    context = {
        'title':title,
        'contact_details': contact_details,
        'reviews': reviews, 
        'social_links': social_links,
    }
    
    
    return render(request, 'main/about.html', context)


def works(request):
    
    contact_details = ContactDetails.objects.all()
    projects = Projects.objects.all()
    
    social_links = Socials.objects.all()
    
    title = 'Portfolio'
    
    context = {
        'title':title,
        'contact_details': contact_details, 
        'projects':projects, 
        'social_links': social_links,
    }
    
    
    return render(request, 'main/works.html', context)


def workDetails(request, pk):
    
    title = 'Portfolio Details'
    
    project = Projects.objects.get(id=pk)
    
    contact_details = ContactDetails.objects.all()
    social_links = Socials.objects.all()
    
    context = {
        'project':project,
        'contact_details': contact_details,
        'title':title, 
        'social_links': social_links,
    }
    
    
    return render(request, 'main/work-details.html', context)
