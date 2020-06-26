from django import forms
from django.contrib.auth.forms import UserCreationForm

from home.models import Contact


class Contact(forms.ModelForm):
    Email = forms.EmailField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder' : 'email'
        }
    ))
    Name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'name'
        }
    ))
    TellUs = forms.CharField( widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))



    class Meta:
        model = Contact
        fields = ("Email", "Name", "TellUs")


