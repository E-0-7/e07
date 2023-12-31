from django.shortcuts import render
from .models import PinjamBuku
from .forms import PinjamFormByID
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from katalog_buku.models import Buku
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core import serializers
import json
from django.contrib.auth.models import User


# Create your views here.
def list_pinjam_buku(request):
    user = request.user

    pinjam_buku = PinjamBuku.objects.filter(user=user)
    buku = Buku.objects.all()

    if user.is_authenticated:
        context = {
            'nama_aplikasi' : "Pinjam Buku",
            'buku' : buku,
            'login_user': user,
            'pinjam_buku': pinjam_buku,        
        }
        return render(request, 'list_pinjam_buku.html', context)
    
def get_katalog_pinjam_buku(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def display_pinjam_buku(request):
    user = request.user
    buku = Buku.objects.all()

    if request.user.is_authenticated:
        context = {
            'nama_aplikasi' : "Pinjam Buku",
            'buku':buku,
            'login_user': user,
        }
        return render(request,'katalog_pinjam_buku.html', context)

def get_pinjam_data_ajax(request):
    user = request.user
    if user.is_authenticated:
        if request.user.username == "pustakawan":
            pinjam_buku = PinjamBuku.objects.all()
        else:
            pinjam_buku = PinjamBuku.objects.filter(user=user)
    else:
        return HttpResponse("User not authenticated", status=401)

    data = []
    
    for buku_dipinjam in pinjam_buku:
        buku = buku_dipinjam.buku
        buku_dict = model_to_dict(buku)
        buku_dict['username'] = buku_dipinjam.user.username  # Use the actual user who borrowed the book
        buku_dict['durasi'] = buku_dipinjam.durasi
        buku_dict['nomor_telepon'] = buku_dipinjam.nomor_telepon
        buku_dict['alamat'] = buku_dipinjam.alamat

        data.append(buku_dict)
    
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def add_pinjam_buku_ajax(request, id):
    if request.method == "POST": 
        user = request.user
        buku = get_object_or_404(Buku, pk = id)
        durasi = request.POST.get('durasi')
        nomor_telepon = request.POST.get('nomor_telepon')
        alamat = request.POST.get('alamat')
   
        pinjam_buku_data = PinjamBuku(user=user, buku=buku, durasi=durasi, nomor_telepon=nomor_telepon, alamat=alamat)
        pinjam_buku_data.save()

        return HttpResponse("Created", status=201)
    return HttpResponse("Not Created", status=400)

@csrf_exempt
def create_pinjam_buku(request):
    if request.method == "POST":
        data = json.loads(request.body)
        buku_ambil = Buku.objects.get(pk=int(data["buku"]))
                
        new_pinjam = PinjamBuku.objects.create(
            user = request.user,
            buku = buku_ambil,
            durasi = int(data["durasi"]),
            nomor_telepon = int(data["nomor_telepon"]),
            alamat = data["alamat"],
        )

        new_pinjam.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


def get_pinjam_buku(request):
    pinjam_buku = PinjamBuku.objects.all()

    return HttpResponse(serializers.serialize('json', pinjam_buku), content_type='application/json')