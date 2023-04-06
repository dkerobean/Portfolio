from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user.models import Profile 
from main.models import UserContact, ContactDetails, Review
from .forms import ContactDetailsForm, ReviewForm


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


#Start Contact Details

@login_required(login_url="login")
def viewContact(request):
    
    user_messages = UserContact.objects.all()
    contacts = ContactDetails.objects.all()
    
    context = {
        'contacts':contacts, 
        'user_messages':user_messages
    }
    
    return render(request, 'dashboard/contact/view-contact.html', context)
    

@login_required(login_url="login")
def createContact(request):
    
    user_messages = UserContact.objects.all()
    form = ContactDetailsForm()
    
    if request.method == "POST":
        form = ContactDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Details Added!") 
            return redirect('create-contact')
        
    context = {
        'form':form, 
        'user_messages': user_messages
    }
    
    
    return render(request, 'dashboard/contact/create-contact.html', context)


@login_required(login_url="login")
def updateContact(request, pk):
    
    contact = ContactDetails.objects.get(id=pk)
    user_messages = UserContact.objects.all()
    
    form = ContactDetailsForm(instance=contact)
    
    if request.method == "POST":
        form = ContactDetailsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Updated!")
            return redirect('view-contact')
        
    context = {
        'form':form, 
        'user_messages': user_messages
    }
    
    return render(request, 'dashboard/contact/update-contact.html', context)


""" USER REVIEWS """

@login_required(login_url="login")
def createReview(request):
    
    user_messages = UserContact.objects.all()
    
    form = ReviewForm()
    
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review Added!')
            return redirect('create-review')
    
    context = {
        'user_messages':user_messages, 
        'form':form
    }
    
    return render(request, 'dashboard/user_reviews/create-review.html', context)


@login_required(login_url="login")
def viewReview(request):
    
    user_messages = UserContact.objects.all()
    
    reviews = Review.objects.all()
    
    context = {
        'reviews':reviews, 
        'user_messages': user_messages
    }
    
    return render(request,'dashboard/user_reviews/view-reviews.html', context)


@login_required(login_url="login")
def updateReview(request, pk):
    
    user_messages = UserContact.objects.all()
    
    review = Review.objects.get(id=pk)
    
    form = ReviewForm(instance=review)
    
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review Updated')
            return redirect('view-reviews')
    
    context = {
        'user_messages': user_messages, 
        'form':form
    }
    
    return render(request, 'dashboard/user_reviews/view-reviews.html', context)


""" ADMIN LOGIN """

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