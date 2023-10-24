from django import forms
from django.forms import ModelForm
from .models import RequestBuku
from django.contrib.auth.models import User

class RequestBukuForm(ModelForm):
    class Meta:
        model = RequestBuku
        fields = ['judul_buku', 'author', 'tahun_publikasi']
        widget = {
            'judul_buku': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'tahun_publikasi': forms.NumberInput(attrs={'class': 'form-control'}),
        }