from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="kontak"),
    path('tambah-kontak', add_kontak, name="tambah-kontak"),
    path('load-more', load_more, name='load-more'),
    path('get-data', get_data, name='get_data'),
    path('add/', add_data, name='add'),

]

