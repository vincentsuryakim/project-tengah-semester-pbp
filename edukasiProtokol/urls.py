from django.urls.conf import path
from .views import buat_artikel, index, next_artikel

urlpatterns = [
    path('', index, name='index_edukasi'),
    path('buat-artikel', buat_artikel, name='buat_artikel'),
    path('next-artikel', next_artikel, name='next_artikel')
]

