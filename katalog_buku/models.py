from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    judul = models.CharField(max_length=255)
    image = models.URLField()
    penulis = models.CharField(max_length=255)
    tahun_terbit = models.IntegerField()
    jumlah = models.IntegerField()