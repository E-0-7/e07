from django.db import models
from katalog_buku.models import Buku

class DonasiBuku(models.Model):
    buku = models.OneToOneField(Buku, on_delete=models.CASCADE)
    jumlah_donasi = models.IntegerField()