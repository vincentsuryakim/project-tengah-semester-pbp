from django.shortcuts import render

def index(request):
    response = {'msg': 'Hello World'}
    return render(request, 'vaksin_covid.html', response)
