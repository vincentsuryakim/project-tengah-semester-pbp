from models import Artikel
from django import forms
from django.forms import ModelForm

class FormArtikel(ModelForm):
    class Meta:
        model = Artikel
        fields = ['Judul', 'Tanggal_publish', 'Penulis', 'Isi']