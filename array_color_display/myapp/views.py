from django.shortcuts import render

def array_display(request):
    numbers = list(range(1, 21))   # example: 1–20
    return render(request, 'myapp/display.html', {'numbers': numbers})
