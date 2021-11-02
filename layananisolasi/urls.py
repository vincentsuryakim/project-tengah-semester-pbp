from django.urls import path
from .views import index,lengkap

urlpatterns = [
    path('', index, name='layananisolasi'),
    path('lengkap-layanan',lengkap, name='lengkap'),
]