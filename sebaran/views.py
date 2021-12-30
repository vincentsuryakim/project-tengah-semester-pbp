from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt

from django.http.response import HttpResponse
import json

from .models import Sebaran, SebaranUser
from .forms import SebaranForm

# Index View
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

    if (form.is_valid() and request.method == "POST" and request.user.is_superuser):
        form.save()
        return HttpResponseRedirect("/sebaran")

    if request.user.is_authenticated:
        try:
            response['sebaran_user'] = SebaranUser.objects.get(user_id=request.user.id)
        except SebaranUser.DoesNotExist:
            response['sebaran_user'] = None

    return render(request, 'sebaran_index.html', response)

def sebaran_json(request):
    response = {
        'sebaran': list(Sebaran.objects.order_by('-jumlah_kasus_aktif').values()),
        'terkonfirmasi': Sebaran.objects.aggregate(Sum('jumlah_kasus_terkonfirmasi'))['jumlah_kasus_terkonfirmasi__sum'],
        'aktif': Sebaran.objects.aggregate(Sum('jumlah_kasus_aktif'))['jumlah_kasus_aktif__sum'],
        'sembuh': Sebaran.objects.aggregate(Sum('jumlah_sembuh'))['jumlah_sembuh__sum'],
        'meninggal': Sebaran.objects.aggregate(Sum('jumlah_meninggal'))['jumlah_meninggal__sum'],
    }

    return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def add_sebaran(request):
    if (request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        provinsi = body['provinsi']
        terkonfirmasi = body["terkonfirmasi"]
        aktif = body["aktif"]
        sembuh = body["sembuh"]
        meninggal = body["meninggal"]

        try:
            sebaran = Sebaran(provinsi=provinsi, jumlah_kasus_terkonfirmasi=terkonfirmasi, jumlah_kasus_aktif=aktif, jumlah_sembuh=sembuh, jumlah_meninggal=meninggal)
            sebaran.save()
            return HttpResponse("Successful", status=200)
        except Sebaran.DoesNotExist:
            print("An error occurred")
            return HttpResponse("An error occurred", status=400, content_type="text/plain")
    return HttpResponse("Must use POST Method", status=405, content_type="text/plain")

# Mengubah data suatu provinsi pada model Sebaran
def edit_sebaran(request):
    if (request.method == "POST" and request.user.is_superuser):

        # Get data from request body
        id = request.POST.get("id")
        provinsi = request.POST.get("provinsi")
        terkonfirmasi = request.POST.get("terkonfirmasi")
        aktif = request.POST.get("aktif")
        sembuh = request.POST.get("sembuh")
        meninggal = request.POST.get("meninggal")

        try:
            sebaran = Sebaran.objects.get(id=id)
            sebaran.provinsi = provinsi
            sebaran.jumlah_kasus_terkonfirmasi = terkonfirmasi
            sebaran.jumlah_kasus_aktif = aktif
            sebaran.jumlah_sembuh = sembuh
            sebaran.jumlah_meninggal = meninggal
            sebaran.save()
        except Sebaran.DoesNotExist:
            print(f"Sebaran object with ID: {id} does not exist")
    
    return HttpResponseRedirect("/sebaran")

# Menambahkan provinsi anda ke model SebaranUser
def edit_user(request):
    if (request.method == "POST" and request.user.is_authenticated):
        provinsi = request.POST.get("provinsi")

        try:
            sebaran_user = SebaranUser(user_id=User.objects.get(id=request.user.id), provinsi=Sebaran.objects.get(provinsi=provinsi))
            sebaran_user.save()
        except User.DoesNotExist:
            print(f"User object with ID: {request.user.id} does not exist")
        except Sebaran.DoesNotExist:
            print(f"Sebaran object with Provinsi: {provinsi} does not exist")
        except IntegrityError:
            print(f"SebaranUser object with User ID: {request.user.id} already exists")

    return HttpResponseRedirect("/sebaran")

# Mengubah provinsi anda saat ini pada model SebaranUser
def edit_existing_user(request):
    if (request.method == "POST" and request.user.is_authenticated):
        provinsi = request.POST.get("provinsi")

        try:
            sebaran_user = SebaranUser.objects.get(user_id=request.user.id)
            sebaran_user.provinsi = Sebaran.objects.get(provinsi=provinsi)
            sebaran_user.save()
        except SebaranUser.DoesNotExist:
            print(f"SebaranUser object with User ID: {request.user.id} does not exist")
        except Sebaran.DoesNotExist:
            print(f"Sebaran object with Provinsi: {provinsi} does not exist")
    
    return HttpResponseRedirect("/sebaran")

# Menghapus provinsi anda saat ini pada model SebaranUser
def delete_user(request):
    if (request.method == "POST" and request.user.is_authenticated):
        try:
            sebaran_user = SebaranUser.objects.get(user_id=request.user.id)
            sebaran_user.delete()
        except SebaranUser.DoesNotExist:
            print(f"SebaranUser object with User ID: {request.user.id} does not exist")

    return HttpResponseRedirect("/sebaran")