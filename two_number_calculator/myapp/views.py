from django.shortcuts import render
from .forms import NumberForm

def add_numbers(request):
    result = None
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['num1']
            n2 = form.cleaned_data['num2']
            result = n1 + n2
    else:
        form = NumberForm()

    return render(request, 'myapp/calc.html', {
        'form': form,
        'result': result
    })
