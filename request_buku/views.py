from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import RequestBuku, StatusRequest
from .forms import RequestBukuForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core import serializers
from django.contrib.auth import authenticate, login

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