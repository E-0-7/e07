from django.shortcuts import render
from katalog_buku.models import Buku
from .models import BukuDonasi

def donasi_buku_form(request):
    if request.method == "POST":
        name = request.POST["name"]
        title = request.POST["title"]
        author = request.POST["author"]
        year = request.POST["year"]
        edition = request.POST["edition"]
        donation_amount = request.POST["amount"]
        image_url = request.POST["imageUrl"]

        book = Buku.objects.filter(judul=name)
        print(book)
        if not book.exists():
            book = Buku(judul=title, image=image_url, penulis=author, tahun_terbit=year, jumlah=0)
        else:
            book = book[0]
        
        book.jumlah += int(donation_amount)
        donation = BukuDonasi(book=book, donator=name, donation_amount=donation_amount)

        book.save()
        donation.save()

    return render(request, 'donasi_buku.html', {})

def donasi_buku_main(request):
    donations = BukuDonasi.objects.all()

    total_donations = 0
    for donation in donations:
        total_donations += donation.donation_amount

    context = {
        'donations': donations,
        'total_donations': total_donations,
    }

    return render(request, 'main_donasi_buku.html', context)

