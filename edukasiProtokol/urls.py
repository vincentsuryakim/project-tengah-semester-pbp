from django.urls.conf import path
from .views import buat_artikel, index, artikel_edukasi

urlpatterns = [
    path('', index, name='index_edukasi'),
    path('buat-artikel', buat_artikel, name='buat_artikel'),
]

