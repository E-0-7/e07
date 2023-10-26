from django.urls import path
from .views import login_user, logout_user
from request_buku.views import status_request_buku
from django.urls import path

app_name="register"

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('request_buku/', status_request_buku, name='status_request_buku'),
    # path('register/', )
]
