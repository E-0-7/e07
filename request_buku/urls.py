from django.urls import path
from .views import status_request_buku, add_request_buku_view, login_user
app_name = 'request_buku'

urlpatterns = [
    path('', status_request_buku, name='status_request_buku'),
    path('add/', add_request_buku_view, name='add_request_buku'),
    path('login/', login_user, name='login_user'),
]