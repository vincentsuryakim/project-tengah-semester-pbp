from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="kontak"),
    path('tambah-kontak', add_kontak, name="tambah-kontak"),
    path('load-more', load_more, name='load-more'),
    path('json', json, name='json'),
    path('add/', add_data, name='add'),

]

