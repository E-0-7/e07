from django.shortcuts import render
from katalog_buku.models import Buku

def donasi_buku_form(request):
    if request.method == "POST":
        name = request.POST["name"]
        book = Buku.objects.filter(judul=name)
        if not book.exists:
            book = Buku(judul)
    return render(request, 'donasi_buku.html', {})
