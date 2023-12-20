from django.urls import path
from .views import list_beli_buku, get_beli_data_ajax, add_beli_buku_ajax, get_katalog_beli_buku, display_beli_buku, create_beli_buku, get_beli_buku
app_name = 'beli_buku'

urlpatterns = [
    path('list_beli_buku/', list_beli_buku, name='list_beli_buku'),
    path('get_beli_data_ajax/', get_beli_data_ajax, name='get_beli_data_ajax'),
    path('add_beli_buku_ajax/<int:id>', add_beli_buku_ajax, name='add_beli_buku_ajax'),
    path('get_katalog_beli_buku/', get_katalog_beli_buku, name='get_katalog_beli_buku'),
    path('', display_beli_buku, name='display_beli_buku'),
    path('create_beli_buku/', create_beli_buku, name='create_beli_buku'),
    path('get_beli_buku/', get_beli_buku, name='get_beli_buku'),
]