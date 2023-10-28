from django.db import models
from katalog_buku.models import Buku
from django.contrib.auth.models import User

# Create your models here.

class PinjamBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    durasi = models.IntegerField()
    nomor_telepon = models.IntegerField()
    alamat = models.TextField()
    metode_pembayaran = models.CharField(max_length=20, default='Debit', choices=[('Debit', 'Debit'), ('Kredit', 'Kredit'), ('E-Wallet', 'E-Wallet')], null = True, blank = True)