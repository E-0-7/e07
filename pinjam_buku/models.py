from django.db import models
from katalog_buku.models import Buku
from django.contrib.auth.models import User

# Create your models here.

class PinjamBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    durasi = models.IntegerField(default=1, null=True, blank=True)
    nomor_telepon = models.IntegerField(default=62, null=True, blank=True)
    alamat = models.TextField(default="UI", null=True, blank=True)