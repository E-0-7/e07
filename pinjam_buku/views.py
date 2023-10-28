from django.shortcuts import render
from .models import PinjamBuku
from .forms import PinjamForm, PinjamFormByID
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from katalog_buku.models import Buku
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json

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

@csrf_exempt
def get_pinjam_data_ajax(request):
    user = request.user
    pinjam_buku = PinjamBuku.objects.filter(user=user)
    if user.is_authenticated:
        if request.user == "pustakawan":
            pinjam_buku = PinjamBuku.objects.all()
    data = []
    
    for buku_dipinjam in pinjam_buku:
        buku = buku_dipinjam.buku
        buku_dict = model_to_dict(buku)
        buku_dict['username'] = user.username
        buku_dict['durasi'] = buku_dipinjam.durasi
        buku_dict['nomor_telepon'] = buku_dipinjam.nomor_telepon
        buku_dict['alamat'] = buku_dipinjam.alamat

        data.append(buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def get_pinjam_data_ajax_user(request):
    user = request.user
    pinjam_buku = PinjamBuku.objects.filter(user=user)
    if user.is_authenticated:
        if request.user == "pustakawan":
            pinjam_buku = PinjamBuku.objects.all()
    data = []
    
    for buku_dipinjam in pinjam_buku:
        buku = buku_dipinjam.buku
        buku_dict = model_to_dict(buku)
        buku_dict['username'] = user.username
        buku_dict['durasi'] = buku_dipinjam.durasi
        buku_dict['nomor_telepon'] = buku_dipinjam.nomor_telepon
        buku_dict['alamat'] = buku_dipinjam.alamat

        data.append(buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

def add_pinjam_buku(request):
    form = PinjamForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        pinjam_buku = form.save(commit=False)
        pinjam_buku.user = request.user
        pinjam_buku.save()
        return HttpResponseRedirect(reverse('pinjam_buku:list_pinjam_buku'))
    
    context = {"form": form}
    return render(request, 'add_pinjam_buku.html', context)

def add_pinjam_buku_by_id(request,id):
    form = PinjamFormByID(request.POST or None)

    if form.is_valid() and request.method == "POST":
        pinjam_buku = form.save(commit=False)
        pinjam_buku.buku = get_object_or_404(Buku, pk = id)
        pinjam_buku.user = request.user
        pinjam_buku.save()
        return HttpResponseRedirect(reverse('pinjam_buku:list_pinjam_buku'))
    
    context = {"form": form}
    return render(request, 'add_pinjam_buku.html', context)

@csrf_exempt
def add_pinjam_buku_ajax(request, id):
    if request.method == "POST": 
        user = request.user
        buku = get_object_or_404(Buku, pk = id)
        durasi = request.POST.get('durasi')
        nomor_telepon = request.POST.get('nomor_telepon')
        alamat = request.POST.get('alamat')
   
        pinjam_buku_data = PinjamBuku(user=user, buku=buku, durasi=durasi, nomor_telepon=nomor_telepon, alamat=alamat, metode_pembayaran=None)
        pinjam_buku_data.save()

        return HttpResponse("Created", status=201)
    return HttpResponse("Not Created", status=400)