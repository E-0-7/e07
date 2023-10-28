from django.urls import path
from .views import list_pinjam_buku, add_pinjam_buku, add_pinjam_buku_by_id, get_pinjam_data_ajax, add_pinjam_buku_ajax, get_pinjam_data_ajax_user
app_name = 'pinjam_buku'

urlpatterns = [
    path('', list_pinjam_buku, name='list_pinjam_buku'),
    path('add_pinjam_buku/', add_pinjam_buku, name='add_pinjam_buku'),
    path('add_pinjam_buku/<int:id>', add_pinjam_buku_by_id, name='add_pinjam_buku_by_id'),
    path('get_pinjam_data_ajax/', get_pinjam_data_ajax, name='get_pinjam_data_ajax'),
    path('add_pinjam_buku_ajax/<int:id>', add_pinjam_buku_ajax, name='add_pinjam_buku_ajax'),
    path('json/', get_pinjam_data_ajax_user, name='get_pinjam_data_ajax_user'),
]