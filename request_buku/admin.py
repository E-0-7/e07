from django.contrib import admin

# Register your models here.
from .models import RequestBuku, StatusRequest

admin.site.register(RequestBuku)
admin.site.register(StatusRequest)