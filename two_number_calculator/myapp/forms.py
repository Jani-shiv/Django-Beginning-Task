from django import forms

class NumberForm(forms.Form):
    num1 = forms.IntegerField(label="First Number", widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter first number'
    }))
    num2 = forms.IntegerField(label="Second Number", widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter second number'
    }))
