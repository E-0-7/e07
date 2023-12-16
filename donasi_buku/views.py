from django.shortcuts import render
from katalog_buku.models import Buku
from .models import BukuDonasi
from .forms import DonationForm
from django.http.response import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url='register:login')
def donasi_buku_main(request):
    form = DonationForm(request.POST or None)
    donations = BukuDonasi.objects.filter(user=request.user)

    total_donations = 0
    for donation in donations:
        total_donations += donation.donation_amount

    context = {
        'donations': donations,
        'total_donations': total_donations,
        'login_user': request.user,
        'form': form,
    }

    return render(request, 'main_donasi_buku.html', context)

def get_donations(request):
    donations = BukuDonasi.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", donations), content_type="application/json")

def get_donations_by_book(request, title):
    title = title.replace("+", " ")
    donations = BukuDonasi.objects.filter(user=request.user).filter(title__icontains=title)
    return HttpResponse(serializers.serialize("json", donations), content_type="application/json")

def get_donations_by_author(request, author):
    author = author.replace("+", " ")
    donations = BukuDonasi.objects.filter(user=request.user).filter(author__icontains=author)
    return HttpResponse(serializers.serialize("json", donations), content_type="application/json")

@csrf_exempt
def donate_book_ajax(request):
    if request.method == 'POST':
        user = request.user
        donator = request.user.username
        donation_amount = request.POST["donation_amount"]
        title = request.POST["title"]
        author = request.POST["author"]
        year = request.POST["year"]
        image_url = request.POST["image_url"]

        donation = BukuDonasi(user=user, donator=donator, donation_amount=donation_amount, title=title, author=author, year=year, image_url=image_url)
        donation.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_donation_ajax(request, id):
    if request.method == "DELETE":
        donation = BukuDonasi.objects.get(pk=id)
        donation.delete()
        return HttpResponse("Deleted", status=201)
    return HttpResponseNotFound()

