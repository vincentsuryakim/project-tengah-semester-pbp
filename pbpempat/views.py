from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import IntegrityError

def login(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(request.POST.get("next"))
        else:
            response = HttpResponse('Invalid Login')
            response.status_code = 401
            return response
    return redirect('/')

def register(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError as e:
            response = HttpResponse('Username already exists')
            response.status_code = 409
            return response

        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect(request.POST.get("next"))
    return redirect('/')

def logout(request):
    auth_logout(request)
    return redirect(request.GET.get("next"))