from django.shortcuts import render
from .models import BeliBuku
from .forms import BeliFormByID
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from katalog_buku.models import Buku
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers
import json

# Create your views here.
def list_beli_buku(request):
    user = request.user
    beli_buku = BeliBuku.objects.filter(user=user)
    buku = Buku.objects.all()

    if user.is_authenticated:
        context = {
            'nama_aplikasi' : "Beli Buku",
            'buku' : buku,
            'login_user': user,
            'beli_buku': beli_buku,
        }
        return render(request, 'list_beli_buku.html', context)
    
def get_katalog_beli_buku(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def display_beli_buku(request):
    user = request.user
    buku = Buku.objects.all()

    if request.user.is_authenticated:
        context = {
            'nama_aplikasi' : "Beli Buku",
            'buku':buku,
            'login_user': user,
        }
        return render(request,'katalog_beli_buku.html', context)

@csrf_exempt
def get_beli_data_ajax(request):
    user = request.user
    beli_buku = BeliBuku.objects.filter(user=user)
    if user.is_authenticated:
        if request.user.username == "pustakawan":
            beli_buku = BeliBuku.objects.all()
        else:
            beli_buku = BeliBuku.objects.filter(user=user)
    else:
        return HttpResponse("User not authenticated", status=401)
    data = []
    
    for buku_dibeli in beli_buku:
        buku = buku_dibeli.buku
        buku_dict = model_to_dict(buku)
        buku_dict['username'] = user.username
        buku_dict['jumlah_buku'] = buku_dibeli.jumlah_buku
        buku_dict['nomor_telepon'] = buku_dibeli.nomor_telepon
        buku_dict['alamat'] = buku_dibeli.alamat
        buku_dict['metode_pembayaran'] = buku_dibeli.metode_pembayaran

        data.append(buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def add_beli_buku_ajax(request, id):
    if request.method == "POST": 
        user = request.user
        buku = get_object_or_404(Buku, pk=id)
        jumlah_buku = request.POST.get('jumlah_buku')
        nomor_telepon = request.POST.get('nomor_telepon')
        alamat = request.POST.get('alamat')
        metode_pembayaran = request.POST.get('metode_pembayaran', 'COD')
   
        beli_buku_data = BeliBuku(user=user, buku=buku, jumlah_buku=jumlah_buku, nomor_telepon=nomor_telepon, alamat=alamat, metode_pembayaran=metode_pembayaran)
        beli_buku_data.save()

        return HttpResponse("Created", status=201)
    return HttpResponse("Not Created", status=400)


@csrf_exempt
def create_beli_buku(request):
    if request.method == "POST":
        data = json.loads(request.body)
        buku_ambil = Buku.objects.get(pk=int(data["buku"]))

        beli_beli = BeliBuku.objects.create(
            user=request.user,
            buku=buku_ambil,
            jumlah_buku=int(data["jumlah"]),
            nomor_telepon=int(data["nomor_telepon"]),
            alamat=data["alamat"],
            metode_pembayaran=data["metode_pembayaran"]
        )

        beli_beli.save()
        response_data = {"status": "success"}

        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)



def get_beli_buku(request):
    beli_buku = BeliBuku.objects.all()

    return HttpResponse(serializers.serialize('json', beli_buku), content_type='application/json')