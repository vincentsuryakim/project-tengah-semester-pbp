from django.shortcuts import render

def index(request):
    response = {'msg': 'Hello World'}
    return render(request, 'index_Infid.html', response)