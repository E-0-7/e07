from django.urls import path
from .views import status_request_buku, add_request_buku_view, login_user, add_request_buku_ajax, get_request_data
from .views import json_format

app_name = 'request_buku'

urlpatterns = [
    path('', status_request_buku, name='status_request_buku'),
    path('add/', add_request_buku_view, name='add_request_buku'),
    path('login/', login_user, name='login_user'),
    path('json/', json_format, name='json_format'),
    path('get_item/', get_request_data, name='get_request_data'),
    path('add_ajax/', add_request_buku_ajax, name='add_request_buku_ajax'),
]