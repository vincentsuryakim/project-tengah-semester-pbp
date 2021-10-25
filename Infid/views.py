from django.shortcuts import render

def index(request):
    response = {'msg': 'Hello World'}
    return render(request, 'index_Infid.html', response)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        html = 'pages/login.html'
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('story9_app:surprise')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, html)
        return render(request, html)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('story9_app:surprise')
    else:
        form = RegisterForm()

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('story9_app:login')

        context = {'form' : form}
        html = 'pages/register.html'
        return render(request, html, context)
