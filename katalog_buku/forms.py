from django import forms
from .models import Buku

class ProductForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ["isbn", "book_title", "book_author", "tahun_publikasi", "penerbit", "url_foto_kecil", "url_foto_medium", "url_foto_large", "book_price"]
