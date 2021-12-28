from django.urls import path
from .views import index,lengkap,get_note,add_note

urlpatterns = [
    path('', index, name='layananisolasi'),
    path('lengkap-layanan',lengkap, name='lengkap'),
    path('get-note', get_note, name='getnote'),
    path('add-note', add_note, name='addnote'),
]