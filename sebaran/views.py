from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .models import Sebaran, SebaranUser
from .forms import SebaranForm

# Create your views here.

def index(request):
    response = {
        'sebaran': Sebaran.objects.all().order_by('-jumlah_kasus_aktif'),
        'sebaran_values': str(list(Sebaran.objects.order_by('-jumlah_kasus_aktif').values())),
        'terkonfirmasi': Sebaran.objects.aggregate(Sum('jumlah_kasus_terkonfirmasi'))['jumlah_kasus_terkonfirmasi__sum'],
        'aktif': Sebaran.objects.aggregate(Sum('jumlah_kasus_aktif'))['jumlah_kasus_aktif__sum'],
        'sembuh': Sebaran.objects.aggregate(Sum('jumlah_sembuh'))['jumlah_sembuh__sum'],
        'meninggal': Sebaran.objects.aggregate(Sum('jumlah_meninggal'))['jumlah_meninggal__sum'],
        'provinsi': Sebaran.objects.values('provinsi').order_by(Lower('provinsi'))
    }

    form = SebaranForm(request.POST or None)

    if (form.is_valid() and request.method == "POST"):
        form.save()
        return HttpResponseRedirect("/sebaran")

    if request.user.is_authenticated:
        try:
            response['sebaran_user'] = SebaranUser.objects.get(user_id=request.user.id)
        except SebaranUser.DoesNotExist:
            response['sebaran_user'] = None

    return render(request, 'sebaran_index.html', response)

def edit_sebaran(request):
    if (request.method == "POST"):

        # Get data from request body
        id = request.POST.get("id")
        provinsi = request.POST.get("provinsi")
        terkonfirmasi = request.POST.get("terkonfirmasi")
        aktif = request.POST.get("aktif")
        sembuh = request.POST.get("sembuh")
        meninggal = request.POST.get("meninggal")

        sebaran = Sebaran.objects.get(id=id)
        sebaran.provinsi = provinsi
        sebaran.jumlah_kasus_terkonfirmasi = terkonfirmasi
        sebaran.jumlah_kasus_aktif = aktif
        sebaran.jumlah_sembuh = sembuh
        sebaran.jumlah_meninggal = meninggal
        sebaran.save()
    
    return HttpResponseRedirect("/sebaran")

def edit_user(request):
    if (request.method == "POST"):
        provinsi = request.POST.get("provinsi")

        if (not SebaranUser.objects.filter(user_id=request.user.id).exists()):
            sebaran_user = SebaranUser(user_id=User.objects.get(id=request.user.id), provinsi=Sebaran.objects.get(provinsi=provinsi))
            sebaran_user.save()

    return HttpResponseRedirect("/sebaran")

def edit_existing_user(request):
    if (request.method == "POST"):
        provinsi = request.POST.get("provinsi")

        sebaran_user = SebaranUser.objects.get(user_id=request.user.id)
        sebaran_user.provinsi = Sebaran.objects.get(provinsi=provinsi)
        sebaran_user.save()
    
    return HttpResponseRedirect("/sebaran")

def delete_user(request):
    if (request.method == "POST"):
        sebaran_user = SebaranUser.objects.get(user_id=request.user.id)
        sebaran_user.delete()

    return HttpResponseRedirect("/sebaran")