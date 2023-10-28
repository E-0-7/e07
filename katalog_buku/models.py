from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    isbn = models.CharField(max_length=255, null=True, blank=True)
    book_title = models.CharField(max_length=255, null=True, blank=True)
    book_author = models.CharField(max_length=255, null=True, blank=True)
    tahun_publikasi = models.IntegerField(null=True, blank=True)
    penerbit = models.CharField(max_length=255, null=True, blank=True)
    url_foto_kecil = models.URLField(null=True, blank=True)
    url_foto_medium = models.URLField(null=True, blank=True)
    url_foto_large = models.URLField(null=True, blank=True)