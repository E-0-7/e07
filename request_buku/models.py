from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RequestBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    judul_buku = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, default='Tidak diketahui')
    tahun_publikasi = models.IntegerField(null=True, default=-1)
    isi_buku = models.TextField(null=True, default='Tidak diketahui')
    tanggal_request = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.judul_buku} - {self.user}"

class StatusRequest(models.Model):
    buku = models.ForeignKey(RequestBuku, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='PENDING', choices=[('PENDING', 'PENDING'), ('DITERIMA', 'DITERIMA'), ('DITOLAK', 'DITOLAK')])

    def __str__self(self):
        return f"{self.buku.judul_buku} - {self.status}"
