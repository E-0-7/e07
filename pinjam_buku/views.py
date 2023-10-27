from django.shortcuts import render
from .models import PinjamBuku
from .forms import PinjamForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def list_pinjam_buku(request):
    user = request.user

    pinjam_buku = PinjamBuku.objects.filter(user=user)

    if user.is_authenticated:
        context = {
            'nama_aplikasi' : "Pinjam Buku",
            'login_user': user,
            'pinjam_buku': pinjam_buku,        
        }
        return render(request, 'request_buku.html', context)

def add_pinjam_buku(request):
    form = PinjamForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        pinjam_buku = form.save(commit=False)
        pinjam_buku.user = request.user
        pinjam_buku.save()
        return HttpResponseRedirect(reverse('request_buku:status_request_buku'))
    
    context = {"form": form}
    return render(request, 'add_request_buku.html', context)