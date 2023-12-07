from django.contrib import admin

# Register your models here.
from .models import RequestBuku, StatusRequest, RequestStatusBuku

admin.site.register(RequestBuku)
admin.site.register(StatusRequest)
admin.site.register(RequestStatusBuku)