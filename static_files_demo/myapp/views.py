from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def services(request):
    return render(request, 'myapp/services.html')

def contact(request):
    return render(request, 'myapp/contact.html')
