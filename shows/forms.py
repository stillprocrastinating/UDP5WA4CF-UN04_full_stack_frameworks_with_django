from django import forms
from django.forms import ModelForm
from shows.models import ShippingInfo


class ShippingForm(ModelForm):
    class Meta:

        model = ShippingInfo
        exclude = ['user']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone (optional)'
            }),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'address': forms.TextInput(attrs={
                'placeholder': 'Street address'
            }),
            'address_line_two': forms.TextInput(attrs={
                'placeholder': 'Address instructions'
            }),
            'city': forms.TextInput(attrs={'placeholder': 'Town'}),
            'postcode': forms.TextInput(attrs={'placeholder': 'Post code'})
        }
