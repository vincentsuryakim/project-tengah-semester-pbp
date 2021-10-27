from django.shortcuts import render, redirect
from .models import Regist
from .forms import RegistForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def index(request):
    regist = Regist.objects.all()  # TODO Implement this
    response = {'register': regist}
    paginator=Paginator(regist,2)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'tim_pakar.html',{'posts':posts_obj})

@login_required(login_url='/login/')
def add_regist(request):
    form = RegistForm()
    if request.method == "POST":
        form = RegistForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('../timPakarCovid')
    response = {'form': form}
    return render(request, 'timpakar_form.html', response)

def load_more(request):
    offset=int(request.POST['offset'])
    limit=2
    posts=Regist.objects.all()[offset:limit+offset]
    totalData=Regist.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })


