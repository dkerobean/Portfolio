from django.shortcuts import render


def home(request):
    
    return render(request, 'main/home.html')


def contact(request):
    
    return render(request, 'main/contact.html')


def about(request):
    
    return render(request, 'main/about.html')


def works(request):
    
    return render(request, 'main/works.html')