from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse, response
from .models import dataVaksin
# Create your views here.

def index(request):
    data = dataVaksin.objects.all()
    response = {'datavaksin' : data}
    paginator=Paginator(data,2)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'datavaksin.html',{'posts':posts_obj})
    
@login_required(login_url='/login/')
def load_more2(request):
    offset=int(request.POST['offset'])
    limit=2
    posts=dataVaksin.objects.all()[offset:limit+offset]
    totalData=dataVaksin.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })