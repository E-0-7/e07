from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import RequestBuku, StatusRequest
from .forms import RequestBukuForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core import serializers
import json
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt 
from datetime import date, datetime
from django.forms.models import model_to_dict

# Create your views here.
def status_request_buku(request):
    user = request.user

    request_buku = RequestBuku.objects.filter(user=user)
    status_request = StatusRequest.objects.filter(buku__user=user)
    
    if user.username == 'pustakawan':
        request_buku = RequestBuku.objects.all()
        status_request = StatusRequest.objects.all()

    if user.is_authenticated:
        context = {
            'nama_aplikasi' : "Request Buku",
            'login_user': user,
            'request_buku': request_buku,
            'status_request': status_request,
            'jumlah_request': len(request_buku),
        }
        return render(request, 'request_buku.html', context)
    else:
        return redirect('login')

def add_request_buku_view(request):
    form = RequestBukuForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        request_buku = form.save(commit=False)
        request_buku.user = request.user
        status_buku = StatusRequest(buku=request_buku, status='PENDING')
        request_buku.save()
        status_buku.save()
        return HttpResponseRedirect(reverse('request_buku:status_request_buku'))
    
    context = {"form": form}
    return render(request, 'add_request_buku.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('request_buku:status_request_buku')
        else:
            messages.info(request, 'Username atau password salah')
    context = {}
    return render(request, 'login.html', context)

def json_format(request):
    user = request.user
    status_requests = StatusRequest.objects.all()
    data = []
    
    for status_request in status_requests:
        request_buku = status_request.buku
        request_buku_dict = model_to_dict(request_buku)
        request_buku_dict['status'] = status_request.status

        request_date = status_request.buku.tanggal_request

        request_buku_dict['tanggal_request'] = request_date.strftime("%b. %d, %Y") 
        
        
        data.append(request_buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

def get_request_data(request):
    status_requests = StatusRequest.objects.filter(buku__user=request.user)

    data = []
    
    for status_request in status_requests:
        request_buku = status_request.buku
        request_buku_dict = model_to_dict(request_buku)
        request_buku_dict['status'] = status_request.status

        request_date = status_request.buku.tanggal_request

        request_buku_dict['tanggal_request'] = request_date.strftime("%b. %d, %Y") 
        data.append(request_buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def add_request_buku_ajax(request):
    if request.method == "POST":
        user = request.user
        judul_buku = request.POST.get('judul_buku')
        author = request.POST.get('author')
        tahun_publikasi = request.POST.get('tahun_publikasi')
        isi_buku = request.POST.get('isi_buku')
        
        request_buku_data = RequestBuku(user=user, judul_buku=judul_buku, author=author, tahun_publikasi=tahun_publikasi, isi_buku=isi_buku, tanggal_request=date.today())
        request_buku_data.save()
        status_buku = StatusRequest(buku=request_buku_data, status='PENDING')
        status_buku.save()

        return HttpResponse("Created", status=201)
    return HttpResponse("Not Created", status=400)

@csrf_exempt
def delete_request_buku_ajax(request, id):
    if request.method == "DELETE":
        try:
            item = get_object_or_404(RequestBuku, pk=id)
            item.delete()
            return HttpResponse("Deleted", status=200)
        except RequestBuku.DoesNotExist:
            return HttpResponse({'error': 'Item not found'}, status=404)
        except StatusRequest.DoesNotExist:
            return HttpResponse({'error': 'Item not found'}, status=404)

def filter_data_by_judul_buku(request):
    user = request.user
    status_requests = StatusRequest.objects.filter(buku__user=user).order_by('buku__judul_buku')
    data = []
    
    for status_request in status_requests:
        request_buku = status_request.buku
        request_buku_dict = model_to_dict(request_buku)
        request_buku_dict['status'] = status_request.status

        request_date = status_request.buku.tanggal_request

        request_buku_dict['tanggal_request'] = request_date.strftime("%b. %d, %Y") 
        data.append(request_buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

def pending_request(request):
    status_requests = StatusRequest.objects.filter(buku__user=request.user, status='PENDING')
    data = []
    
    for status_request in status_requests:
        request_buku = status_request.buku
        request_buku_dict = model_to_dict(request_buku)
        request_buku_dict['status'] = status_request.status

        request_date = status_request.buku.tanggal_request

        request_buku_dict['tanggal_request'] = request_date.strftime("%b. %d, %Y") 
        data.append(request_buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

def diterima_request(request):
    status_requests = StatusRequest.objects.filter(buku__user=request.user, status='DITERIMA')
    data = []
    
    for status_request in status_requests:
        request_buku = status_request.buku
        request_buku_dict = model_to_dict(request_buku)
        request_buku_dict['status'] = status_request.status

        request_date = status_request.buku.tanggal_request

        request_buku_dict['tanggal_request'] = request_date.strftime("%b. %d, %Y") 
        data.append(request_buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

def ditolak_request(request):
    status_requests = StatusRequest.objects.filter(buku__user=request.user, status='DITOLAK')
    data = []
    
    for status_request in status_requests:
        request_buku = status_request.buku
        request_buku_dict = model_to_dict(request_buku)
        request_buku_dict['status'] = status_request.status

        request_date = status_request.buku.tanggal_request

        request_buku_dict['tanggal_request'] = request_date.strftime("%b. %d, %Y") 
        data.append(request_buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

def filter_data_by_author(request):
    user = request.user
    status_requests = StatusRequest.objects.filter(buku__user=user).order_by('buku__author')
    data = []
    
    for status_request in status_requests:
        request_buku = status_request.buku
        request_buku_dict = model_to_dict(request_buku)
        request_buku_dict['status'] = status_request.status

        request_date = status_request.buku.tanggal_request

        request_buku_dict['tanggal_request'] = request_date.strftime("%b. %d, %Y") 
        data.append(request_buku_dict)
    
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, content_type='application/json')

