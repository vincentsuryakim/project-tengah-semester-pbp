from django.shortcuts import render

# Create your views here.
def index(request):
    response = {'msg': 'Hello World'}
    return render(request, 'timpakar.html', response)