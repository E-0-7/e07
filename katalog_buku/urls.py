from .views import get_books
from django.urls import path

app_name = "katalog_buku"

urlpatterns = [
    path("json/", get_books, name="get_books"),
]
