from django.urls import path
from .views import index, add_kontak, load_more


urlpatterns = [
    path('', index, name="kontak"),
    path('tambah-kontak', add_kontak, name="tambah-kontak"),
    path('load-more', load_more, name='load-more'),
]

