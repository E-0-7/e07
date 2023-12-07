from django.urls import path
from .views import status_request_buku, add_request_buku_view, add_request_buku_ajax, get_request_data
from .views import json_format, get_request_status
from .views import delete_request_buku_ajax, search, team, create_request_buku, get_request_json
from .views import get_status_json

app_name = 'request_buku'

urlpatterns = [
    path('', status_request_buku, name='status_request_buku'),
    path('add/', add_request_buku_view, name='add_request_buku'),
    path('json/', json_format, name='json_format'),
    path('search/', search, name='search'),
    path('get_item/', get_request_data, name='get_request_data'),
    path('add_ajax/', add_request_buku_ajax, name='add_request_buku_ajax'),
    path('delete_request_buku/<int:id>', delete_request_buku_ajax, name='delete_request_buku_ajax'),
    path('team/', team, name='team'),
    path('create-request-buku/', create_request_buku, name='create_request_buku'),
    path('get_request_json/', get_request_json, name='get_request_json'),
    path('get_status_json/', get_status_json, name='get_status_json'),
    path('get_request_status/', get_request_status, name='get_request_status'),
]
