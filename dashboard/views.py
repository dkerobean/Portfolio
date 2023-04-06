from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user.models import Profile 
from main.models import UserContact, ContactDetails
from .forms import ContactDetailsForm


@login_required(login_url="login")
def adminHome(request):
    
    user_messages = UserContact.objects.all()

    context = {
        'user_messages': user_messages
    }
    
    return render(request, 'dashboard/inbox/home.html', context)


@login_required(login_url="login")
def adminInbox(request):
    
    user_messages = UserContact.objects.all()
    
    context = {
        'user_messages':user_messages
    }
    
    return render(request,'dashboard/inbox/inbox.html', context)


@login_required(login_url="login")
def inboxRead(request, pk):
    
    user_messages = UserContact.objects.all()
    message = UserContact.objects.get(id=pk)
    
    context = {
        'message':message, 
        'user_messages': user_messages
    }
    

    return render(request, 'dashboard/inbox-read.html', context)


""" Start Of Contact Details """


@login_required(login_url="login")
def viewContact(request):
    
    contacts = ContactDetails.objects.all()
    
    context = {
        'contacts':contacts
    }
    
    return render(request, 'dashboard/contact/view-contact.html', context)
    

@login_required(login_url="login")
def createContact(request):
    
    form = ContactDetailsForm()
    
    if request.method == "POST":
        form = ContactDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Details Added!") 
            return redirect('create-contact')
        
    context = {
        'form':form
    }
    
    
    return render(request, 'dashboard/contact/create-contact.html', context)


@login_required(login_url="login")
def updateContact(request, pk):
    
    contact = ContactDetails.objects.get(id=pk)
    
    form = ContactDetailsForm(instance=contact)
    
    if request.method == "POST":
        form = ContactDetailsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Updated!")
            return redirect('view-contact')
        
    context = {
        'form':form
    }
    
    return render(request, 'dashboard/contact/update-contact.html', context)


def adminLogin(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Success')
            return redirect('admin-home')
        else:
            messages.error(request, 'Username or password incorrect')
            
            
    return render(request, 'dashboard/login.html')