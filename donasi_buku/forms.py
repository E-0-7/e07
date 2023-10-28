from django.forms import ModelForm
from django import forms
from .models import BukuDonasi

class DonationForm(ModelForm):
    class Meta:
        model = BukuDonasi
        fields = ["title", "author", "year", "image_url", "donation_amount"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'donation_amount': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required'}),
        }