from django.shortcuts import render
from django.db.models import Sum

from .models import Sebaran, SebaranUser

# Create your views here.

def index(request):
    response = {
        'sebaran': Sebaran.objects.all().order_by('-jumlah_kasus_aktif'),
        'sebaran_values': str(list(Sebaran.objects.order_by('-jumlah_kasus_aktif').values())),
        'terkonfirmasi': Sebaran.objects.aggregate(Sum('jumlah_kasus_terkonfirmasi'))['jumlah_kasus_terkonfirmasi__sum'],
        'aktif': Sebaran.objects.aggregate(Sum('jumlah_kasus_aktif'))['jumlah_kasus_aktif__sum'],
        'sembuh': Sebaran.objects.aggregate(Sum('jumlah_sembuh'))['jumlah_sembuh__sum'],
        'meninggal': Sebaran.objects.aggregate(Sum('jumlah_meninggal'))['jumlah_meninggal__sum']
    }

    if request.user.is_authenticated:
        response['sebaran_user'] = SebaranUser.objects.get(user_id=request.user.id)
    return render(request, 'sebaran_index.html', response)