from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Print to terminal
            print("📝 Form Submission:")
            for key, val in form.cleaned_data.items():
                print(f"  {key}: {val}")
            # Redirect or re-render with success flag
            return render(request, 'myapp/form.html', {
                'form': ContactForm(),  # empty form
                'success': True
            })
    else:
        form = ContactForm()

    return render(request, 'myapp/form.html', {'form': form})
