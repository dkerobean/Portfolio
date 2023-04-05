from django.shortcuts import render, redirect
from user.models import Profile 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from main.models import UserContact


@login_required(login_url="login")
def adminHome(request):
    
    user_messages = UserContact.objects.all()

    context = {
        'user_messages': user_messages
    }
    
    return render(request, 'dashboard/home.html', context)


@login_required(login_url="login")
def adminInbox(request):
    
    user_messages = UserContact.objects.all()
    
    context = {
        'user_messages':user_messages
    }
    
    return render(request,'dashboard/inbox.html', context)


@login_required(login_url="login")
def inboxRead(request, pk):
    
    user_messages = UserContact.objects.all()
    message = UserContact.objects.get(id=pk)
    
    context = {
        'message':message, 
        'user_messages': user_messages
    }
    

    return render(request, 'dashboard/inbox-read.html', context)


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