from django.urls import path
from .views import status_request_buku, add_request_buku_view, add_request_buku_ajax, get_request_data
from .views import json_format , diterima_request, ditolak_request, pending_request
from .views import delete_request_buku_ajax, search, team

app_name = 'request_buku'

urlpatterns = [
    path('', status_request_buku, name='status_request_buku'),
    path('add/', add_request_buku_view, name='add_request_buku'),
    path('json/', json_format, name='json_format'),
    path('search/', search, name='search'),
    path('get_item/', get_request_data, name='get_request_data'),
    path('add_ajax/', add_request_buku_ajax, name='add_request_buku_ajax'),
    path('diterima_request/', diterima_request, name='diterima_request'),
    path('ditolak_request/', ditolak_request, name='ditolak_request'),
    path('pending_request/', pending_request, name='pending_request'),
    path('delete_request_buku/<int:id>', delete_request_buku_ajax, name='delete_request_buku_ajax'),
    path('team/', team, name='team'),
]