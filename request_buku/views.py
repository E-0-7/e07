from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import RequestBuku, StatusRequest, RequestStatusBuku
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
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='register:login')
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

def json_format(request):
    
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

def get_request_json(request):
    request_buku = RequestBuku.objects.filter(user=request.user)

    if request.user == 'pustakawan':
        request_buku = RequestBuku.objects.all()
    
    return HttpResponse(serializers.serialize('json', request_buku), content_type='application/json')


def get_status_json(request):
    status_requests = StatusRequest.objects.all()

    if request.user == 'pustakawan':
        status_requests = StatusRequest.objects.all()
    
    return HttpResponse(serializers.serialize('json', status_requests), content_type='application/json')
    

def get_request_data(request):
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

def team(request):
    return render(request, 'team.html')

def search(request):
    search_query = request.GET.get('search')
    if search_query:
        status_requests = StatusRequest.objects.filter(buku__user=request.user, buku__judul_buku__icontains=search_query)

        context = {
            'login_user': request.user,
            'status_requests': status_requests,
        }

        return render(request, 'search.html', context)

def get_request_status(request):
    status_requests = RequestStatusBuku.objects.filter()

    if request.user == 'pustakawan':
        status_requests = RequestStatusBuku.objects.all()
    
    return HttpResponse(serializers.serialize('json', status_requests), content_type='application/json')

@csrf_exempt
def create_request_buku(request):
    if request.method == 'POST':
            
        data = json.loads(request.body)

        new_request = RequestBuku.objects.create(
            user = request.user,
            judul_buku = data["judul_buku"],
            author = data["author"],
            tahun_publikasi = int(data["tahun_publikasi"]),
            isi_buku = data["deskripsi"],
            tanggal_request = date.today()
        )

        new_request.save()
        status_buku = StatusRequest(buku=new_request, status='PENDING')
        status_buku.save()

        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_request_buku(request, id):
    if request.method == "POST":
        try:
            item = get_object_or_404(RequestBuku, pk=id)
            item.delete()
            return HttpResponse("Deleted", status=200)
        except RequestBuku.DoesNotExist:
            return HttpResponse({'error': 'Item not found'}, status=404)
        except StatusRequest.DoesNotExist:
            return HttpResponse({'error': 'Item not found'}, status=404)



