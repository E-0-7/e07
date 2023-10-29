from django.db import models
from katalog_buku.models import Buku
from django.contrib.auth.models import User

# Create your models here.

class BeliBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    jumlah_buku = models.IntegerField(default=1, null=True, blank=True)
    nomor_telepon = models.IntegerField(default=62, null=True, blank=True)
    alamat = models.TextField(default="UI", null=True, blank=True)
    book_price = models.IntegerField(null=True, blank=True)

    METODE_PEMBAYARAN_CHOICES = [
        ('COD', 'COD (Cash on Delivery)'),
        ('CARD', 'Credit/Debit Card'),
        ('EWALLET', 'E-Wallet'),
    ]

    metode_pembayaran = models.CharField(max_length=7, choices=METODE_PEMBAYARAN_CHOICES, default='COD')