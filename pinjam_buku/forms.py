from django.forms import ModelForm
from .models import PinjamBuku

# class PinjamForm(ModelForm):
#     class Meta:
#         model = PinjamBuku
#         fields = ["buku", "durasi", "nomor_telepon", "alamat"]

class PinjamFormByID(ModelForm):
    class Meta:
        model = PinjamBuku
        fields = ["durasi", "nomor_telepon", "alamat"]