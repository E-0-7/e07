from .views import get_books, get, add_product_ajax
from django.urls import path

app_name = "katalog_buku"

urlpatterns = [
    path("json/", get_books, name="get_books"),
    path('', get, name="name"),
    path('/tambah-buku/', add_product_ajax, name="add_product_ajax")
]
