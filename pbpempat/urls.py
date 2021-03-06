"""pbpempat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
import Infid.urls as Infid
import sebaran.urls as sebaran
import TimPakar.urls as TimPakar
import RSRujukan.urls as rsrujukan
import layananisolasi.urls as layananisolasi
import vaksincovid.urls as vaksincovid
import edukasiProtokol.urls as edukasiProtokol
import kontak.urls as kontak

from .views import login, register, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(Infid)),
    path('sebaran/', include(sebaran)),
    path('rsrujukan/', include(rsrujukan)),
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('layananisolasi/', include(layananisolasi)),
    path('timPakarCovid/', include(TimPakar)),
    path('vaksincovid/', include(vaksincovid)),
    path('edukasiProtokol/', include(edukasiProtokol)),
    path('kontak/', include(kontak)),
]
