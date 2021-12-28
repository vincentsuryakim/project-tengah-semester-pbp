import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import NoteForm
from .models import Note
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    notes = Note.objects.all()
    form = NoteForm(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/layananisolasi')
    response = {'form': form, 'notes': notes}
    paginator = Paginator(notes, 3)
    page_number = request.GET.get('page')
    posts_obj = paginator.get_page(page_number)
    return render(request, 'layananisolasi.html', {'posts': posts_obj})


# Load More
def lengkap(request):
    offset = int(request.POST['offset'])
    limit = 3
    posts = Note.objects.all()[offset:limit + offset]
    totalData = Note.objects.count()
    data = {}
    posts_json = serializers.serialize('json', posts)
    return JsonResponse(data={
        'posts': posts_json,
        'totalResult': totalData
    })

def get_note(request):
    posts = Note.objects.all()
    data = serializers.serialize('json', posts)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_note(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    notes = Note(**data)
    notes.save()
    return JsonResponse({
        "success": "Berhasil ditambahkan",
    })
