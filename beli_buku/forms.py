from django.forms import ModelForm
from .models import BeliBuku

class BeliFormByID(ModelForm):
    class Meta:
        model = BeliBuku
        fields = ["jumlah_buku", "nomor_telepon", "alamat", "book_price", "metode_pembayaran"]