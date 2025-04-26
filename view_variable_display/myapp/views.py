from django.shortcuts import render

def show_variable(request):
    my_variable = "Hello, this is coming from views.py!"
    return render(request, 'show_variable.html', {'my_variable': my_variable})
