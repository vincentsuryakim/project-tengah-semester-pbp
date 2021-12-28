import json
from json.encoder import JSONEncoder
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import RumahSakit, BookingRS
from .forms import BookingForm, AddRS
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    rs = RumahSakit.objects.all()
    context = {'rs':rs}
    return render(request, 'RSRujukan.html', context)


def booking(request):
    bookingRs = BookingRS.objects.all()
    total_booking = bookingRs.count()

    form = BookingForm()
    if request.is_ajax():
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg': 'Success'
            })

    context = {
        'forms' : form,
        'total_booking' : total_booking,
        'booking' : bookingRs,
    }
    return render(request, 'form_rs.html', context)

def book_user(request):
    form = BookingForm()
    if request.is_ajax():
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg': 'Success'
            })

    context = {'forms' : form}
    return render(request, 'user_booking.html', context)

def create_rs(request):
    form = AddRS()
    if request.is_ajax():
        form = AddRS(request.POST)
        if form.is_valid:
            form.save()
            return JsonResponse({
                'msg' : 'Success'
            })
    context = {
        'forms' : form,
    }
    return render(request, 'add_rs.html', context)

def book_delete(request, id):
    delete_book = get_object_or_404(BookingRS, id=id)
    if request.method == 'POST':
        delete_book.delete()
    return redirect('/')

def updateUser(request):
    users = BookingRS.objects.all()
    return JsonResponse({"users":list(users.values())})

def getRS(request):
    rs = RumahSakit.objects.all()
    data = serializers.serialize('json', rs)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_book(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    bookingrs = BookingRS(**data)
    bookingrs.save()
    return JsonResponse({
        "success": "Berhasil ditambahkan",
    })