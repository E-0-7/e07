from django.db import models
from django.contrib.auth.models import User
from katalog_buku.models import Buku
from datetime import date

class BukuDonasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donator = models.CharField(max_length=255)
    donation_date = models.DateField(default=date.today)
    donation_amount = models.IntegerField()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    image_url = models.URLField(null=True)
    status = models.CharField(max_length=15, default='PENDING', choices=[('PENDING', 'PENDING'), ('DITERIMA', 'DITERIMA'), ('DITOLAK', 'DITOLAK')])

    @staticmethod
    def compare(a: 'BukuDonasi', b: 'BukuDonasi') -> int:
        if a.status == 'PENDING' and b.status != 'PENDING':
            return -1
        elif a.status != 'PENDING' and b.status == 'PENDING':
            return 1
        else:
            if a.donation_date < b.donation_date:
                return -1
            elif a.donation_date > b.donation_date:
                return 1
            else:
                return 0