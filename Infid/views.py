from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    response = {'msg': 'Hello World'}
    return render(request, 'index_Infid.html', response)

def index(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'Login':
            # your sign in logic goes here
            if request.user.is_authenticated:
                return redirect('/')
            else:
                html = 'templates/layaout.html'
                if request.method == 'POST':
                    username = request.POST.get('username')
                    password = request.POST.get('password')

                    user = authenticate(request, username = username, password = password)

                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        messages.info(request, 'Username or password is incorrect')
                        return render(request, html)
                return render(request, html)

        elif request.POST.get('submit') == 'Signup':
            # your sign up logic goes here
            if request.user.is_authenticated:
                return redirect('/')
            else:
                form = RegisterForm()

                if request.method == 'POST':
                    form = RegisterForm(request.POST)
                    if form.is_valid():
                        form.save()
                        user = form.cleaned_data.get('username')
                        messages.success(request, 'Account was created for ' + user)
                        return redirect('/')

                context = {'form' : form}
                html = 'templates/layout.html'
                return render(request, html, context)


def logout(request):
    logout(request)
    return redirect('home_url')

# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     else:
#         html = 'templates/layaout.html'
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username = username, password = password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('Infid:')
#             else:
#                 messages.info(request, 'Username or password is incorrect')
#                 return render(request, html)
#         return render(request, html)

# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('Infid:')
#     else:
#         form = RegisterForm()

#         if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)
#                 return redirect('Infid:')

#         context = {'form' : form}
#         html = 'templates/layout.html'
#         return render(request, html, context)
