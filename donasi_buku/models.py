from django.db import models
from katalog_buku.models import Buku
from datetime import date

class BukuDonasi(models.Model):
    book = models.OneToOneField(Buku, on_delete=models.CASCADE)
    donator = models.CharField(max_length=255)
    donation_date = models.DateField(default=date.today)
    donation_amount = models.IntegerField()