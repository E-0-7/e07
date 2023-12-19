from .views import get_books, get, add_product_ajax, search, add_product_flutter
from django.urls import path

app_name = "katalog_buku"

urlpatterns = [
    path("json/", get_books, name="get_books"),
    path('', get, name="get"),
    path('search/', search, name="search"),
    path('tambah-buku/', add_product_ajax, name="add_product_ajax"),
    path('tambah-buku-flutter/', add_product_flutter, name='add_product_flutter'),
]
