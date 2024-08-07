# forms.py
from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'city', 'zip', 'country']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }