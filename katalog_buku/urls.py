from .views import get_books
from django.urls import path

app_name = "book"

urlpatterns = [
    path("json/", get_books, name="get_books"),
]
