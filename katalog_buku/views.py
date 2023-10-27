from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import Buku

# Create your views here.
def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def get(request):
    all_product = Buku.objects.all()
    context = {'buku':all_product}
    return render(request,'katalog_buku.html', context)

