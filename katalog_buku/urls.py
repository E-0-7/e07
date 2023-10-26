from django.urls import path
from .views import Katalog_view

urlpatterns = [
   path("",Katalog_view.as_view(), name= "all-product"),
]