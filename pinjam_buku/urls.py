from django.urls import path
from .views import list_pinjam_buku, add_pinjam_buku
app_name = 'pinjam_buku'

urlpatterns = [
    path('', list_pinjam_buku, name='list_pinjam_buku'),
    path('add_pinjam_buku/', add_pinjam_buku, name='add_pinjam_buku'),
]