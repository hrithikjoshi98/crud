from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name': 'Name', 
                  'email': 'Email',
                  'password': 'Password'}
        widgets = {'password':forms.PasswordInput()}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'desc', 'price', 'quantity']
        