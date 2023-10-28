from django.urls import path
from .views import *

app_name = 'donasi_buku'

urlpatterns = [
    path('', donasi_buku_main, name='donasi_buku_main'),
    path('add/', donasi_buku_form, name='donasi_buku_form'),
]