from django.urls import path
from .views import login_user, logout_user, register, login_flutter, logout_flutter
from request_buku.views import status_request_buku
from django.urls import path

app_name="register"

urlpatterns = [
    path('login/', login_flutter, name='login'),
    path('logout/', logout_flutter, name='logout'),
    path('register/', register, name='register'),
]
