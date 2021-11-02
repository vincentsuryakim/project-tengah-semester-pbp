from django.shortcuts import redirect, render
from django.http import response, JsonResponse
from .models import Kontak
from .forms import KontakForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core import serializers

def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        kontaks = Kontak.objects.filter(title__icontains=q)
    else:
        kontaks = Kontak.objects.all()
    # Pagintion
    paginator = Paginator(kontaks, 4)
    page_number = request.GET.get('page')
    kontaks_obj = paginator.get_page(page_number)
    return render(request, 'kontak.html', {'kontaks': kontaks_obj})

@login_required(login_url='/login/')
def add_kontak(request):
    form = KontakForm()
    if request.method == "POST":
        form = KontakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../kontak')
    response = {'form': form}
    return render(request, 'form_tambah_kontak.html', response)


def load_more(request):
    offset = int(request.POST['offset'])
    limit = 3
    kontaks = Kontak.objects.all()[offset:limit+offset]
    totalData = Kontak.objects.count()
    data = {}
    kontaks_json = serializers.serialize('json', kontaks)
    return JsonResponse(data={
        'kontaks': kontaks_json,
        'totalResult': totalData
    })
