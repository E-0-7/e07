"""
URL configuration for flex_lib project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("request_buku/", include("request_buku.urls"), name="request_buku"),
    path('donasi_buku/', include('donasi_buku.urls'), name="donasi_buku"),
    path("pinjam_buku/", include("pinjam_buku.urls"), name="pinjam_buku"),
    path("beli_buku/", include('beli_buku.urls'), name="beli_buku"),
    path('', include('katalog_buku.urls'), name="katalog_buku"),
    path('auth/', include('register.urls'), name="auth"),
]
