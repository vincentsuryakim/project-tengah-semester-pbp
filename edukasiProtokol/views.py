from django.shortcuts import render
from edukasiProtokol.forms import FormArtikel
from .models import Artikel
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required

def index(request):
    data_artikel = Artikel.objects.all()
    response = {'data_artikel':data_artikel}
    return render(request, 'edukasi_protokol.html', response)

def buat_artikel(request):
    if request.method == 'POST':
        form = FormArtikel(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = FormArtikel()
    return render(request, 'artikel_form.html', {'form': form})

@login_required(login_url = 'login')
def artikel_edukasi(request, id):
    contents = Artikel.objects.all().get(id=id)
    response = {'contents':contents}
    return render(request, 'artikel_view.html', response)



