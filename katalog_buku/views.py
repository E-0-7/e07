from django.shortcuts import render
from django.views import View
from .models import Buku

class Katalog_view(View):
    def get(self, request):
        all_product = Buku.objects.all()
        context = {'buku':all_product}
        return render(request,'katalog_buku.html', context)