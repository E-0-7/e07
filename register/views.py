from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from katalog_buku.views import katalog_buku_view
from request_buku.views import status_request_buku
from django.http import HttpResponseRedirect

# Create your views here.
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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('register:login'))
    return response