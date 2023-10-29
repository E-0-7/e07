from django.urls import path
from .views import *

app_name = 'donasi_buku'

urlpatterns = [
    path('', donasi_buku_main, name='donasi_buku_main'),
    path('add/', donasi_buku_form, name='donasi_buku_form'),
    path('get-donations', get_donations, name='get_donations'),
    path('get-donations-by-book/<str:title>', get_donations_by_book, name='get_donations_by_book'),
    path('donate/', donate_book_ajax, name='donate_book_ajax'),
    path('delete/<int:id>', delete_donation_ajax, name='delete_donation_ajax')
]