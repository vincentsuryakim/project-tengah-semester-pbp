from django.shortcuts import render
from edukasiProtokol.forms import FormArtikel
from .models import Artikel
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Artikel.objects.filter(title__icontains=q)
    else:
        posts=Artikel.objects.all()
    # Pagintion
    paginator=Paginator(posts,6)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'edukasi_protokol.html', {'data_artikel':posts_obj})

def buat_artikel(request):
    if request.method == 'POST':
        form = FormArtikel(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/edukasiProtokol/')
    else:
        form = FormArtikel()
    return render(request, 'artikel_form.html', {'form': form})

@login_required(login_url = 'login')
def artikel_edukasi(request, id):
    contents = Artikel.objects.all().get(id=id)
    response = {'contents':contents}
    return render(request, 'artikel_view.html', response)

def next_artikel(request):
    offset=int(request.POST['offset'])
    limit= 6
    posts=Artikel.objects.all()[offset:limit+offset]
    totalData=Artikel.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })

def get_data(request):
    if 'q' in request.GET:
        q = request.GET['q']
        articles = Artikel.objects.filter(title__icontains=q).order_by('id')
    else:
        articles = Artikel.objects.all().order_by('id')
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def add_data(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    new_article = Artikel(**data)
    new_article.save()
    return JsonResponse({
        "success": "New Article Successfully Added",
    })
