from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import Buku
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.db.models import Q

# Create your views here.
def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def get(request):
    all_product = Buku.objects.all()
    context = {'buku':all_product}
    if request.user.is_authenticated:
        context = {
            'buku': all_product,
            'login_user': request.user
            }
        if request.user.username != "pustakawan":
            return render(request,'katalog_users.html', context)
        if request.user.username == "pustakawan":
            return render(request,'katalog_pustakawan.html', context)
    return render(request,'katalog_buku.html', context)

def search(request):
    buku_dicari = request.GET.get('search')
    print("buku_dicari: ", buku_dicari)
    if buku_dicari:
        hasil_buku = Buku.objects.filter(Q(book_title__icontains=buku_dicari) | Q(book_author__icontains=buku_dicari) | Q(penerbit__icontains=buku_dicari) | Q(tahun_publikasi__icontains=buku_dicari))

        context = {'buku': hasil_buku}

        return render(request, 'search_buku.html', context)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        isbn = request.POST.get("isbn")
        book_title = request.POST.get("book_title")
        book_author = request.POST.get("book_author")
        tahun_publikasi = request.POST.get("tahun_publikasi")
        penerbit = request.POST.get("penerbit")
        url_foto_kecil = request.POST.get("url_foto_kecil")
        url_foto_medium = request.POST.get("url_foto_medium")
        url_foto_large = request.POST.get("url_foto_large")
        book_price = request.POST.get("book_price")

        new_product = Buku(isbn=isbn, book_title=book_title, book_author=book_author, tahun_publikasi=tahun_publikasi, penerbit=penerbit, 
                           url_foto_kecil=url_foto_kecil, url_foto_medium=url_foto_medium, url_foto_large=url_foto_large, book_price=book_price)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

