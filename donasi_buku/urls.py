from django.urls import path
from .views import *

app_name = 'donasi_buku'

urlpatterns = [
    path('', donasi_buku_main, name='donasi_buku_main'),
    path('get-donations/', get_donations, name='get_donations'),
    path('get-donations-by-book/<str:title>', get_donations_by_book, name='get_donations_by_book'),
    path('get-donations-by-author/<str:author>', get_donations_by_author, name='get_donations_by_author'),
    path('donate/', donate_book_ajax, name='donate_book_ajax'),
    path('delete/<int:id>', delete_donation_ajax, name='delete_donation_ajax'),
    path('donate-flutter/', donate_book_flutter, name='donate_flutter'),
    path('delete-flutter/', delete_book_flutter, name='delete_flutter'),
    path('approve-flutter/', approve_book_flutter, name='approve_book_flutter'),
    path('reject-flutter/', reject_book_flutter, name='reject_book_flutter'),
]