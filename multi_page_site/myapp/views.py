from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')
