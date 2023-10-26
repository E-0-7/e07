from django import forms
from .models import Buku

class FormBuku(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ["judul", "penulis", "tahun_terbit", "image", "jumlah"]