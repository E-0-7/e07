from django.forms import ModelForm
from .models import PinjamBuku

class PinjamFormByID(ModelForm):
    class Meta:
        model = PinjamBuku
        fields = ["durasi", "nomor_telepon", "alamat"]