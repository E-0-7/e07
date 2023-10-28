from django.urls import path
from .views import *

app_name = 'donasi_buku'

urlpatterns = [
    path('', donasi_buku_form, name='donasi_buku')
]